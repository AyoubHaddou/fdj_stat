from json import encoder
from pandas.core.indexes.base import Index
import streamlit as st 
import pandas as pd
from streamlit import cursor 
from pymongo import MongoClient
from fonction import * 
import plotly.graph_objects as go
import plotly.express as px


# => Import de ma database sur mongodb cloud 
# client = MongoClient('mongodb+srv://ayoub:dnU*r*kNQXMj2pv@cluster0.pblvj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
client = MongoClient(**st.secrets["mongo"])
db = client.Database_scrapy.Loto2

# Declaration des variables et des listes et des Df
a = st.sidebar.selectbox('Hello',['Accueil','Recherches','Visualisations','FDJ-Generator'])
col1,col2,col3 = st.columns(3)
acol1,acol2 = st.columns(2)
numeros_chance = [i for i in range (1,11)]
numeros_complet = [i for i in range(1,50)]

cursor = list(db.find({},{'_id':0}))
df = pd.DataFrame(cursor)
n = [n for n in df['Numero']]
df2 = pd.DataFrame(n)
df2.index += 1 

table_chance_100 = []
for i in numeros_chance:
    table_chance_100.append({'N° chance' :  i, 'en %' : (count_number_chance(df,i) / 2094 * 100)})
df_table_chance_100 = pd.DataFrame(table_chance_100)
df_table_chance_100.index = numeros_chance

table_100 = []
for i in numeros_complet:
    table_100.append({'Numero' :  i, 'en %' : (count_number(df,i) *100 / (len(df)*5))})
df_table_100 = pd.DataFrame(table_100)
df_table_100.index +=1 

table_c_100 = []
for i in numeros_complet:
    table_c_100.append({'Nombre de sortie' :  count_number(df,i), 'En %' : float(count_number(df,i)* 100 / (len(df)*5))})
main_df_1 = pd.DataFrame(table_c_100)
main_df_1.index +=1 

table_c_100_chance = []
for i in numeros_chance:
    table_c_100_chance.append({'Nombre de sortie' :  count_number_chance(df,i), 'En %' : float(count_number_chance(df,i)* 100 / len(df))})
main_df_2 = pd.DataFrame(table_c_100_chance)
main_df_2.index += 1 



if a == 'Accueil':
    st.title('FDJ - Statistiques \n--------')
    st.header('Quelques opérations mathématiques pour devenir Millionnaire ? ')
    st.text('Ici vous trouverez les résultats du Loto depuis janvier 2009. ')
    st.text("Des applications mathématiques permettent d'obtenir toute sorte d'informations et de \nvisualisations graphiques que je vous propose sur ce site.")
    st.text("Clic sur l'onglet Recherche ou visualisation pour en savoir plus. \n ")
    st.markdown('--------------\nCeci est un site à but éducatif et récréatif. Je déni toute responsabilité de perte aux jeux. Si toutefois vous gagnez, n\'hésitez pas à me remercier sur azerty@gmail.com')

if a == 'Recherches':

    with acol2:
        st.subheader('Recherche')
        search_5 = st.selectbox('Dans les 5 numéros:', main_df_1.index)
        apply_5 = st.button('Appliquer pour les 5 numéros')
        apply_6 = st.button('Appliquer le filtre pour tout les numéros')
        search_1 = st.selectbox('Pour le numéro chance :', main_df_2.index)
        apply_1 = st.button('Appliquer pour le numéro chance')

    with acol1 :
        st.subheader('Liste des tirages depusi 2009')
        if apply_5:
            st.dataframe(mask_search_5(df2,search_5), height=400)
        elif apply_1:
            st.dataframe(mask_search_1(df2,search_1), height=400)
        elif apply_6:
            st.dataframe(mask_all(df2,search_5), height=400)
        else:
            st.dataframe(df2, height=330)

    apply_a = st.selectbox('Recherche avancé :', [i for i in range(0,50)])
    if apply_a > 0 :
        with acol1:
            st.write('Recherche avancé pour les 5 Numéros :')
            st.dataframe(main_df_1.loc[apply_a:apply_a])
        with acol2:
            if apply_a <= 10 :
                st.write('Recherche avancé pour le numéro bonus')
                st.dataframe(main_df_2.loc[apply_a:apply_a])
    else:
        with acol1:
            st.subheader('Recherche avancé pour les 5 Numéros :')
            st.dataframe(main_df_1)
        with acol2:
            st.subheader('Recherche avancé pour le N° chance :')
            st.dataframe(main_df_2)
    st.text('On remarque des tendances de parution à 2 et 10% \nClic sur visualisation pour en voir plus à ce sujet.')


