#!/bin/bash

# Exit on error
set -e

echo "🚀 Preparing Kisan Saathi Backend for GitHub..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
fi

# Create .gitignore file if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo "📝 Creating .gitignore file..."
    cat > .gitignore << EOL
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# Environment variables
.env

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOL
fi

# Add all files to git
echo "📦 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Initial commit for Render deployment"

echo "✅ Code is ready for GitHub!"
echo "📝 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Follow the instructions GitHub provides to push your code"
echo "3. Go to render.com and create a new Web Service"
echo "4. Connect it to your GitHub repository"
echo "5. Configure the service with:"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: python run.py"
echo "   - Environment Variables:"
echo "     - PYTHON_VERSION: 3.9.0"
echo "     - PORT: 8000"
echo "     - DEBUG: False" 