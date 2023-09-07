import tkinter
from functools import partial
from tkinter import *

window= Tk()
window.title("BMI Calculator")

def bmi(label_result, ht, wt):
    ht=float((ht.get()))
    wt=float((wt.get()))
    ht=ht/100
    bmi=float(wt/(ht*ht))
    bmi=round(bmi,1)

    conclusion= ""

    if bmi<18.5:
        conclusion="Under Weight"
    elif bmi>=18.5 and bmi<24.9:
        conclusion="Normal"
    elif bmi>=25 and bmi<29.9:
        conclusion="Over Weight"
    elif bmi>=30 and bmi<34.9:
        conclusion="Obesity (Class 1)"
    elif bmi>=35 and bmi<39.9:
        conclusion="Obesity (Class 2)"
    elif bmi>=40:
        conclusion="Extreme Obesity"
    else:
        conclusion="Enter a valid number"

    output= "BMI = "+str(bmi)+"\n" +conclusion
    label_result.config(text=output)
    return

ht= tkinter.StringVar()
wt= tkinter.StringVar()

heightText= Label(window,text="Enter Your Height (cm)").grid(row=0, padx=10, pady=10)
height=Entry(window, textvariable = ht ).grid(row=0, column=1, padx=10,pady=10)

weightText=Label(window,text="Enter Your Weight (kg)").grid(row=1, padx=10,pady=5)
weight=Entry(window, textvariable = wt ).grid(row=1, column=1, padx=10,pady=5)

labelResult = tkinter.Label(window)
labelResult.grid(row=4, column=0)

bmi = partial(bmi, labelResult, ht, wt)
btn=Button(window,text="Calculate BMI",command = bmi).grid(row=2, column=1, padx=20,pady=5)

window.geometry("400x300+10+10")

window.mainloop()