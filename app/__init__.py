from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from .auth.auth import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(title="Kisan Saathi API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Import routes after app is created
from app.routes import weather_routes, crop_routes, disease_routes, market_routes, soil_routes, chatbot_routes

# Include routers
app.include_router(weather_routes.router, prefix="/api/weather", tags=["weather"])
app.include_router(crop_routes.router, prefix="/api/crops", tags=["crops"])
app.include_router(disease_routes.router, prefix="/api/diseases", tags=["diseases"])
app.include_router(market_routes.router, prefix="/api/market", tags=["market"])
app.include_router(soil_routes.router, prefix="/api/soil", tags=["soil"])
app.include_router(chatbot_routes.router, prefix="/api/chatbot", tags=["chatbot"])

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # For development, accept any username/password
    # In production, you would verify against a database
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
async def root():
    return {"message": "Welcome to Kisan Saathi API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()} 