import base64
import csv
import json
import time

import requests
import urllib3

urllib3.disable_warnings()

def fulfill_csv(file, headerlines, start, end, add_head=True):
    data = combine_data(start, end)
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if add_head:
            writer.writerows(headerlines)
        writer.writerows(data)

def combine_data(start, end, isFile=True):
    if isFile:
        data = []
        for i in range(start, end+1):
            d = [str(i)+".test.com.", 3600, "A", "1.1.1.1", "是", "", "", 1, "t"]
            data.append(d)
    else:
        data_tmp = []
        for i in range(start, end):
            s = f"""{str(i)}.test.com., 3600, A, 1.1.1.1, 是, "", "", 1, t"""
            data_tmp.append(s)
            data = '\n'.join(data_tmp)
    return data

def add_massive_rrs(urlbase, file, view, zone, file_or_content=True):
    url = urlbase + f"/views/{view}/zones/{zone}/rrs"
    if file_or_content:
        with open(file, 'rb') as f:
            file_content_base64 = base64.b64encode(f.read())  # 记录文件内容
            resources_content = str(file_content_base64, 'utf-8')
    else:
        # file regards as a file content
        # file_content = '\n'.join(file)
        resources_content = str(base64.b64encode(bytes(file, encoding="GBK")), 'utf-8')
    payload = json.dumps({
            "comment": "",
            "content_type": "csv",
            "zone_file": "C:\\fakepath\\com.csv",
            "zone_content": resources_content
    })
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    return response.text, response.status_code

def add_protected_domain(urlbase, name, domaincategory, number=1):
    url = urlbase + f"/key_domains/domainname-names/{domaincategory}$W10="
    if number == 1:
        payload = json.dumps({
            "domain_names": [f"1.{name}"],
            "is_enable": "yes"
        })
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        print(response.status_code)
    else:
        domain_all = []
        round = number // 200
        remainder = number % 200
        if round >= 1:
            for i in range(1, round+1):
                domain_in = []
                for j in range(1, 201):
                    domain_in.append(f"{200*(i-1)+j}.{name}")
                domain_all.append(domain_in)
        domain = []
        if remainder > 0:
            for i in range(1, remainder+1):
                domain.append(f"{200*round+i}.{name}")
            domain_all.append(domain)
            # print(domain_all)
        for d in domain_all:
            payload = json.dumps({
                "domain_names": d,
                "is_enable": "yes"
            })
            response = requests.request("POST", url, data=payload, headers=headers, verify=False)
            print(response.status_code)

def create_zone(url, view_name, zone_name):
    url_zone = url + f"/views/{view_name}/zones"
    payload_keys = json.dumps({
        "zone_type": "auth",
        "name": zone_name,
        "owners": [
            "local.masterha",
            "local.slve81",
            "local.slave89oe",
            "local.slave59",
            "local.slave58kl86"
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

def create_view(url, view_name):
    url_views = url + "/views"
    payload_keys = json.dumps({
        "comment": "",
        "name": view_name,
        "owners": [
            "local.masterha",
            "local.slve81",
            "local.slave89oe",
            "local.slave59",
            "local.slave58kl86"
        ],
        "acls": [
            "acl_all"
        ],
        "black_acls": [],
        "filter_aaaa": "no",
        "recursion_enable": "yes",
        "allow_recursive": "all",
        "non_recursive_acls": [],
        "ecs_recurse_domains": [],
        "ecs_exact_match": "no",
        "bind_ips": [
            "0.0.0.0"
        ],
        "try_final_after_forward": "no",
        "fail_forwarder": "",
        "limit_ips": [],
        "need_tsig_key": "no",
        "filter_aaaa_ips": [
            "any"
        ],
        "tsig_host": []
    })
    response = requests.request("POST", url_views, headers=headers, data=payload_keys, verify=False)
    print(response.text)

def ip2int(ip):
    lis = ip.split('.')
    return int("%02x%02x%02x%02x" % (int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3])), 16)

def int2ip(num):
    hexIP = str('%08x' % num)
    return str("%i.%i.%i.%i" % (int(hexIP[0:2], 16), int(hexIP[2:4], 16), int(hexIP[4:6], 16), int(hexIP[6:8], 16)))

def add_view_zone_rr(url, view_num, zone_num, rr_num):
    for i in range(1, view_num+1):
        view_name = "zcl_" + str(i)
        create_view(url, view_name)
        for j in range(1, zone_num+1):
            zone_name = "comz_" + str(j)
            create_zone(url, view_name, zone_name)
            for k in range(1, rr_num+1):
                rr_name = "rr" + str(k)
                record = [int2ip(ip2int("1.1.1.1") + k)]
                create_rr(url, view_name, zone_name, rr_name, "A", record)
                time.sleep(1)

urlbase = "https://10.2.44.80:20120"

headers = {
      'Authorization': 'Basic YWRtaW46YWRtaW4=',
      'Content-Type': 'application/json'
    }

headerlines = [["记录名称", "TTL", "记录类型", "记录值", "是否启用", "有效截期", "到期策略", "", "xxx"],
               ["test.com.", 3600, "SOA", "ns.test.com. mail.test.com. 4 28800 3600 604800 1800", "是", "", "", 1, "t"],
               ["test.com.", 3600, "NS", "ns.test.com.", "是", "", "", 1, "t"],
               ["ns.test.com.", 3600, "A", "127.0.0.1", "是", "", "", 1, "t"]]

# fulfill_csv(r"C:\Users\fu\Downloads\test.com.csv", headerlines, 20001, 40000)
view = "view_zcl"
zone = "test.com"

# for i in range(2, 5001):
#     if i == 1:
#         start = 20000 * (i-1) + 1
#         end = 20000 * i
#         file_name = r"C:\Users\fu\Downloads" + f"\\test.com-{str(i)}.csv"
#         fulfill_csv(file_name, headerlines[0], start, end-1, add_head=True)
#         print(add_massive_rrs(urlbase, file_name, view, zone))
#     else:
#         start = 200 * (i-1) + 20001
#         end = 200 * i + 20000
#         # file_content = combine_data(start, end, isFile=False)
#         # # print(file_content)
#         # print(add_massive_rrs(urlbase, file_content, view, zone, file_or_content=False))
#         file_name = r"C:\Users\fu\Downloads" + f"\\test.com-tmp.csv"
#         fulfill_csv(file_name, [headerlines[0],], start, end - 1, add_head=True)
#         print(add_massive_rrs(urlbase, file_name, view, zone))

# add_protected_domain(urlbase, "com", "test", number=20001)
add_view_zone_rr(urlbase, 200, 50, 1)