if a == "FDJ-Generator":
    with acol1:
        st.write('Voici les 10 numéros les moins parut depuis 2009 :')
        main_df_1['En %'] = main_df_1['En %'].sort_values()
        st.dataframe(main_df_1[0:10])   
    with acol2:
        st.write('Voici les 5 premiers numéros chances les moins parrut depuis 2009:')
        main_df_2['En %'] = main_df_2['En %'].sort_values()
        st.dataframe(main_df_2[0:5], height=350)
        st.write('Voici les parrutions par tranche de dizaine depuis 2009 :')
        tenth = count_tenth(df2)
        st.write(pd.DataFrame(tenth, index=tenth.keys())[0:1])

    st.write(f'Voici donc une séries aléatoire en tenant compte des informations précédentes: ')
    gen = st.button('Clic pour générer un code')
    if gen:
        st.text('Voici ton code :')
        st.selectbox('Quelques tirages possibles',gen_loto(df2))



if a == 'Visualisations':

    st.subheader('Visualisation du camanbert de la repartition des tirages')
    fig6 = px.pie(main_df_1, values=main_df_1['Nombre de sortie'], names=[i for i in range(1,50)])
    st.write(fig6)
    st.markdown('On constate un équilibre des tirages autour des 2% pour les 5 numéros')

    st.subheader('\nVisualisation du camanbert de la repartition des tirages du num chance')
    fig7= px.pie(main_df_2, values=main_df_2['Nombre de sortie'], names=[i for i in range(1,11)])
    st.write(fig7)
    st.markdown('On constate aussi un équilibre des tirages autour des 10% pour le numéro chance')


    st.subheader('Histogramme des 5 numéros')
    fig1 = px.bar(main_df_1, x=main_df_1.index, y='Nombre de sortie')
    st.write(fig1)
    fig2 = go.Figure(
    data=[go.Bar(y=main_df_1['En %'],x=numeros_complet)],
    layout_title_text="'Histogramme des 5 numéros en pourcentage")
    st.write(fig2)

    st.subheader('Histogramme du numéro chance')
    fig3 = px.bar(main_df_2, x=main_df_2.index, y='Nombre de sortie')
    st.write(fig3)
    fig4 = go.Figure(
    data=[go.Bar(y=main_df_2['En %'],x=numeros_chance)],
    layout_title_text="Histogramme du numéro chance en pourcentage")
    st.write(fig4)


    fig5 = px.histogram(df2.loc[0:,0:4])
    st.write(fig5)


    st.text('Pourrait-on prévoir que les numéro qui n\'ont pas encore atteint les 2% \nsont plus suceptible de sortir lors des prochains tirages ?')
    st.text('Clic sur l\'onglet FDJ-GENERATOR pour obtenir ton jeux aléatoire \nen tenant compte des ses informations')


# Pour plus tard ? 

# num = []
# for i in range(1,50):
#     num.append({'Numero :'+str(i) : count_number(df,i)})
# num_df = pd.DataFrame(num)
# num_df.index += 1 

# num_p = []
# for i in range(1,50):
#     num_p.append({i : count_number(df,i) * 100 / (len(df)*5)})
# num_p_df = pd.DataFrame(num_p)
# num_p_df.index = [i for i in range (1,50)]
# num_chance = []
# for i in range(1,11):
#     num_chance.append({i : count_number_chance(df,i)})
# df_num_chance = pd.DataFrame(num_chance)
# df_num_chance.index += 1

# num_chance_p = []
# for i in range(1,11):
#     num_chance_p.append({i : count_number_chance(df,i) / 2094 *100})
# df_num_chance_p = pd.DataFrame(num_chance_p)
# df_num_chance_p.index += 1 

# if a == 'Visualisations':
#     st.header('Visualisations des tirages sur les 5 numéros')
#     st.subheader('Nombre de parution :')
#     st.bar_chart(num_df)
#     st.subheader('Nombre de parution en pourcentage')
#     st.bar_chart(num_p_df)
#     st.header('Visualisations des tirages pour le numéro chance')
#     st.subheader('Nombre de parution :')
#     st.bar_chart(df_num_chance)
#     st.subheader('Nombre de parution en pourcentage')
#     st.bar_chart(df_num_chance_p)
#     st.text('Les tendances à 2% pour les 5 numéros et à 10% pour le numéro chance \nsont bien visibles par ses graphiques')
#     st.text('Pourrait-on prévoir que les numéro qui n\'ont pas encore atteint les 2% \nsont plus suceptible de sortir lors des prochains tirages ?')
#     st.text('Clic sur l\'onglet FDJ-GENERATOR pour obtenir ton jeux aléatoire \nen tenant compte des ses informations')

# if a == 'En vrac':
#     with col1:
#         st.write('Les 5 N° - Parution en %')
#         st.dataframe(df_table_100)
        
#     with col2:
#         st.write('Le N° chance - Parution en %')
#         st.dataframe(df_table_chance_100)
        
#     with col3:
#         st.write('Nombre de parution de chaque dizaine depuis 2009')
#         st.write(count_tenth(df2))