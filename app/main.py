from fastapi import FastAPI
# from routers import category
from routers import task, user
import uvicorn

app = FastAPI()



@app.get("/")
async def welcome():
    # return {"message": "My shop"}
    return {"message": "Welcome to Taskmanager"}

# app.include_router(category.router)

app.include_router(user.router)
app.include_router(task.router)