def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

# T-Test
def ttest_ind_manual(group1, group2):
    n1, n2 = len(group1), len(group2)

    mean1, mean2 = mean(group1), mean(group2)
    var1, var2 = variance(group1), variance(group2)

    numerator = mean1 - mean2
    denominator = ((var1 / n1) + (var2 / n2)) ** 0.5

    t_stat = numerator / denominator
    return t_stat

# ANOVA
def f_oneway_manual(*groups):
    k = len(groups)  # jumlah grup
    all_data = [x for group in groups for x in group]
    N = len(all_data)

    grand_mean = mean(all_data)

    # SSB (Between)
    ssb = 0
    for group in groups:
        n = len(group)
        m = mean(group)
        ssb += n * (m - grand_mean) ** 2

    # SSW (Within)
    ssw = 0
    for group in groups:
        m = mean(group)
        for x in group:
            ssw += (x - m) ** 2

    # Degree of freedom
    dfb = k - 1
    dfw = N - k

    # Mean square
    msb = ssb / dfb
    msw = ssw / dfw

    # F-statistic
    f_stat = msb / msw

    return f_stat

# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------

group_a = [70, 70, 70, 70, 70]
group_b = [70, 70, 70, 70, 70]
group_c = [70, 70, 80, 70, 70]

# T-Test (contoh A vs C)
t_stat = ttest_ind_manual(group_a, group_c)
print("T-Statistic:", t_stat)

# ANOVA
f_stat = f_oneway_manual(group_a, group_b, group_c)
print("F-Statistic:", f_stat)