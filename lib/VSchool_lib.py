import pyautogui as pag
import clipboard as cb
import pandas as pd
import os, sys
import time

PATH = '/home/lloli/Documents/GitHub/Sorn'
ID =  os.path.join(PATH,'assets/id.png')
ANS = os.path.join(PATH,'assets/ans.png')
NEXT =  os.path.join(PATH,'assets/next.png')
HUB = os.path.join(PATH,'assets/ss.png')
QU = os.path.join(PATH,'assets/nt.png')
ส่ง = os.path.join(PATH,'assets/send_.png')
ยืน = os.path.join(PATH,'assets/stand.png')
ยืนน = os.path.join(PATH,'assets/stand2.png')
load2 = os.path.join(PATH,'assets/load2.png')
ตก = os.path.join(PATH,'assets/fall.png')
LAST = os.path.join(PATH,'assets/LAST.png')
SEND = os.path.join(PATH,'assets/send_PRETEST.png')
SEND2 = os.path.join(PATH,'assets/send2.png')
X = os.path.join(PATH,'assets/X.png')
UNWANTED = os.path.join(PATH,'assets/UNWANTED.png')
CONFIRM_PT = os.path.join(PATH,'assets/CONFIRM_PT.png')

data_path = '/home/lloli/Documents/GitHub/Sorn/all.csv'
data = pd.read_csv(data_path)


lst_ID = data['id'].to_list()
lst_ANS = data['ans'].to_list()

def getID():

    lc = pag.locateCenterOnScreen(image=ID)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=ID)
        print('ID not Found')


    pag.tripleClick(lc)
    pag.hotkey('ctrl','c')

    while not cb.paste().count('-') == 3:
        pag.tripleClick(lc)
        pag.click(lc)
        pag.hotkey('ctrl','c')

    pag.click(lc)
    print(cb.paste().split()[-1])
    return cb.paste().split()[-1]

def getANS():

    lc = pag.locateCenterOnScreen(image=ANS)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=ANS)
        print('ANS not Found')


    pag.tripleClick(lc)
    pag.hotkey('ctrl','c')

    while not ' ' in cb.paste():
        pag.tripleClick(lc)
        pag.click(lc)
        pag.hotkey('ctrl','c')

    pag.click(lc)
    print(cb.paste().split()[-1])
    return cb.paste().split()[-1]    
    
def Next():
    e = 0
    lc = pag.locateCenterOnScreen(image=NEXT)

    while lc == None:
        lc = pag.locateCenterOnScreen(image=NEXT)
        print('NEXT not Found')
        for i in range(0,3):
            pag.press('pagedown')
        time.sleep(1)
        lc = pag.locateCenterOnScreen(image=NEXT)


        e  = e+1
        if e == 3:
            for i in range(0,3):
                pag.press('pageup')
            time.sleep(1)
            lc = pag.locateCenterOnScreen(image=HUB)
            while lc == None:
                pag.press('pageup')
                time.sleep(1)
                lc = pag.locateCenterOnScreen(image=HUB)
                print('HUB not found')
                
    pag.click(lc)
    time.sleep(2)
    
    print('clicked NEXT/HUB')

    return e

def find_LAST():
    lc = pag.locateCenterOnScreen(image=LAST)
    if lc == None:
        pag.press('pagedown')
        pag.press('pagedown')
        pag.press('pagedown')
        time.sleep(1)
        lc = pag.locateCenterOnScreen(image=LAST)
    return lc

def to_ANSWER():
    o = 0
    lc = pag.locateCenterOnScreen(image=QU)
    while lc == None:
        pag.press('pagedown')
        time.sleep(1)
        lc = pag.locateCenterOnScreen(image=QU)
        if o == 5:
            lc = pag.locateCenterOnScreen(image=LAST)
            
    pag.click(lc)
    print('Clicked ข้อสอบ')

    lc = pag.locateCenterOnScreen(image=ส่ง)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=ส่ง)

    pag.click(lc)
    print('Clicked ส่ง')

    lc = pag.locateCenterOnScreen(image=ยืน)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=ยืน)
        while lc == None:
            lc = pag.locateCenterOnScreen(image=ยืนน)

    pag.click(lc)
    print('Clicked ยืนยัน')


    lc = pag.locateCenterOnScreen(image=ตก)
    while lc == None:
        pag.click(x=1463, y=489)
        lc = pag.locateCenterOnScreen(image=ตก)

    pag.click(lc)
    print('Clicked ตกลง')

