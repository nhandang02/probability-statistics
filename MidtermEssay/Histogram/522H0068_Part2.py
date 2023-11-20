import cv2                                          
import numpy as np        
#Histogram Equalization  
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)                       
height, width = img.shape
#tính histogram cho ảnh
his_arr = np.zeros(256)
for i in range(height):
    for j in range(width):
        his_arr[img[i,j]] += 1
#chuẩn hóa ảnh
his_arr = his_arr / (height*width)
#tính cdf cho ảnh
cdf = np.zeros(256)
cdf[0] = his_arr[0]
for i in range(1,256):
    cdf[i] = cdf[i-1] + his_arr[i]
#tạo giá trị cường độ mới
frequency = np.round(cdf*255)
#áp dụng cường độ mới vào ảnh
img_equalized = np.zeros_like(img)
for i in range(height) :
    for j in range(width):
        img_equalized[i,j] = frequency[img[i,j]]
#lưu ảnh đã cân bằng và hiển thị nó
cv2.imwrite('equalized_image.jpg',img_equalized)
cv2.imshow('Ảnh gốc', img)
cv2.imshow('Ảnh sau khi cân bằng', img_equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()    