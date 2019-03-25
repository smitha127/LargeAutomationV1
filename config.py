import requests


class config:

    def Headers(self):

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
            }
            return headers

    def credintials(self):
        login_data = {
            'userName': 'Amey.Patil@quest-global.com',
            'password': 'Quest=1234',
            'Login': 'Log in'
        }
        return login_data


    def session(self):
     s=requests.session()
     return s
