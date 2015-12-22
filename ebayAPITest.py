from ebaysdk.finding import Connection as Finding
try:
    api = Finding(appid="Rude4e6e0-28f2-48c3-95c7-aa95b8eb2ac")
    response = api.execute('findItemsAdvanced', {'keywords': 'Python'})
    print(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())
