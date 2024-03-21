"""
Script to download data from the Plausible API.

https://plausible.io/docs/stats-api#top-pages
"""

import os

import urllib3  # pip install "urllib3>=2"

# Get your API key from https://plausible.io/settings
API_KEY = TODO_ENTER_YOUR_API_KEY
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
OUTPUT_DIR = "output"


def get_data(http: urllib3.PoolManager, prop: str) -> int:
    print(f"Getting data for {prop}")
    page = 1
    requests = 0
    while True:
        url = (
            "https://plausible.io/api/v1/stats/breakdown"
            "?site_id=docs.python.org"
            "&period=6mo"
            f"&property={prop}"
            f"&limit=1000&page={page}"
            "&metrics=visitors,pageviews,bounce_rate,visit_duration,visits,events"
        )
        resp = http.request("GET", url, headers=HEADERS)
        requests += 1
        print(page, resp.status, len(resp.json()["results"]))
        if not len(resp.json()["results"]):
            break
        output_filename = f"{OUTPUT_DIR}/{prop.replace(':', '-')}-{page:02d}.json"
        with open(output_filename, "w") as f:
            f.write(resp.data.decode())
        page += 1
    return requests


def main() -> None:
    http = urllib3.PoolManager()
    requests = 0
    os.system(f"mkdir -p {OUTPUT_DIR}")

    # https://plausible.io/docs/stats-api#properties
    for prop in (
        "event:page",
        "visit:entry_page",
        "visit:exit_page",
        "visit:source",
        "visit:referrer",
        "visit:utm_medium",
        "visit:utm_source",
        "visit:utm_campaign",
        "visit:utm_content",
        "visit:utm_term",
        "visit:device",
        "visit:browser",
        "visit:browser_version",
        "visit:os",
        "visit:os_version",
        "visit:country",
        "visit:region",
        "visit:city",
    ):
        requests += get_data(http, prop)

    print(f"Total requests made: {requests}")


if __name__ == "__main__":
    main()
