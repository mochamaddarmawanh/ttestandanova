import pandas as pd
from scipy import stats

file_csv_name = input("Masukkan nama csv file: ")
df = pd.read_csv(file_csv_name)

offline = df[df['metode_pembelajaran'] == 'offline']['nilai_ujian']
online = df[df['metode_pembelajaran'] == 'online']['nilai_ujian']

# --- One Sample T-Test (dibandingkan dengan nilai 85)
t_stat, p_value = stats.ttest_1samp(offline, 85)

print("\nT TEST (Offline):\n")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# --- Tampilkan tabel offline
print("\n=== DATA OFFLINE ===")
print(df[df['metode_pembelajaran'] == 'offline'])