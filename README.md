# Student Management API

This is a RESTful API built with FastAPI and MongoDB for managing student records. The API provides endpoints for creating, retrieving, updating, and deleting student data.

## Features

- Create a new student record
- List all students or filter by country and age
- Update an existing student's information
- Delete a student record

## Technologies Used

- Python
- FastAPI
- MongoDB (with PyMongo driver)
- Pydantic

## Getting Started

### Prerequisites

- Python 3.7 or higher
- MongoDB Atlas account (or a local MongoDB instance)

### Installation

1. Clone the repository: git clone https://github.com/pridhvi02/fastapi_student_manager_api.git
2. Navigate to the project directory: cd fastapi_student_manager_api
3. Create a virtual environment and activate it:

**On Windows:**
python -m venv env
env\Scripts\activate

**On Linux/macOS:**
python3 -m venv env
source env/bin/activate

4. Install the required dependencies:
pip install -r requirements.txt

5. Set the MongoDB connection string as an environment variable:

**On Windows:**
set MONGODB_URI="mongodb+srv://pridhvi:pkm1234@cosmo.meqn6gt.mongodb.net/?retryWrites=true&w=majority&appName=cosmo"

**On Linux/macOS:**
export MONGODB_URI="mongodb+srv://pridhvi:pkm1234@cosmo.meqn6gt.mongodb.net/?retryWrites=true&w=majority&appName=cosmo"

### Running the API

To start the API server, run:
uvicorn main:app --reload

The API will be available at `http://localhost:8000`.
