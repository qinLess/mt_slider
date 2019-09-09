import requests
import json


def get_page_data(requests_code):
    headers = {
        'Referer': 'https://passport.meituan.com/account/unitivelogin?service=phoenix&continue=https%3A%2F%2Fwww.zhenguo.com%2Fauth%2Fauthenticated%2F%3Fcontinue%3D%252F&risk_partner=93',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    data = {
        'requestCode': requests_code,
        'feVersion': '1.4.0',
        'source': '1'
    }
    url = 'https://verify.meituan.com/v2/ext_api/page_data'
    res = requests.post(url, headers=headers, data=data).json()
    print('page_data: ', res['data'])
    return res


def get_code(request_code, page_data):
    tb_data = requests.post('http://127.0.0.1:7000/tbToken', data=json.dumps(page_data), headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }).json()
    print('tb_data: ', tb_data)
    headers = {
        # 'Authorization': 'Bearer ' + request_code,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://epassport.meituan.com',
        'Referer': 'https://passport.meituan.com/account/unitivelogin?service=phoenix&continue=https%3A%2F%2Fwww.zhenguo.com%2Fauth%2Fauthenticated%2F%3Fcontinue%3D%252F&risk_partner=93',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    data = {
        'id': 71,
        'request_code': request_code,
        'behavior': tb_data['behavior'],
        'fingerprint': 'undefined',
        '_token': tb_data['token'],
    }
    url = 'https://verify.meituan.com/v2/ext_api/login/verify'
    res = requests.post(url, headers=headers, data=data).json()
    print('response_code: ', res)
    return res


def main():
  requests_code = 'aa3cf08a9dc245d9b0ca4f12c4a76ae5'
  page_data = get_page_data(requests_code)
  res_code = get_code(requests_code, page_data)['data']


if __name__ == "__main__":
    main()
