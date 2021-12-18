from json import encoder
import streamlit as st 
import pandas as pd
from streamlit import cursor 
from pymongo import MongoClient
from fonction import * 
# import plotly.graph_objects as go
# import plotly.express as px


# => Import de ma database sur mongodb cloud 
client = MongoClient('mongodb+srv://ayoub:dnU*r*kNQXMj2pv@cluster0.pblvj.mongodb.net/test')
# client = MongoClient(**st.secrets["mongo"])
db = client.Database_scrapy.Loto2

# Declaration des variables et des listes et des Df
a = st.sidebar.selectbox('Hello',['En Datafram','Les 5 numéros gagnant','Le numéro chance','Recherche','With plotly'])
col1,col2,col3 = st.columns(3)
acol1,acol2 = st.columns(2)

cursor = list(db.find({},{'_id':0}))
df = pd.DataFrame(cursor)
n = [n for n in df['Numero']]
df2 = pd.DataFrame(n)
df2.index += 1 

table_chance_100 = []
for i in range(1,11):
    table_chance_100.append({'N° chance' :  i, 'en %' : (count_number_chance(df,i) / 2094 * 100)})
df_table_chance_100 = pd.DataFrame(table_chance_100)
df_table_chance_100.index = [i for i in range (1,11)]

table_100 = []
for i in range(1,50):
    table_100.append({'Numero' :  i, 'en %' : (count_number(df,i) / 2094 * 100)})
df_table_100 = pd.DataFrame(table_100)
df_table_100.index +=1 
num = []
for i in range(1,50):
    num.append({'Numero :'+str(i) : count_number(df,i)})
num_df = pd.DataFrame(num)
num_df.index += 1 

num_p = []
for i in range(1,50):
    num_p.append({i : count_number(df,i) / 2094 *100})
num_p_df = pd.DataFrame(num_p)
num_p_df.index = [i for i in range (1,50)]
num_chance = []
for i in range(1,11):
    num_chance.append({i : count_number_chance(df,i)})
df_num_chance = pd.DataFrame(num_chance)
df_num_chance.index += 1

num_chance_p = []
for i in range(1,11):
    num_chance_p.append({i : count_number_chance(df,i) / 2094 *100})
df_num_chance_p = pd.DataFrame(num_chance_p)
df_num_chance_p.index += 1 

table_chance_100_t = []
for i in range(1,11):
    table_chance_100_t.append({'Nombre de sortie' :  count_number_chance(df,i), 'Proba en %' : (count_number_chance(df,i) / 2094 * 100)})
df_table_chance_100_t = pd.DataFrame(table_chance_100_t)
df_table_chance_100_t.index += 1 

table_c_100 = []
for i in range(1,50):
    table_c_100.append({'Nombre de sortie' :  count_number(df,i), 'Proba en %' : float(count_number(df,i) / 2094 * 100)})
result = pd.DataFrame(table_c_100)
result.index +=1 

table_c_100_chance = []
for i in range(1,11):
    table_c_100_chance.append({'Nombre de sortie' :  count_number_chance(df,i), 'Proba en %' : float(count_number_chance(df,i) / 2094 * 100)})
result1 = pd.DataFrame(table_c_100_chance)
result1.index += 1 

if a == 'En Datafram':


    with acol1:
        st.write('Nombre et pourcentage de sortie gagnante des 5premiers numéros depuis 2009')
        st.dataframe(result)
        st.write('Les listes gagnante depuis janvier 2009')
        st.dataframe(df2)

    with acol2:
        st.write('Nombre et pourcentage de sortie gagnante pour le numero chance depuis 2009')
        st.dataframe(result1)
        st.write('Les listes avec dates')
        df.index += 1 
        st.write(df)




if a == 'Recherche':
    with col1:
        st.write('Les 5N - Parution en %')
        st.dataframe(table_100)
        
    with col2:
        st.write('Le N chance - Parution en %')
        st.dataframe(table_chance_100)

    with col3:
        st.write('Recherche par numéro :')
        st.selectbox('Numéro :', result.index)
        st.button('Appliquer')
        st.write('Recherche par numéro chance :')
        st.selectbox('Numéro :', result1.index)
        st.button('Appliquer ')

    st.write('Nombre de fois dans chaque dizaine :')
    st.write(count_tenth(df2))


if a == 'Les 5 numéros gagnant':
    st.subheader('Nombre de tirage pour chacun des 5 numéros')
    st.bar_chart(num_df)
    st.subheader('Nombre de tirage pour chacun des 5 numéros en pourcentage')
    st.bar_chart(num_p_df)
    st.subheader('Superposition du pourcentage et du nombre de sortie par numéro sous différentes vues')
    st.line_chart(result)
    st.area_chart(result)
    st.bar_chart(result)


if a == 'Le numéro chance':
    st.subheader('Nombre de tirage pour chaque numéro chance')
    st.bar_chart(df_num_chance)
    st.subheader('Nombre de tirage pour chacun numéro chance en pourcentage')
    st.bar_chart(df_num_chance_p)
    st.subheader('Superposition du pourcentage et du nombre de sortie par numéro sous différentes vues')
    st.line_chart(result1)
    st.area_chart(result1)
    st.bar_chart(df_table_chance_100_t)

# if a == 'With plotly':

#     fig = px.bar(result, x=result.index, y='Nombre de sortie')
#     st.write(fig)
#     fig = go.Figure(
#     data=[go.Bar(y=result['Proba en %'],x=[i for i in range(1,11)])],
#     layout_title_text="Nombre de sortie")
#     st.write(fig)


#     fig = go.Figure(
#     data=[go.Bar(y=result['Nombre de sortie'],x=[i for i in range(1,50)])],
#     layout_title_text="Nombre de sortie")
#     st.write(fig)


