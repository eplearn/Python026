
import asyncio
import aiohttp
import json


class Receiver:

    def __init__(self, requests_number, filename, url):
        self.max_index = requests_number  # количество запросов
        self.filename = filename
        self.url = url

    async def receive_data(self, session, index):
        async with session.get(self.url) as response:
            data = await response.read()  # исходное содержание ответа сервера
            data = json.loads(data).get('cell_phone')  # json преобразуется в словарь, извлекается значение по ключу
            self.save_data(data, index)  # номер телефона передаётся на запись

    def save_data(self, input_data, index):
        output_data = f'task {index}.  {input_data}\n'  # формируется строка, которая буде записана в файл
        with open(f'{self.filename}', 'a') as f:
            f.write(output_data)

    async def execute(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for i in range(self.max_index):
                task = asyncio.create_task(self.receive_data(session, i))  # формируется задание
                tasks.append(task)  # задание добавляется в список заданий
            await asyncio.gather(*tasks)  # запуск всех заданий, содержащихся в списке заданий

    def run(self):
        loop = asyncio.get_event_loop()  # создаётся объект цикла событий
        loop.run_until_complete(self.execute())  # цикл событий исполняется, пока main() не закончит свою работу
