# Project-4-Predicting-Hospital-Readmission-for-Diabetes
## Background
We are looking to predict hospital readmissions for diabetic patients within a 30 day period, focusing on features that impact readmission, based on the patient's state after being discharged from the hospital. The cost of hospital readmission accounts for a large portion of hospital inpatient services spending. Diabetes is not only one of the top ten leading causes of death in the world, but also the most expensive chronic disease in the United States. Hospitalized patients with diabetes are at higher risk of readmission than those without diabetes. American hospitals spent over $41 billion on diabetic patients who got readmitted within 30 days of discharge. Being able to determine factors that lead to higher readmission in such patients, and correspondingly being able to predict which patients will get readmitted can help hospitals save millions of dollars while improving quality of care. Therefore, reducing readmission rates for diabetic patients has a great potential to reduce medical cost. 

Data Source: https://www.kaggle.com/iabhishekofficial/prediction-on-hospital-readmission/data (102k rows of data, 49 features)


## Preprocessing of the data

Data Set Description

**Data Cleaning**
- Reduced the data set to include only the intersted features we will use for prerdiction (race, age, gender, weight, time_in_hospital, max_glu_serum, insulin, diabetesMed)
- Check for and Dropped invalid values (?)
- Converted readmitted column to binary field
- Determine the number of unique values in each column.  Dropped colum (max_glu_serum) since there was only 1 unique value
- Convert categorical data to numberic with 'pdget_dummies'
- Split the preprocessed data into a training and testing dataset
- Create a StandardScaler instances
- Fit the StandardScale
- Scale the data
-
## Compile, Train and Evaluate the Model

-Define the model - deep neural net, i.e., the number of input features and hidden nodes for each layer.(Explain why chose the nodes we did)
-Complie the model
-Train the model
-Evaluate the model using test data
-Export our model to HDF5 file





