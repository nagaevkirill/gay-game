import json
from random import randint


def reg_user(user_id, user_name):
    check_unique = True
    with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
        data_raw = json.load(file)
        users_dict = data_raw['users']

        # проверка что пользователя нет в базе данных
        for item in users_dict:
            if item == user_id:
                check_unique = False

        # если пользака нет, то добавляем
        if check_unique:
            users_dict.update({user_id: {
                                            'name': user_name,
                                            'pidor_count': 0
                                        }
            })
            with open('pid_data/new_db.json', 'w', encoding='UTF-8') as file:
                json.dump(data_raw, file, indent=4)
            return 'Ты зареган, бро'
        else:
            return 'Ты уже зарегистрирован'

def return_statistic():
    card_info = ''
    with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
        user_dict = json.load(file)['users']

        for item in user_dict:
            card_info = card_info + user_dict[item]['name'] + ' был пидором ' + str(user_dict[item]['pidor_count']) + ' раз(а) \n'

        return card_info

def gaycount_update(user_id):
    with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
        data_raw = json.load(file)
        users_dict = data_raw['users']
        # print(users_dict)
        user_card = {
            "name": users_dict[user_id]['name'],
            "pidor_count": users_dict[user_id]['pidor_count'] + 1
        }
        users_dict.update({user_id: user_card})
        with open('pid_data/new_db.json', 'w', encoding='UTF-8') as file:
            json.dump(data_raw, file, indent=4)
        return 1

def viktorina():
    # Считываем с БД запускалась ли викторина
    with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
        data_raw = json.load(file)
        users_dict = data_raw['params']

    if users_dict["viktorina-was-started"] == "no":
        with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
            data_raw = json.load(file)
            users_dict = data_raw['users']
            user_list = []
            # Собираем список всех пользователей и выбираем из них случайным образом "счастливчика"
            for item in users_dict:
                user_list.append(item)
        user_id = user_list[randint(1, len(user_list))-1]
        user_name = users_dict[user_id]['name']

        # обращаемся к базе и обновляем стату пользаку
        res_count = gaycount_update(user_id)

        # проставить флаг успешно запущенной викторины на пидордня
        if res_count == 1 :
            with open('pid_data/new_db.json', 'r', encoding='UTF-8') as file:
                data_raw = json.load(file)
                param_dict = data_raw['params']
                param_dict['viktorina-was-started'] = 'yes'
            with open('pid_data/new_db.json', 'w', encoding='UTF-8') as file:
                json.dump(data_raw, file, indent=4, ensure_ascii=False)
        # вернуть результат викторины боту. для опубликования в ТГ
        return 'Пидором дня становится - ' + user_name
    else:
        return 'Пидор дня уже был запущен сегодня'

# print(viktorina())
# print(gaycount_update('ID777'))
# print(reg_user("ID777", "kir"))
# print(return_statistic())



