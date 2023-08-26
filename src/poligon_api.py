# imports
import pandas as pd
import requests

# custom imports
from .helper import retry



@retry(ConnectionRefusedError, delay=60, tries=5)
def _get(url):
    r = requests.get(url)
    if r.status_code == 429:
        raise ConnectionRefusedError
    return r.json()


def get_data(ticker, mult, timespan, start, end, API_KEY):
    # request data
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{mult}/{timespan}/{start}/{end}?adjusted=true&sort=asc&apiKey={API_KEY}'
    data = pd.DataFrame()

    # iter over pages
    while True:
        # make request
        r = _get(url)

        # parse data
        df = pd.DataFrame(r['results'])
        data = pd.concat([data, df])

        # break condition
        if 'next_url' not in r:
            break

        # i++
        url = r['next_url']
        url += f'&apiKey={API_KEY}'

    # format data
    data = data.rename(columns={
        't': 'date',
        'o': 'open',
        'h': 'high',
        'l': 'low',
        'c': 'close',
        'v': 'volume',
    })
    data['date'] = pd.to_datetime(data['date'], unit='ms')
    data['ticker'] = ticker
    data = data[['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']]

    return data
