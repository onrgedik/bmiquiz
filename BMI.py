import tkinter
from tkinter import *

window = Tk()

window.minsize(250, 250)
window.grid()
var_entry = StringVar()

#Kg Label
kg_label = Label(window, text="Kilonuzu Giriniz")
kg_label.pack(side=TOP)

#KG entry
kg_entry = (Entry(window))
kg_entry.config(font=("Arial", 10, "bold"))
kg_entry.insert(0, "105")
kg_entry.get()
kg_entry.pack(side=TOP)



#Boy Label
boy_label = Label(window, text="Boyunuzu Giriniz")
boy_label.pack(side=TOP)

#Boy Entry
boy_entry = (Entry(window))
boy_entry.config(font=("Arial", 10, "bold"))
boy_entry.insert(0, "1.8")
boy_entry.get()
boy_entry.pack()


#Sonuç label
cikti_label = Label(window, text="Boy Kilo İndeksiniz")
cikti_label.pack(side=TOP)


def index_hesap():
    if kg_entry.get() == str(kg_entry.get()) and boy_entry.get() == str(boy_entry.get()):
        cikti_label.config(text="Sayı Giriniz")

    vke = int(kg_entry.get()) / float(boy_entry.get()) ** 2

    if   18.5 <= vke >= 24.9:
        cikti_label.config(text="Normal Kilodasınız")
    if vke <= 18.5:
        cikti_label.config(text="Çok Zayıfsın")
    if 25 <= vke >= 29.9:
        cikti_label.config(text="Fazla Kilodasınız")
    if 30 <= vke >= 34.9:
        cikti_label.config(text="1.Derece Obezite")
    if 35 <= vke >= 39.9:
        cikti_label.config(text="2.Derece Obezite")
    if vke >= 40:
        cikti_label.config(text="3.Derece Obezite(Maşallah)")



        


#Hesaplama Butonu

hesap_buton = Button(window, text="Hesapla", command=index_hesap)
hesap_buton.pack(side=TOP)




window.mainloop()