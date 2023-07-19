import pyautogui
import threading
from time import sleep

global p;global v
v = [0,0,0,0]
p = [0,0,0,0,0,0]

def to_float(v):
   try:
       return float(v)
   except Exception:
       return float(0)

def update_vecteur(a,v,p):
    a = a.split(",")

    v[0] += to_float(a[6]) * to_float(a[0])
    v[1] += to_float(a[6]) * to_float(a[1])
    v[2] += to_float(a[6]) * to_float(a[2])

    p[0] += to_float(a[6]) * v[0]
    p[1] += to_float(a[6]) * v[1]
    p[2] += to_float(a[6]) * v[2]

    p[3] += to_float(a[6]) * to_float(a[3])
    p[4] += to_float(a[6]) * to_float(a[4])
    p[5] += to_float(a[6]) * to_float(a[5])

    v[3]+=1
    if (v[3]==50):
        v[0] = v[0]/2
        v[1] = v[1]/2
        v[2] = v[2]/2
        v[3] = 0

    return v,p

def souris(p,v):
    while 1:
        sleep(0.01)
        pyautogui.moveRel(-p[0]*10_000,p[1]*10_000,duration=0)
        p[0] = 0
        p[1] = 0

            

t = threading.Thread(target=souris, args=(p,v,))
t.start()