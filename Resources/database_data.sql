CREATE TABLE dataset (
    id SERIAL PRIMARY KEY,
    race VARCHAR(255),
    gender VARCHAR(255),
    age VARCHAR(255),
    weight VARCHAR(255),
    time_in_hospital VARCHAR(255),
    insulin VARCHAR,
    diabetes_med VARCHAR(255),
    readmitted VARCHAR
)

select * from dataset