
import asyncio

import time
import aiohttp
import logging
import random




#mock data
Email_TO_NAME={
    'alice@gmail.com':"Alice",
    'rahul@gmail.com':"rahul",
    "karan@gmail.com":"karan"
}


# async mock api call

async def get_user_info(email):
    print(f"starts at {time.strftime('%X')}")
    print(f"looking for a name for {email}")
    await asyncio.sleep(10)
    

    name = Email_TO_NAME.get(email,"unknown")
    logging.info(f"name found:{name}")
    return name

async def get_timezone(name):
    logging.info(f"fetching time for {name}")
    await asyncio.sleep(random.uniform(1,2.5)) #simulate delay

    timezone = random.choice(['UTC+1', 'UTC+5:30', 'UTC-4'])
    logging.info(f"{name} is in timezone {timezone}")
    return timezone

async def get_quote():
    logging.info(f"fetching quote")
    await asyncio.sleep(random.uniform(1,2)) #simulate delay

    quote = random.choice(['keep pushing yourself',
                           'try hard until you make it',
                           'stay positive and it will make things happen'])
    
    logging.info(f"fetched quote sucessfully")
    return quote

async def handleteammate(email):
    name = await get_user_info(email)
    timezone, quote = await asyncio.gather(get_timezone(name),get_quote())

    print(f"\n Info For: {name} {email}")
    print(f"\n Timezone: {timezone}")
    print(f"\n Quote : {quote}")


async def main():
    emails = input("enter teammate emails sperated with comma:").split(",")
    emails = [e.strip() for e in emails if e.strip()]

    tasks = [handleteammate(email) for email in emails]
    await asyncio.gather(*tasks)
    print(f"ends at {time.strftime('%X')}")

if __name__ == '__main__':
        asyncio.run(main())
