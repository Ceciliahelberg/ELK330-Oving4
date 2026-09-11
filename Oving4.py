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


