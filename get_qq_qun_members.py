import requests
import jsonpath
import json

def get_url_param_input():
    query = input("请输入要get成员的群号:")
    url = f"https://qinfo.clt.qq.com/cgi-bin/qun_info/get_members_info_v1?&gc={query}&bkn=598824712&src=qinfo_v3"
    return url

def get_header_param_cookie_input():
    cookie = input("请输入抓包win版qq获得的Cookie：")
    return cookie

def send_request(url, cookie):
    headers = {
            "Host": "qinfo.clt.qq.com",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.7.22.29298 Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.1298.400 QQBrowser/9.0.2524.400",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.8",
            "Cookie": cookie
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None    

def main():
    url = get_url_param_input()
    cookie = get_header_param_cookie_input()
    data = send_request(url, cookie)
    if data:
        print("获取到的数据：")
        print(data)
    qqdata = json.loads(data)
    with open("qq.txt", "w") as file:
        for member_id, member_info in qqdata["members"].items():
            print("成员qq号码:", member_id, "成功写入到qq.txt")    
            file.write(member_id + "\n")
if __name__ == "__main__":
    main()