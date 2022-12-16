# Wine Quality Prediction

Ce projet permet de déterminer la qualité d'un vin en fonction de ces caractéristiques.

## Installation

`pip install -r requirements.txt`

## Utilisation

Pour lancer l'api :  
`uvicorn api.app:app --port PORTNUMBER`

Liste des liens FastAPI :  
|Type|Lien|Description|
|-|-|-|
|POST|`/api/predict`|Réalise une prédiction sur un vin|
|GET|`/api/predict`|Retourne le meilleur vin ("vin parfait")|
|GET|`/api/model`|Retourne le modèle séralisé (.joblib)|
|GET|`/api/model/description`|Retourne des informations sur le modèle|
|PUT|`/api/model`|Ajoute un vin dans le modèle|
|POST|`/api/model/retrain`|Réentraine le modèle| 

## Tests

Pour exécuter les tests :  
`pytest`

## Choix technique

Le modèle utilise une régression linéaire pour prédire la qualité d'un vin.  

Expliquer pourquoi [...]  

Choix d'un vin valide ou non -> Analyse des données présente dans le csv ainsi que des recherches et extrapolation. Les limites choisies ne sont pas forcément représentative de la réalité.