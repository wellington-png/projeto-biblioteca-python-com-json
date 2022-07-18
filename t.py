from datetime import datetime, timedelta

now = datetime.now


def soma_data(data, dias):
    data = data + timedelta(days=dias)
    return data


def str_to_datetime(data):
    data = datetime.strptime(data, "%d/%m/%Y")
    return data


def datetime_to_str(data):
    data = data.strftime("%d/%m/%Y")
    return data


print(type(str_to_datetime("01/01/2020")))
print(type(datetime_to_str(datetime.now())))
