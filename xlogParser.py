import urllib.request
import os
import json
from pprint import pprint

projectPath = '/home/ericrao/work/myPythonDemos/xlogParser/'
xlogFilesPath = projectPath + 'xlog/'
xlogURLFile = 'weloveXlogFiles_20180306.txt'


def downloadFile():
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html)


# downloadFile()


if not os.path.exists(xlogFilesPath):
    os.mkdir(xlogFilesPath)


# def createXlogFiles():
#     f = open(path + 'test.txt', 'w+')
#
#
# createXlogFiles()

def readFile():
    f = open(projectPath + xlogURLFile, 'r')
    content = ""
    for line in f:
        # print(line)
        content += line
    data = json.load(f)
    pprint(data)


readFile()
