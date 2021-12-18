from json import encoder
import streamlit as st 
import pandas as pd
from streamlit import cursor 
from pymongo import MongoClient
from fonction import * 


# Import de ma database sur mongodb cloud 
client = MongoClient('mongodb+srv://ayoub:dnU*r*kNQXMj2pv@cluster0.pblvj.mongodb.net/test')
# client = MongoClient(**st.secrets["mongo"])
db = client.Database_scrapy.Loto2

cursor = list(db.find({},{'_id':0}))
df = pd.DataFrame(cursor)
n = [n for n in df['Numero']]
df2 = pd.DataFrame(n)

# Declaration des variables et des listes
a = st.sidebar.selectbox('Hello',['En Datafram','Les 5 numéros gagnant','Le numéro chance','Recherche'])
col1,col2,col3 = st.columns(3)

table_chance_100 = []
for i in range(1,11):
    table_chance_100.append({'N° chance' :  i, 'Proba en %' : (count_number_chance(df,i) / 2094 * 100)})

table_100 = []
for i in range(1,50):
    table_100.append({'Numero' :  i, 'Proba en %' : (count_number(df,i) / 2094 * 100)})

num = []
for i in range(1,50):
    num.append({'Numero :'+str(i) : count_number(df,i)})

num_p = []
for i in range(1,50):
    num_p.append({i : count_number(df,i) / 2094 *100})

num_chance = []
for i in range(1,11):
    num_chance.append({i : count_number_chance(df,i)})

num_chance_p = []
for i in range(1,11):
    num_chance_p.append({i : count_number_chance(df,i) / 2094 *100})

table_chance_100_t = []
for i in range(1,11):
    table_chance_100_t.append({'Nombre de sortie' :  count_number_chance(df,i), 'Proba en %' : (count_number_chance(df,i) / 2094 * 100)})

table_c_100 = []
for i in range(1,50):
    table_c_100.append({'Nombre de sortie' :  count_number(df,i), 'Proba en %' : float(count_number(df,i) / 2094 * 100)})
    
result = pd.DataFrame(table_c_100)
result.index = [i for i in range(1,50)]

table_c_100_chance = []
for i in range(1,11):
    table_c_100_chance.append({'Nombre de sortie' :  count_number_chance(df,i), 'Proba en %' : float(count_number_chance(df,i) / 2094 * 100)})

result1 = pd.DataFrame(table_c_100_chance)
result1.index = [i for i in range(1,11)]

if a == 'En Datafram':

    st.write('Les listes gagnante depuis janvier 2009')
    st.dataframe(df2)
    st.write('Nombre et pourcentage de sortie gagnante des 5premiers numéros depuis 2009')
    st.dataframe(result)
    st.write('Nombre et pourcentage de sortie gagnante pour le numero chance depuis 2009')
    st.dataframe(result1)

    st.write('Les listes avec dates')
    st.write(df)

if a == 'Recherche':
    with col1:
        st.write('Numéro gagnant en %')
        st.dataframe(table_100)
        
    with col2:
        st.write('Numéro chance en %')
        st.dataframe(table_chance_100)

    with col3:
        st.write('Recherche par numéro :')
        st.selectbox('Numéro :', result.index)
        st.button('Appliquer')
        st.write('Recherche par numéro chance :')
        st.selectbox('Numéro :', result1.index)
        st.button('Appliquer ')


if a == 'Les 5 numéros gagnant':
    st.subheader('Nombre de tirage pour chacun des 5 numéros')
    st.bar_chart(num)
    st.subheader('Nombre de tirage pour chacun des 5 numéros en pourcentage')
    st.bar_chart(num_p)
    st.bar_chart(table_c_100)
    st.line_chart(result)
    st.area_chart(result)


if a == 'Le numéro chance':
    st.subheader('Nombre de tirage pour chaque numéro chance')
    st.bar_chart(num_chance)
    st.subheader('Nombre de tirage pour chacun numéro chance en pourcentage')
    st.bar_chart(num_chance_p)
    st.bar_chart(table_chance_100)
    st.bar_chart(table_chance_100_t)
    st.line_chart(result1)
    st.area_chart(result1)



