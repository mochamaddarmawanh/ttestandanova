# t test
from scipy import stats

offline = [
78, 80, 82, 75, 77, 79, 81, 83, 76, 78,
80, 82, 84, 79, 77, 76, 81, 83, 85, 78,
79, 80, 82, 84, 86, 77, 75, 78, 81, 83,
82, 84, 85, 79, 77, 76, 80, 82, 83, 81,
79, 78, 77, 80, 82, 84, 85, 83, 81, 80
]

online = [
70, 72, 75, 68, 74, 73, 71, 69, 76, 72,
74, 75, 77, 73, 71, 70, 72, 74, 76, 73,
72, 71, 70, 74, 76, 78, 69, 68, 72, 74,
75, 77, 73, 71, 70, 72, 74, 76, 75, 73,
72, 70, 69, 71, 73, 75, 77, 76, 74, 72
]

t_stat, p_value = stats.ttest_1samp(offline, 80)
# t_stat, p_value = stats.ttest_ind(offline, online)

print("T TEST:")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)