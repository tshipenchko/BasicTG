#!/bin/bash
cd ~ 
if [ -d "BasicTG" ]; then
  echo "The directory already exists. Please delete the directory to install it completely OR update the repository"
  echo "Run        rm -rf ~/BasicTG             to delete the directory OR"
  echo "Run        cd ~/BasicTG && git pull     to update the repository"
  exit 1
fi

apt update && apt upgrade -y
apt install python -y
pip install telethon
pip install colorama
apt install git -y
git clone https://github.com/arersen/BasicTG
cd BasicTG
cd source
python install.py
cd ..
sh start.sh
