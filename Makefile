GAME = __init__.py
SOURCE =
ifeq ($(OS), Windows_NT)
	PYTHON = python
	ECHO = ECHO
	ACTIVATE = env\Scripts\activate
	PIP = pip
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S), Linux)
		SHELL := /bin/bash
		PYTHON = python3
		ECHO = echo -e -n
		SOURCE = source
		ACTIVATE = env/bin/activate
		PIP = pip3
	endif
endif 

all: setup run

setup:
	@ $(PYTHON) -m venv env
	@ $(SOURCE) $(ACTIVATE)
	@ $(PIP) install -r requirements.txt
run:
	@ $(ECHO) "Playing the game..."
	@ cd mathgame && $(PYTHON) $(GAME)
