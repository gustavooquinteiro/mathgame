import platform
import gettext
if platform.system() is 'Windows':
    language = 'pt_BR'
else:
    language = os.environ.get('LANGUAGE')
try:
    translation = gettext.translation('constants', localedir='locale', languages=[language])
except Exception as e:
    # Send the exception for email
    translation = gettext.translation('constants', localedir='locale', languages=['pt_BR'])
finally:
    translation.install()

"""
Global constants
"""

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frame per seconds
FPS = 60

# Title
TITLE = "Math Game"

#Font
FONT = "Arial"

SPRITE_FOLDER = "spritesheet/"
PLAYER_PNG = "p1_walk.png"
ENEMIES_PNG = "enemies.png"
BACKGROUND_01 = "spritesheet/background_01.png"
BACKGROUND_02 = "spritesheet/background_02.png"
BACKGROUND_03 = "spritesheet/background_03.png"
BACKGROUND_04 = "spritesheet/background_04.png"
BACKGROUND_05 = "spritesheet/background_05.png"
BACKGROUND_06 = "spritesheet/background_06.png"
BACKGROUND_07 = "spritesheet/background_07.png"
BACKGROUND_08 = "spritesheet/background_08.png"
BACKGROUND_09 = "spritesheet/background_09.png"
BACKGROUND_10 = "spritesheet/background_10.png"

TIP_LVL = _("I don't give tips unless you (p)ress me")
TIP_LVL1 = _("Walk around")
TIP_LVL2 = _("Faster")
TIP_LVL3 = _("But don't stay in horizontal")
TIP_LVL4 = _("Face the snake at space")
TIP_LVL5 = _("Or jump them again")
TIP_LVL6 = _("When they come along better go down")
TIP_LVL7 = _("As long you go down more power you get")
TIP_LVL8 = _("Don't need avoid the void anymore")
TIP_LVL9 = _("But you give twice what you have")
TIP_LVL10 = _("As long you stay more you can heal")
