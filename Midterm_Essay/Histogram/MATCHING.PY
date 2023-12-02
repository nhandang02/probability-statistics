import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file 
source_image = cv2.imread("source_image.jpg", cv2.IMREAD_GRAYSCALE)
references_image = cv2.imread("reference_image.jpg", cv2.IMREAD_GRAYSCALE)  

# Lấy ra chiều cao và chiều rộng của ảnh gốc và ảnh tham chiếu
height_source, width_source = source_image.shape[:2]
height_references, width_referecnes = references_image.shape[:2]

# Tính histogram ảnh nguồn 
source_hist = np.zeros(256) 
for x in range(height_source): 
    for y in range(width_source): 
        pixel_values = source_image[x,y] 
        source_hist[pixel_values] += 1 
# Chuẩn hóa hsitogram ảnh gốc
source_hist = source_hist / (height_source * width_source)

# Tính histogram ảnh tham chiếu
references_hist = np.zeros(256) 
for x in range(height_references): 
    for y in range(width_referecnes): 
        pixel_values = references_image[x,y] 
        references_hist[pixel_values] += 1 
# Chuẩn hóa histogram ảnh tham chiếu
references_hist = references_hist / (height_references * width_referecnes)

# Tính hàm phân phối tích lũy (CDF) của ảnh gốc
cdf_source = np.zeros(256) 
cdf_source[0] = source_hist[0]
for i in range(1, 256): 
    cdf_source[i] = cdf_source[i-1] + source_hist[i] 

# Tính hàm phân phối tích lũy (CDF) của ảnh tham chiếu
cdf_references = np.zeros(256) 
cdf_references[0] = references_hist[0]
for i in range(1, 256): 
    cdf_references[i] = cdf_references[i-1] + references_hist[i]

# Tạo bảng tra (mapping array) histogram của ảnh tham chiếu đến histogram của ảnh gốc
# mapping = np.arange(256, dtype=np.uint8)
# for x in range(256): 
#     for y in range(256): 
#         if abs(cdf_source[x] - cdf_references[y]) < 0.001:
#             mapping[x] = y
#             break
mapping = np.zeros(256, dtype=int)
for x in range(256):
    min = float("inf")
    min_val = 0
    for y in range(256):
        valu = np.abs(cdf_references[y] - cdf_source[x])
        if (valu < min):
            min = valu
            min_val = y
    mapping[x] = min_val

# Áp dụng ánh xạ từ histogram của ảnh tham chiếu đến histogram của ảnh gốc
matched_image = source_image.copy()
for x in range(height_source): 
    for y in range(width_source): 
        pixel_value = source_image[x, y]  
        matched_image[x, y] = mapping[pixel_value] 

# Hiển thị ảnh gốc và ảnh đã cân bắng
cv2.imshow('Source Image', source_image)
cv2.imshow('References Image', references_image)
cv2.imshow('Matched Image', matched_image)

# hist1 = cv2.calcHist([source_image], [0], None, [256], [0, 256])
# plot2 = plt.figure(1)
# plt.title('hist1')
# plt.plot(hist1)
# hist2 = cv2.calcHist([references_image], [0], None, [256], [0, 256])
# plot2 = plt.figure(2)
# plt.title('hist2')
# plt.plot(hist2)
# hist3 = cv2.calcHist([matched_image], [0], None, [256], [0, 256])
# plot2 = plt.figure(3)
# plt.title('hist3')
# plt.plot(hist3)
# plt.show()

# plt.hist(source_image.ravel(), 256, [0, 256])
# plt.title('Source Image')
# plt.show()

# plt.hist(references_image.ravel(), 256, [0, 256])
# plt.title('Reference Image')
# plt.show()

# plt.hist(matched_image.ravel(), 256, [0, 256])
# plt.title('Matched Image')
# plt.show()

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

axs[0].hist(source_image.ravel(), 256, [0, 256])
axs[0].set_title('Source Image')

axs[1].hist(references_image.ravel(), 256, [0, 256])  
axs[1].set_title('Reference Image')

axs[2].hist(matched_image.ravel(), 256, [0, 256])
axs[2].set_title('Matched Image')

plt.show()

# Nhấn một nút bất kì để thoát
cv2.waitKey(0)

# Đóng tất cả cửa sổ đang hiển thị
cv2.destroyAllWindows()

