import tkinter, time, pygame, threading, os, keyboard
from pygame import mixer
from PIL import Image
from PIL import ImageTk
import PIL
import piano_lists4 as pl
from tkinter import *
mixer.init()

pygame.mixer.set_num_channels(50)

white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 2
right_oct = 3

left_hand = pl.left_hand
left_hand_black = pl.left_hand_black

right_hand = pl.right_hand
right_hand_black = pl.right_hand_black

piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

for i in range(len(white_notes)):
    #white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))
    white_sounds.append(mixer.Sound(f'assets/notes/{white_notes[i]}.wav'))
for i in range(len(black_notes)):
    #black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))
    black_sounds.append(mixer.Sound(f'assets/notes/{black_notes[i]}.wav'))


win = tkinter.Tk()
win.title('Piano')
#win.call('wm', 'iconphoto', win._w, PhotoImage(file='assets/logo.ico'))
canvas = tkinter.Canvas(win, width=1435, height=300, bg='#f0f0f0')
canvas.pack()

logo = PIL.Image.open(f'assets/logo.jpg')
logores = logo.resize((35, 35), PIL.Image.ANTIALIAS)
logoinst = ImageTk.PhotoImage(logores)
canvas.create_image(1402, 265, anchor=tkinter.NW, image=logoinst)
def draw():
    
    for i in range(28):
        canvas.create_rectangle(0+(50*i), 0, 50+(50*i), 300, fill='#ffffff', tags= 'white'+str(white_notes[i]))
        canvas.create_text(25+(50*i),275,text=white_notes[i],font ='arial 12 bold', fill='#c0c0c0')
    canvas.create_line(2,0,2,300, fill='#000000',)
    l = 0
    
    for i in range(4):
        for j in range(2):
            canvas.create_rectangle(35+(50*j)+(i*350), 0, 65+(50*j)+(i*350), 200,fill='#000000', tags= 'black'+str(black_labels[l]))
            canvas.create_text(50+(50*j)+(i*350),185,text=black_labels[l],font ='arial 8 bold', fill='#aaaaaa')
            l += 1
        for k in range(3):
            canvas.create_rectangle(185+(50*k)+(i*350), 0, 215+(50*k)+(i*350), 200,fill='#000000', tags= 'black'+str(black_labels[l]))
            canvas.create_text(200+(50*k)+(i*350),185,text=black_labels[l],font ='arial 8 bold', fill='#aaaaaa')
            l +=1

    # left hand controls
    for i in range(7):
        canvas.create_text(25+(50*i),250,text=str(left_hand[i]),font ='arial 12 bold', fill='#000000',tags='left_hand')
    l = 0
    for i in range(2):
        canvas.create_text(50+(50*i),150,text=left_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='left_hand')
        l +=1        
    for i in range(3):
        canvas.create_text(200+(50*i),150,text=left_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='left_hand')
        l +=1

    #right hand controls
    for i in range(7):
        canvas.create_text(725+(50*i),250,text=str(right_hand[i]),font ='arial 12 bold', fill='#000000',tags='right_hand')
    l = 0
    for i in range(2):
        canvas.create_text(750+(50*i),150,text=right_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='right_hand')
        l +=1        
    for i in range(3):
        canvas.create_text(900+(50*i),150,text=right_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='right_hand')
        l +=1

    canvas.create_rectangle(1405,5,1430,30,fill='#aaaaaa',tags='lenght')
    canvas.create_text(1417.5,16.5,text="⌒")
    canvas.create_text(1417.5,150,text="©Denis Dinga™", angle=-90, font = 'arial 20 bold')

draw()
tone_lenght = 6000
press_count_len = 0
fade_len = 500
def lenght(sur):
    global tone_lenght
    global press_count_len
    global fade_len
    x = sur.x
    y = sur.y
    if 1405<x<1430 and 5<y<30:
        if press_count_len % 2 ==0:
            fade_len = 2500
            canvas.itemconfig('lenght', width=3)
        else:
            fade_len = 500
            canvas.itemconfig('lenght', width=1)
    press_count_len +=1
    

