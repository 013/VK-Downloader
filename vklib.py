import requests
import json
from bs4 import BeautifulSoup
import os
import sanitize

class vKontakte():
    """VK.com music Library"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.useragent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15'
        self.client = requests.session(headers={'User-Agent': self.useragent})

    def login(self):
        #Login to vk.com

        url = 'http://login.vk.com/'
        postdata = {'act': 'login', 'success_url': '', 'fail_url': '',
                    'try_to_login': '1', 'to': '', 'vk': '', 'al_test': '3',
                    'email': self.username, 'pass': self.password, 'expire': ''}
        try:
            request = self.client.post(url, data=postdata)
        except requests.exceptions.ConnectionError:
            print 'Could not connect.'
            return False
        except requests.exceptions.Timeout:
            print 'The connection timed out.'
            return False
        except:
            print 'Unknown exception'
            return False
        else:
            if "wrong" in request.text:
                return False
            else:
                return request

    def search(self, query, offset = 0):
        #Perform search

        url = 'http://vk.com/audio'
        postdata = {'act': 'search', 'al': '1', 'offset': offset, 'q': query}
        try:
            request = self.client.post(url, data=postdata)
        except requests.exceptions.ConnectionError:
            print 'Could not connect.'
            return False
        except requests.exceptions.Timeout:
            print 'The connection timed out.'
            return False
        except:
            print 'Unknown exception'
            return False
        else:
            return self.parsesearch(request)

    def parsesearch(self, sobject):
        #Parse the search result

        try:
            text = '<html><body>' + sobject.text[2:] + '</body></html>'
            soup = BeautifulSoup(text)
            items = []

            for x in soup.find_all("div", "clear_fix"):
                duration = x.find("div", "duration").text
                download = x.find("input").attrs['value'][:-4]

                info = x.find_all("span")
                artist = info[0].text
                title = info[1].text

                info = {'duration': duration, 'url': download, 'artist': artist, 'title': title}
                items.append(info)
        except:
            return False
        else:
            return items

    def download(self, url, name):
        #Download mp3

        filename = sanitize.sanitize(name)

        request = self.client.get(url)
        
        f = open(os.curdir + "/downloads/" + filename, "wb")

        with f as code:
            code.write(request.content)
        f.close()
        print "done"
