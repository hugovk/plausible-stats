"""
Script to process the data downloaded from the Plausible API via plausible-get.py.
# https://plausible.io/docs/stats-api
"""

import json
from collections import Counter
from pathlib import Path

from rich import print

pages = Counter()
first_dirs = Counter()
junk = []

filenames = Path("2023-08-10-1925").glob("event-page*.json")

for filename in filenames:
    with open(filename) as json_file:
        data = json.load(json_file)
        for entry in data["results"]:
            page = entry["page"]
            visitors = entry["visitors"]

            parts = page.split("/")
            # if parts == ["blank"]:
            #     print(filename)
            try:
                first_dir = parts[1]
                pages[page] = visitors
                first_dirs[first_dir] += visitors
            except IndexError:
                junk.append(entry)

# print(f"{junk=}")

print(f"{len(pages)} total pages\n")

print("Top pages:")
for i, page_count in enumerate(pages.most_common(10)):
    page, count = page_count
    print(f"{i}\t{page}\t{count:,}")
print()

print("Top RST pages (sorted):")
urls = []
for url, _ in pages.most_common(10):
    if url.endswith(".html"):
        url = url.replace(".html", ".rst")
        urls.append("Doc/" + "/".join(url.split("/")[2:]))
for url in sorted(urls):
    print(url)
print()


print("Top initial directories:")
for first_dir, visitors in first_dirs.most_common(10):
    print(f"{first_dir}\t{visitors:>15,}")
print()

print(f"{first_dirs.total():,} initial directories\n")

print("Top FAQs:")
total = 0
for page, visitors in pages.items():
    if page.startswith("/3/faq"):
        print(f"{page}\t{visitors:>15,}")
        total += visitors
print(total)
