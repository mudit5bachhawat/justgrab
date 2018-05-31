__author__ = 'mudit'

import csv, os, time
from treeExtracter import lxmlExtracter

joiner = ' , '


class justExtract():
    xpathLib = {}
    xpathLib["name"] = "//*[@class='fn']/text()"
    xpathLib["contact"] = "//*[@class='tel']//text()"
    xpathLib["address"] = "//aside[@class='continfo nocl']//span[@class='jaddt']/text()"
    xpathLib["website"] = "//*[@class='wsurl']/a/@href"
    xpathLib["linkEachPage"] = '//*[@id="srchpagination"]/a/@href' # '//p[@class="jcnwrp"]/span/a/@href'


    def __init__(self, link):
        self.mainPageLink = link

    def setUrl(self, url):
        self.mainPageLink = url

    def modifyEntry(self, entry):
        if len(entry) == 0:
            entry.append('')

    def uniq(self, input):
        output = []
        for x in input:
            if x not in output:
                output.append(x)
        return output

    def extract(self):

        pageLink = [self.mainPageLink]
        for page in pageLink:

            extracter = lxmlExtracter(page)
            entriesList = extracter.extractLinkWithTree(self.xpathLib["linkEachPage"])
            for LinkInPage in entriesList:
                while (1):
                    tree = lxmlExtracter(LinkInPage)

                    name = tree.extractLinkWithTree(self.xpathLib["name"])
                    address = tree.extractLinkWithTree(self.xpathLib["address"])

                    tel = tree.extractLinkWithTree(self.xpathLib["contact"])
                    tel = self.uniq(tel)

                    website = tree.extractLinkWithTree(self.xpathLib["website"])

                    website = self.uniq(website)

                    self.modifyEntry(website)
                    self.modifyEntry(address)
                    self.modifyEntry(tel)
                    self.modifyEntry(name)
                    # row= [(name[0].strip()).encode('ascii','ignore')]+[address[0].strip().encode('ascii','ignore')]+[((joiner.join(tel)).strip()).encode('ascii', 'ignore')]+[website[0].strip().encode('ascii','ignore')]
                    row = [name[0].strip(), address[0].strip(), tel[0].strip(), website[0].strip()]
                    self.processRow(row)
                    if (row != ['', '', '', '']):
                        break

    def processRow(self, data):
        print data
