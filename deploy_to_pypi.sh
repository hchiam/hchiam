# python3 -m pip install --upgrade build
# python3 -m pip install --upgrade twine

# update code
# update pyproject.toml version number
# remove the old .whl and .gz files
rm -rf dist
python3 -m build
python3 -m twine upload dist/*

# https://pypi.org/project/hchiam
# pip3 install hchiam
