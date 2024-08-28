import statistics
from fractions import Fraction
from decimal import Decimal

#hàm mean 
data = [2,4,6,8,10]
mean = statistics.mean(data)
print("Giá trị trung bình = ", mean)
#tính trung bình số học của dãy phân số
data2 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
fraction_mean = statistics.mean(data2)
print("Giá trị trung bình với dữ liệu phân số = ", fraction_mean)
#tính trung bình số học của dãy số thập phân 
data3 = [Decimal("0.05"), Decimal("0.25"), Decimal("0.6")]
decimal_mean = statistics.mean(data3)
print("Giá trị trung bình với dữ liệu số thập phân = ", decimal_mean)

#hàm fmean
data = [2,4,6,8,10]
weight = [0.1, 0.2, 0.3, 0.4 ,0.5]
unweighted_mean = statistics.fmean(data)
weighted_mean = statistics.fmean(data,weight)
print("Giá trị trung bình khi không có weight : ", unweighted_mean)
print("Giá trị trung bình khi có weight : ", weighted_mean)

#hàm geometric
data = [2, 8, 12, 16, 32] 
geometric_mean = statistics.geometric_mean(data)
print("Giá trị trung bình hình học là:", geometric_mean)

#harmonic_mean()
data = [1, 3, 18, 20, 24] 
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
harmonic_mean_unweighted = statistics.harmonic_mean(data)
harmonic_mean_weighted = statistics.harmonic_mean(data,weights)
print("Trung bình nghịch không có weight :",harmonic_mean_unweighted)
print("Trung bình nghịch có weight :",harmonic_mean_weighted )

#median()
data = [1, 3, 18, 20, 24] 
print("Trung vị của dãy dữ liệu có lẻ phần tử:", statistics.median(data))
data2 = [1, 3, 20, 24] 
print("Trung vị của dãy dữ liệu có chẵn chẵn tử:", statistics.median(data2))

#median_low()
data = [1, 3, 18, 20, 24] 
median_low = statistics.median_low(data)
print("Trung vị thấp của dãy dữ liệu có lẻ phần tử:", median_low)
data2 = [1, 3, 20, 24] 
median_low = statistics.median_low(data2)
print("Trung vị thấp của dãy dữ liệu có chẵn chẵn tử:", median_low)

#median_high()
data = [1, 3, 18, 20, 24] 
median_high = statistics.median_high(data)
print("Trung vị cao của dãy dữ liệu có lẻ phần tử:", median_high)
data2 = [1, 3, 20, 24] 
median_high= statistics.median_high(data2)
print("Trung vị cao của dãy dữ liệu có chẵn chẵn tử:", median_high)

#median_grouped()
data = [1, 3, 3, 18, 24] 
median_grouped = statistics.median_grouped(data)
print("Trung vị được nhóm không có interval:", median_grouped )
median_grouped2 = statistics.median_grouped(data, interval= 2)
print("Trung vị được nhóm có interval = 2:", median_grouped2)

#mode()
data = [1, 3, 3, 18, 24] 
data2 = [Fraction(1,2), Fraction(1,2), Fraction(1,4)]
data3 = [Decimal("0.15"), Decimal("0.15"), Decimal("0.4")]
data4 = ["one", "one" , "two", "three", "four"]
print("Giá trị xuất hiện nhiều nhất của dãy dữ liệu:", statistics.mode(data))
print("Giá trị xuất hiện nhiều nhất của dãy dữ liệu phân số:", statistics.mode(data2))
print("Giá trị xuất hiện nhiều nhất của dãy dữ liệu số thập phân:", statistics.mode(data3))
print("Giá trị xuất hiện nhiều nhất của dãy dữ liệu không phải số:", statistics.mode(data4))

#multimode()
data = [1, 3, 3, 18, 18] 
data2 = [Fraction(1,2), Fraction(1,2), Fraction(1,3), Fraction(1,4)]
data3 = [Decimal("0.15"), Decimal("0.15"), Decimal("0.4")]
data4 = ["one", "one" , "two", "two", "four"]
print("Các giá trị xuất hiện nhiều nhất của dãy dữ liệu:", statistics.multimode(data))
print("Các giá trị xuất hiện nhiều nhất của dãy dữ liệu phân số:", statistics.multimode(data2))
print("Các giá trị xuất hiện nhiều nhất của dãy dữ liệu số thập phân:", statistics.multimode(data3))
print("Các Giá trị xuất hiện nhiều nhất của dãy dữ liệu không phải số:", statistics.multimode(data4))

#quantiles()
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
quantiles = statistics.quantiles(data, n=4, method='exclusive')
print("Phương pháp exclusive:", quantiles)
quantiles = statistics.quantiles(data, n=4, method='inclusive')
print("Phương pháp inclusive:", quantiles)

#pstdev()
data = [1, 8, 18, 20, 24] 
mu = statistics.mean(data)
print("Độ lệch chuẩn của dãy dữ liệu không có mu:", statistics.pstdev(data))
print("Độ lệch chuẩn của dãy dữ liệu có mu:", statistics.pstdev(data,mu))


