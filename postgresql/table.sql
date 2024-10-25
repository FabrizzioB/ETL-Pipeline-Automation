CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    weather TEXT NOT NULL,
    temperature FLOAT,
    min_temperature FLOAT,
    max_temperature FLOAT,
    feels_like_temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    wind_speed FLOAT,
    cloudiness FLOAT,
    sunrise TIMESTAMP,
    sunset TIMESTAMP
);