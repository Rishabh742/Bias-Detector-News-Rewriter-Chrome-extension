Project Overview
This project aims to analyze news articles for potential bias by detecting biased words and rewriting articles in a neutral tone. It includes:

 (1) Flask API – Backend for processing articles
 (2) PostgreSQL Database – Storing article analysis results
 (3) React Dashboard – Displaying article bias metrics
 (4) Chrome Extension – Automatically rewriting biased content

1. Flask API (Backend)
  Key Functionalities:

  (a) Fetches article content from a given URL
  (b) Tokenizes and analyzes the text for biased words
  (c) Stores analysis results in a PostgreSQL database
  (d) Returns a JSON response with biased words & score

How it Works:
 (1) User submits an article URL
 (2) Flask fetches the article content
 (3) Natural Language Processing (NLP) tokenizes and filters words
 (4) Biased words are identified using a predefined dictionary
 (5) Sentiment score is calculated based on bias words
 (6) Results are stored in the database
 (7) API returns the analysis results

Example of API Request:
{
  "url": "https://example.com/news-article"
}

Example of API Response:
{
  "url": "https://example.com/news-article",
  "biased_words": ["fake", "propaganda", "misleading"],
  "bias_count": 3
}

2. PostgreSQL Database (Storage Layer)
  Tables & Schema:
 The project uses PostgreSQL to store analyzed articles.

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL,
    sentiment_score FLOAT,
    biased_words TEXT[],
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Database Purpose:
 (1) Prevents duplicate analysis of the same URL
 (2) Allows tracking of bias trends over time
 (3) Enables historical analysis for reporting

3. React Dashboard (Frontend UI)
A React-based dashboard allows users to:
   (1) Enter URLs for analysis
   (2) View bias scores & biased words
   (3) Visualize trends using charts

React Components:
  (1) URL Input Box – Enter article links
  (2) Bias Analysis Results – Displays detected biased words
  (3) Sentiment Chart – Visualizes bias trends

Example of Frontend Request to API:
axios.post("https://bias-detector-api.onrender.com/analyze", { url })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));

4. Chrome Extension (Auto Rewriter)
  (1) Detects biased words while reading articles
  (2) Suggests neutral alternatives
  (3) Displays a bias score indicator

Extension Features:
  (1) Content Script – Scans article text on any website
  (2) Popup UI – Shows bias level & alternative words
  (3) Rewrite Option – Automatically replaces biased words

Example of Content Script (JavaScript):

const biasWords = ["fake", "propaganda", "misleading"];
document.body.innerHTML = document.body.innerHTML.replace(
  new RegExp(`\\b(${biasWords.join('|')})\\b`, 'gi'), "neutral"
);

Deployment Plan
 (1) Backend (Flask API)
    (a) Deploy on Render: Free hosting for Flask
    (b) Database on Supabase: Free managed PostgreSQL

 (2) Frontend (React Dashboard)
    (a) Deploy on Vercel: Free React hosting
    (b) Connect to Flask API

 (3) Chrome Extension
    (a) Submit to Chrome Web Store for public access

 -> Next Steps & Enhancements
    (1) User Authentication – Personal bias tracking
    (2) Fact-Checking API – Google Fact Check API integration
    (3) Bias Dashboard – Compare news sources for bias trends
