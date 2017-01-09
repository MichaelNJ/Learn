import sqlite3 as lite
import sys
from datetime import time, datetime
import turtle
import logging

logging.basicConfig(filename="rasp.dat", level=logging.INFO)
date = datetime.now()

try:
    import Tkinter as tk

except ImportError:
    import tkinter as tk
    import tkinter.messagebox

root = tk.Tk()
# root.overrideredirect(True)
root.resizable(width=tk.FALSE, height=tk.FALSE)

all_width = 700
all_height = 600

hs = root.winfo_screenheight()
ws = root.winfo_screenwidth()

w = all_width
h = all_height

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Learn with the rasp")
root.config(bg="#f4f4f4")

mark = 0
points = tk.StringVar()

# create the the applications database
"""con = lite.connect("learn.db")
with con:
    cur = con.cursor()
    cur.execute(
        ''' CREATE TABLE Students(Student_name TEXT NOT NULL, tr_name TEXT NOT NULL , time_used TEXT NOT NULL ) ''')
    cur.execute('''INSERT INTO Students VALUES(student_name.get(), teacher_name.get(), str(date))''')
"""
# student and teacher name
student_name = tk.StringVar()
teacher_name = tk.StringVar()

# turtle stuff
# wn = turtle.Screen()

# shapes and hopefully sounds
# variables
a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()
d = tk.StringVar()
e = tk.StringVar()
f = tk.StringVar()
g = tk.StringVar()
h = tk.StringVar()


