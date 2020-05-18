# IQSMS REST Gate

Модуль для работы с REST API смс-шлюза [iqsms.ru](https://iqsms.ru/) (СМС Дисконт)

## Установка

```bash
pip install iqsms-rest
```

## Использование

Для начала использования необходимо инициализировать шлюз при помощи логина и пароля к личному кабинету:
```python
from iqsms import Gate

gate = Gate('login', 'password')
```

### Отправка сообщений

```python
gate.send_message('79990001122', 'Hello, World!')
```
