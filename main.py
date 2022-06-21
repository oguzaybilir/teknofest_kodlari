from time import sleep
import cv2
import pandas as pd 
import numpy as np
import pydicom as dicom
from skimage import exposure

excel_path = "E:\\Saglikta_Yapay_Zeka_Teknofest_Veri\\Training\\Data.xlsx"
ana_path = "E:\\Saglikta_Yapay_Zeka_Teknofest_Veri\\Training\\"
txt_path = "C:\\Users\\oguza\\Desktop\\teknofestverileri\\"

basamak = 4

sinif_sözlük = {

    "Akut apandisit ile uyumlu": "1",
    "Akut kolesistit ile uyumlu": "2",
    "Akut pankreatit ile uyumlu": "3",
    "Böbrek taşı": "4",
    "Üreter taşı": "4",
    "Akut divertikülit ile uyumlu": "5",
    "Abdominal aort anevrizma": "6",
    "Abdominal aort diseksiyon": "6"

}

sayac_1 = 0 
sayac_2 =  0
sayac_3 = 0
sayac_4 = 0
sayac_5 = 0


def excel_okuma_parcalama(excel_path):

    global sayac_1,sayac_2,sayac_3,sayac_4,sayac_5

    data = pd.read_excel(excel_path)
    tüm_degerler  = data.values

    for deger in tüm_degerler:

        try:
            try:

                dosya_klasor = deger[0]
                dosya_adi = deger[1]
                clas = str(deger[3])
                class_id = sinif_sözlük[clas]
                koordinatlar = deger[4]
                koordinatlar = str(koordinatlar)

            except:
                #print(dosya_klasor,dosya_adi,clas, class_id, koordinatlar)
                sayac_4 = sayac_4+1
                pass

            try:
                
                image_yol = ana_path + "\\" + dosya_klasor + "\\" + dosya_adi + ".dcm"
                ds=dicom.dcmread(image_yol)
                dcm_sample=ds.pixel_array
                dcm_sample=exposure.equalize_adapthist(dcm_sample)
                image_weight,image_height = ds.pixel_array.shape
                """
                image_weight,image_height = 512,512 
                """

            except:
                image_weight,image_height = 512,512  # sil burayı 
                sayac_5 = sayac_5+1
                pass


            try:
                box_baslama,box_bitis  = koordinatlar.split("-")
                box_x1,box_y1 = box_baslama.split(",")
                box_x2,box_y2 = box_bitis.split(",")
                box_x1,box_y1,box_x2,box_y2 = int(box_x1),int(box_y1),int(box_x2),int(box_y2)
                box_weight = abs(box_x2-box_x1)
                box_height = abs(box_y2-box_y1)     
                x_x = box_weight / 2
                y_y = box_height / 2 
                x_center = box_x1 + x_x
                y_center = box_y1 + y_y

                x_center_yolo = x_center / image_weight
                y_center_yolo = y_center / image_height 
                yolo_weight = box_weight / image_weight
                yolo_height = box_height / image_height

                
                x_center_yolo = str(round(x_center_yolo,basamak))
                y_center_yolo = str(round(y_center_yolo,basamak))
                yolo_weight = str(round(yolo_weight,basamak))
                yolo_height = str(round(yolo_height,basamak))

                txt_final  = class_id +" "+ x_center_yolo +" "+ y_center_yolo +" "+ yolo_weight +" "+ yolo_height

                txt_yol =txt_path+ dosya_adi +".txt"
                print(txt_final)

                f = open(txt_yol, "x")
                f.write(txt_final)
                f.close()


            
                
            except:
                sayac_3 = sayac_3 + 1
                pass

            sayac_1 = sayac_1 + 1

        except:
            sayac_2 = sayac_2 + 1
            pass

        dosya_klasor =None
        dosya_adi =None
        clas = None
        class_id = None
        koordinatlar =None
        koordinatlar = None

        
tüm_degerler = excel_okuma_parcalama(excel_path)
print("Düzgün işlem :",sayac_1)
print("Genel bütünde takılan işlem :",sayac_2)
print("Hesaplamada takılan işlem :",sayac_3)
print("Giriş veri parcalamada hatalı işlem :",sayac_4)











