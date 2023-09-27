import streamlit as st 
import pandas as pd 
import pickle 

# loading the trained model
pickle_in = open('churn.pkl', 'rb') 
model  = pickle.load(pickle_in)

 #Create a Streamlit web app
st.title('Customer Churn Prediction App')

# Add input elements to collect new customer data
st.sidebar.header('Input Parameters')

# Example input fields (you should customize these to match your model's input features)
customer_name = st.sidebar.text_input('Customer Name')
contract_duration = st.sidebar.selectbox('Contract Duration', ['Month-to-month', 'One year', 'Two year'])
monthly_charges = st.sidebar.number_input('Monthly Charges', min_value=0.0)
total_charges = st.sidebar.number_input('Total Charges', min_value=0.0)


# Create a function to predict churn
def predict_churn(customer_name, contract_duration, monthly_charges, total_charges):
    # Prepare the input data as a dictionary
    new_data = {
        'Contract Duration': contract_duration,
        'Monthly Charges': monthly_charges,
        'Total Charges': total_charges
    }
    
    # Convert the input data into a DataFrame (you should adapt this to your data preprocessing)
    input_data = pd.DataFrame([new_data])
    
    # Make predictions
    prediction = model.predict(input_data)
    
    return prediction

# Add a button to trigger the prediction
if st.sidebar.button('Predict Churn'):
    prediction = predict_churn(customer_name, contract_duration, monthly_charges, total_charges)
    if prediction[0] == 0:
        st.sidebar.success(f'{customer_name} is predicted to stay.')
    else:
        st.sidebar.warning(f'{customer_name} is predicted to churn.')

# Add explanations or additional information as needed
st.write('Welcome to the Customer Churn Prediction App.')


