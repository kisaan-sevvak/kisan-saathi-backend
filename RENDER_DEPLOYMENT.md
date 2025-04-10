# Deploying Kisan Saathi Backend to Render

This guide will walk you through deploying the Kisan Saathi backend to Render using their web interface.

## Prerequisites

1. A GitHub account
2. A Render account (you already have this)
3. Git installed on your local machine

## Step 1: Prepare Your Code for GitHub

Run the preparation script:

```bash
cd backend
./prepare_for_github.sh
```

This will:
- Initialize a Git repository (if not already done)
- Create a `.gitignore` file
- Add all files to Git
- Commit the changes

## Step 2: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner and select "New repository"
3. Name your repository (e.g., "kisan-saathi-backend")
4. Leave it as a public repository
5. Do NOT initialize with a README, .gitignore, or license
6. Click "Create repository"

## Step 3: Push Your Code to GitHub

GitHub will show you commands to push your existing repository. Run these commands in your terminal:

```bash
# Replace YOUR_USERNAME and REPO_NAME with your actual GitHub username and repository name
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub account if you haven't already
4. Select your repository from the list
5. Configure your service:
   - **Name**: kisan-saathi-api
   - **Region**: Choose the closest to your users (e.g., Oregon)
   - **Branch**: main
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python run.py`
   - **Plan**: Free

6. Add the following environment variables:
   - `PYTHON_VERSION`: 3.9.0
   - `PORT`: 8000
   - `DEBUG`: False
   - `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
   - `JWT_SECRET_KEY`: A secure random string for JWT token generation
   - `OPENWEATHER_API_KEY`: Your OpenWeather API key
   - `MARKET_API_URL`: http://127.0.0.1:5000/request (for local development)

7. Click "Create Web Service"

## Step 5: Wait for Deployment

Render will automatically deploy your application. This may take a few minutes. You can monitor the progress in the Render dashboard.

## Step 6: Test Your Deployment

Once deployment is complete, you can test your API using the test script:

```bash
./test_deployment.sh
```

## Step 7: Update Your Flutter App

Update your Flutter app to use the new API URL:

```dart
final String baseUrl = const String.fromEnvironment(
  'API_URL',
  defaultValue: 'https://kisan-saathi-api.onrender.com/api',
);
```

## Troubleshooting

If you encounter issues:

1. **Build Failures**: Check the build logs in the Render dashboard
2. **Runtime Errors**: Check the runtime logs in the Render dashboard
3. **Environment Variables**: Make sure all required environment variables are set
4. **CORS Issues**: Ensure your CORS settings in `main.py` allow requests from your Flutter app

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python on Render](https://render.com/docs/deploy-python) 