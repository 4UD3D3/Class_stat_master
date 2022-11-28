# Introduction

Vos collègues de promotion ont pu mettre en place une plateforme de test comprenant un serveur CAS ainsi qu'un prototype de client en python. Vous trouverez des indices sur leur identité dans les utilisateurs de base.

N'hésitez pas à tout modifier pour adapter cette plateforme de test à votre projet.

# Composition du projet

Vous trouverez dans ce projet :
- cas-ecole Dockerfile : Contient l'image du conteneur qui hébergera le serveur.
- keygen.sh : Script bash qui va initialiser la clé du générateur intégré au CAS et démarre le conteneur avec les options nécessaires.
- dossier cas : Contient deux fichiers de configuration :
  - cas.properties : contient les paramètres du serveur CAS avec les utilisateurs et leurs mots de passe
  - any-100.json : contient le service protégé par le CAS. Ici c'est le serveur http://127.0.0.1:8002/.* qui est protégé.
- Un fichier python client.py qui simule un site qui fera appel au CAS pour l'authentification.

# Prérequis

Tout d'abord, il faut build l'image pour qu'elle soit intégrée à votre registry local. allez dans le dossier cas-ecole puis tapez :
```
sudo docker build --no-cache -t cas-ecole .
```
L'option --no-cache permet de reconstruire l'image à coup sûr en cas de modification des fichiers de configuration.

Vous aurez besoin de python3 pour faire fonctionner le client. Lorsqu'il sera installé, il restera quelques librairies python à installer pour que le client fonctionne. Allez dans la racine du projet puis tapez :
```
pip install -r requirements
```

# Lancement

Exécutez le script shell du dossier cas-ecole avec la commande suivante :
```
sudo cas-ecole/keygen.sh
```
puis exécutez le client via la commande suivante :
```
python3 client.py
```
Allez sur votre navigateur à l'adresse : http://localhost:8002

Si tout se passe bien, le CAS affichera une page d'authentification, vous pourrez utiliser les identifiants définis dans le fichier cas.properties (login: user / mdp : coco par exemple).

Si le compte est reconnu alors le site s'affichera sinon vous serez bloqué.
