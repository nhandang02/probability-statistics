import numpy as np

from scipy.stats import t

luong_mau = [106, 119, 68, 59, 66, 88, 119, 128, 79, 94, 118, 25, 41, 34, 31, 69, 25, 44, 105, 125, 124, 59, 130, 30, 128, 24, 74, 99, 62, 61]

mean_luong = np.mean(luong_mau)
print(mean_luong)
std_luong = np.std(luong_mau, ddof=1)
print(std_luong)
alpha_80 = 0.2
t_alpha_80 = t.ppf(1 - alpha_80 / 2, df=len(luong_mau) - 1)

L_80 = mean_luong - t_alpha_80 * std_luong / np.sqrt(len(luong_mau))
U_80 = mean_luong + t_alpha_80 * std_luong / np.sqrt(len(luong_mau))

alpha_95 = 0.05
t_alpha_95 = t.ppf(1 - alpha_95 / 2, df=len(luong_mau) - 1)

L_95 = mean_luong - t_alpha_95 * std_luong / np.sqrt(len(luong_mau))
U_95 = mean_luong + t_alpha_95 * std_luong / np.sqrt(len(luong_mau))

print(f'Khoảng tin cậy 80%: ({L_80:}, {U_80:}) X00,000 VND')
print(f'Khoảng tin cậy 95%: ({L_95:}, {U_95:}) X00,000 VND')