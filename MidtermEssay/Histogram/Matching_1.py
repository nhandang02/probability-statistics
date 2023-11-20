import cv2
import numpy as np
import matplotlib.pyplot as plt

def match_histogram(image, reference_image):
    # Chuyển ảnh và ảnh tham chiếu sang không gian màu LAB
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    reference_lab = cv2.cvtColor(reference_image, cv2.COLOR_BGR2LAB)

    # Tạo các kênh LAB riêng lẻ
    image_l, image_a, image_b = cv2.split(image_lab)
    reference_l, reference_a, reference_b = cv2.split(reference_lab)

    # So khớp histogram của kênh L (độ sáng)
    matched_l = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(image_l)

    # Kết hợp các kênh sau khi so khớp histogram
    matched_lab = cv2.merge((matched_l, image_a, image_b))

    # Chuyển lại sang không gian màu BGR
    matched_image = cv2.cvtColor(matched_lab, cv2.COLOR_LAB2BGR)

    return matched_image

# Đọc ảnh cần so khớp histogram
image = cv2.imread('img_source.jpg')

# Đọc ảnh tham chiếu
reference_image = cv2.imread('img_references.jpg')

# So khớp histogram
matched_image = match_histogram(image, reference_image)

# Lưu ảnh đã so khớp histogram
cv2.imwrite('matched_image.jpg', matched_image)

# Hiển thị ảnh đã so khớp histogram (tùy chọn)
cv2.imshow('Source Image', image)
cv2.imshow('References Image', reference_image)
cv2.imshow('Matched Image', matched_image)

hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])
plot2 = plt.figure(1)
plt.title('hist1')
plt.plot(hist1)
hist2 = cv2.calcHist([reference_image], [0], None, [256], [0, 256])
plot2 = plt.figure(2)
plt.title('hist2')
plt.plot(hist2)
hist3 = cv2.calcHist([matched_image], [0], None, [256], [0, 256])
plot2 = plt.figure(3)
plt.title('hist3')
plt.plot(hist3)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
