import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gdown
st.title("Analyse des données Uber - Avril 2014")

# Télécharger le fichier CSV à partir de Google Drive
url = "https://drive.google.com/uc?id=1qoK_zLLWWPjY3HaPN4WXH2q1OayJiQtz"
gdown.download(url, "uber-raw-data-apr14.csv", quiet=False)

# Charger les données
df = pd.read_csv("uber-raw-data-apr14.csv", delimiter=',')
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Fonctions pour extraire les informations pertinentes
def get_dom(dt):
    return dt.day

def get_weekday(dt):
    return dt.weekday()

def get_hour(dt):
    return dt.hour

# Appliquer les fonctions pour extraire les informations pertinentes
df['day'] = df['Date/Time'].map(get_dom)
df['weekday'] = df['Date/Time'].map(get_weekday)
df['hour'] = df['Date/Time'].map(get_hour)

# Afficher les premières lignes, les dernières lignes et les informations du DataFrame
st.subheader("Premières lignes")
st.write(df.head())

st.subheader("Dernières lignes")
st.write(df.tail())

st.subheader("Nombre de lignes")
st.write(df.shape[0])

st.subheader("Statistiques descriptives")
st.write(df.describe())


# Créer un histogramme de la distribution du jour du mois
st.subheader("Distribution de la frequence par jour du mois")
fig, ax = plt.subplots()
hist = ax.hist(df["day"], bins=30, rwidth=0.8, range=(0.5, 30.5))

ax.set_xlabel("Days of the month")
ax.set_ylabel("Frequency")

st.pyplot(fig)

def count_rows(rows):
    return len(rows)

by_date = df.groupby('day').apply(count_rows)

# Créer un line plot de la distribution du jour du mois
st.subheader("Distribution de la frequence par jour du mois")
fig, ax = plt.subplots()
ax.plot(by_date)
ax.set_xlabel('Days of the month')
ax.set_ylabel('Frequency')

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Tracer le meme graphique avec un bar plot
st.subheader("Distribution de la frequence par jour du mois")
fig, ax = plt.subplots(figsize=(25, 15))
ax.bar(range(1, 31), by_date.sort_values().values.flatten())
ax.set_xticks(range(1, 31))
ax.set_xticklabels(by_date.sort_values().index, fontsize=14, rotation=45)
ax.set_xlabel('Date of the month', fontsize=20)
ax.set_ylabel('Frequency', fontsize=20)

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Tracer un graphique distribution par jour de semaine avec un bar plot
st.subheader("Distribution de la frequence par jour de semaine")
fig, ax = plt.subplots()
ax.hist(df.weekday, bins=7, rwidth=0.8, range=(-.5, 6.5))
ax.set_xlabel('Days of the week')
ax.set_ylabel('Frequency')
days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
ax.set_xticks(np.arange(7))
ax.set_xticklabels(days)

# Affichage de l'histogramme avec Streamlit
st.pyplot(fig)

# Tracer un graphique distribution par jour de semaine avec un bar plot
st.subheader("Distribution de la frequence par heure")
fig, ax = plt.subplots()
ax.hist(df.hour, bins=24, range=(-0.5, 24))
ax.set_xlabel('Hour of the day')
ax.set_ylabel('Frequency')


# Affichage de l'histogramme avec Streamlit
st.pyplot(fig)

# Tracer une heatmap d'heure par jour de semaine 
st.subheader("Distribution de la frequence par heure et jour de semaine")
df2 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df2, linewidths=.5, ax=ax)
ax.set_ylabel('Jours de la semaine')
ax.set_yticklabels(('Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim', 'Lun'), rotation='horizontal')


# Affichage de la heatmap avec Streamlit
st.pyplot(fig)

# Distribution de latitude et longitude 
st.subheader(" Distribution de latitude et longitude")

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.hist(df['Lon'], bins=100, range=(-74.1, -73.9), color='g', alpha=0.5, label='Longitude')
ax.legend(loc='best')
ax_twiny = ax.twiny()
ax_twiny.hist(df['Lat'], bins=100, range=(40.5, 41), color='r', alpha=0.5, label='Latitude')
ax_twiny.legend(loc='upper left')

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# scatter plot de la latitude et longitude 
st.subheader(" Distribution de latitude et longitude")
fig, ax = plt.subplots(figsize=(15, 15), dpi=100)
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.scatter(df['Lat'], df['Lon'], s=0.8, alpha=0.4)
ax.set_ylim(-74.1, -73.8)
ax.set_xlim(40.7, 40.9)

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# scatter plot de la latitude et longitude 
st.subheader(" Distribution de latitude et longitude")

dico = {0: 'yellow', 1: 'yellow', 2: 'blue', 3: 'yellow', 4: 'yellow', 5: 'yellow', 6: 'yellow'}

# Scatter Plot
fig = plt.figure(figsize=(15, 15), dpi=100)
x = df["Lat"]
y = df["Lon"]
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(x, y, s=0.7, alpha=0.4, c=df["weekday"].map(dico))
plt.ylim(-74.1, -73.8)
plt.xlim(40.7, 40.9)

# Display the plot using Streamlit
st.pyplot(fig)




# Define contact options
contact_options = {
    "Email": "sofianeehamma@gmail.com",
    "LinkedIn": "Sofiane Hamma"
}

# Create sidebar and selectbox for contact options
with st.sidebar:
    st.markdown("# Contact Options")
    selected_contact = st.selectbox("How would you like to be contacted?", list(contact_options.keys()))

# Display selected contact information
st.write(f"**Selected Contact Method:** {selected_contact}")
st.write(f"**Contact Information:** {contact_options[selected_contact]}")