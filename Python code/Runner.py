#importing files
from win10toast import ToastNotifier
import Recipe
from openrecipes import scrapy_prj
# Create an instance of the ToastNotifier class
toast = ToastNotifier()
# Show the notification
toast.show_toast("Notification", "Notification body", duration=20, icon_path="icon.ico", threaded=True)

ingredient_input = input("Enter your ingredients in a list seperated by a ',' ")
ingredient_input_list = ingredient_input.split(",")
for ingredient in ingredient_input_list:
    print(ingredient)