#!env3/bin/python

#coding=utf-8

import requests
import os
import pprint
# pip install requests[socks] pyTelegramBotAPI
# bpython
# pprint.pprint(r.json())

def ftok():
    f = open('token.txt')
    tok = f.read()
#    print(tok)
    f.close()
    return tok

TOKEN = ftok()
print(TOKEN)

list = os.listdir()
# for i in list:
#     print(i
