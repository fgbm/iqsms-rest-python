![Pypi version](https://img.shields.io/pypi/v/iqsms-rest.svg)
![Python versions](https://img.shields.io/pypi/pyversions/iqsms-rest)
[![Upload Python Package](https://github.com/fgbm/iqsms-rest-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/fgbm/django-tmmis/actions/workflows/python-publish.yml)

# IQSMS REST Gate

Модуль для работы с REST API смс-шлюза [iqsms.ru](https://iqsms.ru/) (СМС Дисконт)

## Установка

```bash
pip install iqsms-rest
```

## Использование

Для начала использования необходимо инициализировать шлюз при помощи логина и пароля к личному кабинету:
```python
from iqsms_rest import Gate

gate = Gate('login', 'password')
```

### Отправка сообщений

```python
gate.send_message('79990001122', 'Hello, World!')
```
