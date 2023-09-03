from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import dotenv

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class Hello(BaseModel):
  name: str

@app.get("/hello")
def read_root():
  return {'message': f'Hello, World!'}

@app.post("/hello")
def write_root(name: str):
  return {'message': f'Hello, {name}!'}
