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

def count_number(x,y):
    count = 0 
    for i in range(len(x['Numero'])):
        for j in x['Numero'][i][0:5]:
            if j == y :
                count += 1 
    return count

liste = []
for i in range(1,50):
    liste.append({i : count_number(df,i)})

# import plotly.express as px
# df = px.data.tips()
# fig = px.box(df, y="total_bill")
# st.write(fig.show())

st.subheader('Nombre de tirage pour chacun des 5 numéros')
st.bar_chart(liste)

def count_number_chance(x,y):
    count = 0 
    for i in range(len(x['Numero'])):
        for j in x['Numero'][i][5:]:
            if j == y :
                count += 1 
    return count

liste2 = []
for i in range(1,11):
    liste2.append({i : count_number(df,i)})
st.subheader('Nombre de tirage pour chaque numéro chance')
st.bar_chart(liste2)
