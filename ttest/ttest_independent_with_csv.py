import pandas as pd
from scipy import stats

file_csv_name = input("Masukkan nama csv file: ")
df = pd.read_csv(file_csv_name)

offline = df[df['metode_pembelajaran'] == 'offline']['nilai_ujian']
online = df[df['metode_pembelajaran'] == 'online']['nilai_ujian']
hybrid = df[df['metode_pembelajaran'] == 'hybrid']['nilai_ujian']

print("\n============= PERBANDINGAN OFFLINE VS ONLINE =============\n")

# --- Independent T-Test (offline vs online)
t_stat, p_value = stats.ttest_ind(offline, online)

print("\nINDEPENDENT T TEST (Offline vs Online):\n")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# --- Tampilkan tabel offline
print("\n=== DATA OFFLINE ===")
print(df[df['metode_pembelajaran'] == 'offline'])

# --- Tampilkan tabel online
print("\n=== DATA ONLINE ===")
print(df[df['metode_pembelajaran'] == 'online'])

print("\n============= PERBANDINGAN OFFLINE VS HYBRID =============\n")

# --- Independent T-Test (offline vs online)
t_stat, p_value = stats.ttest_ind(offline, hybrid)

print("\nINDEPENDENT T TEST (Offline vs Hybrid):\n")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# --- Tampilkan tabel offline
print("\n=== DATA OFFLINE ===")
print(df[df['metode_pembelajaran'] == 'offline'])

# --- Tampilkan tabel hybrid
print("\n=== DATA HYBRID ===")
print(df[df['metode_pembelajaran'] == 'hybrid'])

print("\n============= PERBANDINGAN ONLINE VS HYBRID =============\n")

# --- Independent T-Test (online vs online)
t_stat, p_value = stats.ttest_ind(online, hybrid)

print("\nINDEPENDENT T TEST (Online vs Hybrid):\n")
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# --- Tampilkan tabel online
print("\n=== DATA ONLINE ===")
print(df[df['metode_pembelajaran'] == 'online'])

# --- Tampilkan tabel hybrid
print("\n=== DATA HYBRID ===")
print(df[df['metode_pembelajaran'] == 'hybrid'])

print("\n============= SELESAI =============\n")