IF NOT EXIST "env" (
@ ECHO Initializing virtual enviroment...
@ python -m venv env   
@ ECHO Initialized virtual enviroment
@ ECHO Activating virtual enviroment..
@ env\Scripts\activate
@ ECHO Activated virtual enviroment
@ ECHO Installing requirements...
@ pip install -r requirements.txt
@ ECHO Installed requirements
)
@ ECHO Playing the game...
@ cd mathgame && python __init__.py
