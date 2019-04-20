from setuptools import setup

readme = open('README.md').read()
setup(name= 'mathgame',
      version='1.0',
      description='A platform math game', 
      url='http://github.com/gustavooquinteiro/mathgame',
      author='Gustavo Oliveira Quinteiro',
      author_email='gustavooquinteiro@outlook.com',
      long_description = readme,
      license='MIT', 
      packages=['mathgame'],
      zip_safe=False)
