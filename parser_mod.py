import requests
from bs4 import BeautifulSoup

link = 'https://mosautoshina.ru/catalog/tyre/'


def take_size_grid(link):
    width_list = []
    profile_list = []
    diameter_list = []
    
    res = requests.get(url=link)
    soup = BeautifulSoup(res.text, 'lxml')
    
    width = soup.find('select', id = 'tyre_width')
    profile = soup.find('select', id = 'tyre_serial')
    diameter = soup.find('select', id = 'tyre_radial')
    
    for item in width.find_all('option'):
        val = item.get('value')
        if val != '': width_list.append(val)
    
    for item in profile.find_all('option'):
        val = item.get('value')
        if val != '': profile_list.append(val)
    
    for item in diameter.find_all('option'):
        val = item.get('value')
        if val != '': diameter_list.append(val)
    
    return width_list, profile_list, diameter_list


if __name__ == "__main__":
    v1, v2, v3 = take_size_grid(link=link)
    print(f'\n width_list: {v1} \n')
    print(f'profile_list: {v2} \n')
    print(f'diameter_list {v3} \n')
