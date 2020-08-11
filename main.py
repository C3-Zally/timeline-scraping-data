import json
import urllib.request
from io import StringIO

def get_flag():
    ''' Get flags URLs '''

    FLAGS_URLS = 'https://restcountries.eu/rest/v2/all'
    response_flags = urllib.request.urlopen(FLAGS_URLS)
    flags = json.loads(response_flags.read())

    return flags


def get_data():
    ''' Download json data from https://covidatlas.com/data '''

    URL = 'https://liproduction-reportsbucket-bhk8fnhv1s76.s3-us-west-1.amazonaws.com/v1/latest/timeseries-byLocation.json'
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())

    return data


def clean_data():
    ''' Clean data and get the output '''
    flags = get_flag()
    data = get_data()

    covid_data = {}
    covid_data['data'] = []

    for input_data in data:
        if input_data['level'] == 'country':
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

                input_data['flag']=''

                for flag in flags:
                    if flag['alpha2Code'] == input_data['name']:
                        input_data['flag'] = flag['flag']

                covid_data['data'].append(input_data)

    return covid_data


def run():
    ''' Get timeline covid data '''

    countries_data = clean_data()

    with open('data.json', 'w') as outfile:
        json.dump(countries_data, outfile)


if __name__ == "__main__":
    run()
