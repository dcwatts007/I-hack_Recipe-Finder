from plyer import notification
import datetime
# The Food class allows the creation of food objects that hold their name as a string and experationDate as a DateTime object
class Food:
    def __init__(this,name,experationDate):
        this.name=name
        this.experationDate=experationDate
    def __str__(this):
        return f"{this.name}"
#The Recipe Class holds the recipe's name, ingredients, and directions as a string, array, and string respectively
class Recipe:
    def __init__(this,name,ingredients,directions):
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
    def __init__(this,curentfoods,recipes):
        this.curentfoods=curentfoods
        this.recipes=recipes
    def addFood(this,x):
        {
            this.foods.append(x)
        }
    def removeFood(this,x):
        this.foods.remove(x)
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
            can_make_recipe=True
            for ingredient in searcher:
                try:
                    finder.index(ingredient)
                except ValueError:
                    can_make_recipe=False
                    break
            if can_make_recipe:
                makeable_recipes.append(recipe)
        return makeable_recipes
        
exp1='lollypops'
food1=Food('milk',exp1)
food2=Food('sausage',exp1)
food=[food1,food2]
ingredients=['milk']
ingredients2=['wheat','eggs','milk']
recipe2=Recipe('food',ingredients2,'eat')
recipe1=Recipe('milk',ingredients,'drink')
recipe=[recipe2,recipe1]
foods=Foods(food,recipe)
bug=foods.find_recipes()
print(foods.find_recipes())



#sends notifications about food that will expire soon. 
class notify:
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

    
        
        
    