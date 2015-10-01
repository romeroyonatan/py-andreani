from setuptools import setup

setup(name='py-andreani',
      version='0.2beta',
      description='Implementa servicios ofrecidos por API de Andreani',
      author='Yonatan Romero',
      author_email='yromero@openmailbox.org',
      license='GPLv2',
      url='https://github.com/romeroyonatan/py-andreani',
      platforms="Python3",
      keywords="andreani e-commerce ecommerce argentina oca",
      packages=['andreani'],
      install_requires="suds-jurko",
      test_suite="test",
)
