import os
import pydantic

# from utils import tv
from utils import movie

# from utils import general


def driver(movieDBKey: str, path: str):
    options = [" (", "-SEG_MainFeature", "-FPL_MainFeature", "_t"]

    original_files = os.listdir(path)
    files = dict()
    max_file_length = 0
    max__length = 0

    for file in original_files:
        if len(file) > max_file_length:
            max_file_length = len(file)
        if not os.path.isfile(os.path.join(path, file)):
            print(f"Not File: {file}")
        else:
            for option in options:
                split_file = file.split(option)
                if len(split_file) == 2:
                    files[file] = {"": split_file[0]}

    for i, file in enumerate(files):
        title, year = movie.movie_search(files[file], movieDBKey)
        (files[file])

    for i, file in enumerate(files):
        print(f"""{i+1:2}) {file:^{max_file_length}} -> {title} ({year})""")


if __name__ == "__main__":
    # API keys
    movieDBKey = "3da8364d372f30e6c9a6e734c2d2780d"
    path = "/mnt/external_5tb/compressed"

    driver(movieDBKey, path)
