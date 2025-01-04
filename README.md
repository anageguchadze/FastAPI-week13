# FastAPI-week13

This repository contains multiple simple FastAPI applications, each demonstrating different functionalities, such as:

- Calculating the sum of two numbers
- Returning a user's age based on input
- Greeting a user by name

These are basic examples to help you get started with FastAPI and see how simple tasks can be accomplished using this modern web framework.

## Tasks

1. **Age Endpoint (`/age/{user_age}`)**  
   - A basic API that accepts a user's age as a path parameter and returns a message with their age.
   
2. **Sum Endpoint (`/sum/{first_num}/{second_num}`)**  
   - An API that accepts two numbers as path parameters and returns the sum of those numbers.

3. **Hello Endpoint (`/hello/{user_name}`)**  
   - A basic API that greets a user by their name, accepting the name as a path parameter.

## Getting Started

### Prerequisites

To run this project, you will need Python 3.7+ and the following dependencies:

- **FastAPI**
- **Uvicorn** (for running the FastAPI app)

### Installation

1. Clone the repository:
   git clone https://github.com/anageguchadze/FastAPI-week13.git
   cd FastAPI-week13

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install fastapi uvicorn
Running the Application

You can run the FastAPI application with Uvicorn:
uvicorn main:app --reload
main: Refers to the Python file containing your FastAPI app.
app: Refers to the FastAPI instance inside your Python file.
--reload: This option allows the server to automatically restart upon changes to your code.
Now, your application will be running on http://127.0.0.1:8000.

API Endpoints
/age/{user_age}: Get a response with the user's age.
/sum/{first_num}/{second_num}: Get the sum of two numbers.
/hello/{user_name}: Get a greeting message with the user's name.

License
This project is open source and available under the MIT License.