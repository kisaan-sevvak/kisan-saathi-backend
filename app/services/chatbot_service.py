from typing import List
import json
import os
from ..models.chatbot_model import ChatbotResponse, ChatbotSuggestion
from ..utils.weather_utils import get_weather_info
from ..utils.market_utils import get_market_info
from ..utils.crop_utils import get_crop_info

class ChatbotService:
    def __init__(self):
        self.suggestions = [
            ChatbotSuggestion(
                text="What's the weather forecast?",
                type="weather",
                data={"action": "get_weather"}
            ),
            ChatbotSuggestion(
                text="What crops should I grow?",
                type="crop",
                data={"action": "get_crop_recommendations"}
            ),
            ChatbotSuggestion(
                text="What are the current market prices?",
                type="market",
                data={"action": "get_market_prices"}
            ),
            ChatbotSuggestion(
                text="How to treat plant diseases?",
                type="disease",
                data={"action": "get_disease_info"}
            ),
            ChatbotSuggestion(
                text="When should I irrigate my crops?",
                type="irrigation",
                data={"action": "get_irrigation_schedule"}
            ),
            ChatbotSuggestion(
                text="What fertilizers should I use?",
                type="fertilizer",
                data={"action": "get_fertilizer_info"}
            )
        ]

    async def process_message(self, message: str, language: str = "en") -> ChatbotResponse:
        # Convert message to lowercase for easier matching
        message = message.lower()

        # Check for weather-related queries
        if any(word in message for word in ["weather", "rain", "temperature", "forecast"]):
            weather_info = await get_weather_info()
            return ChatbotResponse(
                message=weather_info,
                suggestions=self._get_relevant_suggestions("weather"),
                type="weather"
            )

        # Check for market-related queries
        elif any(word in message for word in ["market", "price", "cost", "rate"]):
            market_info = await get_market_info()
            return ChatbotResponse(
                message=market_info,
                suggestions=self._get_relevant_suggestions("market"),
                type="market"
            )

        # Check for crop-related queries
        elif any(word in message for word in ["crop", "plant", "grow", "harvest"]):
            crop_info = await get_crop_info()
            return ChatbotResponse(
                message=crop_info,
                suggestions=self._get_relevant_suggestions("crop"),
                type="crop"
            )

        # Default response for unrecognized queries
        else:
            return ChatbotResponse(
                message="I'm not sure I understand. Could you please rephrase your question?",
                suggestions=self.suggestions,
                type="text"
            )

    async def get_suggestions(self) -> List[ChatbotSuggestion]:
        return self.suggestions

    def _get_relevant_suggestions(self, category: str) -> List[ChatbotSuggestion]:
        # Return suggestions related to the current topic
        return [s for s in self.suggestions if s.type != category] 