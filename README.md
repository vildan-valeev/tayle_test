# Описание
Система управления стратегиями, с возможностью подключения пользователей(со своим токеном) к выбранной стратегии<br>

Котировки и информация, которая требуется для визуализации по продуктам, <b>App</b> запрашивает по api "напрямую".<br>
Подразумевается, что токен для этого будет использоваться общий (независимый, read only) на всю систему,<br> 
а токены для торговли будут у каждого пользователя и стратегии свои. В рамках проекта используется один токен для app<br>
и для user.<br>

Котировки и информация которая требуется для алготрейдинга, <b>Bot</b> будет получать сам по api.<br>

Результаты торговых операций, ошибки и сообщения, <b>bot</b> будет передавать в app по REST API на DRF.

---
app - приложение для хранения и визуализации данных в браузере, а также для управления торговлей ботом<br>
Стек: django, DRF, postgresql, фронт на шаблонизаторе

bot - приложение(асинхронное) для работы с API Tinkoff, бизнес-логика алгоритмического трейдинга на<br>
несколько алгоритмов и пользователей, с возможностью подключения, отключения, проведения тестов, <br>
выполнения других комманд из <b>App</b> и тд<br>
Стек: aiohttp, 
--- 


---
Requirements for dev:
1. [make](https://www.gnu.org/software/make/)
2. [docker](https://docs.docker.com/engine/install/)
3. [docker-compose](https://docs.docker.com/compose/install/)
4. [python 3.8+](https://www.python.org/downloads/release/python-380/)
---
# Запуск

### Помощь
```makefile
$ make help
```
Вводить дополнительно ничего не нужно, добавление своего токена через админку или пользовательский личный кабинет.

---
## TODO:
1. Убрать из индекса local.py, .env (добавлен только для наглядности...)
2. Для продакшена желательно разделить проект на разные репозитории. Make-команды общие на весь проект
