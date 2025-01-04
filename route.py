from fastapi import FastAPI

app = FastAPI()

@app.get('/hello/{user_name}')
def hello_name(user_name: str):
    return {"message": f"Hello, {user_name}"}