import requests

url = "https://fake-credit-card-generator-json-api.p.rapidapi.com/credit-card"

headers = {
	"X-RapidAPI-Key": "fef8893570mshbcf840ca187333ep137c11jsn72c1560a96b5",
	"X-RapidAPI-Host": "fake-credit-card-generator-json-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

result = response.json()
cvv = result['cvv']
id = result['id']
cardtype = result['card_type']
expire = result['expire']
cardnumber = result['card_number']