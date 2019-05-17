import os
import sys
import pip._internal
import pythoncom
from win32com.shell import shell, shellcon
# import re


def installPkg(pkg):
    pip._internal.main(['install', '--upgrade', pkg])


def makelnks(name, path, fileName, iconpath):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    pathCompleto = sys.executable + " "+fileName
    print(pathCompleto)
    shortcut.SetPath(str(pathCompleto))
    workingDir = os.path.dirname(os.path.abspath(__file__))+path
    workingDir = workingDir.replace('"', "")
    shortcut.SetWorkingDirectory(workingDir)
    shortcut.SetDescription(name)
    shortcut.SetIconLocation(os.path.dirname(
        os.path.abspath(__file__))+path+iconpath, 0)
    desktop_path = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, 0, 0)
    persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(os.path.join(desktop_path, name+".lnk"), 0)


def main():
    # instala pywin32 e pandas
    installPkg('pywin32')
    installPkg('pandas')
    # cria links desktop
    makelnks("Archtimer 1.0", "\\Archtimer\\", "main.py", "cfg\\iconeT.ico")
    makelnks("Archtimer - Config", "\\Archtimer\\",
             "guiWin.py", "cfg\\iconeC.ico")
    makelnks("Archtimer - Pastas", "\\change_dir_files\\",
             "main.py", "iconeDir.ico")


if __name__ == '__main__':
    main()
