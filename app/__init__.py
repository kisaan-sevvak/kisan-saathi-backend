from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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