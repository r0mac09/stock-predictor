from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd

data_path = Path('./data/stocks')
time_format = '%Y-%m-%d'


def find_gaps(df:pd.DataFrame) -> List[Dict]:
    gaps = []

    # Intialize prev with the firs item
    prev = datetime.strptime(df.iloc[0]['Date'], time_format)

    # Iterate from the second to last row
    for i in range(1, len(df)):
        curr = datetime.strptime(df.iloc[i]['Date'], time_format)

        # Compute time difference
        delta = curr-prev

        if delta.days != 1:
            gaps.append({
                'span': delta.days,
                'start': prev,
                'end': curr,
            })
        
        # Update prev
        prev = curr
    
    return gaps


def contigous_regions(df:pd.DataFrame, gaps:List[Dict]):
    # Get the start and end date of the dataframe
    start = datetime.strptime(df.iloc[0]['Date'], time_format)
    end = datetime.strptime(df.iloc[-1]['Date'], time_format)

    chunks = []

    p_start = start

    for i in range(len(gaps)):
        p_end = gaps[i]['start']

        chunks.append({
            'span': p_end - p_start,
            'start': p_start,
            'end': p_end,
        })

        p_start = gaps[i]['end']

    chunks.append({
        'span': end - p_start,
        'start': p_start,
        'end': end,
    })

    return chunks


if __name__ == '__main__':
    print('Starting')

    for csv in data_path.glob('*.csv'):
        df = pd.read_csv(str(csv))
        gaps = find_gaps(df)
        chunks = contigous_regions(df, gaps)
        print([c for c in chunks if c['span'].days >= 7])
