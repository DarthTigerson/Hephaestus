from fastapi import FastAPI
#from routers import 
from database import engine
import models
from starlette.staticfiles import StaticFiles


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")