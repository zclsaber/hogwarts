import requests


class TestToken:


    def test_get_token(self):
        '''
        获取access_token
        :return: access_token
        '''
        corpid = 'xxxx'
        secret = 'xxxx'
        url = 'xxxx'

        # 参数的传入，可以用 params 传入
        # 也可以在 url 后面使用 ？ 后带参数的形式直接传入
        r = requests.get(url)
        access_token = r.json()['access_token']