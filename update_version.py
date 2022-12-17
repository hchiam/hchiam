# pip3 install hchiam
import re
from hchiam import read, write

# https://test.pypi.org/project/hchiam
# https://pypi.org/project/hchiam
# https://github.com/hchiam/hchiam-example-pypi-project/blob/a40b5b66a73b59cb0c7d9e0bd7e7a316a4f5e08a/tests/test_innermodule.py


def get_pyproject_toml_version(pyproject_toml, pattern):
    old_file_text = read(pyproject_toml)
    pyproject_toml_lines = old_file_text.split('\n')
    version_line = [
        line for line in pyproject_toml_lines if pattern.match(line)]
    if len(version_line) != 1:
        raise Exception(
            'The pattern matched more than one line for version number. Please check the file and the regex pattern for errors.')
    version_line = ''.join(version_line)
    # print(version_line)
    version = re.search('"((\d+)\.(\d+)\.(\d+))"', version_line)
    major = version.group(2)
    minor = version.group(3)
    patch = version.group(4)
    old_version = version.group(1)
    new_version = f'{major}.{minor}.{int(patch)+1}'
    return {'old_version': old_version, 'new_version': new_version}


def update_pyproject_toml_version(pyproject_toml, pattern, old_version, new_version):
    response = input(
        f'{old_version} -> {new_version}? Hit Enter. \nOtherwise type #.#.# and hit Enter.\n')

    while response.encode() != b'' and not re.match('\d+\.\d+\.\d+', response):
        response = input(
            f'\nInvalid version: {response}\nHit Enter to update {old_version} -> {new_version} (Otherwise type #.#.# and hit Enter.)\n')

    if response.encode() != b'' and re.match('\d+\.\d+\.\d+', response):
        new_version = response

    print(f'\nUpdating {old_version} -> {new_version}')

    old_file_text = read(pyproject_toml)
    new_file_text = re.sub(
        pattern, f'version = "{new_version}"', old_file_text)
    # print(new_file_text)
    write(pyproject_toml, new_file_text)


pyproject_toml = 'pyproject.toml'
pattern = re.compile('version = "\d+\.\d+\.\d+"')
versions = get_pyproject_toml_version(pyproject_toml, pattern)
print(versions)
old_version = versions['old_version']
new_version = versions['new_version']
update_pyproject_toml_version(
    pyproject_toml, pattern, old_version, new_version)
