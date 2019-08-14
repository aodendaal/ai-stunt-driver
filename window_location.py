from __future__ import absolute_import, division, print_function, unicode_literals
import math
import win32gui

_windowLeft = 0
_windowTop = 0
_windowRight = 0
_windowBottom = 0

_clientLeft = 0
_clientTop = 0
_clientRight = 0
_clientBottom = 0

_windowOffset = 0
_titleOffset = 0

_contentLeft = 0
_contentTop = 0
_contentRight = 0
_contentBottom = 0

_form_name = ""


def set_dimensions(hwnd):
    global _windowLeft
    global _windowTop
    global _windowRight
    global _windowBottom

    global _clientLeft
    global _clientTop
    global _clientRight
    global _clientBottom

    global _windowOffset
    global _titleOffset

    global _contentLeft
    global _contentTop
    global _contentRight
    global _contentBottom

    windowRect = win32gui.GetWindowRect(hwnd)
    clientRect = win32gui.GetClientRect(hwnd)

    _windowLeft = windowRect[0]
    _windowTop = windowRect[1]
    _windowRight = windowRect[2]
    _windowBottom = windowRect[3]

    _clientLeft = clientRect[0]
    _clientTop = clientRect[1]
    _clientRight = clientRect[2]
    _clientBottom = clientRect[3]

    _windowOffset = math.floor(((_windowRight - _windowLeft) - _clientRight) / 2)
    _titleOffset = ((_windowBottom - _windowTop) - _clientBottom) - _windowOffset

    _contentLeft = _windowLeft + _windowOffset
    _contentTop = _windowTop + _titleOffset
    _contentRight = _windowRight - _windowOffset
    _contentBottom = _windowBottom - _windowOffset


def get_dimensions(title):
    global _form_name

    _form_name = title
    win32gui.EnumWindows(callback, None)

    return _contentLeft, _contentTop, _contentRight, _contentBottom


def callback(hwnd, extra):
    name = win32gui.GetWindowText(hwnd)
    if name.find(_form_name) > -1:
        set_dimensions(hwnd)


def main():
    global _form_name

    _form_name = "DOSBox 0.74"
    win32gui.EnumWindows(callback, None)

    print('window rect: {0}, {1}, {2}, {3}'.format(_windowLeft, _windowTop, _windowRight, _windowBottom))
    print('client rect: {0}, {1}, {2}, {3}'.format(_clientLeft, _clientTop, _clientRight, _clientBottom))
    print('window offset: {0}, title offset: {1}'.format(_windowOffset, _titleOffset))
    print('content rect: {0}, {1}, {2}, {3}'.format(_contentLeft, _contentTop, _contentRight, _contentBottom))


if __name__ == '__main__':
    main()
