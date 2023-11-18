import requests


def get_props(api_key,limit=1000):
    url = f"https://www.tokkobroker.com/api/v1/property/?lang=es_ar&limit={limit}&key={api_key}"

    payload = {}
    headers = {
        "authority": "www.tokkobroker.com",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7",
        "cookie": "csrftoken=4yJCmyehkCXGTo6lcFi2xmLrQqKpdnPx; _gcl_au=1.1.968373948.1667051578; _gid=GA1.2.448036400.1667051579; _fbp=fb.1.1667051579113.1208706750; sessionid=30f31183ceebbe18e46e69227126b46a; __hstc=91113221.b47b99be253e6d247e6ed5e2cc373865.1667051708440.1667051708440.1667051708440.1; hubspotutk=b47b99be253e6d247e6ed5e2cc373865; __hssrc=1; _hjSessionUser_1782356=eyJpZCI6IjU4Mjk5MjhiLTU0MjktNWU0YS05MDRlLTk5MjQzNzkxMGE2ZSIsImNyZWF0ZWQiOjE2NjcwNTE3MDc4OTMsImV4aXN0aW5nIjp0cnVlfQ==; _ga_KFHGP220JQ=GS1.1.1667051708.1.1.1667052198.0.0.0; amp_1763a4=iq62bc5GdRtSi4xgOX6szP.Mzg2MTA=..1ggi0cmp7.1ggi0rmsa.0.0.0; _hjSessionUser_1806543=eyJpZCI6ImI1MmIyZmQ2LWJmMTQtNTQxMC1iMTliLTFmYzFlYzE0MmM1NSIsImNyZWF0ZWQiOjE2NjcwNTIzMjYyMzMsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.801216415.1667051579; intercom-session-npgs1vl5=ZDdBOWFlaFBiMGxydFVFMVMvNWZwWFpPTnFkcEFjbDlvbmI2NExrcjhsL2xuTVZBSDBrRUY0TEJzZEJhN3hQMi0tRFhTd2tpTmlXM0VEaUh4R3NEbS9DUT09--26b680cc2f8d0cbb4122ee1484e57d7772358c15; _ga_ZTHF3QDTLE=GS1.1.1667051578.1.1.1667052483.22.0.0; sessionid=8a35472a9e9717b2647703cbe9f920e2",
        "referer": "https://www.tokkobroker.com/api/playground",
        "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    return requests.request("GET", url, headers=headers, data=payload)