# BANK CHURN PREDICTION

**Title:** Bank Customer Churn Prediction

**Prepared for** UMBC Data Science Master Degree Capstone by Dr. Chaoji (Jay) Wang

**Author:** Charan Ganemaneni

**Semester:** UMBC, Spring-2024 Semester

**GitHub Link:** https://github.com/charangani

**Linkedin Profile:** linkedin.com/in/charan-ganemaneni-9779a6158

**Powerpoint Presentation:** https://github.com/charangani/UMBC-DATA606-Capstone/blob/main/docs/Presentation.pptx

**Youtube video:** https://www.youtube.com/watch?v=fVv2gU8gFdc

## Background

The dataset focuses on predicting customer churn in the banking sector. It encompasses various features such as credit score, age, tenure, balance, number of products, credit card status, active membership status, estimated salary, and churn status. Predicting customer churn is pivotal for businesses, particularly in banking, as retaining existing customers is often more cost-effective than acquiring new ones.

### Research Questions:

1. Can we predict if a customer will churn based on their profile information?
    - Sub-questions include:
        - What factors are most influential in predicting customer churn?
        - How does age affect the likelihood of churn?
        - Does having a credit card make a customer more or less likely to churn?
        - How does the number of products a customer uses affect their likelihood of churn?

## Data

- **Data Source:** [Kaggle Dataset - Binary Classification of Bank Churn Synthetic Data](https://www.kaggle.com/datasets/cybersimar08/binary-classification-of-bank-churn-synthetic-data/data)
- **Data Size:** 36.27 MB
- **Data Shape:** 175,028 Rows, 25 Columns

### Data Dictionary:

| Column Name         | Data Type | Definition                              | Potential Values     |
|---------------------|-----------|-----------------------------------------|----------------------|
| Surname             | Categorical | Label Encoded Surnames                 | Various encoded surnames |
| CreditScore         | Numerical | Customer's credit score                | Any numerical value |
| Age                 | Numerical | Customer's age                          | Any numerical value |
| Tenure              | Numerical | Number of years customer has been with the bank | Any numerical value |
| Balance             | Numerical | Customer's account balance              | Any numerical value |
| NumOfProducts       | Numerical | Number of bank products customer uses   | Any numerical value |
| HasCrCard           | Binary    | Whether the customer has a credit card | 1 = yes, 0 = no |
| IsActiveMember      | Binary    | Whether the customer is an active member | 1 = yes, 0 = no |
| EstimatedSalary     | Numerical | Estimated salary of the customer       | Any numerical value |
| Exited              | Binary    | Whether the customer has churned       | 1 = yes, 0 = no |

## Exploratory Data Analysis (EDA)

- Conducted univariate and bivariate analyses to understand feature distributions and their relationship with the target variable 'Exited'.

### Results of EDA:

- The target feature 'Exited' is unbalanced.
- Significant differences in churn rate between countries and genders.
- Active membership appears to impact churn.
  
## Model Training

- Split data into 75% training and 25% test sets.
- Trained models using pandas, scikit-learn, and seaborn libraries.
- Three models trained:
    1. Logistic Regression
    2. Decision Tree Classifier
    3. Random Forest Classifier

### Model Performance:

1. **Logistic Regression Model:**
   - Accuracy: ~83.45%
   - Precision, Recall, and F1-score for both classes.
   
2. **Decision Tree Classifier:**
   - Accuracy: ~86%
   - Precision, Recall, and F1-score for both classes.

3. **Random Forest Classifier:**
   - Accuracy: ~86%
   - Precision, Recall, and F1-score for both classes.

## Conclusion

The Random Forest Classifier outperformed other models in terms of accuracy, precision, recall, and F1-score for predicting customer churn. However, all models demonstrated better prediction for non-churners compared to churners. Future work could explore more complex models and feature engineering to improve recall for the minority class. 

---

**Link to YouTube Video**  
**Link to Final PPT Presentation**
