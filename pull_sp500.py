from pathlib import Path

import yfinance as yf
from tqdm import tqdm

from src.consts import SP500

if __name__ == '__main__':
    target_folder = Path('./data/stocks')

    # Create the folder to save data to if it doesn't exist
    target_folder.mkdir(parents=True, exist_ok=True)

    for token in tqdm(SP500):
        ticker = yf.Ticker(token)

        # Try to collect everything there is for that token
        stocks_df = ticker.history(period='max')

        # Check wether dataframe is empty r has less than 100 rows
        if stocks_df.empty or stocks_df.shape[0] < 100:
            continue

        stocks_df.to_csv(str(target_folder / f'{token}.csv'))
