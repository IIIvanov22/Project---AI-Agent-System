# 🎬 Movie Query Agent with Personalization

This project is an intelligent movie question-answering application built using **Weaviate Agents**. It allows users to query movie data and optionally apply personalized preferences.

## Features

- Ask questions about movies from two collections (`IMDB_2006_2016` and `Movies_5000`)
- Personalized recommendations based on user preferences (genre, minimum rating)
- Toggle personalization on/off
- Clear saved preferences
- Interaction history (last 5 queries)

## Installation

1. Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>

2. Create a virtual environment:

python -m venv .venv

# Activate the environment:
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Create a `.env` file in the project root with your Weaviate credentials:

WEAVIATE_URL=<your_weaviate_cluster_url>
WEAVIATE_API_KEY=<your_weaviate_api_key>

## Running the App

Run the Streamlit app:

streamlit run app.py

Open the link provided by Streamlit (usually http://localhost:8501) in your browser.

## Notes

- The app stores preferences **per session**; no explicit user ID is needed.
- Personalization can be toggled on/off for any query.
- Interaction history shows the last 5 questions asked in the current session.