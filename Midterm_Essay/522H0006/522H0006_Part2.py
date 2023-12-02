import cv2
import numpy as np
import matplotlib.pyplot as plt
   
# Đọc ảnh từ file 
image = cv2.imread("image.jpg") 

# Chuyển ảnh sang dạng kênh màu xám
gray_image = cv2.cvtColor(image, 
cv2.COLOR_BGR2GRAY)

# Lấy ra chiều cao và chiều rộng của ảnh xám
height, width = gray_image.shape[:2]

# Tính histogram của ảnh xám
gray_hist = np.zeros(256) 
for x in range(height): 
    for y in range(width): 
        pixel_values = gray_image[x,y] 
        gray_hist[pixel_values] += 1 

# Chuẩn hóa hsitogram ảnh xám
gray_hist = gray_hist / (height * width)

# Tính hàm phân phối tích lũy (CDF) của ảnh xám
cdf = np.zeros(256) 
cdf[0] = gray_hist[0]
for i in range(1, 256): 
    cdf[i] = cdf[i-1] + gray_hist[i] 

# Chuẩn hóa giá trị CDF về thang đo [0, 255]
normalized_cdf = (cdf * 255)

# Cân bằng Histogram 
equalized_image = gray_image.copy() 
for x in range(height): 
    for y in range(width): 
        pixel = gray_image[x, y]  
        equalized_image[x, y] = normalized_cdf[pixel] 

# Hiển thị ảnh gốc và ảnh đã cân bắng
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Equalized Image', equalized_image)

# Hiển thị lược đồ Histogram của ảnh xám
plot2 = plt.figure(1)
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title('Gray Image')

# Hiển thị lược đồ Histogram của ảnh đã cân bằng
plot2 = plt.figure(2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Equalized Image')
plt.show()

# Nhấn một nút bất kì để thoát
cv2.waitKey(0)

# Đóng tất cả cửa sổ đang hiển thị
cv2.destroyAllWindows()


