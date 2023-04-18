import streamlit as st
import pandas as pd


st.write("""
# Identify the largest number

This app identifies the largest number of the three numbers entered by the user
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("Enter First Number")
    fn = first_number
    second_number = st.number_input("Enter Second Number")
    sn = second_number
    third_number = st.number_input("Enter Third Number")
    tn = third_number
    lst = [fn,sn,tn]
    largest_number = lst[0]
    for number in lst:
       if number > largest_number:
         largest_number = number
    st.write('The largest number is:',largest_number)
    data = {'First Number entered is': first_number,
            'Second Number entered is': second_number,
            'Third Number entered is': third_number,
            }
    features = pd.DataFrame(data, index=[0])
    return features
    

df = user_input_features()
   
#st.subheader('User Input parameters')
#st.write(df.to_dict())


   



