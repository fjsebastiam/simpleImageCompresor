import ntpath
import os
import sys
import easygui
from tkinter import *
import tkinter.filedialog as fd


from service.compressor import all_files_in_folder


def main():
    pathToGet = r"C:\Users\jsebastia\Pictures\Saved Pictures\imagenCompressor\imagenesPrueba"
    pathToSave = r"C:\Users\jsebastia\Pictures\Saved Pictures\imagenCompressor\imagenesComprimidas"

    quality = 40

    respuesta = easygui.buttonbox(msg='Select the way you want to compress images', title='simpleCompressor by JSM',
                                  choices=('One File', 'Selected Files', 'All files in one directory'))

    if respuesta == 'One File':
        a=False
    if respuesta == 'Selected Files':
        filename = easygui.fileopenbox()
    if respuesta == 'All files in one directory':
        pathToGet = easygui.diropenbox(msg="Directory of all files:",title="simpleCompressor by JSM")
        easygui.msgbox("Your path to ge all images is: "+pathToGet, "diropenbox", ok_button="Continue")
        pathToSave = easygui.diropenbox(msg="Directory to Save all images:", title="Control: diropenbox")
        easygui.msgbox("Your path to ge all images is: " + pathToGet, "diropenbox", ok_button="Continue")
        go_to_compress_res = easygui.buttonbox(msg='Caja con varios botones',
                                               title='Your path to ge all images is: ' + pathToGet,
                                               choices=('continue', 'Cancel and exit'))
        if go_to_compress_res == 'continue':
            all_files_in_folder(pathToGet, pathToSave, quality)
        else:
            sys.exit(0)

    #filename = easygui.fileopenbox()

    cwd = os.getcwd()
    print(cwd)

    #root = easygui
    #root.iconbitmap(r'c:\Python32\DLLs\py.ico')
    #root.mainloop()

    #print(filename)
    easygui.msgbox("The task was completed" + pathToGet, "diropenbox", ok_button="Continue")
    sys.exit(0);


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

if __name__ == '__main__':
    window = Tk()

    window.title("Welcome to LikeGeeks app")

    #window.mainloop()

    filez = fd.askopenfilenames(parent=window, title='Choose a file')

    pathToGet = r"C:\Users\jsebastia\Pictures\Saved Pictures\imagenCompressor\imagenesPrueba\saturnohd.jpg"

    print(filez)
    #main()

