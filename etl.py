import pandas as pd
import constants

def staging(path: str)-> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def transform(df: pd.DataFrame, columns: list)-> pd.DataFrame:
    df = df.rename(columns = constants.column_change, inplace=True)
    return df

df= staging("zomato.csv")

zomato = transform(df, constants.column_list)

print(df.head(10))

