#!/usr/bin/env python
import os
from pprint import pprint
import requests


SLACK_TOKEN = os.environ["SLACK_TOKEN"]
SLACK_BASE_URL = "https://slack.com/api"


def main():
    # Get list of channels; authenticate with token in the header
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    resp = requests.get(f"{SLACK_BASE_URL}/channels.list", headers=headers)
    pprint(resp.json())

    print()

    # Get list of channels; authenticate with token encoded in url
    resp = requests.get(f"{SLACK_BASE_URL}/channels.list?token={SLACK_TOKEN}")
    pprint(resp.json())

    print()

    # Get list of channels; authenticate with token encoded in url
    data = {"token": SLACK_TOKEN}
    resp = requests.post(f"{SLACK_BASE_URL}/channels.list", data=data)
    pprint(resp.json())

    print()


if __name__ == "__main__":
    main()
