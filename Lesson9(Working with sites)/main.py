import urllib.request
import requests

# создаем объект, который будет раскрывать сайт
opener = urllib.request.build_opener()

response = opener.open("https://httpbin.org/get") # берем данные сайта urllib.requests
print(response.read())

print("\n\n") # ответы будут разные

response = requests.get("https://httpbin.org/get") # берем данные сайта requests
print(response.content)


print("\n\n")

# создаем объект, который будет раскрывать сайты
# создание post запроса с данными header
response = requests.post("https://httpbin.org/post", data="Salam", headers={"h1": "Ay Rafael!"})
print("text - ", response.text)



"""Парсинг сайтов"""

response = requests.get("https://coinmarketcap.com")
print(response.text, "\n\n")

res_parse_list = []

# делим сайт на строчные элементы
response_text = response.text
response_parse = response_text.split("<span>")

# парсим все через знак доллара
for parse_elem1 in response_parse:
    if(parse_elem1.startswith("$")):
        for parse_elem2 in parse_elem1.split("</span>"):
            # проверяем если знак доллара есть и второй элемент цифра - значит это курс
            if(parse_elem2.startswith("$") and parse_elem2[1].isdigit()):
                res_parse_list.append(parse_elem2)

# узнаем курс биткоина
bitcoin_exchange_rate = res_parse_list[1]
print(res_parse_list, "\n\n")
print(bitcoin_exchange_rate)