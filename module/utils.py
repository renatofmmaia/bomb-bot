import time

def date_formatted(format = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime())

def replace(string, strReplace):
        if strReplace and string.endswith(strReplace):
            return string[:-len(strReplace)]
        return string