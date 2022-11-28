#!/bin/bash
echo "starting initialisation"
(cd /platform;npm install)
(cd /cas;python3 -m pip install -r requirements.txt)
echo "initialisatiàn finished you can run start.sh now"