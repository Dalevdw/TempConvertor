from tkinter import*

temp = Tk()
temp.title("Temperature Converter")
TempCon = Frame(temp)
TempCon.grid()

celTempVar = IntVar()
celTempVar.set(int(0))
fahTempVar = IntVar()
fahTempVar.set(int(0))

celLabel = Label (temp, text = "Celcius: ", fg = "black")
celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

celEntry = Entry (temp, width = 10, state='disabled', textvariable = celTempVar)
celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )

fahLabel = Label (temp, text = "Fahrenheit: ",fg = "black")
fahLabel.grid(row = 2, column = 2, pady = 10, sticky = NW)

fahEntry = Entry (temp, width = 10, textvariable = fahTempVar, state='disabled')
fahEntry.grid(row = 2, column = 2, pady = 10, sticky = NW, padx = 125 )


def activate_cel():
    if (cel_Button['state'] == NORMAL):
        cel_Button.config(state=DISABLED)
    else:
        cel_Button.config(state=NORMAL)

cel_Button = Button(temp,text="Activate-Celsius to Fahrenheit", command=activate_cel)
cel_Button.grid(row=3,column=1)


def activate_fahr():
    if (fahr_Button['state'] ==NORMAL):
        fahr_Button.config(state=DISABLED)
    else:
        fahr_Button.config(state=NORMAL)

fahr_Button = Button(temp,text="Activate-Fahrenheit to Celsius", command=activate_fahr)
fahr_Button.grid(row=3, column=2)


def calculate():
    celc_Temp = celTempVar.get()
    fahr_Temp = fahTempVar.get()

    if celTempVar.get() !=0.0:
        celc_To_fahr = float((float(celc_Temp) * 9 / 5) + 32)
        print(celc_To_fahr)
        fahTempVar.set(celc_To_fahr)

    elif fahTempVar.get() !=0.0:
        fahr_To_celc = float((float(fahr_Temp) - 32) * 5 / 9)
        print(fahr_To_celc)
        celTempVar.set(fahr_To_celc)

calcButton=Button (TempCon, text = "Calculate Conversion", justify = CENTER, command = calculate)
calcButton.grid(row = 6, column = 1)


def clear():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    clear_message = Label(top, text = "Cleared")
    clear_button = Button(top, text="OK", command=top.destroy)

    clear_message.grid(row = 0, padx = 5, pady = 5)
    clear_button.grid(row = 1,column=5)

    fahTempVar.set(int(0))
    celTempVar.set(int(0))


clearButton = Button (temp, text = "Clear", justify = CENTER,command = clear)
clearButton.grid(row=6,column=2)


temp.mainloop()
