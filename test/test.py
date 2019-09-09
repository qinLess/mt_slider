"""美团商家后台模拟滑块验证码破解测试"""
import requests
import json


def get_page_data(requests_code):
    headers = {
        'Referer': 'https://epassport.meituan.com/account/unitivelogin?bg_source=3&service=waimai&platform=2&continue=http://e.waimai.meituan.com/v2/epassport/entry&left_bottom_link=%2Faccount%2Funitivesignup%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FsignUp%26extChannel%3Dwaimaie%26ext_sign_up_channel%3Dwaimaie&right_bottom_link=%2Faccount%2Funitiverecover%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FchangePwd',
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
        'Authorization': 'Bearer ' + request_code,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://epassport.meituan.com',
        'Referer': 'https://epassport.meituan.com/account/unitivelogin?bg_source=3&service=waimai&platform=2&continue=http://e.waimai.meituan.com/v2/epassport/entry&left_bottom_link=%2Faccount%2Funitivesignup%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FsignUp%26extChannel%3Dwaimaie%26ext_sign_up_channel%3Dwaimaie&right_bottom_link=%2Faccount%2Funitiverecover%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FchangePwd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    data = {
        'request_code': request_code,
        'behavior': tb_data['behavior'],
        'fingerprint': 'undefined',
        '_token': tb_data['token'],
    }
    url = 'https://verify.meituan.com/v2/ext_api/merchantlogin/verify?id=71'
    res = requests.post(url, headers=headers, data=data).json()
    print('response_code: ', res)
    return res


def login(res_code, req_code):
    data = {
        'captchaCode': '',
        'captchaToken': '',
        'error': '需要滑块验证',
        'isFetching': 'false',
        'login': 'abcdefg',
        'loginType': 'account',
        'part_key': '',
        'password': '1234567',
        'rohrToken': requests.post('http://127.0.0.1:7000/token').text,
        'success': '',
        'verifyRequestCode': req_code,
        'verifyResponseCode': res_code,
        'verifyType': '3'
    }
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '1197',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'wm_order_channel=default; utm_source=; _lxsdk_cuid=16c03238f20c8-079f6dc811d2e4-2d604637-3d10d-16c03238f20c8; _lxsdk=16c03238f20c8-079f6dc811d2e4-2d604637-3d10d-16c03238f20c8; ta.uuid=1153492041913815133; isUuidUnion=true; iuuid=16c03238f20c8-079f6dc811d2e4-2d604637-3d10d-16c03238f20c8; uuid=0fafc85a87b1bb4a33ac.1565576631.1.0.0; _lxsdk_s=16c83a326b3-050-123-e31%7C%7C6',
        'Host': 'epassport.meituan.com',
        'Origin': 'https://epassport.meituan.com',
        'Referer': 'https://epassport.meituan.com/account/unitivelogin?bg_source=3&service=waimai&platform=2&continue=http://e.waimai.meituan.com/v2/epassport/entry&left_bottom_link=%2Faccount%2Funitivesignup%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FsignUp%26extChannel%3Dwaimaie%26ext_sign_up_channel%3Dwaimaie&right_bottom_link=%2Faccount%2Funitiverecover%3Fbg_source%3D3%26service%3Dwaimai%26platform%3D2%26continue%3Dhttp%3A%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2FchangePwd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    url = 'https://epassport.meituan.com/api/account/login?service=waimai&bg_source=3&loginContinue=http:%2F%2Fe.waimai.meituan.com%2Fv2%2Fepassport%2Fentry&loginType=account'
    res = requests.post(url, headers=headers, data=data)
    print('res: ', res)


def main():
    # 这个需要从官网获取
    requests_code = '6406c39006804b3d88af87c94cfaac9f'
    page_data = get_page_data(requests_code)
    res_code = get_code(requests_code, page_data)['data']
    # if res_code.get('response_code', None):
    #     login(requests_code, res_code['response_code'])


if __name__ == '__main__':
    main()
