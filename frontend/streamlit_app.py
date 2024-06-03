# import streamlit as st
# import requests

# st.title('Iris Species Prediction')

# sepal_length = st.slider('Sepal Length', 4.0, 8.0)
# sepal_width = st.slider('Sepal Width', 2.0, 5.0)
# petal_length = st.slider('petal Length', 1.0, 6.9)
# petal_width = st.slider('petal Width', 0.0, 2.5)

# #Convert to float
# sepal_length=float(sepal_length)
# sepal_width=float(sepal_width)
# petal_length = float(petal_length)
# petal_width = float(petal_width)

# input_data = {
#             "features": [sepal_length, 
#                         sepal_width,
#                         petal_length, 
#                         petal_width]
            
#               }  
# st.write(input_data)
# response = requests.post('http://127.0.0.1:8000/predict/', json=input_data)
# st.write(response.json())
# prediction = response.json()
# st.write(f"Predicted Species: {prediction}")


import streamlit as st
import requests

st.title('Iris Species Prediction')

# User inputs
sepal_length = st.slider('Sepal Length', 4.0, 8.0)
sepal_width = st.slider('Sepal Width', 2.0, 5.0)
petal_length = st.slider('Petal Length', 1.0, 6.9)
petal_width = st.slider('Petal Width', 0.0, 2.5)

# Convert to float
sepal_length = float(sepal_length)
sepal_width = float(sepal_width)
petal_length = float(petal_length)
petal_width = float(petal_width)

input_data = {
    "features": [sepal_length, sepal_width, petal_length, petal_width]
}

st.write(input_data)

# Send request to FastAPI backend
# In streamlit_app.py
response = requests.post('http://backend:8000/predict/', json=input_data) 

if response.status_code == 200:
    prediction = response.json()
    st.write(f"Predicted Species: {prediction}")

    # Display the numerical values in a textbox
 #   st.text_area("Numerical Prediction Values", prediction)
else:
    st.write("Error: Unable to get prediction from the API.")
