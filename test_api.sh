#!/bin/bash

# Exit on error
set -e

echo "🧪 Testing Kisan Saathi API..."

# Get the API URL from command line or use default
API_URL=${1:-"https://kisan-saathi-api.onrender.com"}
echo "🌐 Using API URL: $API_URL"

# Function to test an endpoint
test_endpoint() {
    local endpoint=$1
    local expected=$2
    local name=$3
    
    echo "🔍 Testing $name endpoint..."
    response=$(curl -s "$API_URL$endpoint")
    
    if echo "$response" | grep -q "$expected"; then
        echo "✅ $name test passed"
        return 0
    else
        echo "❌ $name test failed"
        echo "   Response: $response"
        return 1
    fi
}

# Test health endpoint
test_endpoint "/api/health" "healthy" "Health check"

# Test root endpoint
test_endpoint "/" "Welcome" "Root"

# Test chatbot suggestions endpoint
test_endpoint "/api/chatbot/suggestions" "text" "Chatbot suggestions"

# Test weather endpoint
test_endpoint "/api/weather/current" "temperature" "Weather current"

# Test market endpoint
test_endpoint "/api/market/prices" "price" "Market prices"

echo "✅ All tests completed!"
echo "🌍 Your API is successfully deployed and accessible at: $API_URL"
echo "📚 API documentation is available at: $API_URL/docs" 