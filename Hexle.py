import tkinter as tk
import random
import math

root=tk.Tk()
root.geometry("700x400")
root.title("Hexle")
g_var=tk.StringVar()
n_var= tk.IntVar()
closeRange = tk.IntVar()
correctRange = tk.IntVar()

guesses = []
indicators = []

def changedRange(value):
    init()

def init():
    global secretHex
    global main
    for g in guesses: 
        g.destroy()
    for i in indicators: 
        i.destroy()
    guesses.clear()
    indicators.clear()
    g_var.set("")
    n_var.set(value=0)
    guess_entry.grid(row=0,column=3)
    secretHex = hex(random.randint(0,15)).split('x')[-1]+hex(random.randint(0,15)).split('x')[-1]+hex(random.randint(0,15)).split('x')[-1]+hex(random.randint(0,15)).split('x')[-1]+hex(random.randint(0,15)).split('x')[-1]+hex(random.randint(0,15)).split('x')[-1]
    f_color = fontPolarity("#"+secretHex)
    main = tk.Label(root, text="What Color \nis this?",bg="#"+secretHex,fg=f_color,height=12,width=12)
    main.grid(row=0,column=2,rowspan=6)
    strt_btn.config(text = 'Reset')
    sub_btn.config(text = "Submit")
    sub_btn.grid(row=7,column=3)
    strt_btn.grid(row=8,column=3)

def fontPolarity(h):
    h_len = len(h)
    h_r = h[h_len-6:h_len-4]
    h_g = h[h_len-4:h_len-2]
    h_b = h[h_len-2:h_len]
    if(int(h_r,16) + int(h_g,16) + int(h_b,16) < 384):
        font_color = "#FFFFFF"
    else:
        font_color = "#000000"
    return font_color

