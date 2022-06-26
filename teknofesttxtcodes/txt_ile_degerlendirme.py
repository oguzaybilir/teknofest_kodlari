import glob

klasor_yolu = "C:/Users/oguza/Desktop/etiketler/oturum_2_img/oturum6"

txt_yollar = glob.glob(klasor_yolu + "/*.txt")
count = 0
sonuclar = []


for txt in txt_yollar:

    content = open(txt, "r")
    rtn = content.read().splitlines()
    for r in rtn:
        sonuclar.append(r[0])
    content.close()


print("Araç ",sonuclar.count("0"))
print("Yaya ",sonuclar.count("1"))
print("UAP ",sonuclar.count("2"))
print("UAİ ",sonuclar.count("3"))



