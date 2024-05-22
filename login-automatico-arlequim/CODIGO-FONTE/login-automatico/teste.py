from seleniumbase import BaseCase
from time import sleep


class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://google.com")



print("Finalizando")
