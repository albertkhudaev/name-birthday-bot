import requests
import re
import asyncio

pattern = r"Сегодня, \d+ \w+, по церковному православному календарю отмечается \d+ \w+:.+именины"
namepattern = r">\w+</a>"

async def findnames():
    res = requests.get("https://my-calend.ru/name-days")
    birth = []
    names = []
    outnames = []
    
    line = res.text
    if len(re.findall(pattern, line)) > 0:
        birth = re.findall(pattern, line)

    names = re.findall(namepattern, birth[0])
    for name in names:
        name = re.findall(r"\w\w+", name)
        outnames.append(name[0])
    
    return outnames

