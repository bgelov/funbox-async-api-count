# funbox-async-api-count

## Задача
```
Есть три сервера "maria.ru", "rose.ru", "sina.ru", которые по GET-запросу отдают свою метрику.
Напишите на вашем любимом скриптовом языке программирования (Ruby, Perl, PHP, Python, Groovy, . . .)
программу, которая будет опрашивать три сервера каждую минуту и выводить в консоль эту метрику рядом с названием сервера.

Формат запроса:
GET http://servername/api/count

Формат ответа:
{"count": 42}

Формат вывода:
2022-05-20 13:01:00 maria.ru 42
2022-05-20 13:01:00 rose.ru 43
2022-05-20 13:01:00 sina.ru 45
2022-05-20 13:02:00 maria.ru 32
2022-05-20 13:02:00 rose.ru 33
2022-05-20 13:02:00 sina.ru 34
```

## Решение

Код: [main.py](https://github.com/bgelov/funbox-async-api-count/blob/main/main.py)

- Обращения к API происходит каждую минуту в 00 секунд
- Обращения происходят асинхронно

![pycharm64_ZBFp1rLoGB](https://github.com/bgelov/funbox-async-api-count/assets/5302940/9d7c4b49-6dc9-46dd-98c1-a3d40e5c93e4)

- В случае недоступности хоста выводим в консоль ошибку и значение прочерк

![buidL4lMP5](https://github.com/bgelov/funbox-async-api-count/assets/5302940/091526d1-94d2-4aa3-bfe1-942976135a0b)
