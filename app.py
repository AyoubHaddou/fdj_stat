from json import encoder
import streamlit as st 
import pandas as pd
from streamlit import cursor 
from pymongo import MongoClient




client = MongoClient('mongodb+srv://ayoub:dnU*r*kNQXMj2pv@cluster0.pblvj.mongodb.net/test')
db = client.Database_scrapy.Loto2
# db_test = pd.read_json('Loto2.json',orient='records', encoding='utf-8')
# cursor_test = list(db.find({},{'_id':0}))
cursor = list(db.find({},{'_id':0}))


df = pd.DataFrame(cursor)
a = [i for i in df['Numero']]
df2 = pd.DataFrame(a)


# df1 = pd.DataFrame({'Annee' : 2019, 'Jour' : 10 , 'Numero' : ['1,2,3']})

# st.write(df2)
st.sidebar.selectbox('Hello',['Datafram','Statistiques'])
st.write(df)
st.write(df2)




