#coding=utf8
import thread
import time
import os

import urllib2

import json

class wordutil:
    def __init__(self):
        self.Alive=1
        self.count=1
        self.word='abcdefghijklmnopqrstuvwxyz'
        self.url="http://fanyi.youdao.com/openapi.do?keyfrom=youdaomini&key=1877956118&type=data&doctype=json&version=1.1&q="

    def threadTest(self):
        while self.count:
            var = os.popen('xsel').read()
            if(var!=self.word and var!=''):
                varr = self.getRequestWord(var)
                print varr
                searchurl=self.url+varr
                ret=''
                req = urllib2.Request(searchurl)
                res_data = urllib2.urlopen(req)
                ret = res_data.read()
                if(ret==''):
                    print 'error!'
                else:
                    #print ret
                    self.getResult(ret)
                self.word=var
            time.sleep(0.2)


    def getRequestWord(self,word):
        text = word.split('\n')[0].strip().strip('\r\n').strip('\r\n\x00')
        #print text
        return text


    def getResult(self,word):
        orijson = {}
        try:
            orijson = json.loads(word)
        except ValueError:
            print "解析错误，请重新取词"
            return

        ret_key = orijson.keys()
        if("errorCode" in orijson):
            codenum = orijson["errorCode"]
            if(codenum==20):
                print "翻译文本过长"
                return
            elif(codenum==30):
                print "无法进行有效的翻译"
                return
            elif(codenum==40):
                print "不支持的语言类型"
                return
            elif(codenum==50):
                print "无效的key"
                return
            elif(codenum==50):
                print "无辞典结果，仅在获取辞典结果生效"
                return
        if("translation" in orijson):
            print "翻译：",orijson["translation"][0]
        if("basic" in ret_key):
            if("us-phonetic" in orijson["basic"]):
                print "美式发音",orijson["basic"]["us-phonetic"]
            if("uk-phonetic" in orijson["basic"]):
                print "英式发音",orijson["basic"]["uk-phonetic"]
            if("explains" in orijson["basic"]):
                explains = orijson["basic"]["explains"]
                for ex in explains:
                    print ex

    def run(self):
        thread.start_new_thread(self.threadTest,())
