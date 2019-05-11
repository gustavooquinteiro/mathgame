import platform
import gettext

def getSystemLanguage(system):
    import locale
    if system is 'Windows':
        import ctypes
        windll = ctypes.windll.kernel32
        return locale.windows_locale[windll.GetUserDefaultUILanguage()]
    else:
        locale.setlocale(locale.LC_ALL, "")
        return locale.getlocale(locale.LC_MESSAGES)[0]



language = getSystemLanguage(platform.system())
try:
    translation_constants = gettext.translation(
        'constants', 
        localedir='locale', 
        languages=[language]
        )
except FileNotFoundError as error:
    translation_constants = gettext.translation(
        'constants', 
        localedir='locale',
        languages=['en']
        )
finally:
    translation_constants.install()
