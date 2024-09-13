import json
import requests
import urllib3

urllib3.disable_warnings()

def flushdns_dedicated(view_name, domain_name, url, role, header):
    url_clean = url + f"/groups/local/members/{role}/cache/clean"
    payload_keys = json.dumps({
        "view_name": view_name,
        "domain_name": domain_name,
        "a": "b"
    })
    response = requests.request("POST", url_clean, headers=header, data=payload_keys, verify=False)
    # logging.info(f"清除视图 {view_name} 的指定缓存：{domain_name}")
    # logging.info(response.text)
    print(response)

url = "https://10.2.15.212:20120"
header = {
      'Authorization': 'Basic YWRtaW46YWRtaW4=',
      'Content-Type': 'application/json'
    }

flushdns_dedicated("default", "a.b.c", url, "win92", header)