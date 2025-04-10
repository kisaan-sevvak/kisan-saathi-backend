#!/bin/bash

# Exit on error
set -e

echo "🚀 Deploying Kisan Saathi Backend to Render..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if render-cli is installed
if ! command -v render &> /dev/null; then
    echo "📦 Installing render-cli..."
    curl -o render https://render.com/download/render-linux-amd64
    chmod +x render
    sudo mv render /usr/local/bin/
fi

# Login to Render (if not already logged in)
echo "🔑 Logging in to Render..."
render login

# Create a new web service
echo "🌐 Creating web service on Render..."
render create web-service \
    --name kisan-saathi-api \
    --env python \
    --build-command "pip install -r requirements.txt" \
    --start-command "python run.py" \
    --plan free \
    --region oregon

# Set environment variables
echo "🔧 Setting environment variables..."
render env set \
    --service kisan-saathi-api \
    PYTHON_VERSION=3.9.0 \
    PORT=8000 \
    DEBUG=False

echo "✅ Deployment initiated! Check your Render dashboard for progress."
echo "🌍 Your API will be available at: https://kisan-saathi-api.onrender.com"
echo "📚 API documentation will be at: https://kisan-saathi-api.onrender.com/docs" 