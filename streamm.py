import streamlit as sl
import pandas as pd
sl.write("""
# My Fist StremLit app
Hello *World!*
""")
container=sl.empty()
container2=sl.empty()
user=container.text_input("Enter Username","Nick")
passw=container2.text_input("Enter Password",type="password")
if user == "shankar" and passw == "abc":
    container.empty()
    container2.empty()
    age=sl.slider("How old are you?",0,100,10)
    sl.write("I am "+str(age) +" years old")
    file1=sl.file_uploader("Choose an excel file only")
    if file1 is not None:
        df=pd.read_excel("C:\\Users\\Admin\\Downloads\\"+file1.name)
        sl.write(df)
        csv = df.to_csv().encode("utf-8")
        sl.download_button("Download data as CSV",csv,"myfile.csv","text/csv")

    dt=sl.date_input("Pick a date")
    sl.write("YOU SELECTED DATE : "+str(dt))

    pets=['Cats','Dogs','Cows']
    pet=sl.radio("Pick a pet",pets)
    sl.write("You chose "+pet)
else:
    sl.error("Invalid Credetials")
