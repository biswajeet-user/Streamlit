import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Biswajeet Nayak(Title)")
st.header("Biswajeet Nayak(Header)")
st.subheader("Biswajeet Nayak(Subheader)")
st.write("Biswajeet Nayak(Text)") #write method = print()
st.markdown("Biswajeet Nayak(Markdown)")
st.caption("Biswajeet Nayak(Caption)")


st.image("Biswa.jpeg")


#checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("Welcome")

#button
st.button("Submit")
#radio--->bullet point
st.radio("Pick your city",['Rajgangpur','Rourkela','Panposh'])
#selectbox--->dropdown
st.selectbox("Pick your city",['Rajgangpur','Rourkela','Panposh'])
#multiselect
st.multiselect("Choose your favorite sports",["Cricket",'Football','baseball'])
#slider
st.select_slider("give a remark",['good','best','excellent'])
st.slider("your mark",0,100)



toggle = st.toggle("Activate")
if toggle:
    st.write("welcome to the features")

number = st.number_input("Enter a Number")
st.write("you entered",number)

date = st.date_input("Enter your DOB", value=None)
st.write("your DOB",date)

Time= st.time_input("set alarm",value=None)  #value=None means,No implicit value will be added.

st.number_input("Enter a number")
st.text_input("Enter a text")
st.date_input("Enter Date",value=None)
st.time_input("enter time")
st.text_area("description")
st.file_uploader("Upload your file")
st.color_picker("choose a color")




st.sidebar.title("My life My rule")
st.sidebar.image("Biswa.jpeg")




st.success("success")
st.error("error")
st.warning("warning")
st.info("information")
st.exception(RuntimeError("RuntimeErrorException"))



df=pd.DataFrame(np.random.randn(50,20),columns=('col %d'% i for i in range(20)))
#(np.random.randn(50,20)-->This generate a 50*20(50 rows and 20 cols) numpy array of random numbers drawn from a standatrd norml distribution(mean=0,std=1)
#columns=('col %d'% i for i in range(20)))--> col from col0 to col 19
st.dataframe(df)



df=pd.DataFrame(np.random.randn(10,5),columns=('col %d'% i for i in range(5)))
st.table(df)

#Basically both st.dataframe(df)=st.table(df), but have some minute difference like table structure instance dataframe has rounded corner while table has no rounded corner and slightly difference in colour



#Highlighters
col1,col2,col3=st.columns(3)
col1.metric('Temperature','70 ^ F','1.2 ^F')
col2.metric('Wind','9 mph','-4%')
col3.metric('Humidity','70%','1.2%')

col,tol=st.columns(2)
col.metric('Weight','70kg')




prompt = st.chat_input("say something")
if prompt:
    st.write("User has entered prompt = ",prompt)




with st.status("step 1"):
    st.write('step 2')
    time.sleep(1)
    st.write('step 3')
    time.sleep(1)
    st.write('step 4')
    time.sleep(1)
st.button("Rerun")





chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.table(chart_data)
st.area_chart(chart_data)


bar_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.bar_chart(bar_data)

line_data=pd.DataFrame(np.random.randn(20,2),columns=['a','b'])
st.line_chart(line_data)

df=pd.DataFrame({'lat':[18.5164],
                 'lon':[73.8561]})
st.map(df)

line_data=pd.DataFrame(np.random.randn(20,2),columns=['a','b'])
st.scatter_chart(line_data)

with st.chat_message("user"):
    st.write("Hello")
    


















