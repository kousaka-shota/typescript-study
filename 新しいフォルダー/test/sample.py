import requests
import json


def main():
    url = "https://apitest-1-z5842447.deta.app/"
    body = {
        "x": 3,
        "y": 4
    }
    res = requests.post(url, json=body)
    print(res.json())


if __name__ == "__main__":
    main()
