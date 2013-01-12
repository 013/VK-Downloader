import os
import platform
import json
import re
import requests
import sanitize
from bs4 import BeautifulSoup

class Vkontakte():
    """VK.com music Library

        This library provides functionality for logging in, searching and
        downloading Mp3's from the Russian Facebook clone VK.com
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.useragent = ("Mozilla/5.0 (Windows NT 6.2; WOW64) "
                          "AppleWebKit/537.15 (KHTML, like Gecko) "
                          "Chrome/24.0.1295.0 Safari/537.15")
        self.client = requests.session()
        self.client.headers.update({"User-Agent": self.useragent})


    def login(self):
        """Login to vk.com
        """

        url = 'http://login.vk.com/'
        postdata = {'act': 'login', 'try_to_login': '1', 'to': '', 'vk': '',
                    'al_test': '3', 'email': self.username,
                    'pass': self.password, 'expire': ''}
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

    def search(self, query, offset=0):
        """Perform search
        """

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
            return self.parse_search(request)

    def parse_search(self, sobject):
        """Parse the search result
        """

        try:
            text = '<html><body>' + sobject.text[2:] + '</body></html>'
            soup = BeautifulSoup(text)
            items = []

            for x in soup.find_all("div", "clear_fix"):
                duration = x.find("div", "duration").text
                download = x.find("input").attrs['value'][:-4]

                for node in x.findAll("a", attrs={"href": re.compile('/search*')}):
                    artist = ''.join(node.findAll(text=True))

                for node in x.findAll("span", "title"):
                    title = ''.join(node.findAll(text=True))

                info = {'duration': duration, 'url': download,
                        'artist': artist, 'title': title}
                items.append(info)
        except:
            return False
        else:
            return items

    def download(self, url, name):
        """Download mp3
        """

        filename = sanitize.sanitize(name)
        request = self.client.get(url, stream=True)

        if platform.system() == "Windows":
            filepath = os.curdir + "/downloads/" + filename
        elif platform.system() == "Darwin":
            filepath = "/Users/" + os.getenv('USER') + "/Music/" + filename
        else:
            filepath = os.curdir + "/downloads/" + filename

        with open(filepath, "wb") as code:
            for chunk in request.iter_content(1024):
                if not chunk:
                    break

                code.write(chunk)

    def get_size(self, url):
        """Get size of mp3
        """

        try:
            request = self.client.head(url)
            mbDiv = 1024.0 * 1024.0
            size = float(request.headers['content-length']) / div
            return size
        except:
            return False
