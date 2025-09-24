from src.recommender import AnimeRecommender
from src.vector_store import VectorStoreBuilder
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.custom_exception import CustomException
from utils.logger import get_logger


logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    """recommendation pipeline"""
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommedation Pipeline....")
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)
            logger.info("Pipeline initialized successfully...")

        except Exception as e:
            logger.error(f"Failed to initilize pipeline {str(e)}")
            raise CustomException("Error during pipeline initialization", e)
        
    def recommend(self, query:str) -> str:

        try:
            logger.info(f"Received a query {query}")
            recommendation = self.recommender.get_reccomendation(query)
            logger.info("Recommendation generated suceesfully..")
            return recommendation
        
        except Exception as e:
            logger.info(f"Failed to get the recommendation {str(e)}")
            raise CustomException("Error during giving reccomndation", e)
        


        