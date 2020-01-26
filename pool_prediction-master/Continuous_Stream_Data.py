
# coding: utf-8

# In[1]:


import requests
import time
import datetime

f_name = input("dataset name:")
f = open(f_name,"a")
keys = ["price_usd","24h_volume_usd","market_cap_usd","available_supply","total_supply","percent_change_1h","percent_change_24h","percent_change_7d"]
vals = [0]*len(keys)

while True:
    data = requests.get("").json()[0] # data goszakupki
    bkc = requests.get("").json() # Api goszakupki
    for d in data.keys():
        if d in keys:
            indx = keys.index(d)
            vals[indx] = data[d]
    for val in vals:
        f.write(val+",")

    f.write("{},{},{}".format(bkc["USD"]["sell"],bkc["USD"]["buy"],bkc["USD"]["15m"]))
    f.write(","+datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
    f.write("\n")
    f.flush()
    time.sleep(60)

