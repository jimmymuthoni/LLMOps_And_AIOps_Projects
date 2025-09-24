import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Anime Recommender", layout="wide")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences e.g: Anime with school setting")
if query:
    with st.spinner("Fetching recommndations..."):
        ressponse = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(ressponse)

