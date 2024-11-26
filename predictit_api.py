import requests
import json


class PredictitAPI:

    def __init__(self, market_id = 'all'):
        
        self.market_id = market_id
    
        if self.market_id == 'all':
            self.url = 'https://www.predictit.org/api/marketdata/all/'
        else:
            self.url = f'https://www.predictit.org/api/marketdata/markets/{market_id}'

    def download_data(self, file_name = 'predictit_data.json'):
        response = requests.get(self.url)
        json_data = response.json()

        with open(file_name, 'w', encoding = 'utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    
    api = PredictitAPI()

    api.download_data()