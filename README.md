# Math Game  
This is a 2D platform game written in Python using the Pygame library. The game is a upgrade type game, i.e, each complete level gives the player a new skill to proceed with.

With simple enemies mechanics and jump skill this is a short game to entertain    

## Requirements

  + Python 3.7.2 or higher

  + All libraries needed are listed in [requirements file](requirements.txt).


## Configuration 

  First of all, make sure that you have Python installed in your machine

  1. Linux and Mac machine have Python by default (go to third step).
  2. For Windows machine<sup>1</sup>, [download Python installer here](https://www.python.org/downloads/).
  3. Look for the right version, use the command `python --version` in your Terminal or Command Prompt to verify.
  + If your version is lower than required one, see [pyenv project](https://github.com/pyenv/pyenv) if keep the lower version is needed, otherwise upgrade them.  

  4. For UNIX platforms, install the libraries required with ``` make requirements ``` in Terminal on the project folder
  + ``` make all ``` or simply ``` make ``` will install requirements and start the game 

  5. For Windows, after downloaded and installed Python, install libraries double-clicking in the ``` Makefile.bat ``` file on the project folder

## How to use

  For UNIX platforms, use the following commad to start the game:

  
  ```bash
  make play 
  ```

  In Windows, double-click in ``` start_game.bat ``` or just double-click in ``` __init__.py ``` file, inside mathgame folder

## License

  This game is under the [MIT License](LICENSE)

## Author

  This game is made by [Gustavo Oliveira Quinteiro](mailto:gustavooquinteiro@outlook.com)

<sup>1</sup> All the procedures were tested only in Windows 10 
