import glob

klasor_yolu = "dosya yolunu girin"

txt_yollar = glob.glob(klasor_yolu + "/*.txt")
count = 0
sonuclar = []
ayri_yol = []

for c in txt_yollar:
    ayri_yol.append(c.split("\\")[-1])


for txt in txt_yollar:

    content = open(txt, "r")
    rtn = content.read().splitlines()
    
    f = open(f"C:\\Users\\Username\\Desktop\\klasor_ismi\\{ayri_yol[count]}aa", "w+")
    count += 1
    for r in rtn:
        a = r[0]
        a=int(a)

        if a == 1:
            print("eski ",a)
            a = 3
            print("yeni ",a)
            
        elif a == 3:
            print("eski ",a)
            a = 1
            print("yeni ",a)

        f.write((str(a)+str(r[1:]))+"\n")
    f.close()
    content.close()




