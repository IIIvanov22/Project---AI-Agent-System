# 📚 Collections and Data Description

This project uses **two movie collections** stored in Weaviate:

## 1. IMDB_2006_2016

- **Source**: Publicly available IMDb dataset covering movies released between 2006 and 2016.  
- **Number of records**: ~10,000 movies  
- **Fields included**:
  - `title` — Movie title  
  - `year` — Release year  
  - `rating` — IMDb rating (0–10 scale
  - `votes` — Number of votes received
  - `genre` — Movie genres (e.g., Drama, Comedy, Action)
  - `director` — Director(s) of the movie
  - `cast` — Main actors/actresses
  - `runtime` — Duration in minutes
  - `revenue` — Box office revenue (when available)
  - `description` — Short synopsis of the movie

**Purpose in the project**: This collection allows the Query Agent to answer user questions about popular movies, ratings, directors, genres, and yearly trends.

## 2. Movies_5000

- **Source**: A smaller curated dataset of 5,000 movies for quick experimentation and testing.  
- **Fields included**:
  - `title` — Movie title
  - `year` — Release year
  - `rating` — IMDb or other source rating
  - `genre` — Movie genres
  - `description` — Short synopsis
  - `director` — Director(s) of the movie

**Purpose in the project**: This smaller collection is used for rapid testing, debugging, and to demonstrate personalized recommendations without querying a very large dataset.

---

**Notes**:

- Both collections are **indexed in Weaviate** with vector embeddings for semantic search.  
- The fields are chosen to support natural language questions like:  
  - “Which movie was the highest rated in 2010?”  
  - “Show me action movies directed by Christopher Nolan.”  
  - “Recommend comedies with ratings above 8.”  
- The two collections together allow the Query Agent and Personalization Agent to demonstrate both **accurate query answering** and **personalized recommendations**.