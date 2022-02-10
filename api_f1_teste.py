## Ergast API dados da F1

import requests
import pandas as pd
import numpy as np

## Dados das corridas 
## extraindo via API e salvando na pasta data em csv

races = {'season': [],
        'round': [],
        'circuit_id': [],
        'lat': [],
        'long': [],
        'country': [],
        'date': [],
        'url': []}

for year in list(range(1950,2021)):
    
    url = 'https://ergast.com/api/f1/{}.json'
    r = requests.get(url.format(year))
    json = r.json()

    for item in json['MRData']['RaceTable']['Races']:
        try:
            races['season'].append(int(item['season']))
        except:
            races['season'].append(None)

        try:
            races['round'].append(int(item['round']))
        except:
            races['round'].append(None)

        try:
            races['circuit_id'].append(item['Circuit']['circuitId'])
        except:
            races['circuit_id'].append(None)

        try:
            races['lat'].append(float(item['Circuit']['Location']['lat']))
        except:
            races['lat'].append(None)

        try:
            races['long'].append(float(item['Circuit']['Location']['long']))
        except:
            races['long'].append(None)

        try:
            races['country'].append(item['Circuit']['Location']['country'])
        except:
            races['country'].append(None)

        try:
            races['date'].append(item['date'])
        except:
            races['date'].append(None)

        try:
            races['url'].append(item['url'])
        except:
            races['url'].append(None)
        
races = pd.DataFrame(races)

import os
if not os.path.exists('./data'):
    os.mkdir('./data')

races.to_csv('./data/races.csv', index = False)

## F1 ROUNDS
race = pd.read_csv('./data/races.csv')

rounds = []
for year in np.array(race.season.unique()):
    rounds.append([year, list(race[race.season == year]['round'])])

## F1 resultados
results = {'season': [],
          'round':[],
           'circuit_id':[],
          'driver': [],
           'date_of_birth': [],
           'nationality': [],
          'constructor': [],
          'grid': [],
          'time': [],
          'status': [],
          'points': [],
          'podium': [],
          'url': []}

for n in list(range(len(rounds))):
    for i in rounds[n][1]:
    
        url = 'http://ergast.com/api/f1/{}/{}/results.json'
        r = requests.get(url.format(rounds[n][0], i))
        json = r.json()

        try:

            for item in json['MRData']['RaceTable']['Races'][0]['Results']:
                try:
                    results['season'].append(int(json['MRData']['RaceTable']['Races'][0]['season']))
                except:
                    results['season'].append(None)

                try:
                    results['round'].append(int(json['MRData']['RaceTable']['Races'][0]['round']))
                except:
                    results['round'].append(None)

                try:
                    results['circuit_id'].append(json['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId'])
                except:
                    results['circuit_id'].append(None)

                try:
                    results['driver'].append(item['Driver']['driverId'])
                except:
                    results['driver'].append(None)

                try:
                    results['date_of_birth'].append(item['Driver']['dateOfBirth'])
                except:
                    results['date_of_birth'].append(None)

                try:
                    results['nationality'].append(item['Driver']['nationality'])
                except:
                    results['nationality'].append(None)

                try:
                    results['constructor'].append(item['Constructor']['constructorId'])
                except:
                    results['constructor'].append(None)

                try:
                    results['grid'].append(int(item['grid']))
                except:
                    results['grid'].append(None)

                try:
                    results['time'].append(int(item['Time']['millis']))
                except:
                    results['time'].append(None)

                try:
                    results['status'].append(item['status'])
                except:
                    results['status'].append(None)

                try:
                    results['points'].append(int(item['points']))
                except:
                    results['points'].append(None)

                try:
                    results['podium'].append(int(item['position']))
                except:
                    results['podium'].append(None)

                try:
                    results['url'].append(json['MRData']['RaceTable']['Races'][0]['url'])
                except:
                    results['url'].append(None)

        except:
            print(rounds[n][0], i)
            print ("Error : %s : %s " % (rounds[n][0], i))

results = pd.DataFrame(results)

results.to_csv('./data/results.csv', index = False)