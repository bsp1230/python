from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
 
# from app.controllers.exceldata_controller import router as exceldata_router
 
app = FastAPI()
 
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get('/index')
async def home():
    return "Application Running..."


@app.get("/greet")
async def index():
   return {"message": "Hello World"}
 
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="localhost", port=8080)
 