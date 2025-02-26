
5. Database for Tracking Article Bias

To maintain a history of analyzed articles and their bias scores, we need a database. PostgreSQL or MongoDB can store the article text, detected bias 
words, and sentiment scores.

For a PostgreSQL-based solution, we define the schema:

CREATE TABLE articles (

    id SERIAL PRIMARY KEY,

    url TEXT UNIQUE NOT NULL,

    content TEXT NOT NULL,

    sentiment_score FLOAT,

    biased_words TEXT[],

    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
