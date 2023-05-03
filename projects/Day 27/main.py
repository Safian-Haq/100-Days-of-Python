# from tkinter import *
#
#
#
#
# window = Tk()
# window.title('Title')
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# # Label
# label = Label(text='Label', font=('Arial', 24, 'bold'))
# label.grid(column=0, row=0)
#
#
#
#
# def action():
#     label['text'] = user_input.get()
#
#
#
# user_input = Entry(width=20)
# user_input.insert(END, 'Type here!')
# user_input.grid(column=3,row=3)
#
#
# button = Button(text='Click Me!', command=action)
# button.grid(column=1,row=1)
#
# new_button = Button(text='NewButton')
# new_button.grid(column=2, row=0)
#
# # text = Text(height=5, width=30)
# # # text.focus()
# # text.insert(END, 'Multi-line text entry.')
# # text.pack()
#
# # def check_fun():
# #     if not check_state.get():
# #         print('Unchecked')
# #     else:
# #         print("Checked")
# #
# # check_state = IntVar()
# # check_button = Checkbutton(text='Is On?', variable=check_state, command=check_fun)
# #
# # check_button.pack()
# #
# # def rb_fun():
# #     print(rb_state.get())
# #
# # rb_state = IntVar()
# # rb = Radiobutton(text='Op1', value=1,
# #                  variable=rb_state, command=rb_fun)
# # rb2 = Radiobutton(text='Op2', value=2,
# #                   variable=rb_state, command=rb_fun)
# # rb.pack()
# # rb2.pack()
# #
#
# window.mainloop()
#

from tkinter import *
from functools import partial

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.maxsize(width=300, height=200)
window.config(padx=50, pady=50)

result = 0


def miles_to_kn():
    l_result.config(
        text= str(
            round(float(user_input.get()) * 1.60934, 3)
        )
    )


# Widgets
user_input = Entry(width=10)

l_miles = Label(text='Miles', padx=5, pady=5)

l_body_1 = Label(text='is equal to', padx=5, pady=5)
l_result = Label(text='0', padx=5, pady=5)
l_body_2 = Label(text='Km', padx=5, pady=5)

b_cal = Button(text='Calculate', width=10, padx=5, pady=5, command=miles_to_kn)

# Widgets placement grid
user_input.grid(column=1, row=0)
l_miles.grid(column=2, row=0)
l_body_1.grid(column=0, row=1)
l_body_2.grid(column=2, row=1)
l_result.grid(column=1, row=1)
b_cal.grid(column=1, row=2)

window.mainloop()
