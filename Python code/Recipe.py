from plyer import notification
import datetime
# The Food class allows the creation of food objects that hold their name and experationDate
class Food:
    def __init__(this,name,experationDate):
        this.name=name
        this.experationDate=experationDate
    def __str__(this):
        return f"{this.name}"
#The Foods Class allows an array of food objects that the user has, allowing us to search this array
#To remove items when they are used or expire, and add items when the user buys groceries. 
#It also is the basis for searching for recipes that the user can make by using the array of 
#Food to find recipes
class Foods:
    def __inti__(this,food):
        this.food=food
    def addFood(this,x):
        {
            this.food.append(x)
        }
    def removeFood(this,x):
        this.food.remove(x)
    #Finds the Recipes that the user can make with the food they have.
    def find_recipes(this,recipes):
        ingredients=[]
        for x in this.food:
            ingredients.append(x.name)
        matching_recipes = []
        for recipe, recipe_ingredients in recipes.items():
            if all(ingredient in ingredients for ingredient in recipe_ingredients):
                matching_recipes.append(recipe)
        return matching_recipes
#sends notifications about food that will expire soon. 
    def message(this):
        expiring=[]
        for x in this.Food:
            if x.experationDate.timestamp-604800<datetime.date.today().timestamp():
                expiring.append(x)
        if expiring.__len__!=0:
            message=''
            for food in expiring:
                message += food.name+' will expire in '+(food.experationDate.timestamp()-datetime.date.today().timestapm())/86400+'days\n'
            title = 'Food is about to expire',
            notification.notify(title=title, message=message, timeout=30)


if __name__ == '__main__': assert False, 'This is a class file.'

    
        
        
    