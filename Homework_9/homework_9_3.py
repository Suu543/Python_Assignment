from tkinter import *

app = Tk()
result = 0


def setTextInput(input_elem, result):
    input_elem.delete(0, "end")
    input_elem.insert(0, result)


def convertKmToMile():
    global result
    result = float(inputKM.get()) * 0.609344
    setTextInput(inputMile, result)


def convertMileToKm():
    global result
    result = float(inputMile.get()) * 1.609344
    setTextInput(inputKM, result)


inputDirKM = StringVar(None)
inputKM = Entry(app, textvariable=inputDirKM, width=30)
inputKM.grid(row=1, column=1)

labelTextKM = StringVar()
labelTextKM.set('Km')
labelDirKM = Label(app, textvariable=labelTextKM)
labelDirKM.grid(row=1, column=2)


inputDirMile = StringVar(None)
inputMile = Entry(app, textvariable=inputDirMile, width=30)
inputMile.grid(row=1, column=3)

labelTextMile = StringVar()
labelTextMile.set("Mile")
labelDirMile = Label(app, textvariable=labelTextMile)
labelDirMile.grid(row=1, column=4)

km = Button(app, text="Km -> Mile", command=convertKmToMile)
mile = Button(app, text="Km <- Mile", command=convertMileToKm)

km.grid(row=2, column=1)
mile.grid(row=2, column=3)

app.mainloop()
