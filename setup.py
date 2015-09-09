from distutils.core import setup
setup(name='py-andreani',
      version='0.1',
      description='Implemeta servicios ofrecidos por API de Andreani',
      author='Yonatan Romero',
      author_email='yromero@openmailbox.org',
      url='https://github.com/romeroyonatan/py-andreani',
      platforms="Python3",
      packages=['andreani'],
      requires=['suds'],
      )
