import requests
import json
import pandas as pd
from datetime import datetime

import os
#print(os.environ.get('REQUESTS_CA_BUNDLE'))
#os.environ.pop('REQUESTS_CA_BUNDLE')

# Define arquivo de saída p/ armazenar os tweets
#data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#out = open(f"tweets_coletados_{data_hoje}.txt", "w")

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url():
    query = "@ZupInnovation"
    tweet_fields = "tweet.fields=author_id,text"
    #filters = "start_time=2022-03-16T00:00:00.00Z&end_time=2022-03-21T00:00:00.00Z"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields#, filters
    )
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers, verify=False)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def paginate(url, headers, next_token=""):
    if next_token:
        full_url = f"{url}&next_token={next_token}"
    else:
        full_url = url
    data = connect_to_endpoint(full_url, headers)
    yield data
    if "next_token" in data.get("meta", {}):
        yield from paginate(url, headers, data['meta']['next_token'])

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    results = []
    for json_response in paginate(url, headers):
        s1 = json.dumps(json_response, indent=4, sort_keys=True)
        raw = json.loads(s1)
        raw = raw.get("data")
        for i in raw:
            results.append(i)
    df = pd.json_normalize(results)
    df.to_csv('./tweets_teste.csv', index = False)
    #print(df)    
    
#dataset_principal = main()

if __name__ == "__main__":
    main()