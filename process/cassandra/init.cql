-- Create the keyspace
CREATE KEYSPACE IF NOT EXISTS DATN
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- Switch to the keyspace
USE DATN;

-- Create the table
CREATE TABLE IF NOT EXISTS city_intro (
    city_id TEXT PRIMARY KEY,
    city_name TEXT,
    country_name TEXT,
    city_image TEXT,
    title TEXT,
    intro TEXT,
    activity LIST<TEXT>
);

-- Create the table
CREATE TABLE IF NOT EXISTS hotel_data (
    hotel_url TEXT,
    hotel_name TEXT,
    total_hotel_reviews INT,
    star FLOAT,
    hotel_address TEXT,
    price INT,
    review_date DATE,
    reviewer_rating INT,
    reviewer_contribution INT,
    reviewer_link TEXT,
    reviewer_title_comment TEXT,
    reviewer_comment TEXT,
    reviewer_stay_date DATE,
    reviewer_trip_type TEXT,
    sentiment_score FLOAT,
    city TEXT,
    country TEXT,
    hotel_id TEXT,
    inserted_date TIMESTAMP,
    PRIMARY KEY (hotel_url, inserted_date, reviewer_link)
);
