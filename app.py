from fastapi import FastAPI


app = FastAPI(title="Striper")

@app.get("/")
def root():
    return {"hello": "World"}