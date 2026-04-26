import pandas as pd
from scipy import stats

file_csv_name = input("Masukkan nama csv file: ")
df = pd.read_csv(file_csv_name)

offline = df[df['metode_pembelajaran'] == 'offline']['nilai_ujian']
online = df[df['metode_pembelajaran'] == 'online']['nilai_ujian']
hybrid = df[df['metode_pembelajaran'] == 'hybrid']['nilai_ujian']

print("\n============= PERBANDINGAN OFFLINE VS ONLINE VS HYBRID =============\n")

f_stat, p_value = stats.f_oneway(offline, online, hybrid)

print("\nANOVA (Offline vs Online VS HYBRID):\n")
print("F-Statistic:", f_stat)
print("P-Value:", p_value)

# --- Tampilkan tabel offline
print("\n=== DATA OFFLINE ===")
print(df[df['metode_pembelajaran'] == 'offline'])

# --- Tampilkan tabel online
print("\n=== DATA ONLINE ===")
print(df[df['metode_pembelajaran'] == 'online'])

# --- Tampilkan tabel hybrid
print("\n=== DATA HYBRID ===")
print(df[df['metode_pembelajaran'] == 'hybrid'])

print("\n============= SELESAI =============\n")