import datetime
# import ebaysdk
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

try:
    api = Connection(appid='JeffreyC-Streetwe-PRD-f2f871c7c-922e659d', config_file=None)
    response = api.execute('findCompletedItems', {'keywords': 'supreme arc logo crewneck'})

    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    for i in response.reply.searchResult.item:
        print i
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)

except ConnectionError as e:
    print(e)
    print(e.response.dict())