import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# Đọc ảnh từ đường dẫn file. Trả về ảnh.
def read_image(file_path):
    img = cv.imread(file_path)
    assert img is not None, "file could not be read, check with os.path.exists()"
    return img

# Chuyển đổi ảnh sang dạng grayscale. Trả về ảnh grayscale.
def convert_to_grayscale(image):
    grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return grayscale_img

# Tính histogram của ảnh. Trả về histogram và các khoảng giá trị.
def compute_histogram(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    return hist, bins

# Tính tích lũy chuẩn hóa của histogram. Trả về tích lũy chuẩn hóa.
def compute_cumulative_histogram(hist):
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    return cdf_normalized

# Vẽ đồ thị histogram.
def plot_histogram(hist):  
    plt.hist(hist.flatten(), bins=256, range=[0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('histogram'), loc='upper left')
    plt.show()

# Vẽ đồ thị tích lũy chuẩn hóa.
def plot_cumulative_histogram(cdf):
    plt.plot(cdf, color='b')
    plt.legend(('cdf'), loc='upper left')
    plt.show()

# # Đường dẫn đến file ảnh
# file_path = 'image.jpg'
# # Đọc ảnh
# img = read_image(file_path)
# # Chuyển đổi ảnh sang grayscale
# grayscale_img = convert_to_grayscale(img)
# # Tính histogram
# hist, bins = compute_histogram(grayscale_img)
# # Tính tích lũy chuẩn hóa
# cdf_normalized = compute_cumulative_histogram(hist)
# # Vẽ đồ thị histogram
# plot_histogram(hist)
# # Vẽ đồ thị tích lũy chuẩn hóa

def equalize_image(file_path):
    # Đọc ảnh
    img = read_image(file_path)
    grayscale_img = convert_to_grayscale(img)
    equalized_image = img.copy()  
    hist = compute_histogram(grayscale_img)
    normalized_cdf = compute_cumulative_histogram(hist)
    
    for x in range(img.shape[0]): 
        for y in range(img.shape[1]): 
            pixel_value = img[x, y]  
            equalized_image[x, y] = normalized_cdf[pixel_value]
    return equalized_image

equalized_image = equalize_image('image.jpg')

cv.imshow('Gray Image', convert_to_grayscale(read_image('image.jpg')))
cv.imshow('Equalized Image', equalized_image)