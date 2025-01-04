from fastapi import FastAPI

app = FastAPI()

@app.get('/age/{user_age}')
def get_age(user_age: int):
    return {"message": f"Your age is {user_age}"}