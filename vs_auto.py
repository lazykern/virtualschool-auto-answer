import pyautogui as auto
import pandas as pd
import os,sys
import clipboard as cb
LIB = '/home/lloli/Documents/Projects/VSchool'
VSchool = '/home/lloli/Documents/GitHub/Sorn'
sys.path.append(VSchool)
sys.path.append(LIB)
import VSchool_lib as vsl
import vschool_lib as vs
import pandas as pd
import time

df = pd.read_csv(os.path.join(VSchool,'all.csv'))
choice_1 = os.path.join(VSchool,'assets/1.png')
choice_2 = os.path.join(VSchool,'assets/2.png')
choice_3 = os.path.join(VSchool,'assets/3.png')
choice_4 = os.path.join(VSchool,'assets/4.png')
choice_5 = os.path.join(VSchool,'assets/5.png')
choice_5_old = os.path.join(VSchool,'assets/5_old.png')
choice_1E = os.path.join(VSchool,'assets/1E.png')
choice_2E = os.path.join(VSchool,'assets/2E.png')
choice_3E = os.path.join(VSchool,'assets/3E.png')
choice_4E = os.path.join(VSchool,'assets/4E.png')
choice_5E = os.path.join(VSchool,'assets/5E.png')
choice_1E1 = os.path.join(VSchool,'assets/1E1.png')
choice_2E1 = os.path.join(VSchool,'assets/2E1.png')
choice_3E1 = os.path.join(VSchool,'assets/3E1.png')
choice_4E1 = os.path.join(VSchool,'assets/4E1.png')
choice_1E2 = os.path.join(VSchool,'assets/1E2.png')
choice_2E2 = os.path.join(VSchool,'assets/2E2.png')
choice_3E2 = os.path.join(VSchool,'assets/3E2.png')
choice_4E2 = os.path.join(VSchool,'assets/4E2.png')
quiz_50 = os.path.join(VSchool,'assets/QUIZ_50.png')
quiz_10 = os.path.join(VSchool,'assets/QUIZ_10.png')
id  = os.path.join(VSchool,'assets/id_TAKE.png')
load = os.path.join(VSchool,'assets/load.png')
sv1  = os.path.join(VSchool,'assets/save.png')
sv2  = os.path.join(VSchool,'assets/save_old.png')
skp1  = os.path.join(VSchool,'assets/skip.png')
skp2  = os.path.join(VSchool,'assets/skp.png')
white = os.path.join(VSchool,'assets/white.png')

def getID():

    lc = auto.locateCenterOnScreen(id)
    while lc == None:
        if lc == None:
            auto.press('pageup')
            auto.press('pageup')
            time.sleep(1)
        
        lc = auto.locateCenterOnScreen(id)
        sys.stdout.write("\r" + "ID not found")
        sys.stdout.flush()
        time.sleep(0.25)

    sys.stdout.write("\r"+ "ID found")
    sys.stdout.flush()
    auto.tripleClick(lc)
    auto.hotkey('ctrl','c')

    while not cb.paste().count('-') == 3:
        auto.tripleClick(lc)
        auto.click(lc)
        auto.hotkey('ctrl','c')

    auto.click(lc)
    
    sys.stdout.write("\r" + "ID found")
    sys.stdout.flush()
    return cb.paste()

def save():


    lc_save = auto.locateCenterOnScreen(sv1)
    if lc_save == None:
        lc_save = auto.locateCenterOnScreen(sv2)
    while lc_save == None:
        auto.press('pagedown')
        auto.press('pagedown')
        time.sleep(1)
        lc_save = auto.locateCenterOnScreen(sv1)
        if lc_save == None:
            lc_save = auto.locateCenterOnScreen(sv2)
            if lc_save == None:
                sys.stdout.write("\r"+ "SAVE not found")
                sys.stdout.flush()
                time.sleep(0.25)
            
    auto.click(lc_save)

def skip():


    lc_skip = auto.locateCenterOnScreen(skp1)
    if lc_skip == None:
        lc_skip = auto.locateCenterOnScreen(skp2)
        
    while lc_skip == None:

        auto.press('pagedown')
        auto.press('pagedown')
        time.sleep(1)
        
        lc_skip = auto.locateCenterOnScreen(skp1)
        if lc_skip == None:
            lc_skip = auto.locateCenterOnScreen(skp2)
            if lc_skip == None:
                sys.stdout.write("\r"+ "SKIP not found")
                sys.stdout.flush()
                time.sleep(0.25)

        
    auto.click(lc_skip)

