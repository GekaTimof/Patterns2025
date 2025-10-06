from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model
from Src.Models.Ingredient_model import ingredient_model

###############################################
# Модель для хранения рецептов
# Хранит массив всех ингридиентов. Каждый ингридиент храниет
# (название ингредиента, количество, еденицы измерения)
###############################################
class recipe_model(abstact_model):
    def __init__(self, name: str = None):
        super().__init__()
        if name is not None: self.name = name
        # Массив ингридиентов
        self.__ingredients = []

    @property
    def ingredients(self) -> list[ingredient_model]:
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: list[ingredient_model]):
        validator.validate(value, list)
        for item in value:
            validator.validate(item, ingredient_model)
        self.__ingredients = value

    # Метод для добавления одного ингредиента
    def add_ingredient(self, ingredient: ingredient_model):
        validator.validate(ingredient, ingredient_model)
        self.__ingredients.append(ingredient)

    # Метод для удаления ингредиента
    def remove_ingredient(self, ingredient: ingredient_model):
        if ingredient in self.__ingredients:
            self.__ingredients.remove(ingredient)

    # Фабричный метод для формирования рецепта с названием из массива ингридиентов
    @staticmethod
    def create_recipe(self, name: str, ingredients) -> 'recipe_model':
        item = recipe_model(name)
        for ingredient in ingredients:
            item.add_ingredient(ingredient)
        return item
