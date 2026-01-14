from fastapi import FastAPI

app = FastAPI()

@app.get("/testeEndpoint")
def root():
    print('teste de commit!!')
    return {"status": "ok"}