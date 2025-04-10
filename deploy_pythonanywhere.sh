#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Python Anywhere deployment process..."

# Check if Python Anywhere CLI is installed
if ! command -v pa &> /dev/null; then
    echo "📦 Installing Python Anywhere CLI..."
    pip install pythonanywhere
fi

# Login to Python Anywhere
echo "🔑 Logging in to Python Anywhere..."
echo "Please enter your Python Anywhere username:"
read username
echo "Please enter your Python Anywhere token (from https://www.pythonanywhere.com/account/#api-token):"
read token

# Create a new web app
echo "📁 Creating a new Python Anywhere web app..."
pa create_webapp --framework flask --python 3.10 kisan-saathi-api

# Upload files
echo "📤 Uploading files to Python Anywhere..."
pa upload --username $username --token $token backend/app /home/$username/kisan-saathi-api/app
pa upload --username $username --token $token backend/requirements.txt /home/$username/kisan-saathi-api/requirements.txt
pa upload --username $username --token $token backend/run.py /home/$username/kisan-saathi-api/run.py

# Install dependencies
echo "📦 Installing dependencies..."
pa run --username $username --token $token "cd /home/$username/kisan-saathi-api && pip install -r requirements.txt"

# Configure the web app
echo "🔧 Configuring the web app..."
pa set_webapp_config --username $username --token $token kisan-saathi-api --wsgi-file /var/www/$username_pythonanywhere_com_wsgi.py --virtualenv-path /home/$username/.virtualenvs/kisan-saathi-api

# Reload the web app
echo "🔄 Reloading the web app..."
pa reload_webapp --username $username --token $token kisan-saathi-api

echo "✅ Deployment completed successfully!"
echo "🌐 Your API is now live on Python Anywhere!" 