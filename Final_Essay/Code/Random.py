import random
import math

X = [27,61,52,69,88,85,79,99,77,165,41,83,144,74,143,131,
    34,59,46,105,61,118,114,138,24,67,130,56,99,125,87,30,
    119,40,25,44,123,45,25,94,86,128,69,102,91,106,119,139,
    67,47,62,92,124,31,49,68,109,138,105,84,86,66,128,146,59]

S1 = [106, 119, 68, 59, 66, 88, 119, 128, 79, 94, 118, 25, 41, 34, 31, 69, 25, 44, 105, 125, 124, 59, 130, 30, 128, 24, 74, 99, 62, 61]
S2 = [86, 25, 86, 130, 79, 31, 124, 138, 67, 119, 102, 118, 49, 119, 106]

def expectation(X):
    n = len(X)
    if n == 0:
        return None
    
    expectation = sum(X) / n
    return expectation
  
def variance(X):
    n = len(X)
    if n == 0:
        return None
    
    variance = sum((xi - expectation(X)) ** 2 for xi in X) / n
    return variance

def standard_deviation(X):
    n = len(X)
    if n == 0:
        return None
    
    # Tính phương sai
    variance1 = variance(X)
    
    # Tính căn bậc hai của phương sai
    std_dev = math.sqrt(variance1)
    return std_dev

# print(len(S1))
# print(len(S2))
# print(expectation(S1))
# print(variance(S1))
print(standard_deviation(S1))

print(expectation(S2))
print(variance(S2))
print(standard_deviation(S2))


# def find_S1(X):
#   indexes = random.sample(range(len(X)), 30)
#   for i in indexes:
#     print("STT: ", i+1, end=', ') 
#     print("Lương: ", X[i])
#   print()
  
# print(find_S1(X))

# def find_S2(X):
#   indexes = random.sample(range(len(X)), 15)
#   for i in indexes:
#     print("STT: ", i+1, end=', ') 
#     print("Lương: ", X[i])
#   print()
  
# print(find_S2(X))

