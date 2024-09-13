import logging
import threading

import requests
import json
import urllib3

urllib3.disable_warnings()

urlbase = "https://10.2.15.212:20120"
url2 = "https://10.2.44.55:20120"
headers = {
      'Authorization': 'Basic YWRtaW46YWRtaW4=',
      'Content-Type': 'application/json'
    }

def create_dnssec_ds(zone_name, name, start, stop):
    url_ds = urlbase + "/dnssec-ds"
    for i in range(start, stop):
        # zone_name = "a"
        rdata = "37522 8 2 69807BAE0D589B7E7A23F7297CB59EC9A34C564A23EDE8E177F7F6C9655" + str('%05d' % i)

        payload_keys = json.dumps({
             "view_name": "default",
             "zone_name": zone_name,
             "name": name,
             "type": "DS",
             "ttl": "3600",
             "rdata": rdata,
             "comment": "123"
            })

        response = requests.request("POST", url_ds, headers=headers, data=payload_keys, verify=False)

    print('finished')

def create_dnssec_trusted_anchors(zone_name):
    url_anchors = urlbase + "/trust_anchors"
    payload_keys = json.dumps({
         "zone_name": zone_name,
         "view_name": "default",
         "public_key": [
         "257 3 7 AwEAAespKC+E3yd/xUCLLoUGpy9KCZkKvj2FIbH7Y10oMGWD5hrkaott rIs8itv4r4ijZvoZtixmeKaE22C7CzAcRI1sp91M+gOPUslsru5vWjpS 8wFMiE4twXPqAeT7xLpj+1XsTjeggmkwY0pGqWWPC4ZsTko42a5RrlmE 2bMKbubx"
         ],
         "comment": "123"
        })

    response = requests.request("POST", url_anchors, headers=headers, data=payload_keys, verify=False)
    print(response)
    print("finished")

def create_dnssec_keys(stop, start=1):
    url_keys = urlbase + "/dnssec-autograph/secret-key"
    for i in range(start, stop):
        zsk_name = "zsk" +str(i)
        payload_keys = json.dumps({
             "name": zsk_name,
             "type": "ZSK",
             "algorithm": "NSEC3RSASHA1",
             "size": 1024,
             "rotation_period": 3,
             "common_period": 7,
             "comment": "123"
            })
        response = requests.request("POST", url_keys, headers=headers, data=payload_keys, verify=False)
        print(response)
    print("finished")


# def start_threads(function_name):
#     t1 = threading.Thread(target=function_name, args=(1, 4000))
#     t2 = threading.Thread(target=function_name, args=(4001, 8000))
#     t3 = threading.Thread(target=function_name, args=(8001, 12000))
#     t4 = threading.Thread(target=function_name, args=(12001, 16000))
#     t5 = threading.Thread(target=function_name, args=(16001, 20000))
#     threads = [t1, t2, t3, t4, t5]
#
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     t.join()

# start_threads(create_dnssec_ds)
def create_zone(url, view_name, zone_name):
    url_zone = url + f"/views/{view_name}/zones"
    payload_keys = json.dumps({
        "zone_type": "auth",
        "name": zone_name,
        "owners": [
            "local.master"
        ],
        "server_type": "master",
        "default_ttl": "3600",
        "slaves": [],
        "ad_controller": [],
        "limit_ips": [],
        "acl_names": [],
        "black_acl_names": [],
        "renewal": "no",
        "dsprimary": "no"
    })
    response = requests.request("POST", url_zone, headers=headers, data=payload_keys, verify=False)
    # print(response)

def create_rr(url, view_name, zone_name, name, rtype, value):
    url_rr = url + f"/views/{view_name}/zones/" + zone_name + "/rrs"
    payload_keys = json.dumps({
        "comment": "",
        "name": name,
        "type": rtype,
        "ttl": "3600",
        "rdata": value,
        "is_enable": "yes",
        "expire_is_enable": "no"
    })
    response = requests.request("POST", url_rr, headers=headers, data=payload_keys, verify=False)
    # print(response)

# create_rr("zone1", "a1", "NS", "ns.a1.zone1.")
# create_rr("zone1", "ns.a1", "A", ["1.2.3.4"])

