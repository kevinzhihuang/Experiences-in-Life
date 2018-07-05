import os
from enchant.checker import SpellChecker

path = "/home/kevin/Desktop/"
directory = "Experiences in life"
path_to_directory = os.path.join(path, directory)
checker = SpellChecker("en_US")

for filename in os.listdir(path_to_directory):
    error_count = 0
    if filename.endswith('.txt'):
        with open(os.path.join(path_to_directory, filename)) as f:
            file_text = f.read()
            if 300 >= len(file_text) <= 360:
                checker.set_text(file_text)
                print(filename)
                for error in checker:
                    error_count += 1
                    print(filename + ' Errors: ' + error.word)
                print('-----------------')


