from tkinter import *
from tkcalendar import Calendar
from tkinter.ttk import Combobox
import Recipe
from tkinter import ttk
#importing files
import Recipe
import datetime

#region - our homemade database of recipes. 
recipes = [
    {
        'name': 'Cookies',
        'ingredients': [
            '1 C. butter or margarine, softened',
            '1⁄2 C. granulated sugar',
            '1⁄2 C. packed brown sugar',
            '1 large egg',
            '1 tsp. vanilla',
            '2 C. flour',
            '1⁄2 tsp. baking soda',
            '1⁄4 tsp. salt',
            '1⁄2 C. finely chopped pecans',
            '36 pecan halves or chopped pecans, toasted (optional)'
        ],
        'directions': '''In the bowl of a stand mixer, beat butter and sugars until fluffy. Add egg and vanilla.
Mix in flour, baking soda, and salt and beat until combined. Stir in chopped pecans.
Refrigerate for at least 30 minutes.
Preheat oven to 350°F and form into little balls on a greased cookie sheet. Bake for 10 minutes.'''
    },
    {
        'name': 'Delicious, Rich Brownies',
        'ingredients': [
            '4 eggs, beaten',
            '2 sticks of butter, softened',
            '1 1⁄2 t. salt',
            '1 1⁄2 c. flour',
            '2 c. sugar',
            '1 c. chocolate chips',
            '1⁄2 c. cocoa',
            '1 t. vanilla'
        ],
        'directions': 'Mix together all ingredients. Place in a greased 9x13-pan and bake at 350°F for 25-30 minutes.'
    },
    {
        'name': 'Snickerdoodles',
        'ingredients': [
            '1 c. butter',
            '2 c. sugar',
            '1 pinch salt',
            '1 c. oil',
            '2 t. baking soda',
            '2 t. cream of tartar',
            '2 eggs',
            '1 t. vanilla',
            '5 c. unsifted flour'
        ],
        'directions': '''Cream butter and sugar. Add eggs, oil, salt, and vanilla.
Sift dry ingredients together, then combine all ingredients.
Roll in cinnamon and sugar, and bake at 350°F for 10 minutes.'''
    },
    {
        'name': 'Caramel Popcorn',
        'ingredients': [
            '3⁄4 c. sugar',
            '3⁄4 c. brown sugar',
            '1 c. butter',
            '1⁄2 c. Karo',
            '1⁄4 c. water',
            '1/8 t. cream of tartar'
        ],
        'directions': 'Boil on medium for 5 minutes, then add 1⁄4 t. baking soda.'
    },
    {
        'name': 'Chocolate Bundt Cake',
        'ingredients': [
            'Chocolate cake mix',
            '1 c. sour cream',
            '1 small chocolate pudding mix',
            '1⁄2 c. hot water',
            '4 eggs',
            '1 c. semi-sweet chocolate chips',
            '1 c. oil'
        ],
        'directions': 'Veg shortening on the pan, cook at 325°F for 55 minutes. Sprinkle powdered sugar on top when finished.'
    },
    {
        'name': 'Nugget Pecan Pie',
        'ingredients': [
            '1 c. Karo syrup',
            '3⁄4 c. granulated sugar',
            '4 oz. (1 cube) melted butter',
            '1 tsp. vanilla',
            '3⁄4 c. pecan pieces',
            '3⁄4 c. pecan halves',
            '3 eggs'
        ],
        'directions': 'Mix together syrup and sugar. Add melted butter, and then mix eggs and vanilla. Let stand 1 hour. Place pecan pieces in the bottom of an unbaked pie shell. Pour filling in and cover with pecan halves. Bake 45-50 min. at 325°F.'
    },
    {
        'name': 'White Chocolate Chip Cookies',
        'ingredients': [
            '1 c. brown sugar',
            '1 c. white sugar',
            '1 c. butter (a little soft)',
            '2 eggs',
            '2 1⁄2 t. vanilla',
            '1 t. baking soda',
            '1 t. baking powder',
            '1⁄2 t. salt',
            '2 c. flour',
            '2 c. old-fashioned oats',
            '1 bag white chocolate chips'
        ],
        'directions': '''Mix sugars together, then beat in butter, eggs, and vanilla. Add dry ingredients.
Add 2 c. old-fashioned oats until batter is stiff. Add 1 pkg. white chocolate chips.
Bake at 350°F for 12 minutes.'''
    },
    {
        'name': 'Grandma’s Orange Cookies',
        'ingredients': [
            '2/3 c. sugar',
            '2/3 c. butter',
            '2 eggs',
            '1/2 c. frozen orange juice concentrate',
            '1 1/2 tsp. grated orange zest',
            '2 c. flour',
            '1/2 tsp. baking soda',
            '1/2 tsp. salt'
        ],
        'directions': '''In a large mixing bowl, cream together the sugar and butter.
        Add eggs one at a time, beating well with each addition.
        Stir in the orange juice concentrate and zest.
        Combine the flour, baking soda, and salt; gradually add to the orange mixture.
        Drop dough by rounded teaspoonfuls onto ungreased cookie sheets.
        Bake at 375°F for 10-12 minutes.''',
        "name": "Spaghetti Sauce, Cynthia",
        "ingredients": [
            "Ground beef",
            "Onion",
            "Garlic",
            "Canned tomatoes",
            "Tomato paste",
            "Tomato sauce",
            "Sugar",
            "Salt",
            "Oregano",
            "Basil"
        ],
        "directions": [
            "Brown ground beef, onion, and garlic in a large pot.",
            "Add canned tomatoes, tomato paste, and tomato sauce.",
            "Add sugar, salt, oregano, and basil.",
            "Simmer for at least an hour."
        ]
    },
    {
        "name": "Fettuccini Alfredo, Cynthia",
        "ingredients": [
            "Fettuccini pasta",
            "Butter",
            "Heavy cream",
            "Garlic",
            "Parmesan cheese",
            "Salt",
            "Pepper",
            "Parsley"
        ],
        "directions": [
            "Cook fettuccini pasta according to package instructions.",
            "In a separate pan, melt butter and sauté garlic.",
            "Add heavy cream and heat until simmering.",
            "Stir in Parmesan cheese, salt, and pepper.",
            "Toss the cooked pasta with the sauce and garnish with parsley."
        ]
    },
    {
        "name": "Chicken Stir-Fry, John",
        "ingredients": [
            "Boneless chicken breasts",
            "Soy sauce",
            "Sesame oil",
            "Garlic",
            "Ginger",
            "Broccoli",
            "Red bell pepper",
            "Carrots",
            "Snow peas",
            "Cornstarch"
        ],
        "directions": [
            "Cut chicken into bite-sized pieces and marinate in soy sauce and sesame oil.",
            "In a wok or large skillet, heat oil and sauté garlic and ginger.",
            "Add chicken and cook until no longer pink.",
            "Stir in broccoli, red bell pepper, carrots, and snow peas.",
            "In a separate bowl, mix soy sauce and cornstarch, then pour over the stir-fry.",
            "Cook until the sauce thickens, and the vegetables are tender."
        ]
    },
    {
        "name": "Vegetable Curry, Maria",
        "ingredients": [
            "Onion",
            "Garlic",
            "Ginger",
            "Curry powder",
            "Cumin",
            "Turmeric",
            "Chickpeas",
            "Coconut milk",
            "Carrots",
            "Potatoes",
            "Peas",
            "Cilantro",
            "Lime juice"
        ],
        "directions": [
            "Sauté onion, garlic, and ginger in a large pot.",
            "Add curry powder, cumin, and turmeric; cook for a minute.",
            "Stir in chickpeas, coconut milk, carrots, potatoes, and peas.",
            "Simmer until vegetables are tender.",
            "Garnish with cilantro and lime juice."
        ]
    },
    {
        "name": "Chocolate Chip Cookies, Emily",
        "ingredients": [
            "Butter",
            "Granulated sugar",
            "Brown sugar",
            "Egg",
            "Vanilla extract",
            "All-purpose flour",
            "Baking soda",
            "Salt",
            "Chocolate chips",
        ],
        "directions": [
            "Cream together butter, granulated sugar, and brown sugar.",
            "Beat in the egg and vanilla extract.",
            "In a separate bowl, whisk together flour, baking soda, and salt.",
            "Combine the dry ingredients with the wet mixture and fold in chocolate chips.",
            "Drop spoonfuls of dough onto a baking sheet and bake until golden brown."
        ]
    }
]
#endregion
print(recipes[0])
foods=[]
Pantry=Recipe.Foods(foods,recipes[0]["ingredients"])
window = Tk()
print(Pantry.recipes)
# text labels
label1 = Label(window, text="Welcome to the bodacious bohemoths app", fg='black', font=("Helvetica", 30, "bold"))
label1.place(x=90, y=20)

