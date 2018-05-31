__author__ = 'mudit'

import requests
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# It functions as extracting the tree and its components with xpath
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

class lxmlExtracter():

    requests_session = requests_retry_session()
    def __init__(self):
        self.tree = 0

    def __init__(self, url):
        self.createTreeFromUrl(url)

    def createTreeFromUrl(self, url):
        page = self.requests_session.get(url, headers=headers)
        tree = html.fromstring(page.text)
        self.tree = tree
        return tree

    def extractLinkWithTree(self, xpath):
        temp = self.tree.xpath(xpath)
        return temp

