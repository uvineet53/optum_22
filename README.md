# Project-4-Predicting-Hospital-Readmission-for-Diabetes
## Background
We are looking to predict hospital readmissions for diabetic patients within a 30 day period, focusing on features that impact readmission, based on the patient's state after being discharged from the hospital. The cost of hospital readmission accounts for a large portion of hospital inpatient services spending. Diabetes is not only one of the top ten leading causes of death in the world, but also the most expensive chronic disease in the United States. Hospitalized patients with diabetes are at higher risk of readmission than those without diabetes. Therefore, reducing readmission rates for diabetic patients has a great potential to reduce medical cost. 

Data Source: https://www.kaggle.com/iabhishekofficial/prediction-on-hospital-readmission/data (102k rows of data, 49 features)



## Preprocessing of the data
**Data Cleaning**

- Kept onyl the interested fields (race, age, gender, weight, time_in_hospital, max_glu_serum, insulin, diabetesMed)
- Dropped invalid values (?)
- Converted readmitted column to binary values (reamitted in 30 day - Y/N)
- Created id columns for race, gender, age, weight for analyses



## Compile, Train and Evaluate the Model





