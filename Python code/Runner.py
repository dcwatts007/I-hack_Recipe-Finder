#importing files
from win10toast import ToastNotifier
import Recipe
# Create an instance of the ToastNotifier class
toast = ToastNotifier()
# Show the notification
toast.show_toast("Notification", "Notification body", duration=20, icon_path="icon.ico", threaded=True)