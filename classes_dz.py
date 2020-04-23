from pprint import pprint


class Pets:  # объявление класса Животные
    def __init__(self, kind_of, nickname, weight, voice, character, status, QRcode):
        self.kind_of = kind_of  # вид животного
        self.weight = weight  # масса
        self.animal_voice = voice  # голосовое сообщение от животного
        self.nickname = nickname  # кличка питомца
        self.character = character  # Характер (нордический)
        self.status = status  # накормлено/ненакормлено/не нуждается в накормлено
        self.QRcode = QRcode  # скотоизоляция

    def gimme_skream(self):  # заставь животину заговорить
        return self.animal_voice

    def FedTheAnimal(self):  # метод "накормить" со сменой статуса на "сыт"
        self.status = 'покормлен'
        pprint('Скотина "' + self.nickname + "\": Статус: " + self.status)

    def identification(self):  # Электронный паспорт животного
        pprint('КЛАСС: ' + self.kind_of + '; Кличка: ' + self.nickname +
               '; Вес: ' + str(self.weight) + 'кг.; ' + 'Характер: ' + self.character +
               '; Cтатус: ' + self.status)

    def cattle_walking(self):  # COVID - 19
        if self.QRcode:
            print('Выгул в радиусе 100 метров разрешен')
        else:
            print('Выгул запрещен. Для получения QR кода воспользуйтесь приложением "Колхоз-услуги"')


class egg_out(Pets):  # несение яиц/ характерно для пернатых
    def profit(self):
        if self.nickname == 'Черный плащ':
            print('Черный плащ не несет яйца! он их сшибает!')
        else:
            print('Снесло яйцо чудище пернатое, да не простое, а с плавающей точкой')


class yeld_of_milk(Pets):  # генерация молочных изделий без заменителя молочного жира
    def profit(self):
        print('Мы молока не видали пока')


class woolen(Pets):  # Генерация шерсти мериносов
    def profit(self):
        print('С паршивой овцы хоть что-нибудь')


unkleJoeFarm = []  # Удивительная мультикультурная ферма дядюшки Джо, где есть правда и вымысел, сон и явь :)
# добавление животных на ферму представлено ниже:
unkleJoeFarm.append(egg_out(
    'Селезень', 'Черный плащ', 100500, 'Ну-ка, от винта!', 'борец с преступностью, герой и внештатный агент ШУШУ',
    'Голоден', True))
# gus1 = yeld_of_milk('Селезень','Черный плащ',20,'Ну-ка, от винта!','борец с преступностью, герой и внештатный агент ШУШУ','Голоден',True)
unkleJoeFarm.append(egg_out(
    'Селезень', 'Скрудж McDuck', 40, 'Я съем твою шляпу, как только у тебя окажется больше денег, чем у меня!'
    , 'миллиардер', 'Сыт', True
))
unkleJoeFarm.append(egg_out('Курица','Ко-Ко',3,'Кудах тах тах','Скучная курица из задания, пойдет в суп','Голоден',False))
unkleJoeFarm.append(egg_out('Курица','Куку-Руку',4,'Кудах тах тах','Скучная курица из задания, пойдет в суп','Голоден',False))
unkleJoeFarm.append(yeld_of_milk('Корова','Мурка',3,'Му, чего уж там','Корова из "Простоквашино"','Голоден',True))
unkleJoeFarm.append(yeld_of_milk('Коза','Рогатая',3,'Забодаю-забодаю','Пришла коза рогатая за нарушителями самоизоляции','Голоден',False))
unkleJoeFarm.append(woolen('Овечка','Долли',20,'Немая','Скучная курица из задания, пойдет в суп','Голоден',False))
unkleJoeFarm.append(woolen('Барашек','Шон',40,'Жестикулирует','Озорной, постоянно ищет приключения, всегда трезво оценивает ситуацию (Википедия)','Голоден',True))
temp_weight = unkleJoeFarm[0]
sum_weight = 0
for pet in unkleJoeFarm:
    pet.identification()
    pprint('Говорит: '+ pet.gimme_skream())
    pet.cattle_walking()
    pet.profit()
    #    name = pet.nickname
    weight = pet.weight
    #    print(weight)
    #    print(temp_weight.weight)
    sum_weight += weight
    if weight > temp_weight.weight:
        temp_weight = pet
#        print(weight)
print(sum_weight)
print(f'{temp_weight.nickname} самый тяжелый с весом {temp_weight.weight}')
#       name = pet.nicknam
#   print(name)
