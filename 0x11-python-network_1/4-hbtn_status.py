#!/usr/bin/python3
"""
Python script that fetches a URL using the requests package
"""
import requests


def main():
    """
    Fetches URL using the requests package
    """

    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    body_response = {
        "type": str(type(response.text)),
        "content": response.text
    }

    print("Body response:")
    print("\t- type:", body_response["type"])
    print("\t- content:", body_response["content"])


if __name__ == "__main__":
    main()
