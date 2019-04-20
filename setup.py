import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages

NAME = 'mathgame'
DESCRIPTION = 'A platform game with math elements'
URL = 'http://github.com/gustavooquinteiro/mathgame'
EMAIL = 'gustavooquinteiro@outlook.com'
AUTHOR = 'Gustavo Oliveira Quinteiro'
REQUIRES_PYTHON= '>=3.7.2'
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

try:
      with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as readme:
            long_description =  '\n' + readme.read()
except FileNotFoundError:
      long_description = DESCRIPTION

about = {}
if not VERSION:
      project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
      with open(os.path.join(here, project_slug, '__version__.py')) as f:
            exec(f.read(), about)
else:
      about['__version__'] = VERSION

requirements = []
with open (os.path.join(here, 'requirements.txt')) as required:
      requirements = required.read().split('\n')

setup(
      name=NAME,
      version=about['__version__'],
      description=DESCRIPTION, 
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      long_description=long_description,
      long_description_content_type='text/markdown',
      python_requires=REQUIRES_PYTHON,
      license='MIT', 
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      install_requires=requirements,
      include_package_data=True,
      package_data={
            'mathgame':[
                        'spritesheet/*.png', 
                        'sounds/*.mp3', 
                        'sounds/*.wav',
                        'locale/**'
                        ],
      },
       entry_points={
        'setuptools.installation': [
            'eggsecutable = mathgame.__init__.py:main',
        ]
      },
      zip_safe=False
      )