# 创建100w条DS记录
# for i in range(1, 51):
#     # 创建50个区
#     zone_name = "zone" + str(i)
#     create_zone(zone_name)
#     # 每个区下创建200条NS记录
#     for i in range(1, 201):
#         # 创建 a 记录
#         name_a = "ns.a" + str(i)
#         create_rr(zone_name, name_a, "A", ["1.2.3.4"])
#         # 创建对应的 ns 记录
#         name_ns ="a" + str(i)
#         rr_ns = "ns." + name_ns + "." + zone_name + "."
#         create_rr(zone_name, name_ns, "NS", rr_ns)
#         # 创建完子域授权后，创建DS记录，每个域名下创建100条
#         insert_dnssec_ds('10.2.45.15', zone_name, name_ns + '.' + zone_name + '.', 100)

def ip2int(ip):
    lis = ip.split('.')
    return int("%02x%02x%02x%02x" % (int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3])), 16)

def int2ip(num):
    hexIP = str('%08x' % num)
    return str("%i.%i.%i.%i" % (int(hexIP[0:2], 16), int(hexIP[2:4], 16), int(hexIP[4:6], 16), int(hexIP[6:8], 16)))

# 针对招行131个视图，每个视图里面创建100条域名的A记录
def add_rr_for_cmb(url):
    # 读取json文件
    with open("./operate_zdns/cmb-views.json") as f:
        data = json.load(f)
    for i in data:
        # 获取每个视图名称
        view = i["params"]["name"]
        # 在每个视图下创建一个 cmchina.com 区
        create_zone(url, view, "cmchina.com")
        init = 0
        # 在每个视图的每个 cmchina.com 区下，创建 100 条记录
        for p in range(ip2int("1.1.1.1"), ip2int("1.1.1.101")):
            init += 1
            create_rr(url, view, "cmchina.com", str(init) + "-test-cmb", "A", [int2ip(p)])
        print("add rrs complete for view: ", view)

def check_data_by_view(url, view, zone):
    zones = []
    zone_res = requests.request("GET", url + f"/views/{view}/zones", headers=headers, verify=False)
    data = json.loads(zone_res.text)
    try:
        for zz in data["resources"]:
            zones.append(zz["name"])
        # print(f"view {view} has zone: {zones}")
        rrs = []
        rrs_res = requests.request("GET", url + f"/views/{view}/zones/{zone}/rrs", headers=headers, verify=False)
        data = json.loads(rrs_res.text)
        for rr in data["resources"]:
            rrs.append(rr["name"])
        # print(f"zone {zone} under view {view} has {len(rrs)} records.")
        if len(rrs) != 102:
            return 1
    except KeyError as e:
        # print(e)
        # print(f"view {view} has no zone {zone}")
        return 2

def check_data(url):
    # add_rr_for_cmb()
    with open("./operate_zdns/cmb-views.json") as f:
        data = json.load(f)
    no_enough_rrs = []
    no_zone = []
    for i in data:
        # 获取每个视图名称
        view = i["params"]["name"]
        flag = check_data_by_view(url, view, "cmchina.com")
        if flag == 1:
            no_enough_rrs.append(view)
        elif flag == 2:
            no_zone.append(view)

    print(f"below views have no zone cmchina: {no_zone}")
    print(f"below views have not enough rrs: {no_enough_rrs}")
    return no_zone, no_enough_rrs

def del_zone(url, view_name, zone_name):
    url_zone = url + f"/views/{view_name}/zones"
    payload_keys = json.dumps({
        "_desc" :{
            zone_name: zone_name
        },
        "ids": [zone_name]
    })
    response = requests.request("DELETE", url_zone, headers=headers, data=payload_keys, verify=False)
    print(response)
# no_zone, no_enough_rrs = check_data()
# # for i in no_zone:
# #     create_zone(i, "cmchina.com")
#
# init = 0
# for i in no_enough_rrs:
#     for p in range(ip2int("1.1.1.1"), ip2int("1.1.1.101")):
#         init += 1
#         create_rr(i, "cmchina.com", str(init) + "-test-cmb", "A", [int2ip(p)])

