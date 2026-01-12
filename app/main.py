from fastapi import FastAPI

app = FastAPI()

@app.get("/testeA")
def root():
    print('teste!')
    return {"status": "ok"}