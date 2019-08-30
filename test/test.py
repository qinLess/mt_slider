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
    requests_code = 'b6a6351a70024208b9dba942dc720bc9'
    page_data = get_page_data(requests_code)
    res_code = get_code(requests_code, page_data)['data']
    # if res_code.get('response_code', None):
    #     login(requests_code, res_code['response_code'])


if __name__ == '__main__':
    main()
    # data = {"riskLevel":"71","request_code":"09ded539be504242a676d2728df4ac2b","yodaVersion":"{\"i\":\"4ce7db45663c1c83\",\"d\":\"cfaf693ae95ccb81\"}","type":"71","uniqueId":-2086413074,"country":"中国大陆","sign":"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","mobileInterCode":"86","category":"SINGLE","defaultIndex":0,"verifyMethodVersion":"{\"slider\":\"{\\\"i\\\":\\\"2f5aaa53285ceea2\\\",\\\"d\\\":\\\"46fa0e7c72425adf\\\"}\"}","session":"cmV0dXJuIFszLCAncmV0dXJuIGZ1bmN0aW9uKHgseSx6KXtyZXR1cm4gbmV3IHgobmV3IHooWy01LCAtMTgsIC0xMiwgLTEyNCwgMiwgNzMsIC04OSwgMjksIC03MywgLTgzLCAxOSwgLTYsIC05MSwgODMsIC0xMDIsIC0yOV0pLHkpO30nXQ==","riskLevelInfo":"{\"71\":\"{\\\"desc\\\":\\\"滑块\\\",\\\"name\\\":\\\"slider\\\"}\"}","isDegrade":False,"action":"merchantlogin"}
    # tb_data = requests.post('http://127.0.0.1:8805/server/adminSlider', data=data)
    # print(tb_data.text)
