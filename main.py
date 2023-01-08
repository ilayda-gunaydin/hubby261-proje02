from tkinter import *
from tkinter import ttk
import time
from dataURL import DataURL
from getURL import GetURL

pencere = Tk()
pencere.title("Mini Örümcek")
pencere.iconbitmap("ico/kitap.ico")
pencere.geometry("500x250")

etiket = Label(pencere, text="Mini örümceğe hoşgeldiniz. Çalıştırmak istediğiniz butona tıklayınız.")
etiket2 = Label(pencere, text="-------Menü--------")
etiket.pack()
etiket2.pack()

def urlListele():
    pencere1 = Tk()
    pencere1.title("URL Listele")
    pencere1.geometry("750x650")
    with open ("dataUrl.txt") as f:
        sayfa = f.read()
    buton1 = Button(pencere1, text= "Geri", command= pencere1.destroy)
    buton1.pack()
    etiket= Label(pencere1, text=sayfa)
    etiket.pack()

def urlEkle():
    pencere2 = Tk()
    pencere2.title("URL Ekle")
    pencere2.geometry("500x250")
    etiket= Label(pencere2)
    etiket.pack()
    etiket2= Label(pencere2, text="URL'yi giriniz...")
    etiket2.pack()
    girilenUrl = Entry(pencere2, width=25, borderwidth=1)
    girilenUrl.pack()
    buton = Button(pencere2, text="Kaydet", command=pencere2.destroy)
    buton.pack()
    etiket2= Label(pencere, text="URL kaydınız başarıyla gerçekleşmiştir")
    etiket2.pack()

def orumcekGonder():
    pencere3 = Tk()
    pencere3.title("Örümcek Gönder")
    pencere3.geometry("750x650")
    with open ("getURL.py") as f:
        sayfa = f.read()
    buton3 = Button(pencere3, text= "Geri", command=pencere3.destroy)
    buton3.pack()
    etiket = Label(pencere3, text=sayfa)
    etiket.pack()

def sonuclariListele():
    pencere4 = Tk()
    pencere4.title("Sonuçları Listele")
    pencere4.geometry("750x650")
    with open ("getURL.txt") as f:
        sayfa = f.read()
    buton4 = Button(pencere4, text= "Geri", command=pencere4.destroy)
    buton4.pack()
    etiket= Label(pencere4, text=sayfa)
    etiket.pack()

def quit():
    pencere5 = Tk()
    pencere5.title("Çıkış")
    pencere5.geometry("750x650")

menuOgeleri = ["URL Listele", "URL Ekle", "Örümcek Gönder", "Sonuçları Listele", "Çıkış"]
menuFonksiyonlari = [urlListele, urlEkle, orumcekGonder, sonuclariListele, quit]

for idx, oge in enumerate(menuOgeleri):
    ttk.Button(pencere, text= " " +oge, command=menuFonksiyonlari[idx]).pack()

pencere.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

while True:
    menuSecim = int(input("Seçiminiz: "))
    if menuSecim == 0:
        time.sleep(1)
        break
    elif menuSecim == 1:
        useDataURL.dataRead()
    elif menuSecim == 2:
        useDataURL.dataWrite()
    elif menuSecim == 3:
        useGetURL.getWeb()
    elif menuSecim == 4:
        useGetURL.getList()
    elif menuSecim >= 4:
        print("Seçiminiz 0 ile 4 arasında değil. Tekrar seçim yapın.")
