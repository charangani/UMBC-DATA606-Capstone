import streamlit as st
import pandas as pd
import pickle

# Load the model from the file (make sure to provide the correct path or place the model in the same directory)
model = pickle.load(open('model.pkl', 'rb'))

# Title of the app
st.title('Bank Churn Prediction')

# Ask the user for the input method
input_method = st.radio("Choose input method:", ("Enter single record", "Upload a file"))

if input_method == "Enter single record":
    # User input fields for a single record
    gender = st.radio('Gender', ['Female', 'Male'])
    Female = 1 if gender=='Female' else 0
    Male = 1 if gender=='Male' else 0
    country = st.selectbox('Country', ['France', 'Germany', 'Spain'])
    France = 1 if country=='France' else 0
    Germany = 1 if country=='Germany' else 0
    Spain = 1 if country=='Spain' else 0
    credit_score = st.number_input('Credit Score', min_value=0)
    age = st.number_input('Age', min_value=0)
    tenure = st.number_input('Tenure', min_value=0)
    balance = st.number_input('Balance', min_value=0.0, format='%f')
    num_of_products = st.number_input('Number of Products', min_value=0)
    has_cr_card = st.radio('Has Credit Card', ['Yes', 'No'])
    has_cr_card = 1 if has_cr_card=='Yes' else 0
    is_active_member = st.radio('Is Active Member', ['Yes', 'No'])
    is_active_member = 1 if is_active_member=='Yes' else 0
    estimated_salary = st.number_input('Estimated Salary', min_value=0.0, format='%f')
    
    # Additional input fields
    mem_no_products = st.number_input('Membership Number of Products', min_value=0)
    cred_bal_sal = st.number_input('Credit Balance Salary Ratio', min_value=0.0, format='%f')
    bal_sal = st.number_input('Balance Salary Ratio', min_value=0.0, format='%f')
    tenure_age = st.number_input('Tenure Age Ratio', min_value=0.0, format='%f')
    age_tenure_product = st.number_input('Age Tenure Product', min_value=0)
    
    # Submit button for single record
    if st.button('Predict for single record'):
        # Convert inputs to the format expected by the model
        # (This may include encoding categorical variables, scaling, etc.)
        single_record = pd.DataFrame([[credit_score, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary, country, gender, mem_no_products, cred_bal_sal, bal_sal, tenure_age, age_tenure_product]],
                                     columns=['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Country', 'Gender', 'Mem__no__Products', 'Cred_Bal_Sal', 'Bal_sal', 'Tenure_Age', 'Age_Tenure_product'])
        # Predict and display the result
        prediction = model.predict(single_record)
        st.write('Prediction for the provided record is:', prediction[0])

elif input_method == "Upload a file":
    # File uploader allows user to add their own CSV
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the data into a pandas dataframe
        data = pd.read_csv(uploaded_file)
        
        # Predict the 'Exited' feature
        predictions = model.predict(data.drop(columns=['Exited','Surname','Surname_tfidf_0', 'Surname_tfidf_1', 'Surname_tfidf_2','Surname_tfidf_3', 'Surname_tfidf_4']))
        
        # Combine the predictions with the original data
        data['Predicted Exited'] = predictions
        
        # Display the dataframe with a scrollbar
        st.dataframe(data, height=300)
        
        # Allow the user to download the result as a CSV
        st.download_button(label='Download CSV with predictions', data=data.to_csv(), file_name='predicted_churn.csv', mime='text/csv')

# Add any additional functionality you need below
