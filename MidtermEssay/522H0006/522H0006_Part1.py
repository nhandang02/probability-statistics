import statistics
from fractions import Fraction as F
from decimal import Decimal as D
from statistics import NormalDist

## mean()
# dataset positive
mean1 = statistics.mean(data = [5, 10 , 15, 20])

# dataset negative
mean2 = statistics.mean(data = [-5, 10.32, 15.02, 20.1])

# daset fraction
mean3 = statistics.mean(data = [F(5,2), F(5,10), F(5,15), F(5,20)])

# dataset decimal
mean4 = statistics.mean(data = [D("0.546"), D("0.623"), D("0.821"), D("0.105")])

print('Mean of dataset positive number: ', mean1) # Output: 12.5
print('Mean of dataset negative number: ', mean2) # Output: 10.11
print('Mean of dataset fraction number: ', mean3) # Output:43/48
print('Mean of dataset decimal number: ', mean4) # Output: 0.52375

####################################################################
## fmean() ##
# Example 1:
# dataset positive
fmean1 = statistics.fmean(data = [5, 10 , 15, 20])

# Example 2:
# dataset of process point
point = [10, 8.5, 8, 7.5]
# dataset of weights of process point
weights = [0.1, 0.2, 0.2, 0.5]
fmean2 = statistics.fmean(point, weights)

print('FMean of dataset positive number: ', fmean1) # Output: 12.5
print('FMean of dataset point: ', fmean2) # Output: 8.05

####################################################################
## geometric_mean()
# dataset
geometric_mean1 = statistics.geometric_mean(data = [2, 4, 8])

# daset fraction
data_fraction = [F(5,2), F(5,10), F(5,15), F(5,20)]
geometric_mean2 = statistics.geometric_mean(data = data_fraction)

# dataset decimal
data_decimal = [D("0.546"), D("0.623"), D("0.821"), D("0.105")]
geometric_mean3 = statistics.geometric_mean(data=data_decimal)

print('Geometric Mean of dataset fraction number: ', geometric_mean1)
# Output: 4.0
print('Geometric Mean of dataset decimal number: ', geometric_mean2) 
# Output: 0.5681096832337497
print('Geometric Mean of dataset decimal number: ', geometric_mean3) 
# Output: 0.41381219619987675

####################################################################
## harmonic_mean()
# dataset speed of motor
speed = [20, 80]
weights_speed = [2, 12]

# Example 1:
harmonic_mean1 = statistics.harmonic_mean(speed)
# Example 2:
harmonic_mean2 = statistics.harmonic_mean(speed, weights_speed)

print('Harmonic Mean of speed: ', harmonic_mean1)
# Output: 32
print('Harmonic Mean of speed with weight: ', harmonic_mean2)
# Output: 56

####################################################################
## median()
# dataset with length is even
median1 = statistics.median([10, 20, 30, 40])

# dataset with length is odd
median2 = statistics.median([10, 20, 30, 40, 50])

print('Median of dataset length is even: ', median1)
# Output: 25
print('Median of dataset length is odd: ', median2)
# Output: 30

####################################################################
## median_low()
# dataset with length is even
median_low1 = statistics.median_low([10, 20, 30, 40])

# dataset with length is odd
median_low2 = statistics.median_low([10, 20, 30, 40, 50])

print('Median low of dataset length is even: ', median_low1)
# Output: 20
print('Median low of dataset length is odd: ', median_low2)
# Output: 30

####################################################################
## median_high()
# dataset with length is even
median_high1 = statistics.median_high([10, 20, 30, 40])

# dataset with length is odd
median_high2 = statistics.median_high([10, 20, 30, 40, 50])

print('Median high of dataset length is even: ', median_high1)
# Output: 30
print('Median high of dataset length is odd: ', median_high2)
# Output: 30

####################################################################
## median_grouped()
# median_group with interval default = 1
median_group1 = statistics.median_grouped(data=[2, 3, 3, 3, 4, 5])

