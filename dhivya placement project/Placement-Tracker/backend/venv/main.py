from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Student
from schemas import StudentCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Placement Tracker Running"}

@app.post("/students")
def create_student(student: StudentCreate):

    db = SessionLocal()

    new_student = Student(
        name=student.name,
        department=student.department,
        year=student.year
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student Added Successfully"
    }