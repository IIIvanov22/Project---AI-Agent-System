import os
from dotenv import load_dotenv
import weaviate
from weaviate_agents.query import QueryAgent
import streamlit as st

load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.classes.init.Auth.api_key(WEAVIATE_API_KEY),
)

if not client.is_ready():
    st.error("Weaviate cluster is not ready!")
    st.stop()

query_agent = QueryAgent(
    client=client,
    collections=["IMDB_2006_2016", "Movies_5000"]
)

if "persona" not in st.session_state:
    st.session_state.persona = None

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎬 Movie Query Agent (Personalized)")

st.subheader("🎯 Set Your Preferences")

favorite_genre = st.selectbox(
    "Favorite genre",
    ["Action", "Comedy", "Drama", "Sci-Fi", "Horror"]
)

min_rating = st.slider("Minimum rating", 0.0, 10.0, 7.0)

use_personalization = st.checkbox("Use my preferences", value=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Save Preferences"):
        st.session_state.persona = {
            "genre": favorite_genre,
            "rating": min_rating
        }
        st.success("Preferences saved!")

with col2:
    if st.button("Clear Preferences"):
        st.session_state.persona = None
        st.success("Preferences cleared!")

persona = st.session_state.persona
if persona:
    st.info(f"Current preferences: Genre = {persona['genre']}, Min Rating = {persona['rating']}")

user_question = st.text_input("Ask a question about movies:")

if user_question:
    try:
        st.session_state.history.append({
            "query": user_question
        })

        if persona and use_personalization:
            personalized_query = f"""
            The user prefers {persona['genre']} movies with rating above {persona['rating']}.
            Use this info when answering, only if relevant.

            Question: {user_question}
            """
        else:
            personalized_query = user_question

        result = query_agent.run(personalized_query)

        st.subheader("📝 Answer")
        st.write(result.final_answer)

        st.subheader("📚 Source collection(s)")
        sources = [s.collection for s in result.sources]
        for src in sources:
            st.write(f"- {src}")

        st.subheader("🧠 Recent Interaction History")
        for h in st.session_state.history[-5:]:
            st.write(f"- {h['query']}")

    except Exception as e:
        st.error(f"Error querying the agent: {e}")

client.close()