#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Heroku deployment process..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "📦 Installing Heroku CLI..."
    curl https://cli-assets.heroku.com/install.sh | sh
fi

# Login to Heroku
echo "🔑 Logging in to Heroku..."
heroku login

# Create a new Heroku app
echo "📁 Creating a new Heroku app..."
heroku create kisan-saathi-api

# Set environment variables
echo "🔧 Setting environment variables..."
heroku config:set PYTHON_VERSION=3.10

# Deploy to Heroku
echo "📤 Deploying to Heroku..."
git add .
git commit -m "Deploy to Heroku"
git push heroku main

echo "✅ Deployment completed successfully!"
echo "🌐 Your API is now live on Heroku!" 