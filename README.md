# Image Based Automated Attendance & Analytics System

## Short Description

An AI-powered attendance and analytics platform that automatically identifies students from classroom images using InsightFace and generates attendance insights, reports, and individual student analysis for teachers.

---

# Face Recognition Attendance & Analytics System

A smart AI-based attendance platform designed to automate classroom attendance using face recognition from a single classroom image. The system detects and recognizes multiple students in real time, stores attendance records, and provides detailed attendance analytics for teachers and administrators.

The project uses **InsightFace (buffalo_l model pack)**, which internally includes **RetinaFace** for face detection and **ArcFace** for generating 512-dimensional facial embeddings. The embeddings are matched using cosine similarity for accurate student identification.

In addition to attendance automation, the platform provides attendance analytics such as low-attendance detection, overall classroom attendance trends, and individual student attendance analysis with downloadable reports for teachers.

---

## Features

* Automated attendance marking using face recognition
* Multi-face detection from classroom images
* Embedding-based student identification using cosine similarity
* Attendance analytics and reporting system
* Individual student attendance analysis for teachers
* Detection of low-attendance students
* Downloadable attendance reports
* Secure authentication system
* Full-stack web application with responsive interface

---

## Tech Stack

### Frontend

* React.js
* Axios
* HTML5
* CSS3

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### AI & Computer Vision

* InsightFace (buffalo_l)
* RetinaFace
* ArcFace
* OpenCV
* NumPy

---

## System Workflow

1. Student images are registered in the system
2. InsightFace generates facial embeddings for each student
3. Embeddings are stored in PostgreSQL database
4. A classroom image is uploaded through the frontend
5. RetinaFace detects multiple faces from the image
6. Faces are aligned internally using facial landmarks
7. ArcFace generates 512-dimensional embeddings
8. Cosine similarity is used for face matching
9. Attendance is automatically marked
10. Attendance analytics and reports are generated

---

## Attendance Analytics System

The platform also includes a dedicated analytics module for monitoring and analyzing attendance data.

### Features

* Student-wise attendance percentage analysis
* Identification of low-attendance students
* Classroom attendance trend analysis
* Downloadable attendance reports for teachers
* Individual student attendance monitoring
* Attendance history visualization

This helps teachers efficiently monitor student participation and identify attendance patterns without manual calculations.

---

## Project Architecture

```text
Frontend (React.js)
        ↓
Backend APIs (FastAPI)
        ↓
Face Recognition Pipeline (InsightFace)
        ↓
PostgreSQL Database
```

---

## Installation

### Clone Repository

```bash
git clone <your-github-repo-link>
cd project-folder
```

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### Create `.env` File

```env
DATABASE_URL=your_database_url
```

### Run Backend

```bash
uvicorn app:app --reload
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Model Setup

The model files are not included in this repository due to file size limitations.

Create a `models` folder inside the backend directory and place your model files there before running the application.

---

## Future Enhancements

* Real-time attendance using CCTV streams
* Mobile application integration
* Advanced analytics dashboard
* Notification system for low attendance students
* Cloud deployment optimization

---

## Applications

* Schools
* Colleges
* Smart Classroom Systems
* Training Institutes

---

## Author

Dasari Bhuvan Kumar
