import requests

def main():
    choice = input("Choose r to report and s to post")

    if choice.lower().strip()=='r':
        report_event()

    elif choice.lower().strip() == 's':
        get_events()


def get_events():
    url = 'http://127.0.0.1:8001/api/reports'
    resp = requests.get(url)
    resp.raise_for_status()
    resp = resp.json()
    for r in resp:
        print(f"{r.get('description')} reported in {r.get('location').get('city')}")



def report_event():    
    desc = input('Enter description')
    city = input('Enter city to report for')
    data = {
        'description':desc,
        'location':{
            'city': city
        }
    }
    
    url = 'http://127.0.0.1:8001/api/reports'
    data = requests.post(url,json=data)
    data.raise_for_status()
    resp = data.json()

    return resp.get('id') + "reported for " + resp.get('location').get('city') 

if __name__ == '__main__':
    main()