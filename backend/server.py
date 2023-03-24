
# install and import FastAPI and hypercorn libraries
# Hypercorn is an ASGI web server
# FastAPI is similar to Django, just a bit faster abd more modern
# read more about FastAPI here: https://towardsdatascience.com/create-your-first-rest-api-in-fastapi-e728ae649a60
from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ml import predict

import base64
import json
import logging             
import numpy as np

from controllers.verify import getRandomUser 


class PictureModel(BaseModel):
    img: str

class UserModel(BaseModel):
    account_id: str
    risk: str
    session_count: str
    level: str

class MlPredictionModel(BaseModel):
    id: str
    risk: str
    level: str
    session_count: str
    ff: str
    
    
    


#=== FastAPI configuration part ===
app = FastAPI()

origins = ["*"]

#We define some CORS options in case we would like to deploy and use web browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# === FastAPI configuration part ===

# === Below some examples for RestAPI ===

@app.get("/getUser")
async def getUser():
    print("Received get request at /getUser")
    return "TEMPORARY RESPONSE"

@app.get("/verify")
async def verify():
    print("Receiving post request on /verify")
    #print(getRandomUser())
    return {"result": getRandomUser()}


@app.post("/test")
async def eligibilityMeasure(mlPredictionModel: MlPredictionModel):
    print("Receiving post request on /test")
    #Use model:
    return {"result": predict(mlPredictionModel.ff, mlPredictionModel.session_count, mlPredictionModel.level, mlPredictionModel.risk)}




# === Start server using hypercorn ===
asyncio.run(serve(app, Config()))
# === Start server using hypercorn ===

