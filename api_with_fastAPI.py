
from fastapi import FastAPI

app = FastAPI()

@app.get('/factorial')
def factorial(n:int):
 
    a=1
 
    for i in range(1,n+1):

    

        a = a*i
        # print(a)
    result = {
        "Number": n,
        "Factorial": a,
    }

    return result
    



