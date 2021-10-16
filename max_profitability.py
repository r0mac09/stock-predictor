from pathlib import Path
import pandas as pd

from src.consts import data_path


def max_profitability(df:pd.DataFrame, funds:float=100.0):
    for _, row in df.iterrows():
        funds *= row['High']/row['Low']

    return funds


# TO DO
# Compute the average per month


if __name__ == '__main__':
    for csv in data_path.glob('*.csv'):
        df = pd.read_csv(str(csv))
        print(f'{str(csv)}: {max_profitability(df)}')
