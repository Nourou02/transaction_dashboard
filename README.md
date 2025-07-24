# transaction_dashboard

Ce projet est un dashboard interactif développé avec **Streamlit** pour analyser des transactions financières, identifier des fraudes potentielles et visualiser les comportements selon différents canaux et produits.


## Objectif du projet

- Explorer un jeu de données de transactions financières
- Mettre en évidence les comportements suspects ou frauduleux
- Fournir une interface intuitive pour filtrer, visualiser et comprendre les patterns de fraude
- Déployer un outil interactif accessible en ligne



## Contenu du projet

- `app.py` — Code principal de l'application Streamlit
- `data/Transactions_data_complet.csv` — Fichier de données source
- `exploration_transactions_finance.ipynb` — Analyse exploratoire initiale
- `requirements.txt` — Bibliothèques nécessaires
- `README.md` — Documentation



## Fonctionnalités du dashboard

- **Filtres dynamiques** : par `ChannelId` et `ProductCategory`
- **Indicateurs clés** :
  - Nombre total de transactions
  - Nombre de fraudes
  - Taux de fraude
- **Visualisations** :
  - Distribution des montants par jour de la semaine (boxplot Plotly)
  - Histogramme des montants (Seaborn)
  - Nombre de fraudes par canal (bar chart Plotly)


## Aperçu des données

- Fichier CSV contenant des colonnes comme :
  - `TransactionStartTime` (timestamp)
  - `Amount` (montant)
  - `ChannelId` (canal)
  - `ProductCategory` (produit)
  - `FraudResult` (0 ou 1)

Les données sont pré-traitées pour extraire l’année, le mois, le jour de la semaine, et l’heure.


##  Installation locale

```bash
# Cloner le repo
git clone https://github.com/Nourou02/transaction_dashboard.git
cd transaction_dashboard

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'app
streamlit run app.py
