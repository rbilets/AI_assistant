from ADT.array import Array
from modules.talk import talk
import webbrowser


class NewsADT:
    """
    ADT to work with news article
    """
    def __init__(self):
        """
        Creates the Array to store the information
        """
        self._data = Array(3)

    def add_title(self, title):
        """
        Adds article title
        :param title: str
        :return: None
        """
        self._data[0] = title

    def get_title(self):
        """
        Return article title
        :return: str
        """
        return self._data[0]

    def read_title(self):
        """
        Read article title
        :return: None
        """
        talk(self.get_title())

    def add_description(self, description):
        """
        Adds article description
        :param description: str
        :return:
        """
        self._data[0] = description

    def get_description(self):
        """
        Return article description
        :return: str
        """
        return self._data[0]

    def read_description(self):
        """
        Read article description
        :return:
        """
        talk(self.get_description())

    def add_url(self, url):
        """
        Adds article web url
        :param url: str
        :return:
        """
        self._data[2] = url

    def get_url(self):
        """
        Return article web url
        :return: str
        """
        return self._data[2]

    def open_url(self):
        """
        Opens article in the browser window
        :return: None
        """
        webbrowser.open(self.get_url())


if __name__ == '__main__':
    article1 = NewsADT()
    article1.add_title('Cool')
    article1.add_description('Apple sales reach peak due to the coronavirus attack.')
    article1.add_url('https://www.apple.com/')
    article1.read_title()
    article1.read_description()
    #article1.open_url()