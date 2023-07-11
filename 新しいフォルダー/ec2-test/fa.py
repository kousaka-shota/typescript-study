from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
  return {"hello": "from AWS"}

if __name__ == "__main__":
  uvicorn.run("fa:app", host="43.207.30.36", port=8000, reload=True)