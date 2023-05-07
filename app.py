import joblib
import streamlit as st

# loading the trained model
df = joblib.load(r"C:\Users\Venkatesham\Desktop\internship_2023\loan_prediction\model.joblib")


# defining the func

def prediction(Gender,Married,Education,ApplicantIncome,LoanAmount,Credit_History):
    if Gender == 'Male':
        Gender = 0
    else:
        Gender = 1
    
    if Married == 'Unmarried':
        Married = 0
    else:
        Married = 1

    if Education == 'Not Graduate':
        Education = 0
    else:
        Education = 1


    if Credit_History == 'Unclear Bebts':
        Credit_History = 0
    else :
        Credit_History = 1

    LoanAmount = LoanAmount/1000

    # making prediction

    prediction = df.predict([[Gender,Married,Education,ApplicantIncome,LoanAmount,Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred



# webpage
    st.title("Laptop Prediction")
    Gender = st.selectbox('Gender',('Male','Female'))
    Married = st.selectbox('Marital Status',('Unmarried','Married'))
    Education = st.selectbox('Education',('Not Graduate','Graduate'))
    ApplicantIncome = st.number_input('Applicants monthly income')
    LoanAmount = st.number_input('Total Loan amount')
    Credit_History = st.selectbox('Credit_history',('Unclear Debts','No Unclear Debts'))
    result =''

# prediction button
    if st.button('Prdict'):
        result = prediction(Gender,Married,Education,ApplicantIncome,LoanAmount,Credit_History)
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)

# if __name__=='__main__':
#     main()