# median_group with interval 
median_group2 = statistics.median_grouped(data=[2, 3, 3, 3, 4, 5], interval=2)

print('Median Grouped of dataset:', median_group1)
# Output: 3.1666666666666665
print('Median Grouped of dataset:', median_group2)
# Output: 3.333333333333333

####################################################################
## mode()
# dataset number
data_number = [2, 3, 3, 3, 4, 4, 5]
mode1 = statistics.mode(data_number)

# dataset string
data_string = ["Black", "White", "Blue", "Blue"]
mode2 = statistics.mode(data_string)

print('Mode of dataset number: ', mode1)
# Output: 3
print('Mode of dataset number: ', mode2)
# Output: "Blue"

####################################################################
## multimode()
# dataset number
data_number = [2, 3, 3, 3, 4, 4, 4, 5]
multimode1 = statistics.multimode(data_number)

# dataset string
data_string = ["Black", "Black", "White", "Blue", "Blue"]
multimode2 = statistics.multimode(data_string)

# dataset character
data_character = 'nnnnaaauuudddzzzz'
multimode3 = statistics.multimode(data_character)

print('Modes of dataset number: ', multimode1)
# Output: [3, 4]
print('Modes of dataset string: ', multimode2)
# Output: ["Black", "Blue"]
print('Modes of dataset character: ', multimode3)
# Output: ['n', 'z']

####################################################################
## quantiles() 
# dataset 
data_n = [10, 20, 30, 40, 50, 70, 100]

quantiles1 = statistics.quantiles(data_n, n=4, method="exclusive")
quantiles2 = statistics.quantiles(data_n, n=4, method="inclusive")

print('Quantiles of data_n with method exclusive: ', quantiles1)
# Output: [20.0, 40.0, 70.0]
print('Quantiles of data_n method inclusive: ', quantiles2)
# Output: [25.0, 40.0, 60.0]

####################################################################
                        ## pstdev() ##
# dataset
pstdev = statistics.pstdev(data=[5, 10, 15, 20 ], mu=None)

print('Population Standard deviation of dataset: ', pstdev)
# Output: 5.5901699437494745

####################################################################
## pvariance() 
# dataset
dataset = [1.2, 2.3, 3.4, 4.5, 5.6]
pvariance1 = statistics.pvariance(dataset)

mu = statistics.mean(dataset)
pvariance2 = statistics.pvariance(dataset, mu)

# dataset fraction
pvariance3 = statistics.pvariance(data_fraction)

# datasset decimal
pvariance4 = statistics.pvariance(data_decimal)

print('Population Variance of dataset mu=None: ', pvariance1)
# Output: 2.42
print('Population Variance of dataset mu=mean(dataset): ', pvariance2)
# Output: 2.42
print('Population Variance of dataset fraction: ', pvariance3)
# Output: 665/768
print('Population Variance of dataset decimal: ', pvariance4)
# Output: 0.0685136875

####################################################################
## stdev() 
# dataset
stdev = statistics.stdev(data=[5, 10, 15, 20 ], xbar=None)

print('Standard deviation of dataset: ', stdev)
# Output:  6.454972243679028

####################################################################
## variance() 
# dataset
dataset = [1.2, 2.3, 3.4, 4.5, 5.6]
variance1 = statistics.variance(dataset)

xbar = statistics.mean(dataset)
variance2 = statistics.variance(dataset, xbar)

# dataset fraction
variance3 = statistics.variance(data_fraction)

# datasset decimal
variance4 = statistics.variance(data_decimal)

print('Variance of dataset xbar=None: ', variance1)
# Output: 3.025
print('Variance of dataset xbar=mean(dataset): ', variance2)
# Output: 3.025
print('Variance of dataset fraction: ', variance3)
# Output: 665/576
print('Variance of dataset decimal: ', variance4)
# Output: 0.09135158333333333333333333333

####################################################################
                        ## covariance() ##
# dataset x and y
x = [5, 10 , 15, 20, 25]
y = [4, 9, 14, 19, 24]
z = [1, 5, 9, 13, 17]

