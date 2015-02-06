#!/usr/bin/env python
# coding=utf-8

from wordutil import wordutil

def main():
    dict = wordutil()
    dict.run()

    alive = 1
    while(alive):
        letter = raw_input("Input exit or Ctrl+C to exit ddict\n")
        if(letter=='exit'):
            break


if __name__ == '__main__':
    main()