#left hand

left_count = 0

def left_hand_counter(sur):
    canvas.delete('left_hand')
    print('called?')
    global left_count
    if sur.keysym == 'Down':
        left_count = left_count -1
        if left_count < 0:
            left_count = 0
    if sur.keysym == 'Up':
        left_count = left_count +1
        if left_count > 3:
            left_count = 3
    for i in range(7):
        canvas.create_text(25+(50*i)+(left_count*350),250,text=left_hand[i],font ='arial 12 bold', fill='#000000',tags='left_hand')
    l = 0
    for i in range(2):
        canvas.create_text(50+(50*i)+(left_count*350),150,text=left_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='left_hand')
        l +=1        
    for i in range(3):
        canvas.create_text(200+(50*i)+(left_count*350),150,text=left_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='left_hand')
        l +=1
    print(left_count)

# white left hand
Z_pressed = False
def Z():
    global Z_pressed
    
    if Z_pressed == False:
        print('zzzzzzzz')
        canvas.itemconfig('white'+str(white_notes[0+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[0+(left_count*7)].play(0, tone_lenght)
    Z_pressed = True

def Z_release():
    global Z_pressed
    white_sounds[0+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[0+(left_count*7)]), fill="#ffffff")
    Z_pressed = False

X_pressed = False

def X():
    global X_pressed
    
    if X_pressed == False:
        canvas.itemconfig('white'+str(white_notes[1+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[1+(left_count*7)].play(0, tone_lenght)
    X_pressed = True

def X_release():
    global X_pressed
    white_sounds[1+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[1+(left_count*7)]), fill="#ffffff")
    X_pressed = False
    
C_pressed = False
def C():
    global C_pressed
    
    if C_pressed == False:
        canvas.itemconfig('white'+str(white_notes[2+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[2+(left_count*7)].play(0, tone_lenght)
    C_pressed = True


def C_release():
    global C_pressed
    white_sounds[2+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[2+(left_count*7)]), fill="#ffffff")
    C_pressed = False    

V_pressed = False
def V():
    global V_pressed
    
    if V_pressed == False:
        canvas.itemconfig('white'+str(white_notes[3+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[3+(left_count*7)].play(0, tone_lenght)
    V_pressed = True

def V_release():
    global V_pressed
    white_sounds[3+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[3+(left_count*7)]), fill="#ffffff")
    V_pressed = False 

B_pressed = False
def B():
    global B_pressed
    
    if B_pressed == False:
        canvas.itemconfig('white'+str(white_notes[4+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[4+(left_count*7)].play(0, tone_lenght)
    B_pressed = True

def B_release():
    global B_pressed
    white_sounds[4+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[4+(left_count*7)]), fill="#ffffff")
    B_pressed = False 

N_pressed = False
def N():
    global N_pressed
    
    if N_pressed == False:
        canvas.itemconfig('white'+str(white_notes[5+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[5+(left_count*7)].play(0, tone_lenght)
    N_pressed = True
def N_release():
    global N_pressed
    white_sounds[5+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[5+(left_count*7)]), fill="#ffffff")
    N_pressed = False 

M_pressed = False
def M():
    global M_pressed
    
    if M_pressed == False:
        canvas.itemconfig('white'+str(white_notes[6+(left_count*7)]), fill="gold")
        canvas.update()
        white_sounds[6+(left_count*7)].play(0, tone_lenght)
    M_pressed = True

def M_release():
    global M_pressed
    white_sounds[6+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[6+(left_count*7)]), fill="#ffffff")
    M_pressed = False 
#black  left hand

S_pressed = False
def S():
    global S_pressed
    
    if S_pressed == False:
        canvas.itemconfig('black'+str(black_labels[0+(left_count*5)]), fill="gold")
        canvas.update()
        black_sounds[0+(left_count*5)].play(0, tone_lenght)
    S_pressed = True

def S_release():
    global S_pressed
    black_sounds[0+(left_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[0+(left_count*5)]), fill="#000000")
    S_pressed = False

D_pressed = False

def D():
    global D_pressed
    
    if D_pressed == False:
        canvas.itemconfig('black'+str(black_labels[1+(left_count*5)]), fill="gold")
        canvas.update()
        black_sounds[1+(left_count*5)].play(0, tone_lenght)
    D_pressed = True

def D_release():
    global D_pressed
    black_sounds[1+(left_count*7)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[1+(left_count*5)]), fill="#000000")
    D_pressed = False

G_pressed = False
def G():
    global G_pressed
    
    if G_pressed == False:
        canvas.itemconfig('black'+str(black_labels[2+(left_count*5)]), fill="gold")
        canvas.update()
        black_sounds[2+(left_count*5)].play(0, tone_lenght)
    G_pressed = True

def G_release():
    global G_pressed
    black_sounds[2+(left_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[2+(left_count*5)]), fill="#000000")
    G_pressed = False

H_pressed = False
def H():
    global H_pressed
    if H_pressed == False:
        canvas.itemconfig('black'+str(black_labels[3+(left_count*5)]), fill="gold")
        canvas.update()
        black_sounds[3+(left_count*5)].play(0, tone_lenght)
    H_pressed = True

def H_release():
    global H_pressed
    black_sounds[3+(left_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[3+(left_count*5)]), fill="#000000")
    H_pressed = False

J_pressed = False
def J():
    global J_pressed
    if J_pressed == False:
        canvas.itemconfig('black'+str(black_labels[4+(left_count*5)]), fill="gold")
        canvas.update()
        black_sounds[4+(left_count*5)].play(0, tone_lenght)
    J_pressed = True

def J_release():
    global J_pressed
    black_sounds[4+(left_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[4+(left_count*5)]), fill="#000000")
    J_pressed = False
#left hand

#right hand
right_count = 2

def right_hand_counter(sur):
    canvas.delete('right_hand')
    print('called?')
    global right_count
    if sur.keysym == 'Left':
        right_count = right_count -1
        if right_count < 0:
            right_count = 0
    if sur.keysym == 'Right':
        right_count = right_count +1
        if right_count > 3:
            right_count = 3
    for i in range(7):
        canvas.create_text(25+(50*i)+(right_count*350),250,text=right_hand[i],font ='arial 12 bold', fill='#000000',tags='right_hand')
    l = 0
    for i in range(2):
        canvas.create_text(50+(50*i)+(right_count*350),150,text=right_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='right_hand')
        l +=1        
    for i in range(3):
        canvas.create_text(200+(50*i)+(right_count*350),150,text=right_hand_black[l],font ='arial 8 bold', fill='#ffffff',tags='right_hand')
        l +=1
    print(left_count)

# white right hand
R_pressed = False
def R():
    global R_pressed
    
    if R_pressed == False:
        print('zzzzzzzz')
        canvas.itemconfig('white'+str(white_notes[0+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[0+(right_count*7)].play(0, tone_lenght)
    R_pressed = True

def R_release():
    global R_pressed
    white_sounds[0+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[0+(right_count*7)]), fill="#ffffff")
    R_pressed = False

T_pressed = False

def T():
    global T_pressed
    
    if T_pressed == False:
        canvas.itemconfig('white'+str(white_notes[1+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[1+(right_count*7)].play(0, tone_lenght)
    T_pressed = True

def T_release():
    global T_pressed
    white_sounds[1+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[1+(right_count*7)]), fill="#ffffff")
    T_pressed = False
    
Y_pressed = False
def Y():
    global Y_pressed
    
    if Y_pressed == False:
        canvas.itemconfig('white'+str(white_notes[2+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[2+(right_count*7)].play(0, tone_lenght)
    Y_pressed = True


def Y_release():
    global Y_pressed
    white_sounds[2+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[2+(right_count*7)]), fill="#ffffff")
    Y_pressed = False    

U_pressed = False
def U():
    global U_pressed
    
    if U_pressed == False:
        canvas.itemconfig('white'+str(white_notes[3+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[3+(right_count*7)].play(0, tone_lenght)
    U_pressed = True

def U_release():
    global U_pressed
    white_sounds[3+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[3+(right_count*7)]), fill="#ffffff")
    U_pressed = False 

I_pressed = False
def I():
    global I_pressed
    
    if I_pressed == False:
        canvas.itemconfig('white'+str(white_notes[4+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[4+(right_count*7)].play(0, tone_lenght)
    I_pressed = True

def I_release():
    global I_pressed
    white_sounds[4+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[4+(right_count*7)]), fill="#ffffff")
    I_pressed = False 

O_pressed = False
def O():
    global O_pressed
    
    if O_pressed == False:
        canvas.itemconfig('white'+str(white_notes[5+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[5+(right_count*7)].play(0, tone_lenght)
    O_pressed = True
def O_release():
    global O_pressed
    white_sounds[5+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[5+(right_count*7)]), fill="#ffffff")
    O_pressed = False 

P_pressed = False
def P():
    global P_pressed
    
    if P_pressed == False:
        canvas.itemconfig('white'+str(white_notes[6+(right_count*7)]), fill="gold")
        canvas.update()
        white_sounds[6+(right_count*7)].play(0, tone_lenght)
    P_pressed = True

def P_release():
    global P_pressed
    white_sounds[6+(right_count*7)].fadeout(fade_len)
    canvas.itemconfig('white'+str(white_notes[6+(right_count*7)]), fill="#ffffff")
    P_pressed = False 
#black  left hand

k5_pressed = False
def k5():
    global k5_pressed
    
    if k5_pressed == False:
        canvas.itemconfig('black'+str(black_labels[0+(right_count*5)]), fill="gold")
        canvas.update()
        black_sounds[0+(right_count*5)].play(0, tone_lenght)
    k5_pressed = True

def k5_release():
    global k5_pressed
    black_sounds[0+(right_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[0+(right_count*5)]), fill="#000000")
    k5_pressed = False

k6_pressed = False

def k6():
    global k6_pressed
    
    if k6_pressed == False:
        canvas.itemconfig('black'+str(black_labels[1+(right_count*5)]), fill="gold")
        canvas.update()
        black_sounds[1+(right_count*5)].play(0, tone_lenght)
    k6_pressed = True

def k6_release():
    global k6_pressed
    black_sounds[1+(right_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[1+(right_count*5)]), fill="#000000")
    k6_pressed = False

k8_pressed = False
def k8():
    global k8_pressed
    
    if k8_pressed == False:
        canvas.itemconfig('black'+str(black_labels[2+(right_count*5)]), fill="gold")
        canvas.update()
        black_sounds[2+(right_count*5)].play(0, tone_lenght)
    k8_pressed = True

def k8_release():
    global k8_pressed
    black_sounds[2+(right_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[2+(right_count*5)]), fill="#000000")
    k8_pressed = False

k9_pressed = False
def k9():
    global k9_pressed
    if k9_pressed == False:
        canvas.itemconfig('black'+str(black_labels[3+(right_count*5)]), fill="gold")
        canvas.update()
        black_sounds[3+(right_count*5)].play(0, tone_lenght)
    k9_pressed = True

def k9_release():
    global k9_pressed
    black_sounds[3+(right_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[3+(right_count*5)]), fill="#000000")
    k9_pressed = False

k0_pressed = False
def k0():
    global k0_pressed
    if k0_pressed == False:
        canvas.itemconfig('black'+str(black_labels[4+(right_count*5)]), fill="gold")
        canvas.update()
        black_sounds[4+(right_count*5)].play(0, tone_lenght)
    k0_pressed = True

def k0_release():
    global k0_pressed
    black_sounds[4+(right_count*5)].fadeout(fade_len)
    canvas.itemconfig('black'+str(black_labels[4+(right_count*5)]), fill="#000000")
    k0_pressed = False
#right hand

#left_hand_threads
def Z_thread(sur):
    t1 = threading.Thread(target=Z)
    t1.start()

def X_thread(sur):
    t2 = threading.Thread(target=X)
    t2.start()
    
def C_thread(sur):
    t3 = threading.Thread(target=C)
    t3.start()
def V_thread(sur):
    t4 = threading.Thread(target=V)
    t4.start()
def B_thread(sur):
    t5 = threading.Thread(target=B)
    t5.start()
def N_thread(sur):
    t6 = threading.Thread(target=N)
    t6.start()
def M_thread(sur):
    t7 = threading.Thread(target=M)
    t7.start()
def S_thread(sur):
    t8 = threading.Thread(target=S)
    t8.start()
def D_thread(sur):
    t9 = threading.Thread(target=D)
    t9.start()
def G_thread(sur):
    t10 = threading.Thread(target=G)
    t10.start()
def H_thread(sur):
    t11 = threading.Thread(target=H)
    t11.start()
def J_thread(sur):
    t12 = threading.Thread(target=J)
    t12.start()

#right_hand+threads
def R_thread(sur):
    t13 = threading.Thread(target=R)
    t13.start()

def T_thread(sur):
    t14 = threading.Thread(target=T)
    t14.start()
    
def Y_thread(sur):
    t15 = threading.Thread(target=Y)
    t15.start()
def U_thread(sur):
    t16 = threading.Thread(target=U)
    t16.start()
def I_thread(sur):
    t17 = threading.Thread(target=I)
    t17.start()
def O_thread(sur):
    t18 = threading.Thread(target=O)
    t18.start()
def P_thread(sur):
    t19 = threading.Thread(target=P)
    t19.start()
def k5_thread(sur):
    t20 = threading.Thread(target=k5)
    t20.start()
def k6_thread(sur):
    t21 = threading.Thread(target=k6)
    t21.start()
def k8_thread(sur):
    t22 = threading.Thread(target=k8)
    t22.start()
def k9_thread(sur):
    t23 = threading.Thread(target=k9)
    t23.start()
def k0_thread(sur):
    t24 = threading.Thread(target=k0)
    t24.start()

def Z_release_thread(sur):
    t25 = threading.Thread(target=Z_release)
    t25.start()
def X_release_thread(sur):
    t25 = threading.Thread(target=X_release)
    t25.start()

def C_release_thread(sur):
    t26 = threading.Thread(target=C_release)
    t26.start()
def V_release_thread(sur):
    t27 = threading.Thread(target=V_release)
    t27.start()

def B_release_thread(sur):
    t28 = threading.Thread(target=B_release)
    t28.start()
def N_release_thread(sur):
    t29 = threading.Thread(target=N_release)
    t29.start()

def M_release_thread(sur):
    t30 = threading.Thread(target=M_release)
    t30.start()
def S_release_thread(sur):
    t31 = threading.Thread(target=S_release)
    t31.start()
def D_release_thread(sur):
    t32 = threading.Thread(target=D_release)
    t32.start()
def G_release_thread(sur):
    t33 = threading.Thread(target=G_release)
    t33.start()
def H_release_thread(sur):
    t34 = threading.Thread(target=H_release)
    t34.start()
def J_release_thread(sur):
    t35 = threading.Thread(target=J_release)
    t35.start()

def R_release_thread(sur):
    t36 = threading.Thread(target=R_release)
    t36.start()
def T_release_thread(sur):
    t37 = threading.Thread(target=T_release)
    t37.start()

def Y_release_thread(sur):
    t38 = threading.Thread(target=Y_release)
    t38.start()
def U_release_thread(sur):
    t39 = threading.Thread(target=U_release)
    t39.start()

def I_release_thread(sur):
    t40 = threading.Thread(target=I_release)
    t40.start()
def O_release_thread(sur):
    t41 = threading.Thread(target=O_release)
    t41.start()

def P_release_thread(sur):
    t42 = threading.Thread(target=P_release)
    t42.start()
def k5_release_thread(sur):
    t43 = threading.Thread(target=k5_release)
    t43.start()
def k6_release_thread(sur):
    t44 = threading.Thread(target=k6_release)
    t44.start()
def k8_release_thread(sur):
    t45 = threading.Thread(target=k8_release)
    t45.start()
def k9_release_thread(sur):
    t46 = threading.Thread(target=k9_release)
    t46.start()
def k0_release_thread(sur):
    t47 = threading.Thread(target=k0_release)
    t47.start()
#LEFT
win.bind("<Up>", left_hand_counter)
win.bind("<Down>", left_hand_counter)
win.bind("<KeyPress-z>", Z_thread)
win.bind("<KeyRelease-z>", Z_release_thread)
win.bind("<KeyPress-x>", X_thread)
win.bind("<KeyRelease-x>", X_release_thread)
win.bind("<KeyPress-c>", C_thread)
win.bind("<KeyRelease-c>", C_release_thread)
win.bind("<KeyPress-v>", V_thread)
win.bind("<KeyRelease-v>", V_release_thread)
win.bind("<KeyPress-b>", B_thread)
win.bind("<KeyRelease-b>", B_release_thread)
win.bind("<KeyPress-n>", N_thread)
win.bind("<KeyRelease-n>", N_release_thread)
win.bind("<KeyPress-m>", M_thread)
win.bind("<KeyRelease-m>", M_release_thread)
win.bind("<KeyPress-s>", S_thread)
win.bind("<KeyRelease-s>", S_release_thread)
win.bind("<KeyPress-d>", D_thread)
win.bind("<KeyRelease-d>", D_release_thread)
win.bind("<KeyPress-g>", G_thread)
win.bind("<KeyRelease-g>", G_release_thread)
win.bind("<KeyPress-h>", H_thread)
win.bind("<KeyRelease-h>", H_release_thread)
win.bind("<KeyPress-j>", J_thread)
win.bind("<KeyRelease-j>", J_release_thread)

#RIGHT
win.bind("<Left>", right_hand_counter)
win.bind("<Right>", right_hand_counter)
win.bind("<KeyPress-r>", R_thread)
win.bind("<KeyRelease-r>", R_release_thread)
win.bind("<KeyPress-t>", T_thread)
win.bind("<KeyRelease-t>", T_release_thread)
win.bind("<KeyPress-y>", Y_thread)
win.bind("<KeyRelease-y>", Y_release_thread)
win.bind("<KeyPress-u>", U_thread)
win.bind("<KeyRelease-u>", U_release_thread)
win.bind("<KeyPress-i>", I_thread)
win.bind("<KeyRelease-i>", I_release_thread)
win.bind("<KeyPress-o>", O_thread)
win.bind("<KeyRelease-o>", O_release_thread)
win.bind("<KeyPress-p>", P_thread)
win.bind("<KeyRelease-p>", P_release_thread)
win.bind("<KeyPress-5>", k5_thread)
win.bind("<KeyRelease-5>", k5_release_thread)
win.bind("<KeyPress-6>", k6_thread)
win.bind("<KeyRelease-6>", k6_release_thread)
win.bind("<KeyPress-8>", k8_thread)
win.bind("<KeyRelease-8>", k8_release_thread)
win.bind("<KeyPress-9>", k9_thread)
win.bind("<KeyRelease-9>", k9_release_thread)
win.bind("<KeyPress-0>", k0_thread)
win.bind("<KeyRelease-0>", k0_release_thread)


win.bind("<Button-1>",lenght)

win.mainloop()


