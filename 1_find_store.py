
cookies = {
    'forterToken': '54a264b863e94c88b44e965d7f6e5418_1753679805346__UDF43-m4_24ck_',
    'aws-waf-token': 'b858a3e5-824b-42eb-aa38-ced8551f640f:EQoAhgskEe6EAAAA:bdcoxMqDnXlI8qUmMMejhhFXUdpnrOnsbKBzY4Oews3ALyYEi1+kjl4u7JlBAbHuathpfQESfeyw+vnondzprG2nH0nN0xD4LSdXubjpTiN4szBrnPOE8bLArPHaIwB/UAT/PozScWaZCZKRbuWlVd/9zD7rHFuJOsgvTbvuwtk8cpLxrYGuRstqaAfyvK4P3ja60lZdptI=',
    '__cf_bm': '3ASIClDa0dj6FfM.rU6LNLvk.fPgY0CxFrwVd3TCgeE-1753680174-1.0.1.1-.GLwKePMPLANvR5FzuMaUoJVa61oAj2coH9caaW0OVBuqMpUZQjlpWNgg4HwGqn3CkyWwO9.gpIIdiInRbXD2xV0KpK3TgysSth8ooW3psg',
    '_dd_s': 'logs=0&expire=1753681132460',
    'ahoy_visit': '0527c9e0-630c-4930-8a2c-9ad3882e674e',
    'ahoy_visitor': '357e23d7-28b4-4998-a750-4237f4f48bd0',
    'build_sha': '6635375fce63ebbfff793aa6fd81fa89eed8b49f',
    '_instacart_session_id': 'QURqbmxrVkU3NTUrejNaVVBGWU5lelNJMTNDVXo5amg4NDZBTEViQ0kveDBCWnBQLzhKYko4emlZS0tjNlNTT1BRTmUvYXhxQ2RicUVFRGNBSzFlcnV0VkRtR1llNHFqd25xWURNZTk1SmdnYjN4UmZhOXNPajZNSm1kOGRUWDUxd1dSbVJta29mNHFlU0NUc1dudGp3PT0tLXpSbThGYVBUdUlRQTYvbHRPK09rQVE9PQ%3D%3D--354dafd9a40785f3ae2327414662f7af34a5d0bd',
    'ajs_anonymous_id': '2184ae84-39f8-4a0c-85e7-dd9baa23f24f',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dollarama.instacart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-client-identifier': 'web',
    # 'cookie': 'forterToken=54a264b863e94c88b44e965d7f6e5418_1753679805346__UDF43-m4_24ck_; aws-waf-token=b858a3e5-824b-42eb-aa38-ced8551f640f:EQoAhgskEe6EAAAA:bdcoxMqDnXlI8qUmMMejhhFXUdpnrOnsbKBzY4Oews3ALyYEi1+kjl4u7JlBAbHuathpfQESfeyw+vnondzprG2nH0nN0xD4LSdXubjpTiN4szBrnPOE8bLArPHaIwB/UAT/PozScWaZCZKRbuWlVd/9zD7rHFuJOsgvTbvuwtk8cpLxrYGuRstqaAfyvK4P3ja60lZdptI=; __cf_bm=3ASIClDa0dj6FfM.rU6LNLvk.fPgY0CxFrwVd3TCgeE-1753680174-1.0.1.1-.GLwKePMPLANvR5FzuMaUoJVa61oAj2coH9caaW0OVBuqMpUZQjlpWNgg4HwGqn3CkyWwO9.gpIIdiInRbXD2xV0KpK3TgysSth8ooW3psg; _dd_s=logs=0&expire=1753681132460; ahoy_visit=0527c9e0-630c-4930-8a2c-9ad3882e674e; ahoy_visitor=357e23d7-28b4-4998-a750-4237f4f48bd0; build_sha=6635375fce63ebbfff793aa6fd81fa89eed8b49f; _instacart_session_id=QURqbmxrVkU3NTUrejNaVVBGWU5lelNJMTNDVXo5amg4NDZBTEViQ0kveDBCWnBQLzhKYko4emlZS0tjNlNTT1BRTmUvYXhxQ2RicUVFRGNBSzFlcnV0VkRtR1llNHFqd25xWURNZTk1SmdnYjN4UmZhOXNPajZNSm1kOGRUWDUxd1dSbVJta29mNHFlU0NUc1dudGp3PT0tLXpSbThGYVBUdUlRQTYvbHRPK09rQVE9PQ%3D%3D--354dafd9a40785f3ae2327414662f7af34a5d0bd; ajs_anonymous_id=2184ae84-39f8-4a0c-85e7-dd9baa23f24f',
}

params = {
    'operationName': 'HomepagePbiAutoCompleteLocations',
    'variables': '{"query":"toronto"}',
    'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"145bef7e4a9f2733239c4e1a5ded06c55e39502047153b53c756907d1c0c7146"}}',
}

from curl_cffi import requests
import pydash as _

for itr in range(1, 11):


    response = requests.get(
        'https://dollarama.instacart.com/graphql',
        params=params,
        # cookies=cookies,
        headers=headers
    )


    data = response.json()
    address = _.get(data, 'data.autocompleteLocations.locations[0].streetAddress', 'N/A')
    latitude = _.get(data, 'data.autocompleteLocations.locations[0].coordinates.latitude', 'N/A')
    longitude = _.get(data, 'data.autocompleteLocations.locations[0].coordinates.longitude', 'N/A')
    print(address)
    print(latitude)
    print(longitude)
    print(response.status_code)
    print('\n')