#pvariance()
data = [1, 8, 18, 20, 24] 
mu = statistics.mean(data)
print("Phương sai của dãy dữ liệu không có mu:", statistics.pvariance(data))
print("Phương sai của dãy dữ liệu có mu:", statistics.pvariance(data,mu))
#với phân số và số thập phân
data2 = [Fraction(1,2), Fraction(1,3), Fraction(1,4)]
data3 = [Decimal("0.15"), Decimal("0.25"), Decimal("0.4")]
print("Phương sai của dãy dữ liệu phân số:", statistics.pvariance(data2))
print("Phương sai của dãy dữ liệu số thập phân:", statistics.pvariance(data3))


#stdev()
data = [1, 8, 18, 20, 24] 
xbar = statistics.mean(data)
print("Độ lệch chuẩn mẫu của dãy dữ liệu không có xbar:", statistics.stdev(data))
print("Độ lệch chuẩn mẫu của dãy dữ liệu  có xbar:", statistics.stdev(data,xbar))
data2 = [Fraction(1,2), Fraction(1,3), Fraction(1,4)]
data3 = [Decimal("0.15"), Decimal("0.25"), Decimal("0.4")]
print("Độ lệch chuẩn mẫu của dãy dữ liệu phân số:", statistics.stdev(data2))
print("Độ lệch chuẩn mẫu của dãy dữ liệu số thập phân:", statistics.stdev(data3))

#variance()
data = [1, 8, 18, 20, 24] 
xbar = statistics.mean(data)
print("Phương sai mẫu của dãy dữ liệu không có xbar:", statistics.variance(data))
print("Phương sai mẫu của dãy dữ liệu có xbar:", statistics.variance(data,xbar))
data2 = [Fraction(1,2), Fraction(1,3), Fraction(1,4)]
data3 = [Decimal("0.15"), Decimal("0.25"), Decimal("0.4")]
print("Phương sai mẫu của dãy dữ liệu phân số:", statistics.variance(data2))
print("Phương sai mẫu của dãy dữ liệu số thập phân:", statistics.variance(data3))

#covariance
x = [2, 4, 8, 16, 32] 
y = [1, 3, 5, 7, 9] 
covariance = statistics.covariance(x,y)
print("Hiệp phương sai mẫu của hai dữ liệu:", covariance)


#correlation()
x = [2, 4, 8, 16, 32] 
y = [1, 3, 5, 7, 9] 
correlation = + statistics.correlation(x,y)
print("Hệ số tương quan Pearson của hai dữ liệu:", correlation)

#linear_regression()
#slope là hệ số góc của đường thẳng hồi quy 
#intercept là hệ số giao của đường thẳng hồi quy với trục y
x = [2, 4, 8, 16, 32] 
y = [1, 3, 5, 7, 9] 
a,b = statistics.linear_regression(x,y)
print("Slope = ", a)
print("Intercept = ", b)


#NormalDist
from statistics import NormalDist
data = [1,3,8,13,24,40]
normal_dist = NormalDist.from_samples(data)
print(normal_dist)

#from_samples()
data = [1,3,8,13,24,40]
normal_dist = NormalDist.from_samples(data)
mean = normal_dist.mean
std = normal_dist.stdev
print(f"Giá trị trung bình là : ", mean)
print(f"Độ lệch chuẩn là : std")

#samples()
#Tạo NormalDist có trung bình = 50 và độ lệch chuẩn = 5
normal_dist = NormalDist(mu=50, sigma=5)
#Tạo 5 mẫu từ NormalDist được tạo ở trên
n = 5
random_samples = normal_dist.samples(n)
print("Random Samples:", random_samples)

#pdf()
# Ví dụ: trung bình = 50, độ lệch chuẩn = 5
normal_dist = NormalDist(mu=50, sigma=5)  
x = 50
pdfvalue = normal_dist.pdf(x)
print(f"PDF tại giá trị {x}: {pdfvalue}")

#cdf()
# Ví dụ: trung bình = 50, độ lệch chuẩn = 5
normal_dist = NormalDist(mu=50, sigma=5)  
x = 50
#Tính CDF tại x =50
cdfvalue = normal_dist.pdf(x)
print(f"CDF tại giá trị {x}: {cdfvalue}")

#inv_cdf()
# Tạo một đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=80, sigma=5)
# Tính giá trị ngược của CDF tại p = 0.8
p = 0.8
inv_cdf = normal_dist.inv_cdf(p)
print(f"giá trị ngược của CDF tại p = {p}: {inv_cdf}")

#overlap()
#Tạo hai đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist1 = NormalDist(mu= 80, sigma= 50)
normal_dist2 = NormalDist(mu= 100, sigma= 7)
# Tính độ trùng lặp giữa hai phân phối
overlap_value = normal_dist1.overlap(normal_dist2)
print("Độ trùng lặp giữa hai phân phối :", overlap_value)

#quantiles()
# Tạo đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=100, sigma=5)
# Tính 5 quantiles cho phân phối chuẩn
quantiles = normal_dist.quantiles(5)
print(quantiles)

#zscore()
# Tạo đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=100, sigma=5)
# Tính z-score cho giá trị x = 80
x = 80
z_score = normal_dist.zscore(x)
print(f"Z-score của x = {x}: {z_score}")
