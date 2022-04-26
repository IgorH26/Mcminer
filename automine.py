import pyautogui
import time

def main():
    time.sleep(10)
    a = 0 
    e = True
    Shift(True)
    for _ in range(18):
        mineBlock()
        if Danger() and a < 1:
            goBackward()
            a = 15
            if e:
                turnLeft()
                e = False

            else:
                turnRight()
                e = True

        mineBlock()
        if Danger() and a < 1:
            goBackward()
            a = 15
            if e:
                turnLeft()
                e = False

            else:
                turnRight()
                e = True
        else:
            goForward()
            a = a - 1

        


def Danger():
    e = pyautogui.pixel(957, 567)
    R = e[0]
    print(R)
    if R > 25:
        return True
    return False    



def Shift(x):
    if x ==True:
        pyautogui.keyDown('shift')
    else:
        pyautogui.keyUp('shift')



def mineBlock():
    
    
    pyautogui.mouseDown(button='left')
    time.sleep(0.77)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)



def goForward():
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    time.sleep(0.1)



def goBackward():
    Shift(False)
    pyautogui.keyDown('s')
    time.sleep(2.4)
    pyautogui.keyUp('s')
    Shift(True)
    time.sleep(0.1)

def turnLeft():
    pyautogui.keyDown('left')
    time.sleep(0.9)
    pyautogui.keyUp('left')
    time.sleep(0.1)


def turnRight():
    pyautogui.keyDown('right')
    time.sleep(0.9)
    pyautogui.keyUp('right')
    time.sleep(0.1)



if __name__ =="__main__":
    main()