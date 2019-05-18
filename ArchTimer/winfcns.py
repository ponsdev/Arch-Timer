# import time
# import win32api
from ctypes import Structure, windll, c_uint, sizeof, byref
from win32gui import GetWindowText, GetForegroundWindow


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


def get_fg_win():
    return GetWindowText(GetForegroundWindow())
