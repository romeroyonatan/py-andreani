from setuptools import setup

from pip.req import parse_requirements
from pip.download import PipSession

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='py-andreani',
      version='0.1',
      description='Implemeta servicios ofrecidos por API de Andreani',
      author='Yonatan Romero',
      author_email='yromero@openmailbox.org',
      url='https://github.com/romeroyonatan/py-andreani',
      platforms="Python3",
      packages=['andreani'],
      install_requires=reqs,
      )


