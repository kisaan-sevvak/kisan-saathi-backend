from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.chatbot_model import ChatbotResponse, ChatbotSuggestion
from ..services.chatbot_service import ChatbotService
from ..auth.auth import get_current_user

router = APIRouter(prefix="/chatbot", tags=["chatbot"])
chatbot_service = ChatbotService()

@router.post("/message", response_model=ChatbotResponse)
async def send_message(
    message: str,
    language: str = "en",
    current_user = Depends(get_current_user)
):
    try:
        response = await chatbot_service.process_message(message, language)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/suggestions", response_model=List[ChatbotSuggestion])
async def get_suggestions(
    current_user = Depends(get_current_user)
):
    try:
        suggestions = await chatbot_service.get_suggestions()
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 