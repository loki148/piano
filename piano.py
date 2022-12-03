import tkinter, time, pygame
from pygame import mixer
import piano_lists as pl
mixer.init()

pygame.mixer.set_num_channels(50)

white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 2
right_oct = 3

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))


win = tkinter.Tk()
win.title('Piano')
canvas = tkinter.Canvas(win, width=1435, height=300, bg='grey')
canvas.pack()

def draw():
    for i in range(36):
        canvas.create_rectangle(0+(40*i), 0, 40+(40*i), 300, fill='#ffffff', tags= 'white'+str(white_notes[i]))
        canvas.create_text(20+(40*i),275,text=white_notes[i],font ='arial 12 bold', fill='#c0c0c0')
    l = 0
    for i in range(5):
        for j in range(2):
            canvas.create_rectangle(30+(40*j)+(i*280), 0, 50+(40*j)+(i*280), 200,fill='#000000', tags= 'black'+str(black_labels[l]))
            canvas.create_text(40+(40*j)+(i*280),185,text=black_labels[l],font ='arial 6 bold', fill='#aaaaaa')
            l += 1
        for k in range(3):
            canvas.create_rectangle(150+(40*k)+(i*280), 0, 170+(40*k)+(i*280), 200,fill='#000000', tags= 'black'+str(black_labels[l]))
            canvas.create_text(160+(40*k)+(i*280),185,text=black_labels[l],font ='arial 6 bold', fill='#aaaaaa')
            l +=1
draw()


win.mainloop()
