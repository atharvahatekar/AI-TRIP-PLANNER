from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""
        self.duration = "Full day"
        self.budget = "Mid-range"
        self.travel_style = []
        self.season = "Current season"
        self.accessibility = False

        logger.info("Initialized TravelPlanner instance")

    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=f"Destination: {city}"))
            logger.info(f"City set successfully: {city}")
        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)
        
    def set_interests(self, interests_str: str):
        try:
            # Extract any additional parameters if provided in the interests string
            interests_parts = interests_str.split(", Duration:")
            
            if len(interests_parts) > 1:
                # We have additional parameters
                base_interests = interests_parts[0]
                
                # Extract duration
                duration_parts = interests_parts[1].split(", Budget:")
                if len(duration_parts) > 1:
                    self.duration = duration_parts[0].strip()
                    
                    # Extract budget
                    budget_parts = duration_parts[1].split(", Style:")
                    if len(budget_parts) > 1:
                        self.budget = budget_parts[0].strip()
                        
                        # Extract travel style
                        style_str = budget_parts[1].strip()
                        self.travel_style = [s.strip() for s in style_str.split(",")]
                    else:
                        self.budget = budget_parts[0].strip()
                else:
                    self.duration = duration_parts[0].strip()
                    
                # Set the base interests
                self.interests = [i.strip() for i in base_interests.split(",")]
            else:
                # Just basic interests without additional parameters
                self.interests = [i.strip() for i in interests_str.split(",")]
                
            self.messages.append(HumanMessage(content=f"Interests: {interests_str}"))
            logger.info(f"Interests set successfully: {self.interests}")
            logger.info(f"Additional parameters - Duration: {self.duration}, Budget: {self.budget}, Style: {self.travel_style}")
        except Exception as e:
            logger.error(f"Error while setting interests: {e}")
            raise CustomException("Failed to set interests", e)
    
    def set_trip_parameters(self, duration=None, budget=None, travel_style=None, season=None, accessibility=False):
        """Set additional trip parameters"""
        try:
            if duration:
                self.duration = duration
            if budget:
                self.budget = budget
            if travel_style:
                self.travel_style = travel_style
            if season:
                self.season = season
            self.accessibility = accessibility
            
            logger.info(f"Trip parameters set successfully: Duration: {self.duration}, Budget: {self.budget}, Style: {self.travel_style}")
        except Exception as e:
            logger.error(f"Error while setting trip parameters: {e}")
            raise CustomException("Failed to set trip parameters", e)
        
    def create_itineary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} with interests: {self.interests}")
            logger.info(f"Trip parameters - Duration: {self.duration}, Budget: {self.budget}, Style: {self.travel_style}")
            
            # Include all parameters when generating the itinerary
            itineary = generate_itineary(
                self.city, 
                self.interests,
                duration=self.duration,
                budget=self.budget,
                travel_style=self.travel_style,
                season=self.season,
                accessibility=self.accessibility
            )
            
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itinerary generated successfully")
            return itineary
        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)