def send():
    lc = pag.locateCenterOnScreen(image=SEND)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=SEND)
        if lc == None:
            lc = pag.locateCenterOnScreen(image=SEND2)

    pag.click(lc)
    print('Clicked SEND')

def decline():
    lc = pag.locateCenterOnScreen(image=UNWANTED)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=UNWANTED)

    pag.click(x=975, y=304)
    lc = pag.locateCenterOnScreen(image=UNWANTED)
    if not lc == None:
        pag.click(lc)
    print('Clicked UNWANTED')
    
def confirm():
    time.sleep(2)
    loading = pag.locateCenterOnScreen(image=load2)
    if not loading == None:
        print('Loading')
        time.sleep(10)
    if not loading == None:
        print('Loading')
        time.sleep(10)
    if not loading == None:
        print('Loading')
        time.sleep(10)  
    lc = pag.locateCenterOnScreen(image=ยืน)
    if lc == None:
        lc = pag.locateCenterOnScreen(image=ยืนน)
            
    while lc == None:
        lc = pag.locateCenterOnScreen(image=ยืน)
        if lc == None:
            lc = pag.locateCenterOnScreen(image=ยืนน)
            

    pag.click(lc)
    print('Clicked CONFIRM')
    
def agree_PT():
    lc = pag.locateCenterOnScreen(image=CONFIRM_PT)
    while lc == None:
        pag.moveTo(x=1463, y=489)
        lc = pag.locateCenterOnScreen(image=CONFIRM_PT)
    pag.click(lc)
    print('Clicked AGREE')

def  x():
    lc = pag.locateCenterOnScreen(image=X)
    while lc == None:
        lc = pag.locateCenterOnScreen(image=X)

    pag.click(lc)
    print('Clicked X')
    
def agree():
    lc = pag.locateCenterOnScreen(image=ตก)
    while lc == None:
        pag.moveTo(x=1463, y=489)
        lc = pag.locateCenterOnScreen(image=ตก)

    pag.click(lc)
    print('Clicked AGREE')
    
def gather():
    N=0
    while True:
        lst_ID.append(getID())
        lst_ANS.append(getANS())
        lst_ANS2 = [{'ก':1,'ข':2,'ค':3,'ง':4,'จ':5,'A':1,'B':2,'C':3,'D':4,'E':5}.get(n, n) for n in lst_ANS]
        เฉลย = pd.DataFrame({
            'id' : lst_ID,
            'ans_TH' : lst_ANS,
            'ans' : lst_ANS2
            })

        เฉลย['ans'] = เฉลย['ans_TH'].replace({
                                                'ก':1,
                                                'ข':2,
                                                'ค':3,
                                                'ง':4,
                                                'จ':5,
                                                'A':1,
                                                'B':2,
                                                'C':3,
                                                'D':4,
                                                'E':5
                                            })
        เฉลย['ans_TH'] = เฉลย['ans_TH'].replace({
                                        1:'A',
                                        2:'B',
                                        3:'C',
                                        4:'D',
                                        5:'E'
                                    })
        เฉลย.drop(columns =  'ans_TH').drop_duplicates().sort_values('id').reset_index(drop= True).to_csv(data_path,index=False)
        data = pd.read_csv(data_path)
        data = data.drop(data[data['id'] == data['ans']].index)
        if not 'int' in str(data.dtypes['ans']):
            data = data.drop(data[data['ans'].str.len() > 1].index[0])
        data2 = pd.DataFrame()
        data2['id'] = data['id']
        data2['ans'] = data['ans']
        data2.to_csv(data_path,index=False)
        err = Next()
        N = N +1
        print('Quiz Number:', N,'\n')
        if err == 3: 
            break 

# lst_ID = []
# lst_ANS = []


# for i in range(1,4):
#     print(i)
#     time.sleep(1)
# N = 0

# while True:
#     ไปหาเฉลย()
#     while True:
#         lst_ID.append(getID())
#         lst_ANS.append(getANS())
#         เฉลย = pd.DataFrame({
#             'id' : lst_ID,
#             'ans' : lst_ANS
#             })
#         เฉลย.drop_duplicates().sort_values('id').reset_index(drop= True).to_csv('เอก.csv')
#         err = Next()
#         N = N +1
#         print('Quiz Number:', N,'\n')
#         if err == 3: 
#             break 

