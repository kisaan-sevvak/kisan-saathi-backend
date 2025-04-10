from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class ChatbotResponse(BaseModel):
    message: str
    suggestions: List["ChatbotSuggestion"]
    type: str
    data: Optional[Dict[str, Any]] = None

class ChatbotSuggestion(BaseModel):
    text: str
    type: str
    data: Optional[Dict[str, Any]] = None 