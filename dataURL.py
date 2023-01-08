import os
class DataURL:
    dataFile = "dataURL.txt"

    def __init__(self):
        fileTest = open(self.dataFile, 'a')
        fileTest.close()

    def dataWrite(self):
        dataOpen = open(self.dataFile, 'a')
        siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
        kontrolHttps = siteURL[:7]
        kontrolHtpp = siteURL[:8]
        http = "http://"
        https = "https://"
        if kontrolHttps == http or kontrolHtpp == https:
            dataOpen.write(siteURL + "\n")
            dataOpen.close()
            print("Girmiş olduğunuz URL başarıyla kaydedildi.")
        else:
            print("URL girişini hatalı yaptınız.")
            time.sleep(1)
            print("Lütfen site adresini ön ekiyle birlikte tekrar giriniz.")
            time.sleep(2)

    def dataRead(self):
        dataOpen = open(self.dataFile, 'r')
        if os.stat(self.dataFile).st_size != 0:
            for dataShow in dataOpen:
                print(dataShow)
        else:
            print("Henüz kaydedilmiş adres yok!")
        dataOpen.close()
