import data
import sender_requests


# Функция создание заказа и формирование params для запроса на получение этого заказа
def get_params_of_track_number(body):
    # 1. Отправим запрос на создание заказа и запишем тело ответа
    order_response = sender_requests.post_new_order(body)
    # 2. Подготовим основу для запроса к получению заказа по трек-номеру
    params_tack_number = data.param_track_number
    # 3. Запишем актуальный трек-номер заказа в params_tack_number
    params_tack_number["t"] = order_response.json()["track"]
    # Всё заказ создан, а его трек-номер сформирован и сохранён. Выведем её на выход этой функции
    return params_tack_number


# Тесты:
# Проверим, что после запроса на создание заказа, он был внесен в таблицу Orders
def test_check_order_by_his_number():
    # 1. Отправим запрос на создание заказа и сохраним его трек-номер в виде params
    params_for_get_order = get_params_of_track_number(data.body_order_correct)
    # 2. Отправим запрос на получение заказа по трек-номеру, что мы получили выше, и запишем ответ
    body_request = sender_requests.get_order_by_his_number(params_for_get_order)
    # 3. Проверим, что бэкенд нашел заказ с таким трек-номером в таблице Orders
    assert body_request.status_code == 200
