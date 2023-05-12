import data
import sender_requests


# Функция на создание заказа и сохранения её трек-номера
def get_track_number(body):
    # 1. Отправим запрос на создание заказа и запишем тело ответа
    order_response = sender_requests.post_new_order(body)
    # 2. Перепишем заголовок header_track_number в data.py
    data.param_track_number["t"] = order_response.json()["track"]
    # Всё заказ создан, а его трек-номер сохранён


# Тесты:
# Проверим, что после запроса на создание заказа, он был внесен в таблицу Orders
def test_check_order_by_his_number():
    # 1. Отправим запрос на создание заказа и сохраним его трек-номер в data.param_track_number
    get_track_number(data.body_order_correct)
    # 2. Отправим запрос на получение заказа по трек-номеру, что мы получили выше, и запишем ответ
    body_request = sender_requests.get_order_by_his_number(data.param_track_number)
    # 3. Проверим, что бэкенд нашел заказ с таким трек-номером в таблице Orders
    assert body_request.status_code == 200
