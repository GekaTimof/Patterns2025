from Src.Models.Ingredient_model import ingredient_model
from Src.Models.measurement_model import measurement_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.recipe_model import recipe_model
from Src.reposity import reposity

class start_service:
    __repo: reposity = reposity()

    # создаём пустые словари под ключевые параметры
    def __init__(self):
        self.__repo.data[reposity.measurement_key]: dict = {}
        self.__repo.data[reposity.nomenclature_group_key]: dict = {}
        self.__repo.data[reposity.nomenclature_key]: dict = {}
        self.__repo.data[reposity.recipes_key]: dict = {}


    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance


    # Функция которая задаёт базовые еденицы измерения
    def __default_create_measurements(self):
        # gr - грамм, kg - килограмм, ml - миллилитр, l - литр
        self.__repo.data[reposity.measurement_key]['гр'] = measurement_model.create_gram()
        self.__repo.data[reposity.measurement_key]['кг'] = measurement_model.create_kilogram()
        self.__repo.data[reposity.measurement_key]['л'] = measurement_model.create_liter()
        self.__repo.data[reposity.measurement_key]['мл'] = measurement_model.create_milliliter()


    # Функция которая задаёт базовые группы номенклатур
    def __default_create_nomenclature_group(self):
        group_key = reposity.nomenclature_group_key
        self.__repo.data[group_key]['ММП'] = (
            nomenclature_group_model('ММП', 'Мясо и мясные продукты'))
        self.__repo.data[group_key]['ОК'] = (
            nomenclature_group_model('ОК', 'Овощи и корнеплоды'))
        self.__repo.data[group_key]['Ж'] = (
            nomenclature_group_model('Ж', 'Жидкости'))
        self.__repo.data[group_key]['МП'] = (
            nomenclature_group_model('МП', 'Молочные продукты'))
        self.__repo.data[group_key]['ФЯ'] = (
            nomenclature_group_model('ФЯ', 'Фрукты и ягоды'))
        self.__repo.data[group_key]['ПД'] = (
            nomenclature_group_model('ПД', 'Подсластители и добавки'))
        self.__repo.data[group_key]['ЛО'] = (
            nomenclature_group_model('ЛО', 'Лёд и охлаждающие продукты'))


    # Функция которая задаёт базовые номенклатуры
    def __default_create_nomenclature(self):
        group_key = reposity.nomenclature_group_key
        mes_key = reposity.measurement_key
        self.__repo.data[reposity.nomenclature_key]['Говядина'] = nomenclature_model(
            'Говядина', self.__repo.data[group_key]['ММП'], self.__repo.data[mes_key]['кг'])
        self.__repo.data[reposity.nomenclature_key]['Картофель'] = nomenclature_model(
            'Картофель', self.__repo.data[group_key]['ОК'], self.__repo.data[mes_key]['гр'])
        self.__repo.data[reposity.nomenclature_key]['Морковь'] = nomenclature_model(
            'Морковь', self.__repo.data[group_key]['ОК'], self.__repo.data[mes_key]['гр'])
        self.__repo.data[reposity.nomenclature_key]['Лук'] = nomenclature_model(
            'Лук', self.__repo.data[group_key]['ОК'], self.__repo.data[mes_key]['гр'])
        self.__repo.data[reposity.nomenclature_key]['Томатный сок'] = nomenclature_model(
            'Томатный сок', self.__repo.data[group_key]['Ж'], self.__repo.data[mes_key]['мл'])
        self.__repo.data[reposity.nomenclature_key]['Вода'] = nomenclature_model(
            'Вода', self.__repo.data[group_key]['Ж'], self.__repo.data[mes_key]['л'])
        self.__repo.data[reposity.nomenclature_key]['Замороженные ягоды'] = nomenclature_model(
            'Замороженные ягоды', self.__repo.data[group_key]['ФЯ'], self.__repo.data[mes_key]['гр'])
        self.__repo.data[reposity.nomenclature_key]['Натуральный йогурт'] = nomenclature_model(
            'Натуральный йогурт', self.__repo.data[group_key]['МП'], self.__repo.data[mes_key]['мл'])
        self.__repo.data[reposity.nomenclature_key]['Мед'] = nomenclature_model(
            'Мед', self.__repo.data[group_key]['ПД'], self.__repo.data[mes_key]['мл'])
        self.__repo.data[reposity.nomenclature_key]['Лимонный сок'] = nomenclature_model(
            'Лимонный сок', self.__repo.data[group_key]['Ж'], self.__repo.data[mes_key]['мл'])
        self.__repo.data[reposity.nomenclature_key]['Лёд'] = nomenclature_model(
            'Лёд', self.__repo.data[group_key]['ЛО'], self.__repo.data[mes_key]['гр'])

    # создание массива ингридиентов из массива пар - (номенклатура, количество)
    @staticmethod
    def create_ingredients(data: list):
        ingredients = []
        for nomenclature, amount in data:
            ingredients.append(ingredient_model(nomenclature, amount))
        return ingredients

    # Создание рецепта из массива ингридиентов
    def create_recipe(self, name: str, data: list):
        ingredients = self.create_ingredients(data)
        recipe = recipe_model.create_recipe(name, ingredients)
        self.__repo.data[reposity.recipes_key][name] = recipe

    # Стартовый набор данных
    def data(self):
        return self.__repo.data


    # Основной метод для генерации эталонных данных
    def start(self):
        self.__default_create_measurements()
        self.__default_create_nomenclature_group()
        self.__default_create_nomenclature()


    # Метод создающиё рецепты на основе эталонных данных
    def create(self):
        nomenclatures = self.__repo.data[reposity.nomenclature_key]
        measurements = self.__repo.data[reposity.measurement_key]

        # создаём первый рецепт (Тущёное мясо с овощами)
        name1 = "Тущёное мясо с овощами"
        data1 = [
            (nomenclatures["Говядина"], 1),
            (nomenclatures["Картофель"], 500),
            (nomenclatures["Морковь"], 300),
            (nomenclatures["Лук"], 200),
            (nomenclatures["Томатный сок"], 500),
            (nomenclatures["Вода"], 1),
        ]
        self.create_recipe(name1, data1)

        # создаём второй рецепт (Коктейль ягодный с йогуртом)
        name2 = "Коктейль ягодный с йогуртом"
        data2 = [
            (nomenclatures["Замороженные ягоды"], 400),
            (nomenclatures["Натуральный йогурт"], 300),
            (nomenclatures["Вода"], 1),
            (nomenclatures["Мед"], 50),
            (nomenclatures["Лимонный сок"], 20),
            (nomenclatures["Лёд"], 200),
        ]
        self.create_recipe(name2, data2)


service = start_service()
service.start()
service.create()
print("end")