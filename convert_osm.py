from pyrosm import OSM
import polars as pl
print('Loading OSM file...')
osm = OSM(filepath='./data/extract.osm.pbf')

print('Loading objects...')
buildings = osm.get_buildings()

extract = buildings[[
    'name',
    'addr:street',
    'addr:housenumber',
    'addr:postcode',
    'addr:city',
    'osm_type',
    'geometry'
]]

print('Creating a list of unique postcodes')
osm_codes = extract['addr:postcode'].str.replace(' ', '').dropna().unique()
osm_codes = sorted([int(code) for code in osm_codes])
osm_codes = [code for code in osm_codes if code > 10000 and code < 98700]
print('Saving all objects as CSV...')
pl.DataFrame({ 'postcodes': osm_codes }).write_csv('./data/osm_codes.csv')
