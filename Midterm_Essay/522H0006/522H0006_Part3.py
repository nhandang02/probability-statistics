import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file 
source_image = cv2.imread("source_image.jpg", cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread("reference_image.jpg", cv2.IMREAD_GRAYSCALE)  

# Lấy ra chiều cao và chiều rộng của ảnh gốc và ảnh tham chiếu
height_source, width_source = source_image.shape[:2]
height_reference, width_referecnes = reference_image.shape[:2]

# Tính histogram ảnh gốc và ảnh tham chiếu
source_hist = np.zeros(256) 
for x in range(height_source): 
    for y in range(width_source): 
        pixel_values = source_image[x,y] 
        source_hist[pixel_values] += 1 
    
reference_hist = np.zeros(256) 
for x in range(height_reference): 
    for y in range(width_referecnes): 
        pixel_values = reference_image[x,y] 
        reference_hist[pixel_values] += 1 

# Chuẩn hóa hsitogram ảnh gốc và ảnh tham chiếu
source_hist = source_hist / (height_source * width_source)
reference_hist = reference_hist / (height_reference * width_referecnes)

# Tính hàm phân phối tích lũy (CDF) của ảnh gốc và ảnh tham chiếu
cdf_source = np.zeros(256) 
cdf_source[0] = source_hist[0]
for i in range(1, 256): 
    cdf_source[i] = cdf_source[i-1] + source_hist[i] 

cdf_reference = np.zeros(256) 
cdf_reference[0] = reference_hist[0]
for i in range(1, 256): 
    cdf_reference[i] = cdf_reference[i-1] + reference_hist[i]

# Tạo ánh xạ từ hàm phân phối tích lũy (CDF) của 2 ảnh.
mapping = np.zeros(256, dtype=int)
for x in range(256):
    min = float("inf")
    min_value = 0
    for y in range(256):
        value = np.abs(cdf_reference[y] - cdf_source[x])
        if (value < min):
            min = value
            min_val = y
    mapping[x] = min_val

# Áp dụng ánh xạ từ histogram của ảnh tham chiếu đến histogram của ảnh gốc
matched_image = source_image.copy()
for x in range(height_source): 
    for y in range(width_source): 
        pixel_value = source_image[x, y]  
        matched_image[x, y] = mapping[pixel_value] 

# Hiển thị ảnh gốc, ảnh tham chiếu và ảnh đã cân bắng
cv2.imshow('Source Image', source_image)
cv2.imshow('Reference Image', reference_image)
cv2.imshow('Matched Image', matched_image)

# Hiển thị lược đồ Histogram của ảnh gốc
plot2 = plt.figure(1)
plt.hist(source_image.ravel(), 256, [0, 256])
plt.title('Source Image')

# Hiển thị lược đồ Histogram của ảnh tham chiếu
plot2 = plt.figure(2)
plt.hist(reference_image.ravel(), 256, [0, 256])
plt.title('Reference Image')

# Hiển thị lược đồ Histogram của ảnh đã cân bằng
plot2 = plt.figure(3)
plt.hist(matched_image.ravel(), 256, [0, 256])
plt.title('Matched Image')
plt.show()

# Nhấn một nút bất kì để thoát
cv2.waitKey(0)

# Đóng tất cả cửa sổ đang hiển thị
cv2.destroyAllWindows()