def clickChoice(choice,lang):
    if (lang == 'TH') or (lang == 'th'):
        switcher = {
            1: choice_1,
            2: choice_2,
            3: choice_3,
            4: choice_4,
            5: choice_5
            }
    elif (lang == 'EN') or (lang == 'en'):
        switcher = {
            1: choice_1E,
            2: choice_2E,
            3: choice_3E,
            4: choice_4E,
            5: choice_5E
            }
    choice = int(choice)
    lc_choice = auto.locateCenterOnScreen(switcher[choice])
    print(choice)
    while lc_choice == None:


        if (choice == 5) and (lang == 'th'):
            lc_choice = auto.locateCenterOnScreen('/home/lloli/Documents/GitHub/Sorn/assets/choice_5_old1.png')
                

            
        if lc_choice == None:    
            sys.stdout.write("\r"+ "Choice not found")
            sys.stdout.flush()
            auto.press('pagedown')
            auto.press('pagedown')
            time.sleep(1)
            lc_choice = auto.locateCenterOnScreen(switcher[choice])
            

    print('\n')
    sys.stdout.write("\r" + "Choice found")
    sys.stdout.flush()
    auto.click(lc_choice)
    print('\n(',choice,') Choice clicked') 



def find_loading():
    return auto.locateCenterOnScreen(load)

def find_50():
    return auto.locateCenterOnScreen(quiz_50)

def find_10():
    return auto.locateCenterOnScreen(quiz_10)

def auto_take50(lang):
    wow=[]

    i = 0
    ncorrect = 0
    ndone = 0
    for i in range(1,4):
        sys.stdout.write("\r"+ "Starting in {}".format(i))
        sys.stdout.flush()
        time.sleep(1)
        
    while True:
        time.sleep(1)

        inp = getID()
        print(inp)
        x = vs.answer(inp)
        ndone = ndone+1
        if not x == None:
            clickChoice(x,lang)
            save()
            print('\n')
            ncorrect = ncorrect+1
        else:
            print("\n'"+inp+"' is not in the Database")
            wow.append(inp)
            skip()
            
        while not find_loading == None:
                sys.stdout.write("\r" + "Loading")
                sys.stdout.flush()
                time.sleep(0.25)
                if not auto.locateCenterOnScreen(id) == None:
                    break
        i = i+1
        print(i)
        if (ndone - ncorrect) >= 1:
            break
        if not find_50() == None:
            break
        
    if not find_50() == None:
        inp = getID()
        print(inp)
        x = vs.answer(inp)
        ndone = ndone+1
        if not x == None:
            clickChoice(x,lang)
            save()
            print('\n')
            ncorrect = ncorrect+1
        else:
            print("'"+inp+"' is not in the Database")
        
    print('Done, n(Correct) = ',ncorrect,'\nn(Done) = ', ndone)
    return (ncorrect,ndone,inp)


def auto_take10(lang,nwrong = 1):
    wow=[]

    i = 0
    ncorrect = 0
    ndone = 0
    for i in range(1,4):
        sys.stdout.write("\r"+ "Starting in {}".format(i))
        sys.stdout.flush()
        time.sleep(1)

    while True:
        time.sleep(1)
        inp = getID()
        print(inp)
        x = vs.answer(inp)
        ndone = ndone+1
        if not x == None:
            clickChoice(x,lang)
            save()
            print('\n')
            ncorrect = ncorrect +1
        else:
            print("\n'"+inp+"' is not in the Database")
            wow.append(inp)
            skip()
            
        while not find_loading == None:
                sys.stdout.write("\r" + "Loading")
                sys.stdout.flush()
                time.sleep(0.25)
                if not auto.locateCenterOnScreen(id) == None:
                    break
        i = i+1
        print('\n' ,i)
        if (ndone-ncorrect) >= nwrong:
            break
        if not find_10() == None:
            break
        
    if not find_10() == None:   
        inp = getID()
        print(inp)
        x = vs.answer(inp)
        ndone = ndone+1
        if not x == None:
            clickChoice(x,lang)
            save()
            print('\n')
            ncorrect = ncorrect +1
        else:
            print("'"+inp+"' is not in the Database")
        
    print('Done, n(Correct) = ',ncorrect,'\nn(Done) = ', ndone)
    return (ncorrect,ndone)