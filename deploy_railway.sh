#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Railway deployment process..."

# Login to Railway
echo "🔑 Logging in to Railway..."
railway login

# Create a new project if it doesn't exist
echo "📁 Creating a new Railway project..."
railway init

# Deploy to Railway
echo "📤 Deploying to Railway..."
railway up

echo "✅ Deployment completed successfully!"
echo "🌐 Your API is now live on Railway!" 