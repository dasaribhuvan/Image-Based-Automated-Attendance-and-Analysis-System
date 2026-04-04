import os
from dotenv import load_dotenv
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def send_otp_email(to_email, otp):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    subject = "Face Attendance OTP Verification"

    html_content = f"""
    <html>
    <body>
        <h3>Face Attendance Registration</h3>
        <p>Your OTP is:</p>
        <h2>{otp}</h2>
        <p>This OTP is valid for 5 minutes.</p>
        <p>Do not share this OTP with anyone.</p>
        <br>
        <p>Face Attendance System</p>
    </body>
    </html>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        sender={
            "name": "Face Attendance",
            "email": "admin.mlrit@gmail.com"
        },
        subject=subject,
        html_content=html_content
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
        print("OTP email sent successfully")
        return True

    except ApiException as e:
        print("Error sending email:", e)
        return False