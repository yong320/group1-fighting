import requests
response = requests.post('http://os3-325-52268.vs.sakura.ne.jp/api/trade/start/test0/ryotaro')
session_info = response.json()
session_id = session_info['sessionId']
is_complete = session_info['complete']
request_body_next = {
    'sessionId': session_id,
    'exchangeRequests': [{
    'currencyFrom': 'JPY',
    'currencyTo': 'USD',
    'amount': 1000
    }, {
    'currencyFrom': 'JPY',
    'currencyTo': 'GBP',
    'amount': 1000 
}
]
}
while not is_complete:
    response = requests.post('http://os3-325-52268.vs.sakura.ne.jp/api/trade/next',json=request_body_next)
    next_info = response.json()
    is_complete = next_info['complete']

result = next_info['jpyBalance']
print(result)
