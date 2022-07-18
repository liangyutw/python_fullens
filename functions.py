import define
import re
import requests
from bs4 import BeautifulSoup
import pathlib

def delItem(isNotHttp):

    newData = []
    for url in isNotHttp:

        if url not in define.removeList:
            newData.append(url.replace("/category", ""))

    return list(set(newData))

def prependString(urlData):

    newUrl = []

    for item in urlData:
        result = re.search("^http", item)

        if result is None:
            prefix = define.mainUrl
        else:
            prefix = ''

        newUrl.append(prefix+item.lstrip('/'))

    return newUrl


def get404List(urlData):

    errorUrl = []
    for url in urlData:
        result = requests.head(url)
        if result.status_code == 404:
            errorUrl.append(url)

    return errorUrl


def uniqueList(list):

    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list


def getUrl(result):

    isHttp = []
    noHttp = []
    for i in result:

        # 找出沒有網址的連結
        getUrlResult = re.search("^"+define.mainUrl, i.get(define.subFilterTag))

        if getUrlResult is None:
            noHttp.append(i.get(define.subFilterTag))
        else:
            isHttp.append(i.get(define.subFilterTag))

    return noHttp, isHttp


def singleUrl(url=''):

    response    = requests.get(url)
    soup        = BeautifulSoup(response.text, "html.parser")
    result      = soup.find_all(define.mainFilterTag)

    # 取出所有a的陣列資料
    noHttp, isHttp = getUrl(result)

    # 刪除不要的網址
    usefulUrl = delItem(noHttp)

    # 補上網域名稱
    completeUrl = prependString(usefulUrl)

    # return uniqueList(completeUrl)
    # 結合兩個陣列
    return uniqueList(isHttp) + completeUrl


def mainLogic(allUrl=[]):

    if len(allUrl) > 0:
        for urlItem in allUrl:

            if urlItem != define.mainUrl:
                singleResult = singleUrl(urlItem)
                writeToTxt('mainResult', list(set(singleResult) - set(allUrl)))

    return True

def writeToTxt(filename, data):
    pics = ['.jpg', '.pdf']
    for item in data:
        result = re.search(define.domainName, item)
        if result:

            urlPath = pathlib.Path(item)
            if urlPath.suffix not in pics:
                path = filename.replace(define.mainUrl, '').rstrip('/')+'.txt'
                s = open(path, 'a')
                s.write(item+"\n")
                s.close()

