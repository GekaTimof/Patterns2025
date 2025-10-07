import unittest
from Src.reposity import reposity
from Src.start_service import start_service


# Класс для проверки запуска (переиспользование)
class test_start(unittest.TestCase):
    __start_service: start_service = start_service()

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.__start_service.start()

    # Проверка, что при старте сервиса создаются начальные еденицы измерения
    def test_start_service_rangeNotEmpty(self):
        # Подготовка

        # Действие

        # Проверка
        assert len(self.__start_service.data()) > 0

    # Проверка, что единицы измерения с одинаковым названием это одни и те же еденица измерения
    def test_measurement_relationships(self):
        # Подготовка
        kilogram = self.__start_service.data()[reposity.measurement_key]['кг']
        gram = self.__start_service.data()[reposity.measurement_key]['гр']

        # Действие

        # Проверка
        assert kilogram.base_unit == gram

    # Проверка создания единиц измерения
    def test_measurements_created(self):
        # Подготовка
        measurements = self.__start_service.data()[reposity.measurement_key]

        # Действие

        # Проверка
        assert 'гр' in measurements
        assert 'кг' in measurements
        assert measurements['гр'].name == "gram"
        assert measurements['кг'].name == "kilogram"

    # Проверка установки коэффициента преобразования
    def test_measurement_coefficient(self):
        # Подготовка
        kilogram = self.__start_service.data()[reposity.measurement_key]['кг']

        # Действие

        # Проверка
        assert kilogram.coefficient == 1000

    # Проверка Singleton паттерна
    def test_singleton_pattern(self):
        # Подготовка
        service1 = start_service()
        service2 = start_service()

        # Действие

        # Проверка
        assert service1 is service2

    # Проверка создания групп номенклатур
    def test_nomenclature_groups_creation(self):
        # Подготовка
        groups = self.__start_service.data()[reposity.nomenclature_group_key]

        # Действие

        # Проверка
        assert 'ММП' in groups
        assert groups['ММП'].name == 'ММП'
        assert groups['ММП'].description == 'Мясо и мясные продукты'

    # Проверка создания номенклатур
    def test_nomenclature_creation(self):
        # Подготовка
        nomenclatures = self.__start_service.data()[reposity.nomenclature_key]
        measurement = self.__start_service.data()[reposity.measurement_key]['кг']

        # Действие

        # Проверка
        assert 'Говядина' in nomenclatures
        assert nomenclatures['Говядина'].full_name == 'Говядина'
        assert nomenclatures['Говядина'].measurement == measurement

    # Проверка создания рецептов
    def test_recipes_creation(self):
        # Подготовка
        self.__start_service.create()
        recipes = self.__start_service.data()[reposity.recipes_key]

        # Действие

        # Проверка
        assert 'Тущёное мясо с овощами' in recipes
        assert 'Коктейль ягодный с йогуртом' in recipes

    # Проверка названия и количества ингредиентов рецепта "Тущёное мясо с овощами"
    def test_meat_recipe_ingredients(self):
        # Подготовка
        self.__start_service.create()
        recipes = self.__start_service.data()[reposity.recipes_key]
        meat_recipe = recipes['Тущёное мясо с овощами']

        # Действие

        # Проверка
        assert len(meat_recipe.ingredients) == 6
        assert meat_recipe.name == 'Тущёное мясо с овощами'

    # Проверка названия и количества ингредиентов рецепта "Коктейль ягодный с йогуртом"
    def test_cocktail_recipe_ingredients(self):
        # Подготовка
        self.__start_service.create()
        recipes = self.__start_service.data()[reposity.recipes_key]
        cocktail_recipe = recipes['Коктейль ягодный с йогуртом']

        # Действие

        # Проверка
        assert len(cocktail_recipe.ingredients) == 6
        assert cocktail_recipe.name == 'Коктейль ягодный с йогуртом'

    # Проверка корректности ингредиентов в рецептах
    def test_recipe_ingredients_correctness(self):
        # Подготовка
        self.__start_service.create()
        recipes = self.__start_service.data()[reposity.recipes_key]
        meat_recipe = recipes['Тущёное мясо с овощами']

        # Действие

        # Проверка
        ingredient_names = [ing.nomenclature.full_name for ing in meat_recipe.ingredients]
        assert 'Говядина' in ingredient_names
        assert 'Картофель' in ingredient_names
        assert 'Морковь' in ingredient_names
        assert 'Лук' in ingredient_names
        assert 'Томатный сок' in ingredient_names
        assert 'Вода' in ingredient_names

# Закрывающая скобка класса