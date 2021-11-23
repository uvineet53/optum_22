CREATE TABLE dataset (
    id SERIAL PRIMARY KEY,
    race VARCHAR(255),
    gender VARCHAR(255),
    age VARCHAR(255),
    time_in_hospital VARCHAR(255),
    num_procedures VARCHAR(255),
    num_medications VARCHAR(255),
    readmitted VARCHAR
)

select * from dataset