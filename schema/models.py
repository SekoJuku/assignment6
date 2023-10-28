from pydantic import BaseModel

from model import *
from model import Recipe

class UserResponse:
    user_id: str
    username: str
    role: str
    
    def __init__(self, user: User):
        self.user_id = user.user_id
        self.username = user.username
        self.role = user.role        


class UserRecipeResponse:
    username: str
    title: str
    is_posted: bool

    def __init__(self, recipe: Recipe):
        self.username = recipe.author.username
        self.title = recipe.title
        self.is_posted = recipe.is_posted


class RecipeResponse(UserRecipeResponse):
    recipe_id: int
    serving_size: int
    cooking_time: str
    
    def __init__(self, recipe: Recipe):
        super().__init__(recipe)
        self.recipe_id = recipe.recipe_id
        self.serving_size = recipe.serving_size
        self.cooking_time = recipe.cooking_time


class IngredientResponse:
    recipe_id: int
    title: str
    calories_per_unit: float
    carbohydrates_per_unit: float
    fat_per_unit: float
    protein_per_unit: float
    
    def __init__(self, ingredient: Ingredient):
        self.recipe_id = ingredient.recipe_id
        self.title = ingredient.recipe.title
        nutrition: NutritionValue = ingredient.nutrition
        self.calories_per_unit = nutrition.calories_per_unit
        self.carbohydrates_per_unit = nutrition.carbohydrates_per_unit
        self.fat_per_unit = nutrition.fat_per_unit
        self.protein_per_unit = nutrition.protein_per_unit


class RecipeDifficultyResponse:
    recipe_id: int
    title: str
    difficulty: str

    def __init__(self, recipe: Recipe):
        self.recipe_id = recipe.recipe_id
        self.title = recipe.title
        difficulty: Difficulty = recipe.difficulty
        self.difficulty = self.determine_difficulty(difficulty.number_of_step, difficulty.users_rating)

    def determine_difficulty(self, steps: int, rating: float):
        if steps > 10 and rating > 2.5 and rating < 3.0:
            return "HARD"
        if steps > 5 and steps < 10 and rating > 1.5 and rating < 2.5:
            return "MEDIUM"
        return "EASY"


class CategoryRecipeResponse:
    category_name: str
    size: int
    
    def __init__(self, name: str, size: int) -> None:
        self.category_name = name
        self.size = size


class RecipeResponse(BaseModel):

    recipe_id: int
    author_id: int
    title: str
    serving_size: int
    is_posted: int
    cooking_time: str
    diff_id: int
