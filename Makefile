BASE_FOLDER = mathgame

GREEN=\033[0;32m
NC=\033[0m

all: requirements play

requirements:
	@ echo "Initializing virtual enviroment..."
	@ python3 -m venv env   
	@ echo -e -n " [${GREEN} OK ${NC}]"
	@ echo " Initialized virtual enviroment"

	@ echo "Activating virtual enviroment.."
	@ . env/bin/activate  
	@ echo -e -n " [${GREEN} OK ${NC}]"
	@ echo " Activated virtual enviroment" 
	
	@ echo "Installing requirements..."
	@ pip install -r requirements.txt
	@ echo -e -n " [${GREEN} OK ${NC}]"
	@ echo " Installed requirements"

play:
	@ echo "Playing the game..."
	@ cd mathgame && python3 __init__.py

clean: clean-pyc clean-build

clean-pyc:
	@ echo "Cleaning cache..."
	@ find ./$(BASE_FOLDER) -name '*.pyc' -exec rm --force {} + 
	@ find ./$(BASE_FOLDER) -name '*.pyo' -exec rm --force {} +
	@ find ./$(BASE_FOLDER) -name '*~' -exec rm --force  {} +
	@ echo -e -n " [${GREEN} OK ${NC}]"
	@ echo " Clean"

clean-build:
	@ echo "Cleaning build"
	@ rm --force --recursive build/
	@ rm --force --recursive dist/
	@ rm --force --recursive *.egg-info
	@ echo -e -n " [${GREEN} OK ${NC}]"
	@ echo " Clean"
	
.PHONY: clean all
	
endif