covariance1 = statistics.covariance(x, y)
covariance2 = statistics.covariance(x, z)

print('Covariance of dataset x and y: ', covariance1)
# Output: 62.5
print('Covariance of dataset x and z: ', covariance2)
# Output: 50.0

####################################################################
## correlation() 
x1 = [5, 10, 15, 20]
y1 = [19, 14, 9, 4]
z1 = [4, 9, 14, 19]

correlation1 = statistics.correlation(x1, y1)
correlation2 = statistics.correlation(x1, z1)

print('Correlation of dataset x1 and y1: ', correlation1)
# Output: -1
print('Correlation of dataset x1 and z1: ', correlation2)
# Output: 1

####################################################################
## linear_regression() 
x2 = [1.0, 3.8, 4.5, 10.7]
y2 = [12.34, 34.56, 56.78, 78.99]

a, b = statistics.linear_regression(x2, y2)

linear_regression1 = statistics.linear_regression(x2, data_fraction)

print('Slope (a): ', a)
# Output: 6.596671980868872
print('Intercept (b): ', b)
# Output: 12.684140095655636

####################################################################
#from_samples()
data = [5,10,15,13,25,30]
normal_dist = NormalDist.from_samples(data)
mean = normal_dist.mean
std = normal_dist.stdev
print(f"Mean of dataset: ", mean)
# Output: 16.333333333333332
print(f"Standard deviation of dataset: ", std)
# Output: 9.41629792788369

####################################################################
#samples()
#Tạo NormalDist có trung bình = 70 và độ lệch chuẩn = 3
normal_dist = NormalDist(mu=70, sigma=2)
#Tạo 3 mẫu từ NormalDist được tạo ở trên
n = 3
random_samples = normal_dist.samples(n)
print("Random Samples:", random_samples)
# Output: [69.57916784669153, 70.89855568961391, 71.7040046402573]

####################################################################
#pdf()
# Ví dụ: trung bình = 70, độ lệch chuẩn = 3
normal_dist = NormalDist(mu=70, sigma=3)  
x = 50
pdfvalue = normal_dist.pdf(x)
print(f"PDF at position {x}: {pdfvalue}")
# Output: 2.970300062450727e-11

####################################################################
#cdf()
# Ví dụ: trung bình = 70, độ lệch chuẩn = 3
normal_dist = NormalDist(mu=70, sigma=3)  
x = 50
#Tính CDF tại x =50
cdfvalue = normal_dist.pdf(x)
print(f"CDF at position {x}: {cdfvalue}")
# Output: CDF at position 50: 2.970300062450727e-11

####################################################################
#inv_cdf()
# Tạo một đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=30, sigma=5)
# Tính giá trị ngược của CDF tại p = 0.8
p = 0.8
inv_cdf = normal_dist.inv_cdf(p)
print(f"reverse values of CDF at p = {p}: {inv_cdf}")
# Output: 34.20810616786457

####################################################################
#overlap()
#Tạo hai đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist1 = NormalDist(mu= 70, sigma= 20)
normal_dist2 = NormalDist(mu= 100, sigma= 7)
# Tính độ trùng lặp giữa hai phân phối
overlap_value = normal_dist1.overlap(normal_dist2)
print("Overlap of 2 NormalDist is :", overlap_value)
# Output:  0.2232075252072392

####################################################################
#quantiles()
# Tạo đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=10, sigma=2)
# Tính 5 quantiles cho phân phối chuẩn
quantiles = normal_dist.quantiles(4)
print(quantiles)
# Output: [8.651020499607837, 10.0, 11.348979500392163]

####################################################################
#zscore()
# Tạo đối tượng NormalDist với giá trị trung bình và độ lệch chuẩn
normal_dist = NormalDist(mu=10, sigma=20)
# Tính z-score cho giá trị x = 15
x = 15
z_score = normal_dist.zscore(x)
print(f"Z-score of x = {x}: {z_score}")
# Output : 0.25
