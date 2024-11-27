from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from numpy.linalg import inv

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculateData(BaseModel):
    a1: int | float
    a2: int | float
    l: int | float
    p: int | float
    t: int | float
    e: int | float
    n: int | float
    p: int | float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/calculate")
def calculate(cdata: CalculateData) -> Any:
    matrizk = np.eye(cdata.n)
    matrizx = np.zeros((cdata.n,1))
    matrizf = np.zeros((cdata.n,1))
    areas = []
    y = (cdata.l / (cdata.n -1)) / 1000
    c = 1
    while c <= cdata.n:
        areas.append(((cdata.a1/1000) + ((((cdata.a2/1000)-(cdata.a1/1000))/(cdata.l/1000)) * (y*(c-1))))*(cdata.t/1000))
        c += 1
    matriza = np.transpose(np.array([areas]))
    c = 0
    rigidez = []
    while c < cdata.n -1:
        rigidez.append((cdata.e*(matriza[c+1][0] + matriza[c][0]))/(2*y))
        c +=1
    print(rigidez)
    print("---------------MATRIZ DE RIGIDEZ-------------")
    print(matrizk)
    print("---------------MATRIZ DE DESPLAZAMIENTO-------------")
    print(matrizx)
    print("---------------MATRIZ DE FUERZAS-------------")
    print(matrizf)
    return{"Calculando": "calculado"}