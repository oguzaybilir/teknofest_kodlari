import cv2
import numpy as np
import pydicom as PDCM

def dicomdan_png(dicom_dosya_yolu):
    dicom_resim= PDCM.read_file(dicom_dosya_yolu)

    satirlar=dicom_resim.get(0x00280010).value
    sutunlar=dicom_resim.get(0x00280011).value
    
    ornek_numarasi= int(dicom_resim.get(0x00200013).value)
    
    pencere_merezi=int(dicom_resim.get(0x00281050).value)
    pencere_genişlik=int(dicom_resim.get(0x00281051).value)
    
    max=int((pencere_merezi+pencere_genişlik)/2)
    min=int((pencere_merezi-pencere_genişlik)/2)

    if (dicom_resim.get(0x00281052) is None):
        kesisimi_yeniden_olceklendirme = 0

    else:
        kesisimi_yeniden_olceklendirme = int(dicom_resim.get(0x00281052).value)
    
    if (dicom_resim.get(0x00281053) is None):
        eğimi_yeniden_olceklendirme = 1
    
    else:
        eğimi_yeniden_olceklendirme = int(dicom_resim.get(0x00281053).value)

    
    yeni_gorsel=np.zeros((satirlar,sutunlar), np.uint8)
    pikseller=dicom_resim.pixel_array

    for i in range(satirlar):
        for j in range(sutunlar):
            piksel_degeri = pikseller[i,j]
            yeni_piksel_degeri=piksel_degeri*eğimi_yeniden_olceklendirme + kesisimi_yeniden_olceklendirme

            if (yeni_piksel_degeri > max):
                yeni_gorsel[i][j]=255
            elif (yeni_piksel_degeri < min):
                yeni_gorsel[i][j]=0
            else:
                yeni_gorsel[i][j]=int(((yeni_piksel_degeri-min)/(max-min))*255)
    
    return yeni_gorsel, ornek_numarasi


def main():
    dicom_formatindaki_resim="C:\\Users\\oguza\\Desktop\\saglik_etiketleri\\veriler\\10873356152.dcm"
    
    png_formatindaki_hali , ornek_numarasi = dicomdan_png(dicom_formatindaki_resim)
    cv2.imwrite(str(ornek_numarasi - 1).zfill(4) +".png",png_formatindaki_hali)
    
if __name__ == "__main__":
    main()
    print("Bitti")

