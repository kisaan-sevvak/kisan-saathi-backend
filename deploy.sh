#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting deployment process..."

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t kisan-saathi-api .

# Run database migrations
echo "🔄 Running database migrations..."
docker run --rm \
    -e DATABASE_URL="$DATABASE_URL" \
    kisan-saathi-api \
    python -c "from app.database import engine, Base; Base.metadata.create_all(bind=engine)"

# Start the application
echo "🌟 Starting the application..."
docker run -d \
    --name kisan-saathi-api \
    -p 8000:8000 \
    -e DATABASE_URL="$DATABASE_URL" \
    -e GOOGLE_CLIENT_ID="$GOOGLE_CLIENT_ID" \
    -e SECRET_KEY="$SECRET_KEY" \
    -e OPENWEATHER_API_KEY="$OPENWEATHER_API_KEY" \
    -e DEBUG=False \
    kisan-saathi-api

echo "✅ Deployment completed successfully!" 