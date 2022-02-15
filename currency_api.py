from locale import currency
import requests
import json



response = requests.get('https://any.ge/currency/api.php?info=yvela&fbclid=IwAR2oIXPWQoDNjVkj9zADQukl0HeA08WehIpN6MsH8OIMtBLFFBGnWukIvVU')



def jprint(obj):
    text = json.dumps(obj, sort_keys=True,indent=5)
    return text

pass_times = response.json()['currency']
jprint(pass_times)

cur = {}



for item in pass_times:
    cur[item['cur_code']]=item['cur_value']


# print(cur)
main_dict={}
for currency_code ,rate_valley in cur.items():
    if currency_code=="USD":
        main_dict[currency_code]=rate_valley
    elif currency_code=="GBP":
        main_dict[currency_code]=rate_valley
    elif currency_code=="EUR":
        main_dict[currency_code]=rate_valley
    elif currency_code=="TRY":
        main_dict[currency_code]=rate_valley
    elif currency_code =="CHF":
        main_dict[currency_code]=rate_valley






# ***********************
