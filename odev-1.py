import matplotlib.pyplot as plt
import cv2

def histogram_olustur(resim):
    # Resmin boyutlarını al
    satir, sutun = resim.shape

    # Histogram için boş bir liste oluştur
    histogram = [0] * 256

    # Her bir pixel değerinin sayısını hesapla
    for i in range(satir):
        for j in range(sutun):
            pixel_degeri = resim[i, j]
            histogram[pixel_degeri] += 1

    return histogram

# Resmin yolunu belirtin
resim_yolu = 'image.jpg'

# Resmi oku
resim = cv2.imread(resim_yolu)

# Resmi gri tonlamaya çevir
B = resim[:,:,0]
G = resim[:,:,1]
R = resim[:,:,2]

gri_resim = 0.2989 * R + 0.5870 * G + 0.1140 * B

# Histogramı oluştur
histogram = histogram_olustur(gri_resim.astype(int))

# Histogramı çizme
plt.plot(histogram)
plt.title('Gri Resim Histogramı')
plt.xlabel('Pixel Değeri')
plt.ylabel('Pixel Sayısı')
plt.show()
plt.figure()
plt.imshow(resim)
plt.show()