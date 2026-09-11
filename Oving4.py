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
