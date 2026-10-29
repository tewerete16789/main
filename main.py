meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'РОФЛ': 'шутка',
            'АГРИТЬСЯ': 'злиться'
            }
print('Zdravstvyite, eto pomoshnik perevoda izika podrostkov')
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('net nyshnogo slova')
