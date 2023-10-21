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
#Food to 
class Foods:
    def __inti__(this,food):
        this.food=food

if __name__ == '__main__': assert False, 'This is a class file.'

    
        
        
    