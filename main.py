from datetime import datetime
import aiohttp
import asyncio
import schedule


# Функция для обработки запросов
async def get_count(session, url, srv):
    count = '-'
    try:
        async with session.get(url) as resp:
            json_resp = await resp.json()
            count = json_resp['count']
    except:
        print(f"Error with getting {url}")
    finally:
        payload = {
            'server': srv,
            'count': count
        }
        return payload


# Основная функция
async def main(srv_list):
    async with aiohttp.ClientSession() as session:

        # Создаём таски, передаём url и имя сервера
        tasks = []
        request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for srv in srv_list:
            url = f'http://{srv}/api/count'
            tasks.append(asyncio.ensure_future(get_count(session, url, srv)))

        # Выводим результат
        result = await asyncio.gather(*tasks)
        for r in result:
            print(f"{request_time} {r['server']} {r['count']}")


# Функция для вызова асинхронной функции main
def async_main(srv_list):
    asyncio.run(main(srv_list))


if __name__ == '__main__':
    # Список машин для обращения
    server_list = ["maria.ru", "rose.ru", "sina.ru"]
    # Шедуллер вызывает async_main в каждые 00 секунд каждой минуты
    schedule.every().minute.at(":00").do(async_main, server_list)
    while True:
        schedule.run_pending()
