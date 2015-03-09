#coding=utf8
import time
import os
import sys

import urllib2
import urllib

import json

class wordutil:
    def __init__(self):
        self.Alive=1
        self.count=1
        self.word='abcdefghijklmnopqrstuvwxyz'
        self.url="http://fanyi.youdao.com/openapi.do?keyfrom=youdaomini&key=1877956118&type=data&doctype=json&version=1.1&q="


    def execfind(self):
        var = os.popen('xsel').read()
        if(var!=self.word and var!=''):
            varr = self.getRequestWord(var)
            searchurl = self.url+urllib.quote(varr)
            ret=''
            req = urllib2.Request(searchurl)
            res_data = urllib2.urlopen(req)
            ret = res_data.read()
            if(ret!=''):
                self.word = var
                return self.getResultForWin(var,ret)
        return ""


    def getRequestWord(self,word):
        text = word.split('\n')[0].strip().strip('\r\n').strip('\r\n\x00')
        return text


    def getResultForWin(self,requestword,word):
        orijson = {}
        result = "  [查询]："+"\t"+requestword+"\n"
        try:
            orijson = json.loads(word)
        except ValueError:
            result = result + "解析错误，请重新取词"+"\n"
            return result

        ret_key = orijson.keys()
        if("errorCode" in orijson):
            codenum = orijson["errorCode"]
            if(codenum==20):
                result = result + "翻译文本过长"+"\n"
                return
            elif(codenum==30):
                result = result +"无法进行有效的翻译"+"\n"
                return
            elif(codenum==40):
                result = result +"不支持的语言类型"+"\n"
                return
            elif(codenum==50):
                result = result +"无效的key"+"\n"
                return
            elif(codenum==50):
                result = result +"无辞典结果，仅在获取辞典结果生效"+"\n"
                return
        if("translation" in orijson):
            if(orijson["translation"]==orijson["query"]):
                result = result +"未找到合适的翻译结果"+"\n"
            else:
                result = result +"  [翻译]:\t"+orijson["translation"][0]+"\n"
        if("basic" in ret_key):
            if("us-phonetic" in orijson["basic"]):
                result = result +"  [美式发音]:\t"+orijson["basic"]["us-phonetic"]+"\n"
            if("uk-phonetic" in orijson["basic"]):
                result = result +"  [英式发音]:\t"+orijson["basic"]["uk-phonetic"]+"\n"
            if("explains" in orijson["basic"]):
                explains = orijson["basic"]["explains"]
                result = result +"  [词典]:"+"\n"
                for ex in explains:
                    result = result +"\t"+ex+"\n"
        return result
