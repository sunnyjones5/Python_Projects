import folium
import pandas

# read in data, split date column, clean 
data = pandas.read_csv("Meteorite_Landings.csv")
data[["Date", "Time", "AM_PM"]] = data.year.str.split(" ", expand = True)
data[["Month", "Date", "Yr"]] = data.Date.str.split("/", expand = True)
data = data.rename(columns={'mass (g)': 'Mass'})
data = data.dropna()
data.Yr = data.Yr.astype("int")



# Inititiate Map







