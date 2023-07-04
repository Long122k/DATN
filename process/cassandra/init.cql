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
    hotel_name TEXT,
    total_hotel_reviews TEXT,
    star TEXT,
    hotel_address TEXT,
    price TEXT,
    review_date TEXT,
    reviewer_rating TEXT,
    reviewer_contribution TEXT,
    reviewer_link TEXT,
    reviewer_title_comment TEXT,
    reviewer_comment TEXT,
    reviewer_stay_date TEXT,
    reviewer_trip_type TEXT,
    sentiment_score TEXT,
    PRIMARY KEY (hotel_name)
);
