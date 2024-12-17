import requests
import json

atbilde = requests.get("https://dummyjson.com/recipes")
dati = atbilde.json()

receptes = dati.get("recipes", [])

kartupelu_receptes = []
for recepte in receptes:
     
    if any("potato" in ingredient.lower() for ingredient in recepte.get("ingredients", [])):
        kartupelu_receptes.append(recepte)
        if len(kartupelu_receptes) == 5:
            break
    
with open("kartupelu_receptes.json", "w", encoding="utf-8") as f:
    json.dump(kartupelu_receptes, f, ensure_ascii=False, indent=4)

print("Atlasītās receptes:", kartupelu_receptes)

