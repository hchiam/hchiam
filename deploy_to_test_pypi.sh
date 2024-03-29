# python3 -m pip install --upgrade build
# python3 -m pip install --upgrade twine

# update code
python3 update_version.py # update pyproject.toml version number
# remove the old .whl and .gz files
rm -rf dist
python3 -m build
python3 -m twine upload --repository testpypi dist/*

# https://test.pypi.org/project/hchiam
# python3 -m pip install hchiam
