DIR="$(cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd "$DIR"

if [ -f ./pyray2/PyRay2.py ]; then
  PYRAY_FILE="./pyray2/PyRay2.py"
else
  echo "PyRay2 not found"
	exit 1
fi

python3 -O ${PYRAY_FILE}
