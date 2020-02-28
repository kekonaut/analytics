import requests

api_key = '2849f3bc-8518-478d-8b0b-58d66b22847e'
address = "Шоколадница"


def get_url(api_key, address):
    """Получаем адрес согласно шаблону при помощи API-key и заданного текста"""
    url = "https://geocode-maps.yandex.ru/1.x/?apikey=" + api_key + "&format=json&geocode=" + address.replace(' ', '+')
    print(url)
    return url


def place(api_key, address):
    """Делаем get-запрос с ответом в формате json. Открываем его и находим упоминания всех городов, сел и тд, в которых есть наше место.
    Некоторые города могут быть показаны несколько раз, если там есть несколько мест с одинаковой составляющей.
    Например, если текст = Тверская 7, то Москва будет показана 2 раза, т.к. есть улица Тверская и 1 Тверская-ямская, где есть еще 7 дом"""
    url = get_url(api_key, address)
    response = requests.get(url)
    for item in response.json()['response']['GeoObjectCollection']['featureMember']:
        print(item)
        list = item['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
        for new_item in list:
            if new_item['kind'] == 'locality':
                print(new_item)
                return new_item['name']


def org_place(address):
    """То же, но с апи поиска по организациям"""
    url = "https://search-maps.yandex.ru/v1/?text=" + address.replace(' ',
                                                                      '+') + '&lang=ru_RU&apikey=' + 'd1dbdea9-2174-4f9b-88f5-a8926e1773ea'
    response = requests.get(url)
    for feature in response.json()['features']:
        print(feature['properties']['CompanyMetaData']['address'])
        return feature['properties']['CompanyMetaData']['address']

org_place(address)