class arts():
    def __init__(self, master):
        master.withdraw()
        # craft = tk.Toplevel()
        new = tk.Toplevel()
        new_width = 840
        new_height = 700
        new.geometry('%dx%d' % (new_width, new_height))
        new.resizable(width=tk.FALSE, height=tk.TRUE)
        new.config(bg="#ffffff")
        msg = tk.Label(new, text="Basic Mathematics -Addition", font=('Arial Narrow', 15), bg="#ffffff").grid(row=0, columnspan=2, sticky=tk.W, padx=60)
        one = tk.Label(new, text="1. 35 + 68 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=4, column=0, sticky=tk.W, ipady=10, padx=40)
        two = tk.Label(new, text="2. 77 + 43 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=5, column=0, sticky=tk.W, ipady=10, padx=40)
        three = tk.Label(new, text="3. 818 + 282 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=6, column=0, sticky=tk.W, ipady=10, padx=40)
        four = tk.Label(new, text="4. 19 + 17 + 95 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=7, column=0, sticky=tk.W, ipady=10, padx=40)
        five = tk.Label(new, text="5. 270.8 + 2.73 + 54.6 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=8, column=0, sticky=tk.W, ipady=10, padx=40)

        mark = tk.StringVar()
        mark = 0
        x = tk.StringVar()
        y = tk.StringVar()
        z = tk.StringVar()
        a = tk.StringVar()
        b = tk.StringVar()

        e = tk.StringVar()
        f = tk.StringVar()
        g = tk.StringVar()
        h = tk.StringVar()
        i = tk.StringVar()

        one_e = tk.Entry(new, textvariable=x, text=x, width=5)
        one_e.grid(row=4, column=1, sticky=tk.W, pady=8)
        two_e = tk.Entry(new, textvariable=y, text=y, width=5)
        two_e.grid(row=5, column=1, sticky=tk.W)
        three_e = tk.Entry(new, textvariable=z, text=z, width=5)
        three_e.grid(row=6, column=1, sticky=tk.W, pady=8)
        four_e = tk.Entry(new, textvariable=a, text=a, width=5)
        four_e.grid(row=7, column=1, sticky=tk.W)
        five_e = tk.Entry(new, textvariable=b, text=b, width=5)
        five_e.grid(row=8, column=1, sticky=tk.W, pady=5)

        e_1 = tk.Entry(new, textvariable=e, width=5)
        e_1.grid(row=12, column=1, sticky=tk.W, pady=8)
        e_2 = tk.Entry(new, textvariable=f, width=5)
        e_2.grid(row=13, column=1, sticky=tk.W)
        e_3 = tk.Entry(new, textvariable=g, width=5)
        e_3.grid(row=14, column=1, sticky=tk.W, pady=5)
        e_4 = tk.Entry(new, textvariable=h, width=5)
        e_4.grid(row=15, column=1, sticky=tk.W)
        e_5 = tk.Entry(new, textvariable=i, width=5)
        e_5.grid(row=16, column=1, sticky=tk.W, pady=5)

        msg2 = tk.Label(new, text="Basic Mathematics -Subtraction", font=("Arial Narrow", 15 ), bg="#ffffff").grid(row=11, columnspan=2, ipady=5, sticky=tk.W)
        label = tk.Label(new, text="1.  92 - 78 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=12, column=0, sticky=tk.W, ipady=10, padx=40)
        label = tk.Label(new, text="2.  88 - 39 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=13, column=0, sticky=tk.W, ipady=10, padx=40)
        label = tk.Label(new, text="3.  184 - 157 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=14, column=0, sticky=tk.W, ipady=10, padx=40)
        label = tk.Label(new, text="4.  7567 + 3486", font=("comic sans ms", 11), bg="#ffffff").grid(row=15, column=0, sticky=tk.W, ipady=10, padx=40)
        label = tk.Label(new, text="5.  6163 - 5394 = ", font=("comic sans ms", 11), bg="#ffffff").grid(row=16, column=0, sticky=tk.W, ipady=10, padx=40)
        markl = tk.Label(new, text=mark)
        markl.grid(row=17, column=3)

        def check1():
            global mark
            start.config(state=tk.DISABLED)
            if one_e.get() == "103":
                mark += 1
                markl.config(text=mark)
                one_e.config(bg="green")
            elif one_e.get() == "":
                x.set("??")
            else:
                one_e.config(bg="red")
            check2()

        def check2():
            if two_e.get() == "120":
                two_e.config(bg="green")
                global mark
                mark += 1
                markl.config(text=mark)
            elif two_e.get() == "":
                y.set("??")
            else:
                two_e.config(bg="red")
            check3()

        def check3():
            if three_e.get() == "1100":
                three_e.config(bg="green")
                global mark
                mark += 1
                markl.config(text=mark)
            elif three_e.get() == "":
                z.set("??")
            else:
                three_e.config(bg="red")
            check4()

        def check4():
            if four_e.get() == "131":
                four_e.config(bg="green")
                global mark
                mark += 1
                markl.config(text=mark)
            elif four_e.get() == "":
                a.set("??")
            else:
                four_e.config(bg="red")
            check5()

        def check5():
            if five_e.get() == "328.13":
                five_e.config(bg="green")
                global mark
                mark += 1
                markl.config(text=mark)
            elif five_e.get() == "":
                b.set("??")
            else:
                five_e.config(bg="red")

        def start_over():
            global mark
            mark = 0
            markl.config(text=mark)
            start.config(state=tk.NORMAL)
            one_e.delete(0, tk.END)
            one_e.config(bg="white")
            two_e.delete(0, tk.END)
            two_e.config(bg="white")
            three_e.delete(0, tk.END)
            three_e.config(bg="white")
            four_e.delete(0, tk.END)
            four_e.config(bg="white")
            five_e.delete(0, tk.END)
            five_e.config(bg="white")

        start = tk.Button(new, text="Mark", command=check1, width=15)
        start.grid(row=17, column=0)
        redo = tk.Button(new, text="Start over", width=15, command=start_over)
        redo.grid(row=17, column=1)

        new.title("Math - Lesson 1")


class shapes():

    def __init__(self, master):
        root.withdraw()
        shapes_ = tk.Toplevel()
        shapes_width = 840
        shapes_height = 700
        shapes_.geometry('%dx%d+%d+%d' % (shapes_width, shapes_height, x, y))
        shapes_.resizable(width=tk.FALSE, height=tk.TRUE)
        shapes_.config(bg="#ffffff")

        def check_1():
            if a.get() == "apple" or a.get() == "Apple":
                tk.messagebox.showinfo("Correct!", "Great start! That's one point for you!")
                global mark
                mark += 1
                points.set("You have %d point(s)" % mark)
                ansb_1.config(state=tk.DISABLED)
            elif arduino.get() == "":
                tkinter.messagebox.showinfo("You can do it", "You have to atleast guess!")
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_2():
            if b.get() == "ball" or b.get() == "Ball":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("You have %d point(s)" % mark)
                ansb_2.config(state=tk.DISABLED)

            else:
                tk.messagebox.showerror("whoops", "try one more time")

        def check_3():
            if c.get() == "cat" or c.get() == "Cat":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("You have %d point(s)" % mark)
                ansb_3.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_4():
            if d.get() == "Dog" or d.get() == "dog":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("Wooh!!  %d point(s)!!!" % mark)
                ansb_4.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_5():
            if e.get() == "elephant" or e.get() == "Elephant":
                tk.messagebox.showinfo("Correct!", "Thats one point for you!")
                global mark
                mark += 1
                points.set("Your on fire at %d point(s)" % mark)
                ansb_5.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_6():
            if f.get() == "fish" or f.get() == "Fish":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("You are a Genius!! at %d point(s)" % mark)
                ansb_6.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_7():
            if g.get() == "Ice cream" or g.get() == "ice cream":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("Perfect!! %d point(s)" % mark)
                ansb_7.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def check_8():
            if h.get() == "pig" or h.get() == "Pig":
                tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
                global mark
                mark += 1
                points.set("You are a geek!! with %d point(s)" % mark)
                ansb_8.config(state=tk.DISABLED)
            else:
                tkinter.messagebox.showerror("whoops", "try one more time")

        def print_grade():
            tkinter.messagebox.showerror("Print Your grade",
                                         "Whoops! No printer connected\nPlease connect a printer to print your grade!")

        def help():
            tkinter.messagebox.showinfo("Help!", "")

        def destroyer():
            root.destroy()

        points.set("You have %d points" % mark)
        menu = tk.Menu(shapes_)
        shapes_.config(menu=menu)
        submenu = tk.Menu(menu)
        submenu_ = tk.Menu(menu)
        submenu__ = tk.Menu(menu)
        menu.add_cascade(label="Save grade   ", menu=submenu)
        menu.add_cascade(label="Print my grade   ", command=print_grade)
        menu.add_cascade(label="Help   ", command=help)
        menu.add_cascade(label="Change Subject   ", command=root.deiconify)
        menu.add_cascade(label="Change Lesson  ")
        menu.add_cascade(label="That's enough for today!", command=destroyer)

        question = tk.Label(shapes_,
                            text="Hey there " + student_name.get() + "!, I bet you can recognize this shapes. use them to determine which Alphabet letter this is. Have fun ;-)",
                            font=("Arial Narrow", 14), bg="#ffffff").grid(row=0, columnspan=5, padx=15)
        grade1 = tk.Label(shapes_, textvariable=points, font=("forte", 13), bg="#ffffff").grid(row=1, column=0)
        grade2 = tk.Label(shapes_, textvariable=mark).grid(row=1, column=1)
        a = tk.StringVar()
        b = tk.StringVar()
        c = tk.StringVar()
        d = tk.StringVar()
        p = tk.StringVar()
        arduino = tk.StringVar()
        apple = tk.StringVar()
        android = tk.StringVar()
        rasp = tk.StringVar()
        google = tk.StringVar()
        saf = tk.StringVar()
        windows = tk.StringVar()
        ps = tk.StringVar()

        pic_1 = tk.PhotoImage(file="afor.gif")
        lpic_1 = tk.Label(shapes_, image=pic_1, bg="#ffffff")
        lpic_1.image = pic_1
        lpic_1.grid(row=2, column=0, ipadx=20)
        anse_1 = tk.Entry(shapes_, textvariable=a, relief=tk.GROOVE, bd="2").grid(row=3, column=0, pady=10)
        ansb_1 = tk.Button(shapes_, text="Am i correct?", command=check_1, bg="#237a77")
        ansb_1.grid(row=4, column=0)

        pic_2 = tk.PhotoImage(file="bfor.gif")
        lpic_2 = tk.Label(shapes_, image=pic_2, bg="#ffffff")
        lpic_2.image = pic_2
        lpic_2.grid(row=2, column=1, ipadx=20)
        anse_2 = tk.Entry(shapes_, textvariable=b, relief=tk.GROOVE, bd="2").grid(row=3, column=1, pady=10)
        ansb_2 = tk.Button(shapes_, text="Am i correct?", command=check_2, bg="#33ef2f")
        ansb_2.grid(row=4, column=1)

        pic_3 = tk.PhotoImage(file="cfor.gif")
        lpic_3 = tk.Label(shapes_, image=pic_3, bg="#ffffff")
        lpic_3.image = pic_3
        lpic_3.grid(row=2, column=2, ipadx=20)
        anse_3 = tk.Entry(shapes_, textvariable=c, relief=tk.GROOVE, bd="2").grid(row=3, column=2, pady=10)
        ansb_3 = tk.Button(shapes_, text="Am i correct?", command=check_3, bg="#ffb21c")
        ansb_3.grid(row=4, column=2)

        pic_4 = tk.PhotoImage(file="dfor.gif")
        lpic_4 = tk.Label(shapes_, image=pic_4, bg="#ffffff")
        lpic_4.image = pic_4
        lpic_4.grid(row=2, column=3, ipadx=20)
        anse_4 = tk.Entry(shapes_, textvariable=d, relief=tk.GROOVE, bd="2").grid(row=3, column=3, pady=10)
        ansb_4 = tk.Button(shapes_, text="Am i correct?", command=check_4, bg="#ff4f4f")
        ansb_4.grid(row=4, column=3)

        pic_5 = tk.PhotoImage(file="efor.gif")
        lpic_5 = tk.Label(shapes_, image=pic_5, bg="#ffffff")
        lpic_5.image = pic_5
        lpic_5.grid(row=5, column=0, ipady=35)
        anse_5 = tk.Entry(shapes_, textvariable=e, relief=tk.GROOVE, bd="2").grid(row=6, column=0, pady=10)
        ansb_5 = tk.Button(shapes_, text="Am i correct?", command=check_5, bg="#ff99fb")
        ansb_5.grid(row=7, column=0)

        pic_6 = tk.PhotoImage(file="ffor.gif")
        lpic_6 = tk.Label(shapes_, image=pic_6, bg="#ffffff")
        lpic_6.image = pic_6
        lpic_6.grid(row=5, column=1, ipady=35)
        anse_6 = tk.Entry(shapes_, textvariable=f, relief=tk.GROOVE, bd="2").grid(row=6, column=1, pady=10)
        ansb_6 = tk.Button(shapes_, text="Am i correct?", command=check_6, bg="#11dfd8")
        ansb_6.grid(row=7, column=1)

        pic_7 = tk.PhotoImage(file="ifor.gif")
        lpic_7 = tk.Label(shapes_, image=pic_7, bg="#ffffff")
        lpic_7.image = pic_7
        lpic_7.grid(row=5, column=2, ipady=35)
        anse_7 = tk.Entry(shapes_, textvariable=g, relief=tk.GROOVE, bd="2").grid(row=6, column=2, pady=10)
        ansb_7 = tk.Button(shapes_, text="Am i correct?", command=check_7, bg="#ff99fb")
        ansb_7.grid(row=7, column=2)

        pic_8 = tk.PhotoImage(file="pfor.gif")
        lpic_8 = tk.Label(shapes_, image=pic_8, bg="#ffffff")
        lpic_8.image = pic_8
        lpic_8.grid(row=5, column=3, ipady=35)
        anse_8 = tk.Entry(shapes_, textvariable=h, relief=tk.GROOVE, bd="2").grid(row=6, column=3, pady=10)
        ansb_8 = tk.Button(shapes_, text="Am i correct?", command=check_8, bg="#ff99fb")
        ansb_8.grid(row=7, column=3)
        shapes_.title("Make learning fun using the Raspberry pi")


# for tech lesson
def technology():
    root.withdraw()
    techno = tk.Toplevel()
    tech_width = 840
    tech_height = 700
    techno.geometry('%dx%d+%d+%d' % (tech_width, tech_height, x, y))
    techno.resizable(width=tk.FALSE, height=tk.TRUE)
    logging.info("student named  %s logged in, with teacher %s's permission at %s", student_name.get(), teacher_name.get(), date)
    def check_1():
        if arduino.get() == "arduino" or windows.get() == "Arduino":
            tk.messagebox.showinfo("Correct!", "Great start! That's one point for you!")
            global mark
            mark += 1
            points.set("You have %d point(s)" % mark)
            ansb_1.config(state=tk.DISABLED)
        elif arduino.get() == "":
            tkinter.messagebox.showinfo("You can do it", "You have to atleast guess!")
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_2():
        if apple.get() == "apple" or windows.get() == "Apple":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("You have %d point(s)" % mark)
            ansb_2.config(state=tk.DISABLED)

        else:
            tk.messagebox.showerror("whoops", "try one more time")

    def check_3():
        if android.get() == "android" or windows.get() == "Android":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("You have %d point(s)" % mark)
            ansb_3.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_4():
        if rasp.get() == "raspberry pi" or windows.get() == "Raspberry pi":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("Wooh!!  %d point(s)!!!" % mark)
            ansb_4.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_5():
        if google.get() == "google" or windows.get() == "Google":
            tk.messagebox.showinfo("Correct!", "Thats one point for you!")
            global mark
            mark += 1
            points.set("Your on fire at %d point(s)" % mark)
            ansb_5.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_6():
        if windows.get() == "microsoft" or windows.get() == "Microsoft":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("You are a Genius!! at %d point(s)" % mark)
            ansb_6.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_7():
        if saf.get() == "safaricom" or windows.get() == "Safaricom":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("Perfect!! %d point(s)" % mark)
            ansb_7.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def check_8():
        if ps.get() == "intuitive tech" or windows.get() == "Intuitive tech":
            tkinter.messagebox.showinfo("Correct!", "That's one point for you!")
            global mark
            mark += 1
            points.set("You are a geek!! with %d point(s)" % mark)
            ansb_8.config(state=tk.DISABLED)
        else:
            tkinter.messagebox.showerror("whoops", "try one more time")

    def print_grade():
        tkinter.messagebox.showerror("Print Your grade",
                                     "Whoops! No printer connected\nPlease connect a printer to print your grade!")

    def help():
        tkinter.messagebox.showinfo("Help!",
                                    "Those logos seem familiar, yes? just match them with the tech compay they belong to and your done with this lesson!!")

    def destroyer():
        root.destroy()

    points.set("You have %d points" % mark)
    menu = tk.Menu(techno)
    techno.config(menu=menu)
    submenu = tk.Menu(menu)
    submenu_ = tk.Menu(menu)
    submenu__ = tk.Menu(menu)
    menu.add_cascade(label="Save grade   ", menu=submenu)
    menu.add_cascade(label="Print my grade   ", command=print_grade)
    menu.add_cascade(label="Help   ", command=help)
    menu.add_cascade(label="Change Subject   ", command=root.deiconify)
    menu.add_cascade(label="Change Lesson  ")
    menu.add_cascade(label="That's enough for today!", command=destroyer)

    question = tk.Label(techno,
                        text="Hello " + student_name.get() + ", here is today's challenge...can you guess which Tech companies this logos belong to? \n Pretty easy huh! Just fill your answer in the entries below the logo\n",
                        font=("Arial Narrow", 14)).grid(row=0, columnspan=5)
    grade1 = tk.Label(techno, textvariable=points, font=("forte", 13)).grid(row=1, column=0)
    grade2 = tk.Label(techno, textvariable=mark).grid(row=1, column=1)

    arduino = tk.StringVar()
    apple = tk.StringVar()
    android = tk.StringVar()
    rasp = tk.StringVar()
    google = tk.StringVar()
    saf = tk.StringVar()
    windows = tk.StringVar()
    ps = tk.StringVar()

    pic_1 = tk.PhotoImage(file="arduino.gif")
    lpic_1 = tk.Label(techno, image=pic_1)
    lpic_1.image = pic_1
    lpic_1.grid(row=2, column=0, ipadx=20)
    anse_1 = tk.Entry(techno, textvariable=arduino, relief=tk.GROOVE, bd="2").grid(row=3, column=0, pady=10)
    ansb_1 = tk.Button(techno, text="Am i correct?", command=check_1)
    ansb_1.grid(row=4, column=0)

    pic_2 = tk.PhotoImage(file="apple.gif")
    lpic_2 = tk.Label(techno, image=pic_2)
    lpic_2.image = pic_2
    lpic_2.grid(row=2, column=1, ipadx=20)
    anse_2 = tk.Entry(techno, textvariable=apple, relief=tk.GROOVE, bd="2").grid(row=3, column=1, pady=10)
    ansb_2 = tk.Button(techno, text="Am i correct?", command=check_2)
    ansb_2.grid(row=4, column=1)

    pic_3 = tk.PhotoImage(file="android.gif")
    lpic_3 = tk.Label(techno, image=pic_3)
    lpic_3.image = pic_3
    lpic_3.grid(row=2, column=2, ipadx=20)
    anse_3 = tk.Entry(techno, textvariable=android, relief=tk.GROOVE, bd="2").grid(row=3, column=2, pady=10)
    ansb_3 = tk.Button(techno, text="Am i correct?", command=check_3)
    ansb_3.grid(row=4, column=2)

    pic_4 = tk.PhotoImage(file="rasp.gif")
    lpic_4 = tk.Label(techno, image=pic_4)
    lpic_4.image = pic_4
    lpic_4.grid(row=2, column=3, ipadx=20)
    anse_4 = tk.Entry(techno, textvariable=rasp, relief=tk.GROOVE, bd="2").grid(row=3, column=3, pady=10)
    ansb_4 = tk.Button(techno, text="Am i correct?", command=check_4)
    ansb_4.grid(row=4, column=3)

    pic_5 = tk.PhotoImage(file="google.gif")
    lpic_5 = tk.Label(techno, image=pic_5)
    lpic_5.image = pic_5
    lpic_5.grid(row=5, column=0, ipady=35)
    anse_5 = tk.Entry(techno, textvariable=google, relief=tk.GROOVE, bd="2").grid(row=6, column=0, pady=10)
    ansb_5 = tk.Button(techno, text="Am i correct?", command=check_5)
    ansb_5.grid(row=7, column=0)

    pic_6 = tk.PhotoImage(file="windows.gif")
    lpic_6 = tk.Label(techno, image=pic_6)
    lpic_6.image = pic_6
    lpic_6.grid(row=5, column=1, ipady=35)
    anse_6 = tk.Entry(techno, textvariable=windows, relief=tk.GROOVE, bd="2").grid(row=6, column=1, pady=10)
    ansb_6 = tk.Button(techno, text="Am i correct?", command=check_6)
    ansb_6.grid(row=7, column=1)

    pic_7 = tk.PhotoImage(file="saf.gif")
    lpic_7 = tk.Label(techno, image=pic_7)
    lpic_7.image = pic_7
    lpic_7.grid(row=5, column=2, ipady=35)
    anse_7 = tk.Entry(techno, textvariable=saf, relief=tk.GROOVE, bd="2").grid(row=6, column=2, pady=10)
    ansb_7 = tk.Button(techno, text="Am i correct?", command=check_7)
    ansb_7.grid(row=7, column=2)

    pic_8 = tk.PhotoImage(file="intuitive.gif")
    lpic_8 = tk.Label(techno, image=pic_8)
    lpic_8.image = pic_8
    lpic_8.grid(row=5, column=3, ipady=35)
    anse_8 = tk.Entry(techno, textvariable=ps, relief=tk.GROOVE, bd="2").grid(row=6, column=3, pady=10)
    ansb_8 = tk.Button(techno, text="Am i correct?", command=check_8)
    ansb_8.grid(row=7, column=3)
    techno.title("Make learning fun using the Raspberry pi")


# ensure fields not empty
def check_fields():
    if teacher_name == "" or student_name == "":
        tkinter.messagebox.showwarning("", "Please make sure you give me your name and teachers name :-)")


# for shapes and hopefully sounds
def shape():
    if teacher_name.get() == "" or student_name.get() == "":
        print(student_name.get())
        tkinter.messagebox.showwarning("", "Please make sure you give me your name and teachers name :-)")
    else:
        shapes(root)

def art():
    if teacher_name.get() == "" or student_name.get() == "":
        print(student_name.get())
        tkinter.messagebox.showwarning("", "Please make sure you give me your name and teachers name :-)")
    else:
        arts(root)


welcome = tk.PhotoImage(file="rasp.png")
welcome_label = tk.Label(root, image=welcome)
welcome_label.grid(rowspan=20, column=0)

confirm_one = tk.Label(root, text="But First, your name", font=("Arial Narrow", 12), bg="#f4f4f4")
confirm_one.grid(row=0, column=2, sticky=tk.SE)

confirm_two = tk.Label(root, text="& your Tr.s name :-)", font=("Arial Narrow", 12), bg="#f4f4f4")
confirm_two.grid(row=0, column=3, sticky=tk.SW)

l_name = tk.Label(root, text="Student/Group Name", font="bold", bg="#f4f4f4", fg="#00bf99")
l_name.config(bg="#f4f4f4")
l_name.grid(row=2, column=2, sticky=tk.S)
name = tk.Entry(root, textvariable=student_name, relief=tk.RIDGE, justify=tk.CENTER)
name.grid(row=3, column=2, padx=30, ipady=2, ipadx=5)

l_tr = tk.Label(root, text="Teacher's Name", font="bold", bg="#f4f4f4", fg="#00bf99")
l_tr.config(bg="#f4f4f4")
l_tr.grid(row=2, column=3, sticky=tk.S)
tr_name = tk.Entry(root, textvariable=teacher_name, relief=tk.RIDGE, justify=tk.CENTER)
tr_name.grid(row=3, column=3, padx=30, ipady=2, ipadx=5)

# get student date and time login
date = datetime.now()

good = tk.Label(root, text="Good! now just click", font=("Arial Narrow", 13, "bold"), bg="#f4f4f4", fg="#00bf99")
good.grid(row=5, column=2, sticky=tk.E)

good_two = tk.Label(root, text="on any subject to begin!", font=("Arial Narrow", 13, "bold"), bg="#f4f4f4",
                    fg="#00bf99")
good_two.grid(row=5, column=3, sticky=tk.W)

# The butt-ons ;-)
ss = tk.Button(root, text="Shapes & Sounds\n1/15", width=17, height=2, borderwidth=0, relief=tk.FLAT, command=shape)
tech = tk.Button(root, text="Technology\n1/15", command=technology, width=17, height=2, borderwidth=0, relief=tk.FLAT)
art = tk.Button(root, text="Mathematics", width=17, height=2, borderwidth=0, relief=tk.FLAT, command=art)
math = tk.Button(root, text="Art & Craft", width=17, height=2, borderwidth=0, state=tk.DISABLED,
                 relief=tk.FLAT)
eng = tk.Button(root, text="English", width=17, height=2, borderwidth=0, state=tk.DISABLED,
                relief=tk.FLAT)
swa = tk.Button(root, text="Swahili)", width=17, height=2, borderwidth=0, state=tk.DISABLED,
                relief=tk.FLAT)

ss.grid(row=9, column=2)
tech.grid(row=9, column=3)
art.grid(row=11, column=2)
math.grid(row=11, column=3)
eng.grid(row=13, column=2)
swa.grid(row=13, column=3)

copy = tk.Label(root, text="© Intuitive Tech 2016")
copy.grid(row=19, column=2, sticky=tk.W)

if __name__ == "__main__":
    root.mainloop()
