import requests

# URL for the COVID-19 API
COVID_API_URL = 'https://disease.sh/v3/covid-19/countries'

def fetch_covid_data(region):
    response = requests.get(COVID_API_URL)
    if response.status_code == 200:
        data = response.json()
        for country in data:
            if country['country'].lower() == region.lower():
                return country
        return None
    else:
        print("Failed to fetch data.")
        return None

def display_covid_info(data):
    if data:
        country = data['country']
        cases = data['cases']
        recoveries = data['recovered']
        deaths = data['deaths']
        print(f"COVID-19 Statistics for {country}:")
        print(f"Total Cases: {cases}")
        print(f"Total Recoveries: {recoveries}")
        print(f"Total Deaths: {deaths}")
    else:
        print("No data available for the specified region.")

def main():
    region = input("Enter a country name to get COVID-19 statistics: ")
    covid_data = fetch_covid_data(region)
    display_covid_info(covid_data)

if __name__ == '__main__':
    main()
