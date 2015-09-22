#!/bin/bash

#Comprobaciones:
#   pyflakes
#   PEP8
#   coverage


#pyflakes
echo "## Pyflakes:"
find . -name '*.py' | egrep -v '^./static/' | egrep -v '^./lib/' | egrep -v '^./\w*/migrations/' | egrep -v './ratticweb/(local_)?settings.py' | egrep -v '.ropeproject/' | egrep -v '*__init__.py' | xargs pyflakes

echo "##"

echo "## PEP8:"
pep8 --exclude=migrations,lib,static,.ropeproject --ignore=E501,E225,E128,E124 .

echo "##"

echo "## Tests:"
coverage run --source="andreani" setup.py test
coverage report -m
echo "##"

