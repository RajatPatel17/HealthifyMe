import os 
import pandas as pd
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_api_key = os.getenv('Google_API_KEY2')

# Configure THe Model

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    api_key = gemini_api_key
)


# Design the UI of Application
st.title(":orange[HealthifyMe:] :red[Your Personal Health Assistant]")
st.markdown('''
This Application will Assist you to get better Health Advice.  You can ask your health related issues and get
the personalized guidance.
''')
st.write('''
Follow these Steps :
* Enter Your Details in Sidebar
* Rate Your activity and firness on the scale of 0-5
* Submit your Details
* Ask Your question on the main page
* Click Generate and wait few seconds to get Guidance
''')


# Design the sidebar for all the user parameters

st.sidebar.header(':orange[Enter Your Details]')
name = st.sidebar.text_input('Enter Your Name')
gender = st.sidebar.selectbox('Select Your Gender',['Male','Female'])
age = st.sidebar.text_input('Enter Your Age')
weight = st.sidebar.text_input('Enter Your Weight in Kgs')
height = st.sidebar.text_input('Enter Your Height in cms')
bmi = pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)
active = st.sidebar.slider('Rate Your activity (0-5)',0,5,step=1)
fitness = st.sidebar.slider('Rate Your fitness (0-5)',0,5,step=1)
if st.sidebar.button('Submit'):
    st.sidebar.write(f"{name} your BMI is {round(bmi,2)} Kg/m^2 ")


# Now lets use the gemini model to generate the report
user_input = st.text_input('Ask me your question')
prompt =  f'''
<Role> You are an expert in Health and wellness and have 10+ years
 experience in guiding people
 <Goal> Generate the customizedreport addressing the problem the user has asked.Here is the queston that user Has asked s{user_input}
 <Context> here are the deatails that the user has provided
 name ={name}
 height = {height}
 weight = {weight}
 gender = {gender}
 bmi ={bmi}
 age = {age}
 activity rating =(0,5)
 fitness rating =(0,5)

 
 <Format> Folloeing should be the outline of the report in the sequence provided
 *Start with 2-3line of coomments on th details taht user has provide
 *Explain what real  problem could be on the basis of inpu the user provided 
 * Suggest the possible  reasons for the problem
 * sugeests the possible solutions
 * mention the doctor from which spacialization can visited if required
 * mention any change in the dieswhich us required.
 * In last create a final summary of all the things that has been discussed in the report 

 <Instructions>
 * Use bullet points where ever possible.
 * Create tables to represent any data where ever possible.
 * Strictly do not advice any medicine. 
 
 '''

if st.button('Generate-Report'):
    response = model.invoke(prompt)
    st.write(response.content)