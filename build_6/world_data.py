#import pandas
import pandas as pd
df = pd.read_csv("build_6/world_development_data.csv")
print(df.head()) # the title of the sheets 
print(df.describe())
print(df.shape) # no () because it's an attribute 
print(df.info())

# FILTERING: 

# ROUND 1 
# Countries where > 20% lack clean water 
water_crisis = df[df["clean_water_pct"] < 80]
print(water_crisis[["country", "clean_water_pct"]])

# How many countries where life expectancy below 60 ? 
life = df[df["life_expectancy"] < 60]
print(life[["country", "life_expectancy"]])
print(len(life)) # 13 countries have a life expectancy below 60

# Which country has the highest life expentancy, what is it? 
highest = df.loc[df["life_expectancy"].idxmax()]
print(highest[["country", "life_expectancy"]])

# How many unique regions appear in the data: 
df["region"] = df["region"].str.title().str.strip() # first clean the data
regions = df["region"].unique()
print(regions)

#ROUND 2 

# How many null values 
missing_values = df.isnull().sum()
print(len(missing_values))

#Sub suharan Africa 
ssa = df[df["region"] == "Sub Saharan Africa"]
print(ssa[["country", "region"]])

#write an assert that checks no missing values in clean_water_pct 
df["clean_water_pct"]= df["clean_water_pct"].fillna(0) 
print(df[["clean_water_pct"]])
assert df["clean_water_pct"].notna().all(), "Missing clean water data!"



