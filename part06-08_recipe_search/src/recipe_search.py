# Write your solution here

def open_recipe(filename: str):
    lines = []
    with open(filename) as new_file:
        for line in new_file:
            lines.append(line.strip())
    recipes_list = []
    count = 0
    for i in range(len(lines)):
        if len(recipes_list) == count:
            recipes_list.append([])
        if lines[i] == "":
            count += 1
            continue
        recipes_list[count].append(lines[i])
    recipes_dict = {}
    for recipe in recipes_list:
        value = []
        value.append(int(recipe[1]))
        for i in range(2,len(recipe)):
            value.append(recipe[i])
        recipes_dict[recipe[0]] = value
    return recipes_dict

def search_by_name(filename: str, word: str):
    recipes_dict = open_recipe(filename)
    found_recipes = []
    for recipe in recipes_dict:
        if word.lower() in recipe.lower():
            found_recipes.append(recipe)
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes_dict = open_recipe(filename)
    found_recipes = []
    for recipe in recipes_dict:
        if recipes_dict[recipe][0] <= prep_time:
            found_recipes.append(recipe + f', preparation time {recipes_dict[recipe][0]} min')
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes_dict = open_recipe(filename)
    found_recipes = []
    for recipe in recipes_dict:
        if ingredient in recipes_dict[recipe]:
            found_recipes.append(recipe + f', preparation time {recipes_dict[recipe][0]} min')
    return found_recipes
