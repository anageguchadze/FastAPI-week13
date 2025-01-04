from fastapi import FastAPI

app = FastAPI()

@app.get('/sum/{first_num}/{second_num}')
def sum_func(first_num: int, second_num: int):
    num_sum = first_num + second_num
    return {"sum": num_sum}