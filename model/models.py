from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Float
from sqlalchemy.orm import relationship

from core import Base


class User(Base):
    __tablename__ = "User"

    user_id= Column(Integer, primary_key=True, nullable=False)
    username= Column(String, nullable=False)
    password= Column(String, nullable=False)
    role= Column(String, nullable=False)
    email= Column(String, unique=True)
    age= Column(Integer, nullable=False)


class Admin(Base):
    __tablename__ = "Admin"
    
    id= Column(Integer, primary_key=True, nullable=False)
    user_id= Column(Integer, ForeignKey("User.user_id"))
    admin_permissions= Column(String, nullable=False)
    admin_role= Column(String, nullable=False)

    user = relationship("User")


class RegisteredUser(Base):
    __tablename__ = "RegisteredUser"
    
    id= Column(Integer, primary_key=True, nullable=False)
    user_id= Column(Integer, ForeignKey("User.user_id"))
    user_level= Column(String, nullable=False)
    support_messages= Column(JSON, nullable=False)


class Category(Base):
    __tablename__ = "Category"
    
    category_name= Column(String, primary_key=True, nullable=False)
    description= Column(String, nullable=False) 


class NutritionValue(Base):
    __tablename__ = "NutritionValue"
    
    nv_id= Column(Integer, primary_key=True, nullable=False)
    calories_per_unit= Column(Float, nullable=False)
    carbohydrates_per_unit= Column(Float, nullable=False)
    fat_per_unit= Column(Float, nullable=False)
    protein_per_unit = Column(Float, nullable=False)
    

class Ingredient(Base):
    __tablename__ = "Ingredient"
    
    ingredient_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    measurement_unit = Column(String, nullable=False)
    category_name = Column(String, ForeignKey("Category.category_name"))
    nv_id = Column(Integer, ForeignKey("NutritionValue.nv_id"))
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"))

    recipe = relationship("Recipe")
    nutrition = relationship("NutritionValue", foreign_keys=[nv_id])


class Difficulty(Base):
    __tablename__ = "Difficulty"
    
    diff_id = Column(Integer, primary_key=True, nullable=False)
    preparation_time = Column(String, nullable=False)
    cooking_time = Column(String, nullable=False)
    number_of_step = Column(Integer, nullable=False)
    users_rating = Column(Float, nullable=False)


class Recipe(Base):
    __tablename__ = "Recipe"

    recipe_id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer, ForeignKey("User.user_id"))
    title = Column(String, unique=True, nullable=False)
    serving_size = Column(Integer, nullable=False)
    is_posted = Column(Boolean, nullable=False)
    cooking_time = Column(String, nullable=False)
    diff_id = Column(Integer, ForeignKey("Difficulty.diff_id"))

    author = relationship("User")
    difficulty = relationship("Difficulty", foreign_keys=[diff_id])


class PublicRecipe(Base):
    __tablename__ = "PublicRecipe"
    
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"))
    comments = Column(JSON, nullable=False)
    rating = Column(Float, nullable=False)


class PrivateRecipe(Base):
    __tablename__ = "PrivateRecipe"
    
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"))
    restricted_access = Column(Boolean, nullable=False)


class ProteinFood(Base):
    __tablename__ = "ProteinFood"
    
    id = Column(Integer, primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), nullable=False)
    is_vegan = Column(Boolean, nullable=False)
    isHalal = Column(Boolean, nullable=False)


class Grain(Base):
    __tablename__ = "Grain"
    
    id = Column(Integer, primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), nullable=False)
    isHighFiber = Column(Boolean, nullable=False)
