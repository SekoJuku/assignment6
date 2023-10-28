CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    role VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    UNIQUE (email)
);

CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    admin_permissions VARCHAR(50) NOT NULL,
    admin_role VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE RegisteredUser (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    user_level VARCHAR(20) NOT NULL,
    support_messages JSON NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Category (
    category_name VARCHAR(255) PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE NutritionValue (
    nv_id INT AUTO_INCREMENT PRIMARY KEY,
    calories_per_unit FLOAT(5) NOT NULL,
    carbohydrates_per_unit FLOAT(5) NOT NULL,
    fat_per_unit FLOAT(5) NOT NULL,
    protein_per_unit FLOAT(5) NOT NULL
);

CREATE TABLE Difficulty (
    diff_id INT AUTO_INCREMENT PRIMARY KEY,
    preparation_time VARCHAR(10) NOT NULL,
    cooking_time VARCHAR(10) NOT NULL,
    number_of_step INT NOT NULL,
    users_rating FLOAT(1) NOT NULL
);

CREATE TABLE Recipe (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    serving_size INT NOT NULL,
    is_posted BOOLEAN NOT NULL,
    cooking_time VARCHAR(50) NOT NULL,
    diff_id INT NOT NULL,
    FOREIGN KEY (diff_id) REFERENCES Difficulty(diff_id),
    FOREIGN KEY (author_id) REFERENCES User(user_id),
    UNIQUE (title)
);

CREATE TABLE Ingredient (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    measurement_unit VARCHAR(50) NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    nv_id INT NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (category_name) REFERENCES Category(category_name),
    FOREIGN KEY (nv_id) REFERENCES NutritionValue(nv_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE PublicRecipe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT NOT NULL,
    comments JSON NOT NULL,
    rating FLOAT(3) NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE PrivateRecipe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT,
    restricted_access BOOLEAN,
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE ProteinFood (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_id INT NOT NULL,
    is_vegan BOOLEAN NOT NULL,
    isHalal BOOLEAN NOT NULL,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

CREATE TABLE Grain (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_id INT NOT NULL,
    isHighFiber BOOLEAN NOT NULL,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);
