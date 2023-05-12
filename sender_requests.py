import requests
import configuration


# Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVER + configuration.ORDER_CREATE,  # подставляем полный url
                         json=body)  # здесь тело запроса


# Запрос на получение заказа по его трек-номеру
def get_order_by_his_number(parameters):
    return requests.get(configuration.URL_SERVER + configuration.ORDER_RECEIPT, # подставляем полный url
                        params=parameters)  # здесь параметры запроса
