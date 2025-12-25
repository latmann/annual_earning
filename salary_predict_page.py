import streamlit as st
import joblib
import numpy as np

def load_model():
    data = joblib.load('data.joblib')
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():
    st.title('Software Developer Salary Prediction')

    st.write("""### We need some information to predict the salary""")

    countries = (
        'United States',
        'India',
        'United Kingdom',
        'Germany',
        'Canada',
        'Brazil',
        'France',
        'Spain',
        'Australia',
        'Netherlands',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden',

    )

    education = (
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Master’s degree',
        'Post grad',

    )

    country = st.selectbox('Country', countries)
    education = st.selectbox('Education level', education)

    experience = st.slider('Years of experience',0,50,3)

    ok = st.button('Calculate salary')
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float) 

        salary = regressor.predict(X)
        st.subheader(f'The estimated salary is ${salary[0]:.2f}') 