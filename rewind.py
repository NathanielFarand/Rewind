import tkinter as tk



root = tk.Tk()
root.title("Rewind")


window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
root.configure(bg='#f0f0f0')
font_style = ('Helvetica', 12)


label = tk.Label(root, text="Reminders", font=font_style, bg='#f0f0f0')
label.pack(pady=10)

listbox = tk.Listbox(root, width=40, font=font_style)
listbox.pack(pady=5)

entry = tk.Entry(root, width=30, font=font_style)
entry.pack(pady=5)

#add reminder to the list
add_button = tk.Button(root, text="Add Reminder", font=font_style)
add_button.pack(pady=5)

#recur = green not recuring = red bg
recuring_button = tk.Button(root, text="recuring", bg="green", font=font_style)
recuring_button.pack(pady=5)

#time select
label = tk.Label(root, text="9:40 pm", font=("Arial", 50), bg="black", fg="white")
label.pack(pady=20)


root.mainloop()
