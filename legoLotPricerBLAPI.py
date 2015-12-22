import requests
from random import randint
import random
import hmac

consumer_secret = '51AC9F0EE20245F4A0452E30EE0319AE'

token_secret = '14A648771EE74936AA068B684A96338B'

key = bytearray(consumer_secret + token_secret, 'UTF-8')


#print ('signature = ' + (str)hmac.new(key))


rand_int = str(randint(0, 10000000000))

oauth_nonce = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
print (oauth_nonce)
query_params = { 'Authorization': 'OAuth',
                 'realm': "",
                 'oauth_version' : "1.0",
                 'oauth_consumer_key' : '7C254AD6679343A48D6D02FB8BF8B0B9',
                 'oauth_token': "42F02CB3E206462682E5BB3C41145A76" ,
                 'oauth_timestamp' : rand_int,
                 'oauth_nonce' : oauth_nonce,
                 'oauth_signature_method' : "HMAC-SHA1",
                 'oauth_signature' : "ig43bZXJY5t1wfuEeEUxCQHEw/M="
                 }

r = requests.get("https://api.bricklink.com/api/store/v1/orders?direction=in", params = query_params)

print()
print (rand_int)

print(r.url)
print()
print (r.text)






