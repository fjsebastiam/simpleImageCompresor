import ntpath
import os
import sys
from PIL import Image

formats = ('.jpg', '.jpeg', 'png')

slash = '/'
if sys.platform == "win32":
    slash = '\\'


def all_files_in_folder(pathToGet, pathToSave, quality):
    for file in os.listdir(pathToGet):
        extension = os.path.splitext(file)[1].lower()

        if extension in formats:
            print('compressing', file)
            filepath = os.path.join(pathToGet)

            slash = '/'
            if sys.platform == "win32":
                slash = '\\'

            __compress_file(filepath + slash + file, pathToSave, quality)


def selectionFiles(arrayOfFiles, pathToSave, quality):
    for file in arrayOfFiles:
        extension = os.path.splitext(file)[1].lower()

        if extension in formats:
            print('compressing', file)
            __compress_file(file, pathToSave, quality)


def __path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def __compress_file(file, pathToSave, quality):
    picture = Image.open(file)

    picture.save(pathToSave + slash + "Compressed_" + file,
                 optimize=True,
                 quality=quality)
    return
