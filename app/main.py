from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from google.oauth2 import id_token
from google.auth.transport import requests
from datetime import datetime, timedelta
from typing import Optional
import os
from dotenv import load_dotenv
from app.routes import weather_routes, crop_routes, disease_routes, market_routes, soil_routes, chatbot_routes

load_dotenv()

app = FastAPI(title="Kisan Saathi API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Flutter app's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(weather_routes.router, prefix="/api", tags=["weather"])
app.include_router(crop_routes.router, prefix="/api", tags=["crops"])
app.include_router(disease_routes.router, prefix="/api", tags=["diseases"])
app.include_router(market_routes.router, prefix="/api", tags=["market"])
app.include_router(soil_routes.router, prefix="/api", tags=["soil"])
app.include_router(chatbot_routes.router, prefix="/api", tags=["chatbot"])

# Google OAuth configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Welcome to Kisan Saathi API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/auth/google")
async def google_auth(token: str):
    try:
        # Verify the Google token
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), GOOGLE_CLIENT_ID)

        # Get user info
        userid = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name', '')
        picture = idinfo.get('picture', '')

        # Here you would typically:
        # 1. Check if user exists in your database
        # 2. If not, create a new user
        # 3. Generate a JWT token for your app

        return {
            "status": "success",
            "user": {
                "id": userid,
                "email": email,
                "name": name,
                "picture": picture
            }
        }
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 