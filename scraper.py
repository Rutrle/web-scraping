"""Scrape dummy web site according to tutorial from Real Python website
"""
import requests

jobs_url = "https://realpython.github.io/fake-jobs/"

page = requests.get(jobs_url)

print(page)
# print(dir(page))

print(page.text)