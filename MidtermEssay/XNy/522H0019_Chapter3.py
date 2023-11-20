import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage import exposure

# Đọc ảnh từ đường dẫn file. Trả về ảnh.
def read_image(file_path):
    img = cv2.imread(file_path)
    return img

# Kiểm tra số kênh của ảnh. Trả về số kênh của ảnh.
def check_channels(image):
    return image.ndim

# Áp dụng phép làm tương tự lược đồ màu từ ảnh tham chiếu lên ảnh đầu vào. 
# Trả về ảnh đã được làm tương tự.
def match_histograms(image, reference):
    matched = exposure.match_histograms(image, reference, multichannel=True)
    return matched

# Vẽ các ảnh gốc, ảnh tham chiếu và ảnh đã được làm tương tự.
def plot_images(image, reference, matched):
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)
    for aa in (ax1, ax2, ax3):
        aa.set_axis_off()
    ax1.imshow(image)
    ax1.set_title('Source')
    ax2.imshow(reference)
    ax2.set_title('Reference')
    ax3.imshow(matched)
    ax3.set_title('Matched')
    plt.tight_layout()
    plt.show()

# Vẽ đồ thị histogram của các kênh màu trong ảnh.
def plot_histograms(image, reference, matched):
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
    for i, img in enumerate((image, reference, matched)):
        for c, c_color in enumerate(('red', 'green', 'blue')):
            img_hist, bins = exposure.histogram(img[..., c], source_range='dtype')
            axes[c, i].plot(bins, img_hist / img_hist.max())
            img_cdf, bins = exposure.cumulative_distribution(img[..., c])
            axes[c, i].plot(bins, img_cdf)
            axes[c, 0].set_ylabel(c_color)
    axes[0, 0].set_title('Source')
    axes[0, 1].set_title('Reference')
    axes[0, 2].set_title('Matched')
    plt.tight_layout()
    plt.show()

def perform_histogram_matching(file_path1, file_path2):
    # Đọc ảnh
    image = read_image(file_path1)
    reference = read_image(file_path2)
    # Kiểm tra số kênh của ảnh
    print('No of Channel is: ' + str(check_channels(image)))
    print('No of Channel is: ' + str(check_channels(reference)))
    # Áp dụng phép làm tương tự lược đồ màu
    matched = match_histograms(image, reference)
    # Vẽ các ảnh
    plot_images(image, reference, matched)
    # Vẽ đồ thị histogram
    plot_histograms(image, reference, matched)

# Đường dẫn đến các file ảnh
file_path1 = 'img.jpeg'
file_path2 = '2Fw13.jpeg'
# Thực hiện histogram matching
perform_histogram_matching(file_path1, file_path2)