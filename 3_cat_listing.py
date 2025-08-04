import requests

cookies = {
    # 'ahoy_visit': 'aa3c966c-e170-4beb-9092-493e4ba55fcf',
    '__Host-instacart_sid': 'v2.3e79027b886b88.30TyIIUHJr_FFgyvvvxDSSlSZ0uSScbDf4pqFI-1kgQ',
    # 'ahoy_visitor': '6027b4c2-14d3-4705-9b0c-da7fc25ba153',
    # 'X-IC-bcx': '1',
    # '__cf_bm': 'yg8nPxaFIqpFpTyoLZrka46QGrYenter6lY16eU.QYQ-1753681802-1.0.1.1-FCk1jtWPkN1QJOOlvQbqNXxiK4BDLiXduukcF646r47abhMubiEWaojg9ndp2.A7xae8ryb3_o6_ob.SwtwAW8W2_Pn_tsrEjEhRJ5Jaz88',
    # 'build_sha': '6635375fce63ebbfff793aa6fd81fa89eed8b49f',
    # 'ajs_user_id': '17584500125494152',
    # 'ajs_anonymous_id': '998bf103-bf8e-45ad-8af1-04843e687a10',
    # 'forterToken': '54a264b863e94c88b44e965d7f6e5418_1753681806890__UDF43-mnf-a4_24ck_',
    # 'aws-waf-token': 'b858a3e5-824b-42eb-aa38-ced8551f640f:EQoAt2EpFpYNAAAA:nlbketvccMnBu+ocIBpv3aoRVXLHA+UO1XakDMxRw6Y9gHEWL7C+CuxPBFHy1HpBcLSm9MrdWskALZqVcFUu1BYDo+2+uyHXr32rHyak4VvcehuHDUU1p2zQYgpWIedjPyp1NIYo8y1mL5H9VmFjqb08J2A00+Sw+gDR31iTffOy/5TxCvZrRkhRZIc7so/XXio0iQvvLxY=',
    # '_dd_s': 'logs=0&expire=1753683018214',
    # '_instacart_session_id': 'azI1NlJObHZ0TEFybHQ0ZExvVmxDQ1pYbkVmdDhmcHJsWEg3TS85Rnd2RzRwQ0w2em1FRURZWTNOK1lyOWVjVmJHTlNuTnZYYms2T3IxQ1ZSS0luQjJvamY0NEM0VlRIZmVEMWZUaTlSSlhIR2JZeXBPbFVQWkhzZUgwOWZhUnI5akxGendTb2UrcklGZFNTbFVHS2tnPT0tLXNMZHArbi9WNVh0OWRMT2JQZFMvMnc9PQ%3D%3D--231f319cccef0bd4145885ed2def8181b9f720b1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    # 'referer': 'https://dollarama.instacart.com/store/dollarama/collections/laundry?sisid=111944',
    'referer': 'https://dollarama.instacart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'x-client-identifier': 'web',
    # 'x-page-view-id': 'cd0425dc-c105-5b87-9513-97b250fc3c7f',
    # 'cookie': 'ahoy_visit=aa3c966c-e170-4beb-9092-493e4ba55fcf; __Host-instacart_sid=v2.3e79027b886b88.30TyIIUHJr_FFgyvvvxDSSlSZ0uSScbDf4pqFI-1kgQ; ahoy_visitor=6027b4c2-14d3-4705-9b0c-da7fc25ba153; X-IC-bcx=1; __cf_bm=yg8nPxaFIqpFpTyoLZrka46QGrYenter6lY16eU.QYQ-1753681802-1.0.1.1-FCk1jtWPkN1QJOOlvQbqNXxiK4BDLiXduukcF646r47abhMubiEWaojg9ndp2.A7xae8ryb3_o6_ob.SwtwAW8W2_Pn_tsrEjEhRJ5Jaz88; build_sha=6635375fce63ebbfff793aa6fd81fa89eed8b49f; ajs_user_id=17584500125494152; ajs_anonymous_id=998bf103-bf8e-45ad-8af1-04843e687a10; forterToken=54a264b863e94c88b44e965d7f6e5418_1753681806890__UDF43-mnf-a4_24ck_; aws-waf-token=b858a3e5-824b-42eb-aa38-ced8551f640f:EQoAt2EpFpYNAAAA:nlbketvccMnBu+ocIBpv3aoRVXLHA+UO1XakDMxRw6Y9gHEWL7C+CuxPBFHy1HpBcLSm9MrdWskALZqVcFUu1BYDo+2+uyHXr32rHyak4VvcehuHDUU1p2zQYgpWIedjPyp1NIYo8y1mL5H9VmFjqb08J2A00+Sw+gDR31iTffOy/5TxCvZrRkhRZIc7so/XXio0iQvvLxY=; _dd_s=logs=0&expire=1753683018214; _instacart_session_id=azI1NlJObHZ0TEFybHQ0ZExvVmxDQ1pYbkVmdDhmcHJsWEg3TS85Rnd2RzRwQ0w2em1FRURZWTNOK1lyOWVjVmJHTlNuTnZYYms2T3IxQ1ZSS0luQjJvamY0NEM0VlRIZmVEMWZUaTlSSlhIR2JZeXBPbFVQWkhzZUgwOWZhUnI5akxGendTb2UrcklGZFNTbFVHS2tnPT0tLXNMZHArbi9WNVh0OWRMT2JQZFMvMnc9PQ%3D%3D--231f319cccef0bd4145885ed2def8181b9f720b1',
}


json_data = {
    # "retailerInventorySessionToken":"v1.d34ca7e.17584500125494152-K7C3P1-04517x17616-1-1603-140551-0-0",
    "retailerInventorySessionToken":"",
    "shopId":"111944",
    "postalCode":"K7C3P1",
    # "zoneId":"768",
    "zoneId":"",
    "slug":"laundry",
    "filters":[],
    # "pageViewId":"cd0425dc-c105-5b87-9513-97b250fc3c7f",
    "pageViewId":"",
    "itemsDisplayType":"collections_items_grid",
    "first":4,
    "pageSource":"browse"
}

params = {
    'operationName': 'CollectionProductsWithFeaturedProducts',
    'variables': '{"retailerInventorySessionToken":"v1.d34ca7e.17584500125494152-K7C3P1-04517x17616-1-1603-140551-0-0","shopId":"111944","postalCode":"K7C3P1","zoneId":"768","slug":"laundry","filters":[],"pageViewId":"cd0425dc-c105-5b87-9513-97b250fc3c7f","itemsDisplayType":"collections_items_grid","first":4,"pageSource":"browse"}',
    'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"a937542a79b428d4214c494c9c593e31dbc0ffad635b0cd5ae2fd6e85c11b5e7"}}',
}

import json
from curl_cffi import requests
import pydash as _


params['variables'] = json.dumps(json_data)

response = requests.get(
    'https://dollarama.instacart.com/graphql',
    params=params,
    cookies=cookies,
    headers=headers,
    impersonate='chrome120'
)

print(response.text)
data = response.json()
name = _.get(data, 'data.collectionProducts.items[0].name', 'N/A')
print(name)
print(response.status_code)
