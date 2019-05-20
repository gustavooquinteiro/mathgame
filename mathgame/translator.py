import platform
import gettext
import os

CONST = 'constants' 
LOCALE = 'locale'

def getSystemLanguage(system=platform.system()):
    import locale
    if system is 'Windows':
        import ctypes
        windll = ctypes.windll.kernel32
        return locale.windows_locale[windll.GetUserDefaultUILanguage()]
    else:
        locale.setlocale(locale.LC_ALL, "")        
        return locale.getlocale(locale.LC_MESSAGES)[0]
    
if __name__ == "__main__":
    print(gettext.find(CONST, 
                    localedir=LOCALE,
                    languages=[getSystemLanguage()], 
                    all=True))
else:
    language = getSystemLanguage()
    if gettext.find(CONST, 
                    localedir=LOCALE, 
                    languages=[language], 
                    all=True):
        gettext.translation(CONST,
                            localedir=LOCALE, 
                            languages=[language]).install()        
    else:
        gettext.translation(CONST,
                            localedir=LOCALE,
                            languages=['en']).install()
        
