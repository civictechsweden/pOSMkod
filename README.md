# pOSMkod

pOSMkod is a set of scripts to download Swedish postal code (*postkod*) data from OpenStreetMap (OSM, hence the name)

## What does it do?

A [first script](./download_postnord.py) downloads a updated list of all Swedish postal codes from one of Postnord's private APIs. This script is run every month using a [Github Action](.github/workflows/download_postnord.yml) and the data is pushed to the file [postnord_codes.csv](data/postnord_codes.csv).

[Another Github action](.github/workflows/download_osm.yml) downloads a dump of all Swedish data on OpenStreetMap and extracts all the objects that contain the `addr:postcode` property. It is run every month in the same way and the data is saved to the file [osm_codes.csv](data/osm_codes.csv).

These two lists are compared in order to see what proportion of the postal codes are present on OSM.

In the future, another script will attempt to draw boundaries for each postal code based on the objects associated to it.

## Prerequisites

This code has been designed to run using Github Actions but it is perfectly possible to run it locally.
You will need a recent version of Python (at least 3.9). You can install all its dependencies using:

```bash
pip install -r requirements.txt
```

In order to extract objects from an OSM data dump, you will need osmium, which can be install on Linux with:

```bash
apt install osmium-tool
```

## How to use

The first script can then be run using:

```bash
python download_postnord.py
```

To download OSM data, you can simply use wget:

```bash
wget https://download.geofabrik.de/europe/sweden-latest.osm.pbf -O ./data/sweden-latest.osm.pbf
```

When that is done, you can use [osmium](https://osmcode.org/osmium-tool/) to extract the only objects we need:

```bash
osmium tags-filter ./data/sweden-latest.osm.pbf nwr/addr:postcode -o ./data/extract.osm.pbf
```

Finally, the second python script will extract data from the .pbf file and save it as a table.

```bash
python convert_osm.py
```

## License

This code is licensed under AGPLv3.

The postal code data extracted from OpenStreetMap is licensed under [ODbl](https://www.openstreetmap.org/copyright). The license for Postnord's data is unclear.
