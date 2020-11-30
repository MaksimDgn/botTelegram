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

TOKEN = ''

path = '/home/maksim/projects/py_prj/botTelegram'
listdir = os.listdir(path)

f = 'mytest2.png'
MytestD = '-437278136'
chat_id = '-437278136'

KeyboardButton = 'text'
KeyboardButtonPollType = 'Poll'
InlineKeyboardButton = [{'inline_keyboard': {'text': 'Leabel', 'url':''}}]

def sendMsg(TOKEN, smsg, mesageText):
    #TOKEN = ftok()
   # не работает params = {'chat_id': MytestD, 'text' : 'Привет, Мир!', 'reply_markup': InlineKeyboardButton}
    params = {'chat_id': MytestD, 'text' : 'Привет, Мир!'}
    params['text'] = mesageText
    #params['message'] = mesageText
    metod = smsg
    if metod == 'sendMessage':
        rsend = requests.post('https://api.telegram.org/bot{0}/{1}?'.format(TOKEN, metod), params)
        print("\n Send message done. \n\n")
    if metod == 'sendMedia':
        inF = InputFile()
        parts = inF.infoFile()
        name = inF.getName()
        my_inF = {'id': '12345', 'parts': parts, 'name': name, 'md5_checksum': ''}
        InputPeer = chat_id
        params = {'peer': InputPeer, 'media': my_inF , 'message': mesageText, 'random_id': '0'}
        print(params)
        rsend = requests.post('https://api.telegram.org/bot{0}/{1}?'.format(TOKEN, metod), params)
        print("\nSend Media done. \n\n")
    print(rsend.text)

    
class InputFile:
    def __init__(self, fileName='mytest.png', path=path):
        self.path = path        
        self.fname = fileName
        os.path.getsize(self.fname)
        self.sz = os.path.getsize(self.fname)        
        self.parts = os.path.getsize(self.fname)%1024
        self.szK = os.path.getsize(self.fname)/1024
#        s = 524288 % 1024

    def infoFile(self):
        # print(self.fname)
        # print("Path: {} size: {} bytes".format(self.path, self.sz))
        # print("Path: {}size:  {} Kbytes".format(self.path, self.szK))
        # print(' %d parts'%self.parts)
        return self.parts

    def getName(self):
        return self.fname


    def uploadFile(self):

        f = open(self.fname, 'rb')
        # while line in f:
        #     print(line)
        print('***')
        file = f.read()
        params = {'file_id': '123', 'file_part' : self.parts, 'bytes': file}
        r = requests.post('https://api.telegram.org/bot'+TOKEN+'/upload.saveFilePart?', params)
        print(r.text)
        resultUpdate = r.json()
        print(resultUpdate)
        # for listReq in resultUpdate['result']:
        #     print(listReq['message']['chat'])
       
        f.close()
        print("saveFilePart done.")

    def myinputFile(self, id, parts, name):
        md5_checksum = ''
        f = open(self.fname, 'rb')
        # while line in f:
        #     print(line)
        print('***')
        file = f.read()
        params = {'file_id': '123', 'file_part' : self.parts, 'bytes': file}
        r = requests.post('https://api.telegram.org/bot'+TOKEN+'/upload.saveFilePart?', params)
        print(r.text)
        resultUpdate = r.json()
        print(resultUpdate)
        # for listReq in resultUpdate['result']:
        #     print(listReq['message']['chat'])
       
        f.close()
        print("saveFilePart done.")        



#print('Hello inF:')
#print(my_inF)

print("Dir: %s" %path)
hfile = InputFile('mytest.png',path)
hfile.infoFile()


def result_getupdates(res):
    resultUpdate = res
    in_result = ['message_id', 'from', 'chat', 'date', 'text']
    for listReq in resultUpdate['result']:
        if listReq['message']:
           # print("Сообщение: \n{} ".format(listReq['message']))
            for i in in_result:
                print("{}: {}".format(i, listReq['message'][i]))

def main():
    TOKEN = ftok()
    TOKEN = TOKEN.strip()

    r = requests.post('https://api.telegram.org/bot'+TOKEN+'/getupdates')
    print(r.text)
    print('='*30+' Get_Updates '+'='*30)
    resultUpdate = r.json()
    result_getupdates(resultUpdate)

                   # print("Сообщение от {} c id:{} в чат".format(listReq['message']['chat']['first_name'],  listReq['message']['chat']['id']))

    #params = {'chat_id': '-437278136', 'message': 'TestMedia'}
#    params = {'chat_id': '-437278136', 'media': my_inF , 'message': 'TestMedia'}
   # rsend = requests.post('https://api.telegram.org/bot'+TOKEN+'/sendMedia?', params)


    sendMsg(TOKEN, 'sendMessage', 'KeyboardButton send_message в chat')
    # sendMsg(TOKEN, 'sendMedia', 'KeyboardButton send Media в chat')

if __name__ == '__main__':
    main()