# t1 = threading.Thread(target=check_data, args=(urlbase,))
# t2 = threading.Thread(target=check_data, args=(url2,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# check_data()
# with open("./operate_zdns/cmb-views.json") as f:
#     data = json.load(f)
#     for i in data:
#         # 获取每个视图名称
#         view = i["params"]["name"]
#         # 对每个视图进行删除区操作
#         del_zone(urlbase, view, "cmchina.com")
# source_ips = []
# with open("./operate_zdns/api-requests-acl-200w.json") as f:
#     data = json.load(f)
# for i in data:
#     # 从修改后的 acl 中获取最后一个网段，拼接 ip
#     # print(i)
#     if "modify-acl" in i.get("id"):
#         view_name = i["id"].split(" ")[1]
#         ip = i["params"]["modify_infos"][view_name].split(";")[-1].split("0/24")[0] + "5"
#         # print(ip)
#         # ip = i["params"]["modify_infos"][0].split(";")[-1].split("0/24")[0] + "5"
#         source_ips.append(ip)

# print(source_ips)
# print(len(source_ips))
# from operate_zdns.DoH_request import doh_request

def boce(httpdoh_url, header, scope=None):
    if not scope:
        count_all = 0
        failure = []
        for i in range(1, 101):
            domain_name = str(i) + "-test-cmb.cmchina.com"
            try:
                logging.info(f"拨测域名 {domain_name}")
                delay, response = doh_request(httpdoh_url, domain_name, headers=header)
                logging.info(f"拨测结果： {response}, 解析时延 {delay}")
                count_all += 1
            except Exception as e:
                logging.error(e)
                failure.append(domain_name)
        logging.info(f"拨测成功次数 {count_all}")
        if failure is not []:
            logging.info(f"拨测失败的域名有 {failure}")
    else:
        for domain_name in scope:
            try:
                logging.info(f"拨测域名 {domain_name}")
                delay, response = doh_request(httpdoh_url, domain_name, headers=header)
                logging.info(f"拨测结果： {response}, {delay}")
            except Exception as e:
                logging.error(e)

'''数据准备'''
cmd = """/root/wrk2-master/wrk -t50 -c1000 http://10.2.15.231:5353/dns-query?dns=PjEBAAABAAAAAAAACjEtdGVzdC1jbWIHY21jaGluYQNjb20AAAEAAQ -H "X-Forwarded-For: 20.92.122.5" -H "Connection: close" -d """
http_url = "http://10.2.15.231:5353/dns-query"
urlbase_auth = "https://10.2.44.55:20120"
urlbase_recu = "https://10.2.15.231:20120"
url = [http_url, urlbase_auth, urlbase_recu]
headers_normal = {
      'Authorization': 'Basic YWRtaW46YWRtaW4=',
      'Content-Type': 'application/json'
    }

# 构建源 ip， 用于拨测时进入对应 acl
source_ips = {}
with open("./operate_zdns/api-requests-acl-200w.json") as f:
    data = json.load(f)
for i in data:
    # 从修改后的 acl 中获取最后一个网段，拼接 ip
    if "modify-acl" in i.get("id"):
        view_name = i["id"].split(" ")[1]
        ip = i["params"]["modify_infos"][view_name].split(";")[-1].split("0/24")[0] + "5"
        source_ips[view_name] = ip

# 构建请求头，用于添加源 ip，实现 ecs 载源进入对应视图
header_proxies = []
for view_name, ip in source_ips.items():
    header_proxy = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Content-Type': 'application/json',
        "X-Forwarded-For": ip
    }
    header_proxies.append(header_proxy)

# 构建仅拨测 2 个域名时所用的请求域名
boce_scope = ['1-test-cmb.cmchina.com', '2-test-cmb.cmchina.com']

# 获取所有的视图名
views = []
with open("./operate_zdns/cmb-views.json") as f:
    data = json.load(f)
for i in data:
    # 获取每个视图名称
    view = i["params"]["name"]
    views.append(view)

# 构建所有的域名
domain_names = []
for i in range(1, 101):
    domain_name = str(i) + "-test-cmb.cmchina.com"
    domain_names.append(domain_name)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('./test_boce.log', encoding='utf-8', mode='a')
    ]
)


def find_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

# count = 0
for header in header_proxies:
    # count += 1
    view_match = find_key(source_ips, header["X-Forwarded-For"])
    logging.info(f'拨测源 ip：{header["X-Forwarded-For"]}， 对应视图为{view_match}')
    boce(url[0], header)
# print(count)