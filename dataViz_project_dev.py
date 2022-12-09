import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


# Tableau de bord de l'application
with st.sidebar:
            st.image("datagouv.jpg")
            menu = option_menu(
                "Dashboard", ["2020", '2019', '2018'], 
                icons=['bar-chart-fill', 'bar-chart-fill', 'bar-chart-fill'], menu_icon="cast", default_index=1,
                styles={
                    "icon": {"color": "orange", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                })
            menu


#=================================================================================================================================



#Chargement du jeu de données et enrichissement
df_20=pd.DataFrame()
df_19=pd.DataFrame()
df_18=pd.DataFrame()

@st.cache
def chargement_20():
    
    #Lecture des dataframe
    df_20_initial = pd.read_csv("data/sample_2020.csv",low_memory=False)

    #Sélection des colonnes utiles pour notre user
    df_20 = df_20_initial[["date_mutation", "nature_mutation", "valeur_fonciere", "code_departement", "nombre_pieces_principales", "latitude", "longitude"]]

    #Définitions des fonctions d'enrichissement du jeu de données
    def to_datetime(dt):
        return pd.to_datetime(dt)
    def get_month(dt):
        return dt.month

    #Modification et enrichissement du jeu de données
    df_20.date_mutation=df_20['date_mutation'].map(to_datetime)
    df_20['mois_mutation']=df_20['date_mutation'].map(get_month)
    return df_20

@st.cache
def chargement_19():
    
    #Lecture des dataframe
    df_19_initial = pd.read_csv("data/sample2_2019.csv",low_memory=False)

    #Sélection des colonnes utiles pour notre user
    df_19 = df_19_initial[["date_mutation", "nature_mutation", "valeur_fonciere", "code_departement", "nombre_pieces_principales", "latitude", "longitude"]]


    #Définitions des fonctions d'enrichissement du jeu de données
    def to_datetime(dt):
        return pd.to_datetime(dt)
    def get_month(dt):
        return dt.month

    #Modification et enrichissement du jeu de données
    df_19.date_mutation=df_19['date_mutation'].map(to_datetime)
    df_19['mois_mutation']=df_19['date_mutation'].map(get_month)
    return df_19


@st.cache
def chargement_18():
    
    #Lecture des dataframe
    df_18_initial = pd.read_csv("data/sample2_2018.csv",low_memory=False)

    #Sélection des colonnes utiles pour notre user
    df_18 = df_18_initial[["date_mutation", "nature_mutation", "valeur_fonciere", "code_departement", "nombre_pieces_principales", "latitude", "longitude"]]

    #Définitions des fonctions d'enrichissement du jeu de données
    def to_datetime(dt):
        return pd.to_datetime(dt)
    def get_month(dt):
        return dt.month

    #Modification et enrichissement du jeu de données
    df_18.date_mutation=df_18['date_mutation'].map(to_datetime)
    df_18['mois_mutation']=df_18['date_mutation'].map(get_month)
    return df_18


df_20=chargement_20()
df_19=chargement_19()
df_18=chargement_18()

#=================================================================================================================================


#Petite fonction permettant de déterminer le nombre d'occurences
def count_rows(dt):
    return len(dt)

#======================================Data visualisation==================================================


#Analyse temporelle de la valeur foncière
def evol_temporelle_20():
    st.title("Analyse temporelle de la valeur foncière")
    st.bar_chart(df_20, x='mois_mutation', y='valeur_fonciere')


    #Même graphique mais avec un diagramme circulaire
    fig1_20=px.pie(df_20, values='valeur_fonciere', names='mois_mutation', title="Evolution temporelle de la valeur foncière sur l'ensemble du territoire")

    #Analyse du nombre de mutations par mois
    fig2_20=px.histogram(df_20, x="mois_mutation",text_auto=True, title="Nombre de mutations par mois")
    fig2_20.update_layout(bargap=0.2)

    selectbox_option = st.selectbox("Plus d'analyse temporelle",('Valeur fonciere (pie chart)','Nombre de mutations'))
    if selectbox_option=="Valeur fonciere (pie chart)":
        st.plotly_chart(fig1_20, use_container_width=True)
    elif selectbox_option =="Nombre de mutations":
        st.plotly_chart(fig2_20, use_container_width=True)


def evol_temporelle_19():
    st.title("Analyse temporelle de la valeur foncière")
    st.bar_chart(df_19, x='mois_mutation', y='valeur_fonciere')


    #Même graphique mais avec un diagramme circulaire
    fig1_19=px.pie(df_19, values='valeur_fonciere', names='mois_mutation', title="Evolution temporelle de la valeur foncière sur l'ensemble du territoire")

    #Analyse du nombre de mutations par mois
    fig2_19=px.histogram(df_19, x="mois_mutation",text_auto=True, title="Nombre de mutations par mois")
    fig2_19.update_layout(bargap=0.2)

    selectbox_option = st.selectbox("Plus d'analyse temporelle",('Valeur fonciere (pie chart)','Nombre de mutations'))
    if selectbox_option=="Valeur fonciere (pie chart)":
        st.plotly_chart(fig1_19, use_container_width=True)
    elif selectbox_option =="Nombre de mutations":
        st.plotly_chart(fig2_19, use_container_width=True)


def evol_temporelle_18():
    st.title("Analyse temporelle de la valeur foncière")
    st.bar_chart(df_18, x='mois_mutation', y='valeur_fonciere')


    #Même graphique mais avec un diagramme circulaire
    fig1_18=px.pie(df_18, values='valeur_fonciere', names='mois_mutation', title="Evolution temporelle de la valeur foncière sur l'ensemble du territoire")

    #Analyse du nombre de mutations par mois
    fig2_18=px.histogram(df_18, x="mois_mutation",text_auto=True, title="Nombre de mutations par mois")
    fig2_18.update_layout(bargap=0.2)

    selectbox_option = st.selectbox("Plus d'analyse temporelle",('Valeur fonciere (pie chart)','Nombre de mutations'))
    if selectbox_option=="Valeur fonciere (pie chart)":
        st.plotly_chart(fig1_18, use_container_width=True)
    elif selectbox_option =="Nombre de mutations":
        st.plotly_chart(fig2_18, use_container_width=True)


#=================================================================================================================================


#Analyse géographique de la valeur foncière
def evol_geographique_20():
    st.title('Analyse géographique de la valeur foncière')
    
    #Analyse combinée du nombre de mutations et de la valeur foncière par département
    dep_nb_mutations = df_20.groupby("valeur_fonciere").apply(count_rows)
    fig4_20 = go.Figure(
        data=[
            go.Bar(x=df_20['code_departement'], y=df_20['valeur_fonciere'], yaxis='y', offsetgroup=1, name='valeur_fonciere'),
            go.Bar(name='nombre de mutation', x=df_20["code_departement"].unique(), y=dep_nb_mutations, yaxis='y2', offsetgroup=2)
        ],
        layout={
            'yaxis': {'title': 'Valeur fonciere (in Billion) '},
            'yaxis2': {'title': 'Nombre de mutation par département', 'overlaying': 'y', 'side': 'right'},
            'xaxis' : {'title' : 'Departement'},
            'title' : "Visualisation de la valeur foncière et du nombre de mutations par département"
        }
    )
    fig4_20.update_layout(barmode='group')
    fig4_20.update_traces(marker_line_width = 0)
    st.plotly_chart(fig4_20, use_container_width=True)

    #Observation de la valeur foncière totale par département
    fig5_20 = go.Figure(
    data=[go.Bar(x=df_20['code_departement'], y=df_20['valeur_fonciere'])],
    layout={
        'yaxis': {'title': 'Valeur fonciere (in Billion) '},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Valeur fonciere par Departement'
        }
    )
    fig5_20.update_traces(marker_line_width = 0)

    #Observation du nombre de mutations par département
    fig3_20 = go.Figure(
    data=[go.Bar(x=df_20["code_departement"].unique(), y=dep_nb_mutations)],
    layout={
        'yaxis': {'title': "Nombre de mutations"},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Nombre de mutations par Departement'
        }
    )
    fig3_20.update_traces(marker_line_width = 0)

    #Utilisation de checkbox
    val_fonciere = st.checkbox('Uniquement valeur foncière par département')
    if val_fonciere:
        st.plotly_chart(fig5_20, use_container_width=False)
    nb_mutation = st.checkbox('Uniquement nombre de mutations par département')
    if nb_mutation:
        st.plotly_chart(fig3_20, use_container_width=False)

    #cartographie des valeurs foncière
    st.title("Cartographie des mutations") #Une mutation = une valeur foncière
    df_20_map=df_20[["valeur_fonciere", "longitude", "latitude"]]
    df_20_map.dropna(inplace=True)
    st.map(df_20_map)


def evol_geographique_19():
    st.title('Analyse géographique de la valeur foncière')
    
    #Analyse combinée du nombre de mutations et de la valeur foncière par département
    dep_nb_mutations = df_19.groupby("valeur_fonciere").apply(count_rows)
    fig4_19 = go.Figure(
        data=[
            go.Bar(x=df_19['code_departement'], y=df_19['valeur_fonciere'], yaxis='y', offsetgroup=1, name='valeur_fonciere'),
            go.Bar(name='nombre de mutation', x=df_19["code_departement"].unique(), y=dep_nb_mutations, yaxis='y2', offsetgroup=2)
        ],
        layout={
            'yaxis': {'title': 'Valeur fonciere (in Billion) '},
            'yaxis2': {'title': 'Nombre de mutation par département', 'overlaying': 'y', 'side': 'right'},
            'xaxis' : {'title' : 'Departement'},
            'title' : "Visualisation de la valeur foncière et du nombre de mutations par département"
        }
    )
    fig4_19.update_layout(barmode='group')
    fig4_19.update_traces(marker_line_width = 0)
    st.plotly_chart(fig4_19, use_container_width=True)

    #Observation de la valeur foncière totale par département
    fig5_19 = go.Figure(
    data=[go.Bar(x=df_19['code_departement'], y=df_19['valeur_fonciere'])],
    layout={
        'yaxis': {'title': 'Valeur fonciere (in Billion) '},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Valeur fonciere par Departement'
        }
    )
    fig5_19.update_traces(marker_line_width = 0)

    #Observation du nombre de mutations par département
    fig3_19 = go.Figure(
    data=[go.Bar(x=df_19["code_departement"].unique(), y=dep_nb_mutations)],
    layout={
        'yaxis': {'title': "Nombre de mutations"},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Nombre de mutations par Departement'
        }
    )
    fig3_19.update_traces(marker_line_width = 0)

    #Utilisation de checkbox
    val_fonciere = st.checkbox('Uniquement valeur foncière par département')
    if val_fonciere:
        st.plotly_chart(fig5_19, use_container_width=False)
    nb_mutation = st.checkbox('Uniquement nombre de mutations par département')
    if nb_mutation:
        st.plotly_chart(fig3_19, use_container_width=False)

    #cartographie des valeurs foncière
    st.title("Cartographie des mutations") #Une mutation = une valeur foncière
    df_19_map=df_19[["valeur_fonciere", "longitude", "latitude"]]
    df_19_map.dropna(inplace=True)
    st.map(df_19_map)



def evol_geographique_18():
    st.title('Analyse géographique de la valeur foncière')
    
    #Analyse combinée du nombre de mutations et de la valeur foncière par département
    dep_nb_mutations = df_18.groupby("valeur_fonciere").apply(count_rows)
    fig4_18 = go.Figure(
        data=[
            go.Bar(x=df_18['code_departement'], y=df_18['valeur_fonciere'], yaxis='y', offsetgroup=1, name='valeur_fonciere'),
            go.Bar(name='nombre de mutation', x=df_18["code_departement"].unique(), y=dep_nb_mutations, yaxis='y2', offsetgroup=2)
        ],
        layout={
            'yaxis': {'title': 'Valeur fonciere (in Billion) '},
            'yaxis2': {'title': 'Nombre de mutation par département', 'overlaying': 'y', 'side': 'right'},
            'xaxis' : {'title' : 'Departement'},
            'title' : "Visualisation de la valeur foncière et du nombre de mutations par département"
        }
    )
    fig4_18.update_layout(barmode='group')
    fig4_18.update_traces(marker_line_width = 0)
    st.plotly_chart(fig4_18, use_container_width=True)

    #Observation de la valeur foncière totale par département
    fig5_18 = go.Figure(
    data=[go.Bar(x=df_18['code_departement'], y=df_18['valeur_fonciere'])],
    layout={
        'yaxis': {'title': 'Valeur fonciere (in Billion) '},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Valeur fonciere par Departement'
        }
    )
    fig5_18.update_traces(marker_line_width = 0)

    #Observation du nombre de mutations par département
    fig3_18 = go.Figure(
    data=[go.Bar(x=df_18["code_departement"].unique(), y=dep_nb_mutations)],
    layout={
        'yaxis': {'title': "Nombre de mutations"},
        'xaxis' : {'title' : 'Departement'},
        'title' : 'Nombre de mutations par Departement'
        }
    )
    fig3_18.update_traces(marker_line_width = 0)

    #Utilisation de checkbox
    val_fonciere = st.checkbox('Uniquement valeur foncière par département')
    if val_fonciere:
        st.plotly_chart(fig5_18, use_container_width=False)
    nb_mutation = st.checkbox('Uniquement nombre de mutations par département')
    if nb_mutation:
        st.plotly_chart(fig3_18, use_container_width=False)

    #cartographie des valeurs foncière
    st.title("Cartographie des mutations") #Une mutation = une valeur foncière
    df_18_map=df_18[["valeur_fonciere", "longitude", "latitude"]]
    df_18_map.dropna(inplace=True)
    st.map(df_18_map)


#=================================================================================================================================


#Visualisation de l'impact du nombre de pièces sur la valeur foncière
def np_piece_impact_20():

    st.title("Observation du prix en fonction du temps et du nombre de chambres")
    color = st.select_slider(
     'Veuilez choisir le nombre de chambre.s',
     options=np.arange(0,35))
    
    df_20_slider=df_20[["valeur_fonciere", "mois_mutation", "nombre_pieces_principales"]]
    for i in range(0,35):
        if color==i:
            st.write("Vous avez choisi ",color, " pièce.s principale.s")
            df_20_slider_tmp=df_20_slider[df_20_slider["nombre_pieces_principales"]==i]

            #Valeur foncière par mois
            st.bar_chart(df_20_slider_tmp, x='mois_mutation', y='valeur_fonciere')

            #Nombre de mutations par mois
            fig6_20 = go.Figure(
                data=[go.Bar(x=df_20_slider_tmp["mois_mutation"].unique(), y=df_20_slider_tmp.groupby("valeur_fonciere").apply(count_rows))],
                layout={
                    'yaxis': {'title': "Nombre de mutations"},
                    'xaxis' : {'title' : 'Mois de la mutation'},
                    'title' : 'Nombre de mutations par mois et par nombre de pièces principales'
                    }
            )
            fig6_20.update_traces(marker_line_width = 0)
            st.plotly_chart(fig6_20, use_container_width=True)
            break

def np_piece_impact_19():

    st.title("Observation du prix en fonction du temps et du nombre de chambres")
    color = st.select_slider(
     'Veuilez choisir le nombre de chambre.s',
     options=np.arange(0,35))
    
    df_19_slider=df_19[["valeur_fonciere", "mois_mutation", "nombre_pieces_principales"]]
    for i in range(0,35):
        if color==i:
            st.write("Vous avez choisi ",color, " pièce.s principale.s")
            df_19_slider_tmp=df_19_slider[df_19_slider["nombre_pieces_principales"]==i]

            #Valeur foncière par mois
            st.bar_chart(df_19_slider_tmp, x='mois_mutation', y='valeur_fonciere')

            #Nombre de mutations par mois
            fig6_19 = go.Figure(
                data=[go.Bar(x=df_19_slider_tmp["mois_mutation"].unique(), y=df_19_slider_tmp.groupby("valeur_fonciere").apply(count_rows))],
                layout={
                    'yaxis': {'title': "Nombre de mutations"},
                    'xaxis' : {'title' : 'Mois de la mutation'},
                    'title' : 'Nombre de mutations par mois et par nombre de pièces principales'
                    }
            )
            fig6_19.update_traces(marker_line_width = 0)
            st.plotly_chart(fig6_19, use_container_width=True)
            break


def np_piece_impact_18():

    st.title("Observation du prix en fonction du temps et du nombre de chambres")
    color = st.select_slider(
     'Veuilez choisir le nombre de chambre.s',
     options=np.arange(0,35))
    
    df_18_slider=df_18[["valeur_fonciere", "mois_mutation", "nombre_pieces_principales"]]
    for i in range(0,35):
        if color==i:
            st.write("Vous avez choisi ",color, " pièce.s principale.s")
            df_18_slider_tmp=df_18_slider[df_18_slider["nombre_pieces_principales"]==i]

            #Valeur foncière par mois
            st.bar_chart(df_18_slider_tmp, x='mois_mutation', y='valeur_fonciere')

            #Nombre de mutations par mois
            fig6_18 = go.Figure(
                data=[go.Bar(x=df_18_slider_tmp["mois_mutation"].unique(), y=df_18_slider_tmp.groupby("valeur_fonciere").apply(count_rows))],
                layout={
                    'yaxis': {'title': "Nombre de mutations"},
                    'xaxis' : {'title' : 'Mois de la mutation'},
                    'title' : 'Nombre de mutations par mois et par nombre de pièces principales'
                    }
            )
            fig6_18.update_traces(marker_line_width = 0)
            st.plotly_chart(fig6_18, use_container_width=True)
            break
 


#==============================Fonction principale (main)===================================================
def main():
    if menu=="2020":
        st.title("Analyse des données de 2020")
        evol_temporelle_20()
        evol_geographique_20()
        np_piece_impact_20()

    elif menu=="2019":
        st.title("Analyse des données de 2019")
        evol_temporelle_19()
        evol_geographique_19()
        np_piece_impact_19()

    elif menu=="2018":
        st.title("Analyse des données de 2018")
        evol_temporelle_18()
        evol_geographique_18()
        np_piece_impact_18()

if __name__ == "__main__":
    main()






