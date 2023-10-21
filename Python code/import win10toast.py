# Sample recipe database (you can expand this with more recipes and ingredients)

# Function to find recipes based on available ingredients


# Main program
if __name__ == "__main__":
    user_input = input("Enter a list of food items separated by commas: ").split(",")
    user_ingredients = [item.strip().lower() for item in user_input]

    matching_recipes = find_recipes(user_ingredients)

    if matching_recipes:
        print("You can make the following recipes:")
        for recipe in matching_recipes:
            print(recipe)
    else:
        print("Sorry, you don't have enough ingredients for any recipes.")