import requests

# Replace with your actual API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
TRAFFIC_API_URL = 'https://maps.googleapis.com/maps/api/directions/json'

def fetch_traffic_data(start_point, end_point):
    params = {
        'origin': start_point,
        'destination': end_point,
        'key': API_KEY,
        'departure_time': 'now'
    }
    response = requests.get(TRAFFIC_API_URL, params=params)
    return response.json()

def display_traffic_info(data):
    if data['status'] == 'OK':
        route = data['routes'][0]
        legs = route['legs'][0]
        print(f"Start Address: {legs['start_address']}")
        print(f"End Address: {legs['end_address']}")
        print(f"Duration: {legs['duration']['text']}")
        print(f"Distance: {legs['distance']['text']}")
        if 'steps' in legs:
            print("\nRoute Details:")
            for step in legs['steps']:
                print(f"- {step['html_instructions']} ({step['distance']['text']})")
        print("\nAlternative Routes:")
        for alternative in data.get('routes', [])[1:]:
            print(f"Alternative: {alternative['summary']}")
    else:
        print("Error fetching data:", data['status'])

def main():
    start_point = input("Enter starting point (e.g., 'New York, NY'): ")
    end_point = input("Enter destination (e.g., 'Los Angeles, CA'): ")
    
    traffic_data = fetch_traffic_data(start_point, end_point)
    display_traffic_info(traffic_data)

if __name__ == '__main__':
    main()
