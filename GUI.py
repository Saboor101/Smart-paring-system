from tkinter import *
import pickle

# GUI

root = Tk()


listSlots = []
t = 0
root.config(bg='#78866b')
# GUI Spacing
sp1 = Label(root, text="", padx=20, bg='#78866b')
sp1.grid(row=1, column=2)
sp2 = Label(root, text="", padx=20, bg='#78866b')
sp2.grid(row=1, column=4)

# parent frames
frame = LabelFrame(root, text="Lane 1", padx=3, pady=3, borderwidth=10, bg='#7393B3')
frame.grid(row=0, column=0, columnspan=8)
mainLable = Label(frame, width=100, height=2, compound="c", font=2, bg="#3cb371", bd=0, padx=0)
mainLable.grid(row=0, column=0, columnspan=10)
frame12 = LabelFrame(root, text="Left", padx=3, pady=3, borderwidth=10, bg='#708090')
frame12.grid(row=1, column=0)
frame34 = LabelFrame(root, text="Middle", padx=3, pady=3, borderwidth=10, bg='#708090')
frame34.grid(row=1, column=3)
frame56 = LabelFrame(root, text="Right", padx=3, pady=3, borderwidth=10, bg='#708090')
frame56.grid(row=1, column=6)

# frames for lanes
frame1 = LabelFrame(frame12, text="Lane 1", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame1.grid(row=1, column=0)
frame2 = LabelFrame(frame12, text="Lane 2", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame2.grid(row=1, column=1, sticky='e')
frame3 = LabelFrame(frame34, text="Lane 1", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame3.grid(row=1, column=3)
frame4 = LabelFrame(frame34, text="Lane 2", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame4.grid(row=1, column=4)
frame5 = LabelFrame(frame56, text="Lane 1", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame5.grid(row=1, column=6)
frame6 = LabelFrame(frame56, text="Lane 2", padx=3, pady=3, borderwidth=3, bg='#7393B3')
frame6.grid(row=1, column=7)


# lane 1
for i in range(12):
    globals()['l1%s' % i] = Label(frame1, text=f'L1{i+1}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
    globals()['l1%s' % i].grid(row=t, column=0, pady=5)
    listSlots.append(globals()['l1%s' % i])
    t += 1
t = 0
# lane 2


for i in range(12):
    globals()['l2%s' % i] = Label(frame2, text=f'L2{i+1}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
    globals()['l2%s' % i].grid(row=t, column=0, pady=5)
    listSlots.append(globals()['l2%s' % i])
    t += 1
t = 0


# lane 3
s = 1
for i in range(12):
    if i != 8:
        globals()['m1%s' % s] = Label(frame3, text=f'M1{s}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
        globals()['m1%s' % s].grid(row=t, column=0, pady=5)
        listSlots.append(globals()['m1%s' % s])
        s += 1
    else:
        spacelane3 = Label(frame3, text='', width=20, height=3, compound="c", bg='gray', bd=0, padx=0)
        spacelane3.grid(row=t, column=0, pady=5)
    t += 1
t = 0


# lane 4
s = 1
for i in range(12):
    if i != 8:
        globals()['m1%s' % s] = Label(frame4, text=f'M2{s}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
        globals()['m1%s' % s].grid(row=t, column=0, pady=5)
        listSlots.append(globals()['m1%s' % s])
        s += 1
    else:
        spacelane4 = Label(frame4, text='', width=20, height=3, compound="c", bg='gray', bd=0, padx=0)
        spacelane4.grid(row=t, column=0, pady=5)
    t += 1
t = 0


# lane 5
for i in range(12):
    globals()['r1%s' % i] = Label(frame5, text=f'R1{i+1}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
    globals()['r1%s' % i].grid(row=t, column=0, pady=5)
    listSlots.append(globals()['r1%s' % i])
    t += 1



# lane 6
s = 1
for i in range(12):
    if i != 0:
        globals()['m1%s' % s] = Label(frame6, text=f'R2{s}', width=20, height=3, compound="c", bg="cyan", bd=0, padx=0)
        globals()['m1%s' % s].grid(row=t, column=0, pady=5)
        listSlots.append(globals()['m1%s' % s])
        s += 1
    else:
        spacelane4 = Label(frame6, text='', width=20, height=3, compound="c", bg='gray', bd=0, padx=0)
        spacelane4.grid(row=t, column=0, pady=5)
    t += 1
t = 0

with open('Avail', 'rb') as f:
    avail = pickle.load(f)

def time():
    try:
        with open('Avail', 'rb') as f:
            avail = pickle.load(f)
    except:
        print(1)
        # for i in range(70):
        #     avail.append(0)
        # avail[6] = 1
        # avail[19] = 1
        # avail[22] = 1
        # avail[26] = 1
        # avail[33] = 1
        # avail[42] = 1
        # avail[43] = 1
        # avail[50] = 1
        # avail[51] = 1
        # avail[53] = 1
        # avail[55] = 1
        # avail[57] = 1
        # avail[64] = 1
        # avail[65] = 1

    # print(avail)
    count = 0
    for label in listSlots:
        if avail[count] == 0:
            label.config(bg='#ff6347')
        else:
            label.config(bg='#90ee90')

        count += 1

    mainLable.config(text=f'Available Spaces: {avail[count]}/69')
    mainLable.after(1000, lambda: time())


time()

root.mainloop()
