#!/bin/bash

GREEN="\033[0;32m"
NC="\033[0m"
pyenv=$(find . -type d -name '\env')
if [ ! -d "$pyenv" ]; then
	echo "Initializing virtual enviroment..."
	python3 -m venv env   
	echo -e -n " [${GREEN} OK ${NC}]"
	echo " Initialized virtual enviroment"

	echo "Activating virtual enviroment.."
	source env/bin/activate  
	echo -e -n " [${GREEN} OK ${NC}]"
	echo " Activated virtual enviroment" 

	echo "Installing dependencies..."
	pip install -r requirements.txt
	echo -e -n " [${GREEN} OK ${NC}]"
	echo " Installed dependencies" 
fi

echo "Playing the game..."
cd mathgame && python3 __init__.py
