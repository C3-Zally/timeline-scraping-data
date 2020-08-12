import os
import json
import urllib.request
from io import StringIO

DEBUG = True

def get_flag():
    ''' Get flags URLs '''
    response = []
    if DEBUG:
        with open('data/countries-info.json') as file:
            response = json.loads(file.read())
    else:
        FLAGS_URLS = 'https://restcountries.eu/rest/v2/all'
        response_flags = urllib.request.urlopen(FLAGS_URLS)
        response = json.loads(response_flags.read())
    return response


def get_data():
    ''' Download json data from https://covidatlas.com/data '''
    response = []
    if DEBUG:
        with open('data/timeseries.json') as file:
            response = json.loads(file.read())
    else:
        URL = 'https://liproduction-reportsbucket-bhk8fnhv1s76.s3-us-west-1.amazonaws.com/v1/latest/timeseries-byLocation.json'
        response = urllib.request.urlopen(URL)
        response = json.loads(response.read())
    return response


def clean_data():
    ''' Clean data and get the output '''
    # Get Data
    flags = get_flag()
    data = get_data()
    # Init variables
    covid_data = {}
    covid_data['data'] = []
    # Get Countries Data
    map_object = list(filter(lambda input_data: input_data['level'] == 'country' , data))

    # Filter Info
    for input_data in map_object:
        name = input_data['name']
        if not name.startswith("Unassigned"):
            input_data.pop('level')
            input_data.pop('countryID')
            input_data.pop('tz')
            input_data.pop('slug')
            input_data.pop('locationID')
            input_data.pop('maintainers')
            input_data.pop('links')
            input_data.pop('dateSources')
            input_data.pop('sources')
            # Set Attribute Flag
            input_data['flag'] = ''
            flag = list(filter(lambda flag: flag['alpha2Code'] == name, flags))
            if flag:
                input_data['flag'] = flag.pop()['flag']
            # Add Info
            covid_data['data'].append(input_data)
    # Response Data
    return covid_data


def run():
    ''' Get timeline covid data '''
    folder = 'dist'
    countries_data = clean_data()
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Write Data
    with open(f'{folder}/data.json', 'w+') as outfile:
        json.dump(countries_data, outfile)


if __name__ == "__main__":
    run()
