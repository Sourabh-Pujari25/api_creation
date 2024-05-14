from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    number= int

    app = FastAPI()

@app.put('/factorial')
def factorial(n:Input):
 
    a=1
 
    for i in range(1,n+1):

    

        a = a*i
        # print(a)
    result = {
        "Number": n,
        "Factorial": a,
    }

    return result