import asyncio
import httpx as httpx
import requests

url = 'http://127.0.0.1:5000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}


def request_get():
    res = requests.get(url, headers=headers)
    print("==== requests get ====")
    print(res.status_code)
    print(res.text)


def request_post():
    json_data = {
        "name": "requests",
        "email": "123111111232123",
        "zipcode": "11121-1111"
    }
    res = requests.post(url, headers=headers, json=json_data)
    print("==== requests post ====")
    print(res.status_code)
    print(res.text)


def request_put():
    json_data = {
        "name": "requests",
        "email": "1",
        "zipcode": "11121-1111"
    }
    res = requests.put(url, headers=headers, json=json_data)
    print("==== requests put ====")
    print(res.status_code)
    print(res.text)


def request_patch():
    json_data = {
        "name": "requests",
        "email": "11113233",
    }
    res = requests.patch(url, headers=headers, json=json_data)
    print("==== requests patch ====")
    print(res.status_code)
    print(res.text)


def request_delete():
    json_data = {
        "name": "requests",
    }
    res = requests.delete(f'{url}/{json_data["name"]}', headers=headers)
    print("==== requests delete ====")
    print(res.status_code)
    print(res.text)


def httpx_get():
    res = httpx.get(url, headers=headers)
    print("==== httpx get ====")
    print(res.status_code)
    print(res.text)


def httpx_post():
    json_data = {
        "name": "httpx",
        "email": "123111111232123",
        "zipcode": "11121-1111"
    }
    res = httpx.post(url, headers=headers, json=json_data)
    print("==== httpx post ====")
    print(res.status_code)
    print(res.text)


def httpx_put():
    json_data = {
        "name": "httpx",
        "email": "1",
        "zipcode": "11121-1111"
    }
    res = httpx.put(url, headers=headers, json=json_data)
    print("==== httpx put ====")
    print(res.status_code)
    print(res.text)


def httpx_patch():
    json_data = {
        "name": "httpx",
        "email": "2222222222",
    }
    res = httpx.patch(url, headers=headers, json=json_data)
    print("==== httpx patch ====")
    print(res.status_code)
    print(res.text)


def httpx_delete():
    json_data = {
        "name": "httpx",
    }
    res = httpx.delete(f'{url}/{json_data["name"]}', headers=headers)
    print("==== httpx delete ====")
    print(res.status_code)
    print(res.text)


async def httpx_get_async():
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)
        print("==== httpx get async ====")
        print(res.status_code)
        print(res.text)


async def httpx_post_async():
    json_data = {
        "name": "httpx_async",
        "email": "123111111232123",
        "zipcode": "11121-1111"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=json_data)
        print("==== httpx post async ====")
        print(res.status_code)
        print(res.text)


async def httpx_put_async():
    json_data = {
        "name": "httpx_async",
        "email": "123111111232123",
        "zipcode": "11121-1111"
    }
    async with httpx.AsyncClient() as client:
        res = await client.put(url, headers=headers, json=json_data)
        print("==== httpx put async ====")
        print(res.status_code)
        print(res.text)


async def httpx_patch_async():
    json_data = {
        "name": "httpx_async",
        "email": "123123123123123",
    }
    async with httpx.AsyncClient() as client:
        res = await client.patch(url, headers=headers, json=json_data)
        print("==== httpx patch async ====")
        print(res.status_code)
        print(res.text)


async def httpx_delete_async():
    json_data = {
        "name": "httpx_async",
    }
    async with httpx.AsyncClient() as client:
        res = await client.delete(f'{url}/{json_data["name"]}', headers=headers)
        print("==== httpx delete async ====")
        print(res.status_code)
        print(res.text)


# async def request_get_async():
#     res = requests.get(url, headers=headers)
#     print("==== requests get ====")
#     print(res.status_code)
#     print(res.text)


if __name__ == '__main__':
    request_get()
    request_post()
    request_put()
    request_patch()
    request_delete()

    httpx_get()
    httpx_post()
    httpx_put()
    httpx_patch()
    httpx_delete()

    asyncio.run(httpx_get_async())
    asyncio.run(httpx_post_async())
    asyncio.run(httpx_put_async())
    asyncio.run(httpx_patch_async())
    asyncio.run(httpx_delete_async())

    # asyncio.run(request_get_async())
