#!/usr/bin/env python
# coding=utf-8

import pygtk
pygtk.require('2.0')
import gtk
import gobject
import time
import threading
import os

from wordutil import wordutil

closing = False

def init_ddict():

    vbox = gtk.VBox()
    swindow = gtk.ScrolledWindow()
    text = gtk.TextView()
    text.set_editable(False)
    textbuffer = text.get_buffer()

    textbuffer.set_text("Welcome to DDict")
    text.set_buffer(textbuffer)

    
    swindow.add(text)
    youdao_logo = gtk.Image()
    youdao_logo.set_from_file(get_resource_path("images/youdao.gif"))
    vbox.pack_start(youdao_logo)
    vbox.pack_start(swindow)


    wu = wordutil()

    return text,textbuffer,wu,vbox


def run_tasks(mtext,mtextbuffer,mwordutil,isclose):

    global closing
    gobject.threads_init()
    while(not closing):
        gtk.threads_enter()
        result = mwordutil.execfind()
        #print result
        #print "run"
        if(result!=""):
            mtextbuffer.set_text(result)
            mtext.set_buffer(mtextbuffer)
        gtk.threads_leave()
        time.sleep(0.1)

def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file,rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource


def main():
    txt,txtb,wu,vb = init_ddict()
    global closing

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("DDict")
    window.set_default_size(300,200)
    window.set_keep_above(True)
    window.connect('destroy',main_quit)
    #window.connect("destroy",lambda a:gtk.main_quit())
    window.add(vb)

    window.set_icon_from_file(get_resource_path("images/logo.png"))
    window.show_all()
    thread = threading.Thread(target=run_tasks,args=(txt,txtb,wu,closing))
    #thread.deamon = True
    thread.start()
    gtk.main()

def main_quit():
    global closing
    closing = True
    gtk.main_quit()

if __name__ == '__main__':
    main()
