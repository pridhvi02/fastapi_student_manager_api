from fastapi import FastAPI, HTTPException,Response
from typing import Optional, List
from pydantic import BaseModel, Field
from pymongo import MongoClient
from bson.objectid import ObjectId



app = FastAPI(docs_url="/")

# MongoDB connection
client = MongoClient("mongodb+srv://pridhvi:pkm1234@cosmo.meqn6gt.mongodb.net/?retryWrites=true&w=majority&appName=cosmo")
db = client["students_db"]
students_collection = db["students"]

# Pydantic models
class Address(BaseModel):
    city: str
    country: str

class StudentBase(BaseModel):
    name: str
    age: int
    address: Address

class StudentCreate(StudentBase):
    pass

class StudentFetch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(BaseModel):
    id: str

class Student(BaseModel):
    name: str
    age: int

class StudentListResponse(BaseModel):
    data: List[Student]


# Response model for PATCH /students/{id}
class EmptyResponse(BaseModel):
    class Config:
        schema_extra = {
            "example": {}
        }

# Create student
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    student_dict = student.dict()
    result = students_collection.insert_one(student_dict)
    student_dict["id"] = str(result.inserted_id)
    return { "id" : student_dict["id"]}

# List students
@app.get("/students", response_model=StudentListResponse , status_code=200)
def list_students(country: Optional[str] = None, age: Optional[int] = None):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}
    students = students_collection.find(filters)
    student_list = [Student(name=student["name"], age=student["age"]) for student in students]
    return StudentListResponse(data=student_list)


@app.patch("/students/{id}",status_code=204)
def update_student(id: str, student: StudentUpdate):
    update_data = student.dict(exclude_unset=True)
    print(update_data)
    students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    updated_student = students_collection.find_one({"_id": ObjectId(id)})
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student["id"] = str(updated_student["_id"])
    del updated_student["_id"]
    return {}


# Delete student
@app.delete("/students/{id}", status_code=200)
def delete_student(id: str):
    result = students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}