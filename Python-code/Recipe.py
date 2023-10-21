from plyer import notification
import datetime
# The Food class allows the creation of food objects that hold their name as a string and experationDate as a DateTime object
class Food:
    def __init__(this,name:str,experationDate:datetime):
        this.name=name
        this.experationDate=experationDate
    def __str__(this):
        return f"{this.name}"
#The Recipe Class holds the recipe's name, ingredients, and directions as a string, array, and string respectively
class Recipe:
    def __init__(this,name:str,ingredients:[],directions:str):
        this.name=name
        this.ingredients=ingredients
        this.directions=directions
    def __str__(this):
        return f"{this.name}"
#The Foods Class allows an array of food objects that the user has, allowing us to search this array
#To remove items when they are used or expire, and add items when the user buys groceries. 
#It also is the basis for searching for recipes that the user can make by using the array of 
#Food to find recipes
class Foods:
    def __init__(this,curentfoods:[],recipes:[]):
        this.curentfoods=curentfoods
        this.recipes=recipes
    def __str__(this):
        string = ""
        for food in this.curentfoods:
            string+=str(food)
        return string
        
    def addFood(this,x):
        {
            this.curentfoods.append(x)
        }
    def removeFood(this,x):
        this.curentfoods.remove(x)
    def addRecipe(this,x):
        this.recipes.append(x)
    #Finds the Recipes that the user can make with the food they have.
    def find_recipes(this):
        finder =[]
        makeable_recipes = []
        for food in this.curentfoods:
            finder.append(food.name)
        for recipe in this.recipes:
            searcher=(recipe.ingredients)
           
            for ingredient in searcher:
                can_make_recipe=False
                for name in finder:
                    if(name.lower() in ingredient.lower()):
                        can_make_recipe=True
                        break
                if not can_make_recipe:
                    break
            if can_make_recipe:
                makeable_recipes.append(recipe)
        return makeable_recipes
#sends notifications about food that will expire soon. 
    def notify(this):
        expiring=[]
        food:Food
        for i in range(this.curentfoods.__len__):
            if this.curentfoods[i].experationDate.timestamp()-604800<datetime.date.today().timestamp():
                expiring.append(x)
        if expiring.__len__!=0:
            message=''
            for food in expiring:
                message += food.name+' will expire in '+(food.experationDate.timestamp()-datetime.date.today().timestapm())/86400+'days\n'
            title = 'Food is about to expire',
            notification.notify(title=title, message=message, timeout=30)


if __name__ == '__main__': assert False, 'This is a class file.'

    
        
        
    