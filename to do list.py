import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x600")
root.title("To-do list")


img = Image.open(r"C:\\Users\\Lenovo\\OneDrive\\Pictures\\Saved Pictures\\to.PNG").resize((580, 580))
final_img = ImageTk.PhotoImage(img)

labelx = tk.Label(root, image=final_img)
labelx.image = final_img
labelx.place(x=20, y=20)

l1 = tk.Label(root, text="TASKS", font="arial 16 bold", bg="blue", fg="white")
l1.place(x=250, y=30)


tasks = []
task_y = 70
break_mode = False
done_for_day = False

def save_task(event):
    global task_y
    task_text = task_entry.get()
    if task_text.strip() != "":
        var = tk.IntVar()
        cb = tk.Checkbutton(root, variable=var, bg="white")
        cb.place(x=60, y=task_y)

        task_label = tk.Label(root, text=task_text, font=("Arial", 14), bg="white", fg="black")
        task_label.place(x=90, y=task_y)

        tasks.append((cb, task_label))
        task_y += 30
    task_entry.destroy()


def show_entry(event):
    global task_entry
    if break_mode or done_for_day:
        return
    if event.widget != root and event.widget != labelx:
        return
    task_entry = tk.Entry(root, font=("Arial", 14))
    task_entry.place(x=90, y=task_y)
    task_entry.focus()
    task_entry.bind("<Return>", save_task)


def toggle_break():
    global break_mode
    if done_for_day:
        return
    break_mode = not break_mode
    if break_mode:
        break_button.config(text="RESUME", bg="red")
    else:
        break_button.config(text="BREAK", bg="green")


def finish_day():
    global done_for_day
    done_for_day = True
    break_button.config(state="disabled")
    done_button.config(state="disabled")

    msg = tk.Label(root, text="✅ WELL DONE! DAY COMPLETED.", font=("Arial", 14, "bold"), bg="yellow", fg="black")
    msg.place(x=160, y=task_y + 30)


root.bind("<Button-1>", show_entry)


break_button = tk.Button(root, text="BREAK", font=("Arial", 12, "bold"), bg="green", fg="white", command=toggle_break)
break_button.place(x=500, y=30)


done_button = tk.Button(root, text="Done for the Day", font=("Arial", 12, "bold"), bg="orange", fg="black", command=finish_day)
done_button.place(x=210, y=550)

root.mainloop()
