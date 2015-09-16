#/bin/bash

#Comprobaciones:
#   pyflakes
#   PEP8


#pyflakes
echo "## Pyflakes:"
find . -name '*.py' | egrep -v '^./static/' | egrep -v '^./lib/' | egrep -v '^./\w*/migrations/' | egrep -v './ratticweb/(local_)?settings.py' | egrep -v '.ropeproject/' | xargs pyflakes

echo "##"

echo "## Tests:"
python -m unittest

echo "##"

