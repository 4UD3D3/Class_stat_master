La partie scripts_stats contient tous les scripts nécessaires à la récupérations des fichiers ics
et à leur analyse statistique demandable depuis l'API (app.py sous flask).

Le script extract_stats_ics_to_json.py contient toutes les fonctions pour analyser les fichiers ics.

Lancement API extraction statistiques : python -m flask run

Puis request post sur l'URL "http://localhost:5000/data" pour obtenir les données.

Voir image "how_to_post_request" pour un exemple via Postman.