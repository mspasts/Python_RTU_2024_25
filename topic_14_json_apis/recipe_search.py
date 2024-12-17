import requests
import json
from collections import Counter
import matplotlib.pyplot as plt
 
# API endpoint for recipes
api_url = "https://dummyjson.com/recipes"
 
# Fetch all recipes
response = requests.get(api_url)
# could add a check here if we got a good response code

# the main idea in this exercise was to find the structure of the data and then work with it
# here we have outer layer as dictionary with key "recipes" and value is a list of dictionaries
# outer layer has some other keys that represent metadata which we do not need
data = response.json()["recipes"]
 
# 1a. Filtrē receptes, kas satur 'potato' to sastāvdaļu sarakstā
potato_recipes = [recipe for recipe in data if any('potato' in ingredient.lower() for ingredient in recipe["ingredients"])]
potato_recipes_subset = potato_recipes[:5]
 
# Saglabā kartupeļu receptes JSON failā pašreizējā direktorijā
with open('potato_recipes.json', 'w') as file:
    json.dump(potato_recipes_subset, file, indent=4)
 
# 1b. Filtrē receptes, kur mealType satur 'soup'
soup_recipes = [recipe for recipe in data if "soup" in recipe["mealType"]]
 
# 1c. Izveido lielu sarakstu ar visām sastāvdaļām no visām receptēm
all_ingredients = []
for recipe in data:
    # Pārbauda vai ingredients ir saraksts, ja nē, tad sadala to
    if isinstance(recipe["ingredients"], str):
        ingredients_list = [ingredient.strip() for ingredient in recipe["ingredients"].split(',')]
    else:
        ingredients_list = recipe["ingredients"]
    all_ingredients.extend(ingredients_list)
 
# 1d. Izmanto Counter, lai noteiktu visbiežāk sastopamās sastāvdaļas
ingredient_count = Counter(all_ingredients)
top_5_ingredients = ingredient_count.most_common(5)
 
# Izdrukā top 5 sastāvdaļas
print("Top 5 Most Used Ingredients:")
for ingredient, count in top_5_ingredients:
    print(f"{ingredient}: {count}")
 
# 1e. Uzzīmē histogrammu ar TOP 10 ingredients
top_10_ingredients = ingredient_count.most_common(10)
# here top_10_ingredients is a list of tuples, we need to unpack it for use in plotting
ingredients, counts = zip(*top_10_ingredients)  # atpakojam sastāvdaļas un to skaitu
# if we did not use the above trick we could have done it like this
# ingredients = []
# counts = []
# for ingredient, count in top_10_ingredients:
#     ingredients.append(ingredient)
#     counts.append(count)
 
plt.figure(figsize=(10, 5))
plt.bar(ingredients, counts, color='blue')
plt.xlabel('Ingredients')
plt.ylabel('Count')
plt.title('Top 10 Most Used Ingredients')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
 
# Bonus: Meklētājs
def search_recipe(query):
    '''
    Meklē receptes pēc nosaukuma

    Args:
        query (str): Meklēšanas vaicājums
    Returns:
        list: Receptes, kas satur meklēšanas vaicājumu ar lieliem vai maziem burtiem
    '''
    return [recipe for recipe in data if query.lower() in recipe["name"].lower()]
 
user_query = input("Ievadiet receptes nosaukumu, ko vēlaties meklēt: ")
search_results = search_recipe(user_query)
print(f"Meklēšanas rezultāti par '{user_query}':", search_results)