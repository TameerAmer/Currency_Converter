from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {"Status": "Ok!"}


@app.post("/convert")
def convert_currency(from_to: dict):
    if not from_to:
        return {"Error": "No data provided"}
    currencies = {"USD": 3.19, "EUR": 3.74, "GBP": 4.29, "JPY": 0.020}
    ammount = int(from_to["ammount"])
    from_currency = from_to["from"]
    to_currency = from_to["to"]
    ils_ammount = ammount * currencies[from_currency]
    converted_ammount = ils_ammount / currencies[to_currency]
    return {"Converted ammount": round(converted_ammount, 2)}


@app.get("/currency_value/{curr}")
def get_currency_value(curr):
    currencies = {"USD": 3.19, "EUR": 3.74, "GBP": 4.29, "JPY": 0.020}
    return {"Converted ammount": currencies[curr]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info")
