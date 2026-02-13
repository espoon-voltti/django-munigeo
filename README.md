# django-munigeo (Voltti fork)

This is the Espoon Voltti fork of [django-munigeo](https://github.com/City-of-Helsinki/django-munigeo), based on the 0.2.x line.

The upstream 0.3.x line diverged early from 0.2.x with no upgrade path, so this fork maintains compatibility with modern Django (5.x), Python (3.14+), and other ecosystem packages while staying on the 0.2.x API.

**Primary branch:** `voltti`

---

`munigeo` is a reusable Django application for storing and accessing
municipality-related geospatial data. It can manage following categories of
data:
* Municipalities as containers of everything below
* Administrative divisions (with parent-child relationships and links to Municipalities)
* Streets and address locations on those Streets
* Buildings with 2D-geometries and addresses
* PoIs (Points of Interest) with location and type

If you are using Django Rest Framework (DRF), munigeo also provides you with serializers
for including these in your API.

For actually getting the data into your database application, munigeo provides importer
framework. Currently we only have actual importers for City of Helsinki, but
other are welcome.

## Requirements
Application requires that Django 3 and GDAL 3 are installed beforehand.

## Usage
Install this to your project with `pip install django-munigeo`,
add `munigeo` to your `INSTALLED_APPS` setting.

### Helsinki example
Before you can get Helsinki, you will need the data for Finland first:
```
python manage.py geo_import finland --municipalities
```
then
```
python manage.py geo_import helsinki --divisions
```
