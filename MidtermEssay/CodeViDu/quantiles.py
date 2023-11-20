import statistics

# Tham số đầu vào
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Tính giá trị  phân vị
quantiles = statistics.quantiles(data, n=4, method='exclusive')

# In giá trị phân vị
print("Giá trị các phân vị: ", quantiles)


