import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file 
image = cv2.imread("image.jpg") 

# Chuyển ảnh sang dạng ảnh xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hàm tính histogram bằng phương pháp đếm số pixel tương ứng với mỗi mức xám
def compute_histogram(image):
    hist = np.zeros(256) # Khởi tạo mảng hist có 256 phần tử bằng 0
    # Lặp qua từng pixel trong ảnh   
    for x in range(image.shape[0]): # Duyệt qua từng chiều cao của ảnh
        for y in range(image.shape[1]): # Duyệt qua từng chiều rộng của ảnh
            pixel_values = image[x,y]  # Lấy giá trị pixel hiện tại của ảnh gán vào giá trị pixel_value 
            hist[pixel_values] += 1   # Sau khi đã cập nhật pixel_values thì tăng giá trị của mảng hist lên 1
    return hist  # Sau khi đã cập nhật mỗi pixel tương ứng với mỗi mức xám từ (0-255) thì hàm trả về mảng hist   

# Hàm tính phân phối tích lũy (CDF)
def compute_CDF(histogram):
    cdf = np.zeros(256) # Khởi tạo mảng cdf có 256 phần tử bằng 0
    cdf[0] = histogram[0]  # Gán giá trị đầu tiên của CDF bằng giá trị histogram tương ứng.
    for i in range(1, 256): # Duyệt qua các mức xám từ (1-255)
        cdf[i] = cdf[i-1] + histogram[i]  # Tính giá trị CDF bằng tổng các pixel ở từng mức xám.
    return cdf # Hàm trả mảng phân phối tích lũy của một histogram

# Hàm chuẩn hóa CDF
def normalize_cdf(cdf, height, width):
    normalized_cdf = (cdf * 255) / (height * width)  
    return normalized_cdf # Kết quả trả về là mảng chứa cdf đã được chuẩn hóa

def equalize_image(image):
    equalized_image = image.copy()  # Tạo một bản sao của ảnh đầu vào để lưu ảnh đã cân bằng histogram
    Histogram = compute_histogram(gray_image) # Tính Histogram từ ảnh xám
    CDF = compute_CDF(Histogram) # Tính hàm CDF từ Histogram của ảnh xám
    normalized_cdf = normalize_cdf(CDF, image.shape[0], image.shape[1])  # Chuẩn hóa CDF
    # Lặp qua từng pixel trong ảnh và ánh xạ lại mức sáng
    for x in range(image.shape[0]): # Câu lệnh image.shape[0] trả về chiều cao của ảnh
        for y in range(image.shape[1]): # Câu lệnh image.shape[1] trả về chiều rộng của ảnh
            pixel_value = image[x, y]  # Lấy giá trị pixel hiện tại
            equalized_image[x, y] = normalized_cdf[pixel_value] # Gán giá trị pixel đã ánh xạ lại vào ảnh
    return equalized_image

equalized_image = equalize_image(gray_image) # Gán ảnh đã cân bằng vào biến equalized_image

def resize_image_to_half(image):
    # Lấy kích thước của ảnh gốc
    height, width = image.shape[:2]

    # Sử dụng hàm resize để thay đổi kích thước ảnh về 1/2
    resized_image = cv2.resize(image, (width // 2, height // 2))

    return resized_image

# Hiển thị biểu đồ histogram của ảnh gốc và ảnh đã cân bằng
#gray_image = resize_image_to_half(gray_image)
hist1 = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plot2 = plt.figure(1)
plt.title('Histogram of Gray Image')
plt.plot(hist1)

#equalized_image = cv2.equalizeHist(gray_image)
hist2 = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plot2 = plt.figure(2)
plt.title('Histogram of Equalized Image')
plt.plot(hist2)
plt.show()

# Hiển thị ảnh gốc và ảnh đã cân bắng
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Equalized Image', equalized_image)

# Nhấn một nút bất kì để thoát
cv2.waitKey(0)