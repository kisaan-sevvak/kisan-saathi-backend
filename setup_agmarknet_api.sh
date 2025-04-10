#!/bin/bash

# Exit on error
set -e

echo "🚀 Setting up Agmarknet API..."

# Create a directory for the API
mkdir -p agmarknet_api
cd agmarknet_api

# Clone the repository
echo "📥 Cloning Agmarknet API repository..."
git clone https://github.com/Prajwal-Shrimali/agmarknetAPI.git .

# Create a virtual environment
echo "🔧 Creating virtual environment..."
python -m venv venv
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Start the API server
echo "🌟 Starting Agmarknet API server..."
python APIwebScraping.py &

echo "✅ Agmarknet API is now running at http://127.0.0.1:5000"
echo "📝 You can test it with: http://127.0.0.1:5000/request?commodity=Potato&state=Karnataka&market=Bangalore"
echo "⚠️ Note: The API server is running in the background. To stop it, use: pkill -f 'python APIwebScraping.py'" 