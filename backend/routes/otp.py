import random
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import SessionLocal
from database.models import OTP
from utils.send_email import send_otp_email


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# SEND OTP / RESEND OTP
# -------------------------
@router.post("/send-otp")
def send_otp(email: str, role: str, db: Session = Depends(get_db)):

    email = email.strip().lower()

    # -------------------------
    # Student Validation
    # -------------------------
    if role == "student":
        if not email.endswith("@mlrit.ac.in"):
            raise HTTPException(
                status_code=400,
                detail="Only MLRIT students allowed"
            )

    # -------------------------
    # Teacher Validation
    # -------------------------
    elif role == "teacher":
        if not (
            email.endswith("@mlrit.ac.in")
            or email.endswith("@mlrinstitutions.ac.in")
        ):
            raise HTTPException(
                status_code=400,
                detail="Only MLRIT teachers allowed"
            )

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )

    # -------------------------
    # Delete Old OTPs (Resend Case)
    # -------------------------
    db.query(OTP).filter(
        OTP.email == email
    ).delete()

    db.commit()

    # -------------------------
    # Generate OTP
    # -------------------------
    otp = str(random.randint(100000, 999999))

    expiry = datetime.now(timezone.utc) + timedelta(minutes=5)

    db_otp = OTP(
        email=email,
        otp=otp,
        expires_at=expiry,
        verified=False
    )

    db.add(db_otp)
    db.commit()

    # -------------------------
    # Send Email
    # -------------------------
    email_sent = send_otp_email(email, otp)

    if not email_sent:
        raise HTTPException(
            status_code=500,
            detail="Failed to send OTP email"
        )

    return {
        "message": "OTP sent successfully"
    }


# -------------------------
# VERIFY OTP
# -------------------------
@router.post("/verify-otp")
def verify_otp(
    email: str,
    otp: str,
    db: Session = Depends(get_db)
):

    email = email.strip().lower()

    record = db.query(OTP).filter(
        OTP.email == email
    ).order_by(OTP.id.desc()).first()

    if not record:
        raise HTTPException(
            status_code=400,
            detail="OTP not requested"
        )

    if record.otp != otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    if datetime.now(timezone.utc) > record.expires_at:
        raise HTTPException(
            status_code=400,
            detail="OTP expired"
        )

    record.verified = True
    db.commit()

    return {
        "message": "OTP verified successfully"
    }