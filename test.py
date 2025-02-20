import skroutz
import asyncio
import decodeshit
import cookies
import json
import os

def dapdtj(html):
    os.system("cls")
    print(
        json.dumps(
            obj=[{"name": sku["name"], "price": sku["price"], "image_url": sku["image_url"], "url": f'https://skroutz.gr{sku["sku_url"]}'} for sku in decodeshit.call(
                html=html
            )[0]["initialData"]["data"]["skus"]],
            indent=4
        )
    )

async def run():
    with \
        skroutz.Skroutz() as sk, \
        cookies.Cookie("cookies.skroutz.pkl") as cook:
            if cook.exists:
                sk.scraper.cookies.update(cook.read())
            try:
                while True:
                    html=sk.getJson(
                        sk.search(input("Search :"))
                    ).content
                    dapdtj(html)
            except KeyboardInterrupt:
                exit()
            data = sk.scraper.cookies.get_dict()
            data.pop("__cf_bm")
            cook.write(data)

asyncio.run(run())