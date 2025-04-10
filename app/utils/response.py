from typing import Any, Dict, Optional
from pydantic import BaseModel

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None

def success_response(data: Any = None, message: str = "Success") -> Dict:
    return APIResponse(
        success=True,
        message=message,
        data=data
    ).dict()

def error_response(message: str = "Error", error: str = None) -> Dict:
    return APIResponse(
        success=False,
        message=message,
        error=error
    ).dict() 