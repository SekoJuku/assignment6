from sqlalchemy import func, select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from core import get_db
from model import *
from schema import *

api = APIRouter(tags=["API"])

@api.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@api.get('/admin')
def get_all_admins(
    db: Session = Depends(get_db)
):
    users = db.query(User).filter(User.role == "admin").order_by(User.username).all()
    res = list()
    for e in users:
        res.append(UserResponse(e))
    return res


@api.get("/recipe")
def get_all_recipes(
    db: Session = Depends(get_db)
):
    recipes = db.query(Recipe).all()
    res = list()
    for e in recipes:
        res.append(UserRecipeResponse(e))        
    return res


@api.get("/recipe/{id}")
def get_recipe_by_user(
    id: int,
    db: Session = Depends(get_db)
):
    recipes = db.query(Recipe).filter(Recipe.author_id == id).all()
    res = list()
    for e in recipes:
        res.append(RecipeResponse(e))
    return res


@api.get("/recipe/ingredients/{id}")
def get_ingredients_by_recipe_id(
    id: int,
    db: Session = Depends(get_db)
):
    ingredients = db.query(Ingredient).filter(Ingredient.recipe_id == id).all()
    res = list()
    for e in ingredients:
        res.append(IngredientResponse(e))
    return res


@api.get("/difficulty")
def get_recipe_difficulties(
    db: Session = Depends(get_db)
):
    recipes = db.query(Recipe).all()
    res = list()
    for e in recipes:
        res.append(RecipeDifficultyResponse(e))
    return res


@api.get("/ingredient")
def get_count_of_ingredients_by_category(
    db: Session = Depends(get_db)
):
    categories = db.query(Category).all()
    res = list()
    for category in categories:
        size = db.query(Ingredient).filter(Ingredient.category_name == category.category_name).count()
        res.append(CategoryRecipeResponse(category.category_name, size))
    return res


@api.get("/recipe/posted/", response_model=list[RecipeResponse])
def get_posted(
    db: Session = Depends(get_db)
):
    recipes = db.query(Recipe).filter(Recipe.is_posted == True).all()
    return recipes


@api.get("/recipe/easy/")
def get_easy_recipes(
    db: Session = Depends(get_db)
):
    recipes = db.query(Recipe).join(Recipe.difficulty).filter(Difficulty.users_rating < 1.5).all()
    return recipes


@api.get("/ingredient/")
def get_count_of_ingredients(
    db: Session = Depends(get_db)
):
    return db.query(Ingredient.ingredient_id).count()
