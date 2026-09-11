import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Leser inn CSV-filen
df = pd.read_csv("load_data.csv")

# Endrer datatype til datetime og setter "Time(UTC)" som indeks
df["Time(UTC)"] = pd.to_datetime(df["Time(Local)"], format="%d.%m.%Y %H:%M:%S %z", utc=True)
df = df.set_index("Time(UTC)")
# Gjør om kolonnene "Production" og "Consumption" til float
df["Production"] = df["Production"].str.replace(",", ".").astype(float)
df["Consumption"] = df["Consumption"].str.replace(",", ".").astype(float)

# Oppgave 4
print(df.head())

# Oppgave 5
print(df.index[0])

# Oppgave 6
print(df.loc["2026-01-01 03:00"])

# Henter ut last data for et døgn (9.mars)
døgn = df.loc["2026-03-09 00:00":"2026-03-09 23:00", ["Consumption"]]
print(døgn)

plot = døgn.plot(figsize=(10, 6), color="hotpink")
plt.title("Consumption on March 9, 2026")
plt.xlabel("Time")
plt.ylabel("Consumption")
plt.grid(True)
plt.savefig(r"C:\repos\ELK330-Oving4\oppgave6.png")
plt.show()

# Oppgave 7
# Ny kolonne med netto rpoduksjon (Production - Consumption)
df["Netto"] = df["Production"] - df["Consumption"]

# Oppgave 8
# maksimal produksjon
max_produksjon = df["Production"].max()
max_produksjon_time = df["Production"].idxmax()
# minimal produksjon
min_produksjon = df["Production"].min()
min_produksjon_time = df["Production"].idxmin()
# gjennomsnittlig produksjon
mean_produksjon = df["Production"].mean()
# skriver ut resultatene
print(f"Max produksjon: {max_produksjon:.2f}, Time: {max_produksjon_time}")
print(f"Min produksjon: {min_produksjon:.2f}, Time: {min_produksjon_time}")
print(f"Mean produksjon: {mean_produksjon:.2f}")

# Oppgave 9
# maksimal netto produksjon
max_netto = df["Netto"].max()
max_netto_time = df["Netto"].idxmax()
# minimal netto produksjon
min_netto = df["Netto"].min()
min_netto_time = df["Netto"].idxmin()
# skriver ut resultatene
print(f"Max netto produksjon: {max_netto:.2f}, Time: {max_netto_time}")
print(f"Min netto produksjon: {min_netto:.2f}, Time: {min_netto_time}")

# Oppgave 10
total_production = df["Production"].sum()
print(f"Total produksjon: {total_production:.2f}")
