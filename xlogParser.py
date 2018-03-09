import os
import json
import wget
import requests
import mimetypes
import glob
from subprocess import Popen

projectPath = os.getcwd()
xlogFilesPath = projectPath + '/xlog'
xlogURLFile = '/weloveXlogFiles.txt'


def download_file(url):
    # deletefiles(xlogFilesPath)
    checkdirexist()
    file_name = wget.download(url, xlogFilesPath)
    print(file_name)


def parse_file_content_type(url):
    response = requests.get(url)
    content_type = response.headers['content-type']
    extentions = mimetypes.guess_extension(content_type)
    print(extentions)


def checkdirexist():
    if not os.path.exists(xlogFilesPath):
        os.mkdir(xlogFilesPath)


def deletefiles(path):
    os.removedirs(path)


def createXlogFiles(fileName):
    f = open(xlogFilesPath + fileName, 'wr+')


def read_file():
    f = open(projectPath + xlogURLFile, 'r')
    content = ''
    for line in f:
        content += line
    text = json.loads(content)
    for entry in text['data']['entries']:
        download_file(entry['dl_remove_attname_url'])


def parse_xlog_to_log():
    for filename in glob.glob(xlogFilesPath + '/*.xlog'):
        words = filename.split('/')
        xlogFileName = 'xlog/' + words[len(words) - 1]
        Popen([os.getcwd() + '/decode_mars_log_file.py', os.getcwd() + '/' + xlogFileName])


read_file()
parse_xlog_to_log()