def submit():
    if isHex(g_var.get()):
        g_r = g_var.get()[0:2]
        g_g = g_var.get()[2:4]
        g_b = g_var.get()[4:6]
        a_r = secretHex[0:2]
        a_g = secretHex[2:4]
        a_b = secretHex[4:6]

        font_color = fontPolarity(g_var.get())
        
        lbl = tk.Label(root, text=g_var.get(), font=("calibre", 10, "bold"), bg="#" + g_var.get(), fg=font_color, width=20, height=2 ) 

        if(abs(int(g_r,16) - int(a_r,16)) <= correctRange.get()):
            r_ind = tk.Label(root, text="o", font=("calibre", 10, "bold"), bg="#00ffff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_r,16) - int(a_r,16)) <= correctRange.get()+1):
            r_ind = tk.Label(root, text="!", font=("calibre", 10, "bold"), bg="#ff00ff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_r,16) - int(a_r,16)) <= closeRange.get()):
            r_ind = tk.Label(root, text="-", font=("calibre", 10, "bold"), bg="#ffff00", fg="#000000", width=2, height=2) 
        else:
            r_ind = tk.Label(root, text="x", font=("calibre", 10, "bold"), bg="#ffffff", fg="#000000", width=2, height=2) 

        if(abs(int(g_g,16) - int(a_g,16)) <= correctRange.get()):
            g_ind = tk.Label(root, text="o", font=("calibre", 10, "bold"), bg="#00ffff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_g,16) - int(a_g,16)) <= correctRange.get()+1):
            g_ind = tk.Label(root, text="!", font=("calibre", 10, "bold"), bg="#ff00ff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_g,16) - int(a_g,16)) <= closeRange.get()):
            g_ind = tk.Label(root, text="-", font=("calibre", 10, "bold"), bg="#ffff00", fg="#000000", width=2, height=2) 
        else:
            g_ind = tk.Label(root, text="x", font=("calibre", 10, "bold"), bg="#ffffff", fg="#000000", width=2, height=2) 
        

        if(abs(int(g_b,16) - int(a_b,16)) <= correctRange.get()):
            b_ind = tk.Label(root, text="o", font=("calibre", 10, "bold"), bg="#00ffff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_b,16) - int(a_b,16)) <= correctRange.get()+1):
            b_ind = tk.Label(root, text="!", font=("calibre", 10, "bold"), bg="#ff00ff", fg="#000000", width=2, height=2) 
        elif(abs(int(g_b,16) - int(a_b,16)) <= closeRange.get()):
            b_ind = tk.Label(root, text="-", font=("calibre", 10, "bold"), bg="#ffff00", fg="#000000", width=2, height=2) 
        else:
            b_ind = tk.Label(root, text="x", font=("calibre", 10, "bold"), bg="#ffffff", fg="#000000", width=2, height=2) 
        
        lbl.grid(row=n_var.get(), column=3)
        if n_var.get() >= 0:
            r_ind.grid(row=n_var.get(), column=6)
            g_ind.grid(row=n_var.get(), column=7)
            b_ind.grid(row=n_var.get(), column=8)
        guesses.append(lbl)
        indicators.append(r_ind)
        indicators.append(g_ind)
        indicators.append(b_ind)
        n_var.set(n_var.get() + 1)
        g_var.set("")

        if (abs(int(g_r,16) - int(a_r,16)) <= correctRange.get()) and (abs(int(g_g,16) - int(a_g,16)) <= correctRange.get()) and (abs(int(g_b,16) - int(a_b,16)) <= correctRange.get()):
            endgame(True)
        elif n_var.get() < 6: 
            guess_entry.grid(row=n_var.get(), column=3) 
        else: 
            endgame(False)


def endgame(win):
        
        guess_entry.grid_remove()
        main.config(text = secretHex)
        
        if(win):
            sub_btn.config(text = "You Win!")
        else:
            sub_btn.config(text = "You Lose!")

        if(len(guesses) < 6):
            for i in range(len(guesses),6):
                guesses.append(guesses[len(guesses)-1])

        Guess1_Score = tk.Label(root, text = str(score(guesses[0].cget("text"),secretHex)) + ' Points + ', height=2)
        Guess2_Score = tk.Label(root, text = str(score(guesses[1].cget("text"),secretHex)) + ' Points + ', height=2)
        Guess3_Score = tk.Label(root, text = str(score(guesses[2].cget("text"),secretHex)) + ' Points + ', height=2)
        Guess4_Score = tk.Label(root, text = str(score(guesses[3].cget("text"),secretHex)) + ' Points + ', height=2)
        Guess5_Score = tk.Label(root, text = str(score(guesses[4].cget("text"),secretHex)) + ' Points + ', height=2)
        Guess6_Score = tk.Label(root, text = str(score(guesses[5].cget("text"),secretHex)) + ' Points ', height=2)

        indicators.append(Guess1_Score)
        indicators.append(Guess2_Score)
        indicators.append(Guess3_Score)
        indicators.append(Guess4_Score)
        indicators.append(Guess5_Score)
        indicators.append(Guess6_Score)

        Total_Score = tk.Label(root, text = "Total Score: "+str(score(guesses[0].cget("text"),secretHex)+score(guesses[1].cget("text"),secretHex)+score(guesses[2].cget("text"),secretHex)+score(guesses[3].cget("text"),secretHex)+score(guesses[4].cget("text"),secretHex)+score(guesses[5].cget("text"),secretHex)), height=2)

        Guess1_Score.grid(row=0,column=9)
        Guess2_Score.grid(row=1,column=9)
        Guess3_Score.grid(row=2,column=9)
        Guess4_Score.grid(row=3,column=9)
        Guess5_Score.grid(row=4,column=9)
        Guess6_Score.grid(row=5,column=9)
        Total_Score.grid(row=6,column=9)


def score(str1,str2):
    if isHex(str1):
        s1_r = int(str1[0:2],16)
        s1_g = int(str1[2:4],16)
        s1_b = int(str1[4:6],16)
    else:
        return
    if isHex(str2):
        s2_r = int(str2[0:2],16)
        s2_g = int(str2[2:4],16)
        s2_b = int(str2[4:6],16)
    else:
        return

    rdif = abs(s1_r - s2_r)
    gdif = abs(s1_g - s2_g)
    bdif = abs(s1_b - s2_b)

    bigcalc1 = abs(abs(rdif + gdif) + abs(rdif - gdif) + (2 * bdif))
    bigcalc2 = abs(abs(rdif + gdif) + abs(rdif - gdif) - (2 * bdif))

    combined = 0.25 * (bigcalc1 + bigcalc2)

    score_gradient = 64
    
    return round(max(0,100 * (1 - (combined / score_gradient))),2)

def isHex(s):
    if len(s) == 6:
        for ch in s:
            if ((ch < '0' or ch > '9') and (ch < 'A' or ch > 'F') and (ch < 'a' or ch > 'f')):
                return False 
        return True
    return False

Guess1_Label = tk.Label(root, text = 'Guess 1', font=('calibre',10, 'bold'), height=2)
Guess2_Label = tk.Label(root, text = 'Guess 2', font=('calibre',10, 'bold'), height=2)
Guess3_Label = tk.Label(root, text = 'Guess 3', font=('calibre',10, 'bold'), height=2)
Guess4_Label = tk.Label(root, text = 'Guess 4', font=('calibre',10, 'bold'), height=2)
Guess5_Label = tk.Label(root, text = 'Guess 5', font=('calibre',10, 'bold'), height=2)
Guess6_Label = tk.Label(root, text = 'Guess 6', font=('calibre',10, 'bold'), height=2)

S1_Label = tk.Label(root, text = 'close', font=('calibre',6, 'bold'))
S2_Label = tk.Label(root, text = 'correct', font=('calibre',6, 'bold'))

s1 = tk.Scale(root, variable = closeRange,from_ = 8, to = 64,orient = tk.VERTICAL,command=changedRange) 
s2 = tk.Scale(root, variable = correctRange,from_ = 0, to = 8,orient = tk.VERTICAL,command=changedRange) 

s1.grid(row=0,column=0,rowspan=6)
s2.grid(row=0,column=1,rowspan=6)
S1_Label.grid(row=7,column=0)
S2_Label.grid(row=7,column=1)

Guess1_Label.grid(row=0,column=4)
Guess2_Label.grid(row=1,column=4)
Guess3_Label.grid(row=2,column=4)
Guess4_Label.grid(row=3,column=4)
Guess5_Label.grid(row=4,column=4)
Guess6_Label.grid(row=5,column=4)

guess_entry = tk.Entry(root,textvariable = g_var, font=('calibre',10,'normal'))

strt_btn=tk.Button(root,text = 'Start', command = init)
strt_btn.grid(row=8,column=3)

sub_btn=tk.Button(root,text = 'Submit', command = submit)

root.bind("<Return>", lambda x: submit())
root.bind("<r>", lambda x: init())

root.mainloop()
