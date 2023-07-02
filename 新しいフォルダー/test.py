import requests

def main():
    url='http://127.0.0.1:8000/item/'
    body={
          "name": "string",
          "description": "string",
           "price": 0,
           "tax": 0
           }
    res = requests.post(url,body)
    print(res.json())

if __name__ == "__main__":
    main()
