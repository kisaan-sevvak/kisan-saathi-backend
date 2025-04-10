#!/bin/bash

# Exit on error
set -e

echo "🧪 Testing Kisan Saathi API deployment..."

# API URL
API_URL="https://kisan-saathi-api.onrender.com"

# Test health endpoint
echo "🔍 Testing health endpoint..."
curl -s "$API_URL/api/health" | grep -q "healthy" && echo "✅ Health check passed" || echo "❌ Health check failed"

# Test root endpoint
echo "🔍 Testing root endpoint..."
curl -s "$API_URL/" | grep -q "Welcome" && echo "✅ Root endpoint test passed" || echo "❌ Root endpoint test failed"

# Test chatbot endpoint
echo "🔍 Testing chatbot endpoint..."
curl -s "$API_URL/api/chatbot/suggestions" | grep -q "text" && echo "✅ Chatbot endpoint test passed" || echo "❌ Chatbot endpoint test failed"

echo "✅ All tests completed!"
echo "🌍 Your API is successfully deployed and accessible at: $API_URL"
echo "📚 API documentation is available at: $API_URL/docs" 