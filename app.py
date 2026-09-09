from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def health():
    return "Vicki ThingPark test server OK", 200

@app.post("/lorawan/uplink")
def uplink():
    print("ThingPark request:")
    print(request.headers)
    print(request.get_data(as_text=True))

    return "", 200