label2 = Label(window, text="Please input your ingredients:", fg='black', font=("Helvetica", 24))
label2.place(x=270, y=90)

label4 = Label(window, text="INGREDIENTS", fg='black', font=("Helvetica", 12))
label4.place(x=407, y=185)

label4 = Label(window, text="(input one at a time, press 'enter' after each input)", fg='black', font=("Helvetica", 8))
label4.place(x=340, y=242)


# data = ("one", "two", "three", "four")
# cblabel= Label(window, text="Please select display option:", fg='black', font=("Helvetica", 20))
# cb = Combobox(window, values=data, state="readonly", height= 5 ,font="Verdana 16")
def newtab_recipes():
    root = Tk()
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)
    tab1= ttk.Frame(tabControl)
    tabControl.add(tab1, text = "Recipes")
    tabControl.pack(expand = 1, fill = "both")
    recipe=[]
    recipe=Pantry.find_recipes()
    string=""
    for holder in recipe:
        string+=holder.__str__()+"\n"
    ttk.Label(tab1, text=string).geometry()

btn = Button(window, text = "Go to recipes", command = newtab_recipes)
btn.place(x=310, y=300)
# cb.place(x=342, y=350)





tb1 = Entry(window, bd=5)
tb1.place(x=395, y=210)
def get_value(event):
    tb1_name = tb1.get()
    # Add Calendar
    root = Tk()
    root.geometry("400x400")
    cal = Calendar(root, selectmode = 'day',)
    cal.pack(pady = 20)

    def grad_date():
        food=Recipe.Food(tb1_name,cal.get_date())
        Pantry.addFood(food)
    # Add Button and Label
    btn = Button(root, text = "Get Date", command= grad_date).pack(pady = 20)
window.bind('<Return>',get_value)











# window frame and title
window.title("Hello there!")
window.geometry("1000x600+190+80")
window.mainloop()
    