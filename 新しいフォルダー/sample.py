import requests
import json

def main():
    url= "https://apitest-1-z5842447.deta.app/"
    # https://apitest-1-z5842447.deta.app/ http://127.0.0.1:8000/
    data={
        "x":3,
        "y":4
        }
    res= requests.post(url,json=data)
    print(res.json())


if __name__  =="__main__":
    main()