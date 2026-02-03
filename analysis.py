
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)

df = pd.read_csv("persona3.csv")


## KISIM-1

df.head()
df.shape
type(df)
df.dtypes
df["COUNTRY"].nunique()
df["SOURCE"].nunique()
df["SEX"].nunique()


## KISIM-2

df[df["PRICE"]>0]
df.reset_index()



## KISIM-3

df["AGE_GROUP"] = pd.cut(df["AGE"],bins=[0,18,25,35,50,100],labels=["0-18","19-25","26-35","36-50","51+"])
df["PRICE_LEVEL"]= pd.cut(df["PRICE"],bins=[0,30,70,120],labels=["LOW","MEDIUM","HIGH"])
df["USER_PROFILE"] = (
    df["COUNTRY"].str.upper() + "_" +
    df["SOURCE"].str.upper() + "_" +
    df["SEX"].str.upper()
)

## KISIM-4

avg_price_country = df.groupby("COUNTRY")["PRICE"].mean().reset_index()
avg_age_source = df.groupby("SOURCE")["AGE"].mean().reset_index()
user_count_sex = df.groupby("SEX")["SEX"].count().reset_index(name="say")
user_count_country_sex = df.groupby(["COUNTRY","SEX"])["SEX"].count().reset_index(name="say2")
price_stats_age = df.groupby("AGE")["PRICE"].agg(["max","min","mean"]).reset_index()
highest_avg_age = df.groupby("AGE")["PRICE"].mean().sort_values().tail(1)

df.head()

df.to_csv("cleaned_persona3.csv")

with pd.ExcelWriter("outputs/summary.xlsx") as writer:
    avg_price_country.to_excel(writer, sheet_name="Avg_Price_By_Country", index=False)
    avg_age_source.to_excel(writer, sheet_name="Avg_Age_By_Source", index=False)
    user_count_sex.to_excel(writer, sheet_name="User_Count_By_Sex", index=False)
    user_count_country_sex.to_excel(writer, sheet_name="User_Count_Country_Sex", index=False)
    price_stats_age.to_excel(writer, sheet_name="Price_Stats_By_Age", index=False)
    highest_avg_age.to_excel(writer, sheet_name="Highest_Avg_Price_Age", index=False)
