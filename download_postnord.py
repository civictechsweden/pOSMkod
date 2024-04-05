import requests
import polars as pl
URL = 'https://www.postnord.se/api/location/get-by-location?countryCode=SE&query={}'

data = []

for i in range(100, 987):
    print(f'Fetching postcodes for {i}...')
    response = requests.get(URL.format(i))
    if response.status_code != 429:
        codes = response.json()['postalCodes']
        if codes:
            data.extend(codes)
    else:
        break

print('Saving all postcodes as a file.')
pl.DataFrame(data).write_csv('./data/postnord_codes.csv')
