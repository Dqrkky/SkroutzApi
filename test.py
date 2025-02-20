import skroutz
import asyncio
import decodeshit
import cookies
import html_to_json
import json

def dapdtj(html):
    print(
        json.dumps(
            obj=decodeshit.call(
                html=html
            ),
            indent=4
        )
    )

async def run():
    with \
        skroutz.Skroutz() as sk, \
        cookies.Cookie("cookies.skroutz.pkl") as cook:
            if cook.exists:
                sk.scraper.cookies.update(cook.read())
            html=sk.getJson(
                sk.search("pc psu")
            ).content
            dapdtj(html)
            cloudflare = [i["meta"] for i in html_to_json.convert(html_string=html)["html"][0]["head"][0]["meta"] if "meta" in i]
            if len(cloudflare) > 0:
                sk.scraper.headers.update({
                    "x-csrf-token": cloudflare[0][0]["meta"][0]["_attributes"]["content"]
                })
            html=sk.getJson(
                sk.search("mobile screen replacement")
            ).content
            dapdtj(html)
            data = sk.scraper.cookies.get_dict()
            data.pop("__cf_bm")
            cook.write(data)

asyncio.run(run())