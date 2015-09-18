#/bin/bash

#Comprobaciones:
#   pyflakes
#   PEP8


#pyflakes
echo "## Pyflakes:"
find . -name '*.py' | egrep -v '^./static/' | egrep -v '^./lib/' | egrep -v '^./\w*/migrations/' | egrep -v './ratticweb/(local_)?settings.py' | egrep -v '.ropeproject/' | xargs pyflakes

echo "##"

echo "## PEP8:"
pep8 --exclude=migrations,lib,static,.ropeproject --ignore=E501,E225,E128,E124 .

echo "##"

echo "## Tests:"
coverage run --source="andreani" setup.py test
coverage report -m
echo "##"

