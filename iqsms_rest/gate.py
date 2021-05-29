import base64

# noinspection PyPackageRequirements
import requests


class Gate:
    def __init__(self, login, password, sender=None, root_uri=None):
        self.login = login
        self.password = password
        self.sender = sender
        self.root_uri = root_uri or 'http://api.iqsms.ru/messages/v2/'

    def __get_auth_header(self):
        str_cred = f'{self.login}:{self.password}'
        b64_cred = base64.b64encode(bytes(str_cred, 'utf-8'))
        return {'Authorization': f'Basic {b64_cred.decode("utf-8")}'}

    def __send_request(self, uri, payload=None):
        try:
            r = requests.get(f'{self.root_uri}{uri}', params=payload, headers=self.__get_auth_header())
            return r.text
        except IOError as e:
            return dir(e)

    def balance(self):
        """Проверка состояния счета
        При успешной авторизации, в ответ сервис должен вернуть plain/text ответ вида:
        RUB;540.15
        где в каждой строке 1 значение – тип баланса, 2 значение – баланс.
        :return:
        """
        return self.__send_request('balance')

    def senders(self):
        """Список доступных подписей отправителя
        При успешной авторизации, в ответ сервис должен вернуть plain/text ответ вида:
        Sender_one
        Sender_two
        Sender_three
        где выводится список доступных подписей по одной в каждой строке.
        :return:
        """
        return self.__send_request('senders')

    def status_queue(self, status_queue_name, limit=1):
        """Проверка очереди статусов отправленных сообщений
        :param status_queue_name: Название очереди статусов сообщений. Название очереди устанавливается при передаче сообщения
        :param limit: Количество запрашиваемых статусов из очереди (по умолчанию 1, макс. 1000)
        :return:
        """
        return self.__send_request('statusQueue', {'statusQueueName': status_queue_name, 'limit': limit})

    def status_message(self, ids: list):
        """Проверка состояния отправленного сообщения (до 200 id в запросе)
        :param ids: массив идентификаторов сообщений, которые вернул сервис при отправке сообщений
        :return:
        """
        return self.__send_request('status', {'id': i for i in ids})

    def send_message(self, phone, text, wap_url=None, sender=None, flash=None, schedule_time=None,
                     status_queue_name=None):
        """Передача сообщения
        :param phone: Номер телефона, в формате +71234567890
        :param text: Текст сообщения, в UTF-8 кодировке
        :param wap_url: Wap-push ссылка, в случае, если вы хотите передать wap-push сообщение (например wap.yousite.ru)
        :param sender: Подпись отправителя (например TEST)
        :param flash: Flash SMS – сообщение, которое сразу отображается на экране
        и не сохраняется в памяти телефона (1 – активировано)
        :param schedule_time: Дата для отложенной отправки сообщения, в UTC (2009-01-01T12:30:01+00:00)
        :param status_queue_name: Название очереди статусов отправленных сообщений, в случае, если вы хотите
        использовать очередь статусов отправленных сообщений. От 3 до 16 символов, буквы и цифры (например myQueue1)
        :return:
        """
        payload = {'phone':           phone,
                   'text':            text,
                   'wapurl':          wap_url,
                   'sender':          sender or self.sender,
                   'flash':           flash,
                   'scheduleTime':    schedule_time,
                   'statusQueueName': status_queue_name}
        return self.__send_request('send', payload)
