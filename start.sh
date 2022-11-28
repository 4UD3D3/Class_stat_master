#!/bin/bash
echo "Starting of the aplication..."
current_dir=$PWD

echo "api starting ..."
(cd /scripts_stats;python3 -m flask run)
cd $current_dir
echo "api ok"

echo "node starting ..."
(cd /platform,npm start)
cd $current_dir
echo "node ok"

echo "cas starting ..."
(cd cas/cas-ecole;sudo docker build --no-cache -t cas-ecole)
(cd cas-ecole;sudo ./keygen.sh)
(cd /cas;python3 client.py)
echo "cas ok"