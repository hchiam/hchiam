def main():
    """Entry point for the application script"""


def write(file_name, text):
    f = open(file_name, "w")
    f.write(str(text))
    f.close()


def append(file_name, text):
    f = open(file_name, "a")
    f.write(str(text))
    f.close()


def read(file_name):
    f = open(file_name, "r")
    text = str(f.read())
    f.close()
    return text
