<h1><b>BANK CHURN PREDICTION</b></h1><br>
<h2><b>Title And Author</b></h2>
Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang<br>
Author: Charan Ganemaneni, UMBC, Spring-2024 Semester<br>
GitHub Link: https://github.com/charangani<br>

<h2><b>BACKGROUND</b></h2>
The dataset is about predicting customer churn in the banking sector. It contains various features like credit score, age, tenure, balance, number of products, credit card status, active membership status, estimated salary, and churn status. Predicting customer churn is critical for businesses, especially in the banking sector. Retaining existing customers is often more cost-effective than acquiring new ones. By predicting which customers are likely to churn, banks can proactively address their concerns and improve customer retention1.<br>
Research Questions : <br>
“Can we predict if a customer will churn based on their profile information?” This can be broken down into several sub-questions, such as:<br>
“What factors are most influential in predicting customer churn?”<br>
“How does age affect the likelihood of churn?”<br>
“Does having a credit card make a customer more or less likely to churn?”<br>
“How does the number of products a customer uses affect their likelihood of churn?”<br>
<h2><b>Data</b></h2>
Data sources: https://www.kaggle.com/datasets/cybersimar08/binary-classification-of-bank-churn-synthetic-data/data
Data size: 36.27 MB
Data shape:<br>
rows:<br>175028
columns:<br>25
What does each row represent?(a patient, a school, a crime, etc.)<br>
Each row in the dataset represents a unique customer of the bank.<br>
Data dictionary:<br>
<table>
  
Column Name	Data Type	Definition	Potential Values
Surname	Categorical	Label Encoded Surnames	Various encoded surnames
CreditScore	Numerical	A numerical value representing the customer’s credit score	Any numerical value
Age	Numerical	The customer’s age	Any numerical value
Tenure	Numerical	The number of years the customer has been with the bank	Any numerical value
Balance	Numerical	The customer’s account balance	Any numerical value
NumOfProducts	Numerical	The number of bank products the customer uses	Any numerical value
HasCrCard	Binary	Whether the customer has a credit card	1 = yes, 0 = no
IsActiveMember	Binary	Whether the customer is an active member	1 = yes, 0 = no
EstimatedSalary	Numerical	The estimated salary of the customer	Any numerical value
Exited	Binary	Whether the customer has churned	1 = yes, 0 = no
</table>
Columns name:<br>
'Surname', 'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
       'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited',
       'Surname_tfidf_0', 'Surname_tfidf_1', 'Surname_tfidf_2',
       'Surname_tfidf_3', 'Surname_tfidf_4', 'France', 'Germany', 'Spain',
       'Female', 'Male', 'Mem__no__Products', 'Cred_Bal_Sal', 'Bal_sal',
       'Tenure_Age', 'Age_Tenure_product'<br>
Data type:
| Column | Non-Null Count | Dtype |
|--------|---------------|-------|
| Surname | 175028 | int64 |
| CreditScore | 175028 | float64 |
| Age | 175028 | float64 |
| Tenure | 175028 | float64 |
| Balance | 175028 | float64 |
| NumOfProducts | 175028 | float64 |
| HasCrCard | 175028 | int64 |
| IsActiveMember | 175028 | int64 |
| EstimatedSalary | 175028 | float64 |
| Exited | 175028 | int64 |
| Surname_tfidf_0 | 175028 | float64 |
| Surname_tfidf_1 | 175028 | float64 |
| Surname_tfidf_2 | 175028 | float64 |
| Surname_tfidf_3 | 175028 | float64 |
| Surname_tfidf_4 | 175028 | float64 |
| France | 175028 | int64 |
| Germany | 175028 | int64 |
| Spain | 175028 | int64 |
| Female | 175028 | int64 |
| Male | 175028 | int64 |
| Mem__no__Products | 175028 | float64 |
| Cred_Bal_Sal | 175028 | float64 |
| Bal_sal | 175028 | float64 |
| Tenure_Age | 175028 | float64 |
| Age_Tenure_product | 175028 | float64 |

Potential values (for categorical valuables, what are the categories?)
Which variable/column will be your target/label in your ML model?<br>
Exited column will be the target/label in the machine learning model as it indicates whether the customer has churned or not.<br>
Which variables/columns may be selected as features/predictors for your ML models?<br>
 The features/predictors for the machine learning model could be all the other columns: Surname, CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, and EstimatedSalary. These features can provide valuable insights into the factors that might influence a customer’s decision to churn. However, the actual selection of features would depend on further analysis and feature importance determined by the model. For example, Surname might not be a useful predictor and could be dropped based on the specific use case and data analysis.
