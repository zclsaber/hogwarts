import requests


class TestDepart:

    # 设置一个类级别的装置，用于获取token
    def setup_class(self):
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
        self.access_token = r.json()['access_token'] #或者 r.json().get('access_token')
        return self.access_token

    def test_create_department(self):
        '''
        创建部门
        :return:
        '''
        url = 'xxxxxx'
        param = {
            'access_token': self.access_token
        }
        data = {
            'xx': 'xxxxx'
        }
        # params 和 data 在使用上有一些不同，一个是url携带的参数，一个是请求体的body
        r = requests.post(url=url, param=param, data=data)
        assert 0 == r.json().get('errorcode')