from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from detector import detect_threats
from risk import calculate_risk
from storage import live_events, failed_logins
from storage import current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI SOC Platform Running"}

# ---------------- LOGIN ---------------- #

@app.post("/login")
def login(data: dict):

    username = data["username"]
    password = data["password"]

    global current_user

    if password != "password123":

        live_events.append({
            "event":"Failed Login",
            "user":username
        })

        return {
            "success":False
        }

    current_user = username

    live_events.append({
        "event":"Successful Login",
        "user":username
    })

    return {
        "success":True,
        "username":username
    }

# ---------------- ADMIN ---------------- #

@app.post("/admin")
def admin(data: dict):

    role = data["role"]

    if role.lower() != "admin":

        live_events.append({
            "event": "Privilege Escalation",
            "user": "unknown"
        })

        return {
            "message": "Access Denied"
        }

    return {
        "message": "Admin Access Granted"
    }

# ---------------- FILE UPLOAD ---------------- #

@app.post("/upload")
def upload(data: dict):

    filename = data["filename"]

    if filename.endswith(".exe"):

        live_events.append({
            "event": "Malware Detected",
            "file": filename
        })

    return {
        "message": "File uploaded"
    }

# ---------------- NETWORK SCAN ---------------- #

@app.post("/scan")
def scan(data: dict):

    live_events.append({
        "event": "Port Scan",
        "target": data["target"]
    })

    return {
        "message": "Scan completed"
    }

# ---------------- DATA ---------------- #

@app.get("/timeline")
def timeline():
    return live_events

@app.get("/threats")
def threats():

    return detect_threats(live_events)

@app.get("/risk")
def risk():

    threats = detect_threats(live_events)

    return {
        "risk_score":
        calculate_risk(threats)
    }

@app.get("/user")
def get_user():

    return {
        "username": current_user
    }