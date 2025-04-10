import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "False").lower() == "true"
    ) 