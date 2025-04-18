import asyncio
import asyncio
import time
import aiohttp
import click
import logging
import random







logging.basicConfig(level=logging.INFO, format = '[%(levelname)s]%(message)s')

"""Retry function to handle reuqest failure"""

async def retry_calls(func, retry_call= 3, delay = 1):
    for chances in range(retry_call):
        try: 
            return await func()
        except Exception as e:
            if chances < retry_call -1:
               wait_time = delay * (2** chances) ## we are inreasing waiting time because of error
               logging.warning(f"retry {chances+1}: waiting time {wait_time}s because of error {e}")
               await asyncio.sleep(wait_time)
            else:
                logging.error(f"failed after {retry_call} chances, Error {e}")
                return None
            

"""function to fetch weather info"""

async def fetch_weather(session):
    async def get_info():
        url = "https://api.open-meteo.com/v1/forecast"
        async with session.get(url, timeout = 5, ssl=False) as response:
            await response.json()
            return "28 degree, clear"    #passing predefined value
    return await retry_calls(get_info)


"""function to fetch timezone info"""

async def fetch_timezone(session):
    async def get_info():
        url = "https://worldtimeapi.org/api/timezone/Etc/UTC"
        async with session.get(url, timeout = 5, ssl = False) as response:
            info = await response.json()
            return info.get('timezone', "Unknown timezone")
        
    return await retry_calls(get_info)


"""function to fetch quote for specific teammate"""

async def fetch_quote(session):
    async def get_info():
        url = "https://api.quotable.io/random"
        async with session.get(url, timeout = 5,ssl=False) as response:
            info = await response.json()
            print(info)
            return info.get("content", "no quote Found")
        
    return await retry_calls(get_info)


async def fetch_info_for_single(email):
    logging.info(f"fetching data for: {email}")
    async with aiohttp.ClientSession() as session:

        try:
            timezone = await fetch_timezone(session)
            weather = await fetch_weather(session)
            quote = await fetch_quote(session)
            print(quote)
            logging.info(f"timezone is: {timezone} for email: {email}\n")
            logging.info(f"weather is: {weather} for email: {email}\n")
            logging.info(f"quote is: {quote} for emial: {email}")
        except Exception as e:
            logging.error(f"Error for fetch info for {email}: {e}")




    

"""Cli commands"""

@click.group()
def cli():
    pass


@cli.command()
@click.option('--email','--e', required = True, help="teammmate mail")
def fetch(email):
    asyncio.run(fetch_info_for_single(email))


        

if __name__ == '__main__':
    cli()










