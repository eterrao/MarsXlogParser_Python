import urllib.request
import os
import json
from pprint import pprint

projectPath = '/home/ericrao/work/myPythonDemos/xlogParser/'
xlogFilesPath = projectPath + 'xlog/'
xlogURLFile = 'weloveXlogFiles_20180306.txt'


def downloadFile(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    pprint(html)


if not os.path.exists(xlogFilesPath):
    os.mkdir(xlogFilesPath)

# def createXlogFiles():
#     f = open(path + 'test.txt', 'w+')
#
#
# createXlogFiles()
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';


def readFile():
    f = open(projectPath + xlogURLFile, 'r')
    content = ''
    for line in f:
        # print(line)
        content += line

    text = json.loads(content)
    # pprint(text['data']['entries'])
    for entry in text['data']['entries']:
        print(entry['dl_remove_attname_url'])
        downloadFile(entry['dl_remove_attname_url'])


readFile()
