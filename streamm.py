import streamlit as sl
import pandas as pd
sl.write("""
# Shankar's First app
Hello *World!*, I am Shankar
""")

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
