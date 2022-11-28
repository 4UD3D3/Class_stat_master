# Projet Classtat - Analyse en temps réel de la disponibilité des salles de l'UBS
*Projet par Grégoire Trué, André Gainche, Medhi Le FLoch, Nasim Hammouch*

## Prérequis

- Python3 + Gestionnaire de paquets **pip** pour Python (installé avec python)  
  https://www.python.org/downloads/  
  :warning: *Pensez à ajouter python et pip à vos variables d'environnement PATH si nécessaire*

- Environnement d'exécution **nodejs**  
  https://nodejs.org/en/download/  
  :warning: *Pensez à ajouter nodejs et npm à vos variables d'environnement PATH si nécessaire*

- Gestionnaire de paquets **npm** pour nodejs (installé avec nodejs)

- Navigateur internet, je recommande fortement **palemoon** de très grande qualité  
  https://www.palemoon.org/

## Premier lancement

### Automatique
- Sur Linux : exécuter le script `firststart.sh` qui installera les packages nécessaires.

### Manuel
Dans un **terminal** sur Linux (lancé depuis le répertoire *classtat*)
```
cd platform
npm install

cd ../scripts_stats
python3 -m pip install -r requirements.txt
```

Dans un **terminal** sur Windows (lancé depuis le répertoire *classtat*)
```
cd platform
npm install

cd ..\scripts_stats
python3 -m pip install -r requirements.txt
```

## Lancement du site

### Automatique
- Sur Linux : exécuter le script `start.sh`
- Sur Windows : exécuter le script `run_classtat_windows.bat`

### Manuel
Dans un **terminal** (lancé depuis le répertoire *classtat*)
```
cd scripts_stats
python3 -m flask run
```

Dans un autre terminal (lancé depuis le répertoire *classtat*)
```
cd platform
npm start
```
:warning: *Si des erreurs ont lieu, pensez à vérifiez que tous les packages soient bien installés*

Après cela, la page d'accueil de **Classtat** s'ouvrira automatiquement. Le lancement peut être moins rapide à la première exécution.


## Crédits

#### API par Andréa Gainche et Grégoire Truhé


#### Front-end par Nassim Hmamouche
- Librairie JavaScript : React
- Polices d'écriture : Google Fonts
- Calendrier : date-fns.org

#### Interface CAS par Mehdi Le Floch