import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file 
image = cv2.imread("image.jpg") 

# Chuyển ảnh sang dạng ảnh xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image_to_half(image):
    # Lấy kích thước của ảnh gốc
    height, width = image.shape[:2]

    # Sử dụng hàm resize để thay đổi kích thước ảnh về 1/2
    resized_image = cv2.resize(image, (width // 4, height // 4))

    return resized_image

#gray_image = resize_image_to_half(gray_image)

equalized_image = cv2.equalizeHist(gray_image)

# Hiển thị ảnh gốc và ảnh đã cân bắng
cv2.imshow('Ảnh gốc', gray_image)
cv2.imshow('Ảnh đã cân bằng', equalized_image)
hist2 = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plot2 = plt.figure(2)
plt.title('hist2')
plt.plot(hist2)
plt.show()
# Nhấn một nút bất kì để thoát
cv2.waitKey(0)

# Đóng tất cả cửa sổ đang hiển thị
cv2.destroyAllWindows()