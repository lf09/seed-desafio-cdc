from fastapi import FastAPI

app = FastAPI()

@app.get("/testeA")
def root():
    print('teste de commit!')
    return {"status": "ok"}