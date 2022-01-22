import subprocess

from module.platform import Platform, PlatformEnum


def get_windows():
    return (
        _get_linux_bombcrypto_windows()
        if Platform().get_platform() == PlatformEnum.LINUX
        else _get_bombcrypto_windows()
    )


def _get_linux_bombcrypto_windows():
    stdout = (
        subprocess.Popen(
            "xdotool search --name bombcrypto", shell=True, stdout=subprocess.PIPE
        )
        .communicate()[0]
        .decode("utf-8")
        .strip()
    )
    windows = stdout.split("\n")
    return [LinuxWindow(w) for w in windows]

def _get_bombcrypto_windows():
    import pygetwindow

    return [DefaultWindow(w) for w in pygetwindow.getWindowsWithTitle("bombcrypto")]

class LinuxWindow:
    def __init__(self, window_id) -> None:
        self.window = window_id

    def activate(self):        
        subprocess.Popen(f"xdotool windowactivate {self.window}", shell=True)

class DefaultWindow:
    def __init__(self, window) -> None:
        self.window = window

    def activate(self):
        self.window.activate()
