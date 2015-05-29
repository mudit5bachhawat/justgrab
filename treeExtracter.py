__author__ = 'mudit'

import requests
from lxml import html

# It functions as extracting the tree and its components with xpath

class lxmlExtracter():

    def __init__(self):
        self.tree=0

    def __init__(self,url):
        self.createTreeFromUrl(url)

    def createTreeFromUrl(self,url):
        page = requests.get(url)
        tree = html.fromstring(page.text)
        self.tree=tree
        return tree

    def extractLinkWithTree(self,xpath):
        temp = self.tree.xpath(xpath)
        return temp
