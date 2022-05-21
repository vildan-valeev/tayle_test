# Описание
Пользователь имеет свой аккаунт, у которого может быть несколько счетов со
своим неотрицательным балансом. Остальные поля моделей продумать исходя из
нижеследующего задания.
Пользователей в системе может быть очень много.
Необходимо реализовать страницу, где пользователь сможет:
- найти и выбрать счет другого пользователя, которому он хочет перевести
валюту
- выбрать один или несколько из своих счетов
- указать сумму, которую он хочет перевести
Сумма для перевода должна быть снята равномерно со всех выбранных
пользователем счетов. Так например, если пользователь выбрал 3 своих счета и хочет
перевести 300р, то с каждого счета должно быть снято по 100р.
- 
Также должны быть страницы, где пользователь сможет:
- просматривать все свои переводы, с возможностью пагинации, поиска и
фильтрации по счетам (опционально: по дате, сумме перевода)

- просматривать полную информацию о счете, отдельной страницей
Реализовать с помощью Django и Python 3. Прочие инструменты, такие как DRF,
Celery: опциональны.
Код должен соответствовать PEP8.
Плюсом будет покрытие кода юнит-тестами.
Необходимо все упаковать в Docker - контейнеры.
- 
Опционально(не обязательно к выполнению):
- Продумать отмену транзакции


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
```makefile
$ make develop
```
Создание пользователя из фикстур.
```shell
docker exec -it app poetry run python manage.py loaddata default_data.json
```


---
# Database dump/load
```shell
$ docker exec -it app sh -c "poetry run python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > default_data.json"
docker exec -it app poetry run python manage.py loaddata default_data.json
```
## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```
---
## TODO:
1. Убрать линтеры из poetry во время сборки
2. Убрать db из репозитория(добавил для удобства клонирования и запуска, чтобы не возиться с фикстурами)
3. Написать тесты
4. настроить постгрес

