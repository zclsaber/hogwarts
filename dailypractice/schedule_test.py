import requests
import json
import urllib3

urllib3.disable_warnings()

urlbase = "https://10.2.44.84:20120"

headers = {
      'Authorization': 'Basic YWRtaW46QWRtaW5AMTIz',
      'Content-Type': 'application/json'
    }

def create_acl(url, name, networks: list):
    url_acl = url + "/acls"
    payload = json.dumps({
        "comment": "",
        "name": name,
        "networks": networks,
        "exclude_time_strategies": [],
        "time_strategies": []
    })
    response = requests.request("POST", url_acl, headers=headers, data=payload, verify=False)
    print(response.status_code, response.text)

def create_domain_obj(url, name, ecs="no"):
    url_domain_obj = url + "/domainname-categories"
    payload = json.dumps({
        "name": name,
        "is_ecs": ecs
    })
    response = requests.request("POST", url_domain_obj, headers=headers, data=payload, verify=False)
    print(response.status_code, response.text)

def create_sortlists(url, view, type, source: list, prefered: list):
    type = "acl" if type not in ["acl", "domain"] else type
    url_sortlists = url + f"/views/{view}/sortlists"
    payload = json.dumps({
        "data_type": type,
        "source_data": source,
        "prefered_acl": prefered
    })
    response = requests.request("POST", url_sortlists, headers=headers, data=payload, verify=False)
    print(response.status_code, response.text)


def del_domain_object(url, name: list):
    url_domain_obj = url + "/domainname-categories"
    payload = json.dumps({
        "ids": name
    })
    response = requests.request("DELETE", url_domain_obj, headers=headers, data=payload, verify=False)
    print(response.status_code, response.text)

for i in range(1, 202):
    acl_name = "acl" + str(i)
    obj_name = "ttt" + str(i)
    # networks = ["10.2.45.0/24"]

    # create_acl(urlbase, acl_name, networks)
    # create_domain_obj(urlbase, obj_name)

    preferred_acl = ["test"]
    # create_sortlists(urlbase, "view", "acl", [acl_name], preferred_acl)
    # create_sortlists(urlbase, "view", "domain", [obj_name], preferred_acl)
    del_domain_object(urlbase, [obj_name])