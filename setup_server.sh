#!/bin/bash

# Exit on error
set -e

echo "🚀 Setting up Kisan Saathi Backend Server..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Copy .env.example to .env if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update the .env file with your actual configuration values"
fi

# Start the server
echo "🌐 Starting the server..."
python run.py

# Note: The server will run on http://localhost:8000 by default
# You can access the API documentation at http://localhost:8000/docs 