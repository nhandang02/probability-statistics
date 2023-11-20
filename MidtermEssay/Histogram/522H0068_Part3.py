import cv2                                          
import numpy as np  
#Histogram Matching
model = cv2.imread('reference_image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('source_image.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
height_m, width_m = model.shape
# Tính histogram của ảnh gốc
hist = np.zeros(256)
for i in range(height):
    for j in range(width):
        hist[img[i, j]] += 1
hist = hist / (height * width)
# Tính histogram của ảnh mẫu
hist_model = np.zeros(256)
for i in range(height_m):
    for j in range(width_m):
        hist_model[model[i, j]] += 1
hist_model = hist_model / (height_m * width_m)
# Tính CDF cho ảnh gốc
cdf = np.zeros(256)
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]
# Tính CDF cho ảnh mẫu
cdf_model = np.zeros(256)
cdf_model[0] = hist_model[0]
for i in range(1, 256):
    cdf_model[i] = cdf_model[i-1] + hist_model[i]
# Tạo ánh xạ từ histogram của ảnh mẫu đến histogram của ảnh gốc
mapping = np.arange(256, dtype=np.uint8)
for i in range(256):
    for j in range(256):
        if abs(cdf[i] - cdf_model[j]) < 0.001:
            mapping[i] = j
            break
# Áp dụng ánh xạ lên ảnh đích để khớp với histogram của ảnh nguồn
result_img = img.copy()
for i in range(height):
    for j in range(width):
        result_img[i, j] = mapping[img[i, j]]
# Lưu ảnh đã cân bằng hoặc hiển thị nó
cv2.imwrite('matched_image.jpg', result_img)
cv2.imshow('Ảnh nguồn', img)
cv2.imshow('Ảnh đích', model)
cv2.imshow('Ảnh sau khi cân bằng', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()