import requests
import json

def main():
    url="http://127.0.0.1:8000/Data/"
    body={
  "ShopInfo": {
    "name": "string",
    "location": "string"
  },
  "items": [
    {
      "name": "staaaaa",
      "description": "string",
      "price": 0,
      "tax": 0
    }
  ]
}
    res=requests.post(url,json.dumps(body))
    print(res.json())

if __name__ =="__main__":
    main()