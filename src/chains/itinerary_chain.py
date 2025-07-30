from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY
from typing import List, Optional

llm = ChatGroq(
    groq_api_key = GROQ_API_KEY,
    model_name = "llama-3.3-70b-versatile",
    temperature=0.3
)

# Enhanced prompt template with more parameters
itinerary_prompt = ChatPromptTemplate([
    ("system", """You are a knowledgeable and creative travel assistant specializing in creating personalized travel itineraries.
    
Create a detailed {duration} itinerary for {city} based on the following:
- Traveler interests: {interests}
- Budget level: {budget}
- Travel style: {travel_style}
- Season of visit: {season}
- Accessibility needs: {accessibility}

Your itinerary should include:
1. A catchy title for the itinerary
2. A brief introduction about the destination
3. A well-structured day-by-day plan with:
   - Morning activities
   - Lunch recommendations
   - Afternoon activities
   - Dinner options
   - Evening entertainment if applicable
4. Budget-conscious recommendations that match the specified budget level
5. Estimated costs for major activities and meals
6. Tips for navigating the city
7. Local customs or etiquette to be aware of

Format the itinerary in Markdown with clear headers, bullet points, and emphasis on key information.
Use emojis appropriately to make the itinerary visually engaging.
Include specific venue names, neighborhoods, and practical details.

If accessibility needs are specified, ensure recommendations are accessible.
"""),
    ("human", "Create a personalized itinerary for my trip")
])

def generate_itineary(
    city: str, 
    interests: List[str], 
    duration: str = "Full day",
    budget: str = "Mid-range",
    travel_style: Optional[List[str]] = None,
    season: str = "Current season",
    accessibility: bool = False
) -> str:
    """
    Generate a detailed travel itinerary based on multiple parameters
    
    Args:
        city: Destination city
        interests: List of traveler interests
        duration: Length of trip (Half day, Full day, 2 days, etc.)
        budget: Budget level (Budget, Mid-range, Luxury, No limit)
        travel_style: List of travel styles (Family-friendly, Adventure, etc.)
        season: Season of visit
        accessibility: Whether accessibility accommodations are needed
        
    Returns:
        A formatted itinerary as string
    """
    # Use default empty list if travel_style is None
    if travel_style is None:
        travel_style = ["Cultural"]
    
    # Format parameters for the prompt
    interests_str = ', '.join(interests)
    travel_style_str = ', '.join(travel_style)
    accessibility_str = "Consider accessibility needs" if accessibility else "No specific accessibility needs"
    
    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=city,
            interests=interests_str,
            duration=duration,
            budget=budget,
            travel_style=travel_style_str,
            season=season,
            accessibility=accessibility_str
        )
    )

    return response.content