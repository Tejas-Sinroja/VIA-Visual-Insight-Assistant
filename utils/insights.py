import pandas as pd

# Load data
# food_df = pd.read_csv("food_calorie_info.csv")
food_df = pd.read_csv(r"assets/food_calorie_info.csv")

protein_df = pd.read_csv(r"assets/food_protien_info.csv")

def get_calories_info(food_item):
    """Retrieves calorie level and suggestion for the food item."""
    food_info = food_df[food_df["Food Item"] == food_item].iloc[0]
    return food_info["Calorie Level"], food_info["Suggestion"]

def get_protein_info(food_item):
    """Retrieves protein level and content for the food item."""
    food_info = protein_df[protein_df["Food Item"] == food_item].iloc[0]
    return food_info["Protein (per 100g)"], food_info["Protein Level"]

