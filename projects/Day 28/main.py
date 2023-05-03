from tkinter import *
from pomodoro import Pomodoro

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
#
# window = Tk()
#
# window.title('Pomodoro')
# window.config(padx=100, pady=50, bg=YELLOW)
#
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file='tomato.png')
# canvas.create_image(
#     100,112, image=tomato_img
# )
# canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
#
# l_timer = Label(text='Timer', font=(FONT_NAME, 50, 'bold'),
#                 bg=YELLOW, fg=GREEN)
#
# b_start = Button(text='Start')
# b_reset = Button(text='Reset')
#
#
# # Grid layout
# l_timer.grid(column=1,row=0)
# canvas.grid(column=1,row=1)
# b_start.grid(column=0,row=2)
# b_reset.grid(column=2, row=2)
#
# window.mainloop()

##################################################
# My implementation
##################################################



window = Tk()
p_timer = Pomodoro()

window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(
    100,112, image=tomato_img
)
timer_text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

l_pomodoro_checks = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'normal'))
l_timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'),
                bg=YELLOW, fg=GREEN)

b_start = Button(text='Start', command=p_timer.start_pomodoro_timer)
b_reset = Button(text='Reset', command=p_timer.reset)


# Grid layout
l_timer.grid(column=1,row=0)
canvas.grid(column=1,row=1)
b_start.grid(column=0,row=2)
l_pomodoro_checks.grid(column=1, row=2)
b_reset.grid(column=2, row=2)

def my_loop():
    if p_timer.state is None:
        l_timer.config(text='Timer', fg=GREEN)
        canvas.itemconfig(timer_text, text='00:00')
        l_pomodoro_checks.config(text='✔' * p_timer.pomodoro_count)
        b_start.config(text='Start', command=p_timer.start_pomodoro_timer)
    else:
        current_time = p_timer.get_time()
        canvas.itemconfig(timer_text,
                          text=f'{current_time[0]:02}:{current_time[1]:02}')
        l_pomodoro_checks.config(text='✔'*p_timer.pomodoro_count)

        b_start.config(text='Pause', command=p_timer.update_pause)

        if p_timer.state == 'Work':
            l_timer.config(text='Work', fg=GREEN)
        elif p_timer.state == 'Short Break':
            l_timer.config(text='Break', fg=PINK)
        elif p_timer.state == 'Long Break':
            l_timer.config(text='Break', fg=RED)


    p_timer.update()
    window.after(1000, my_loop)

window.after(1000, my_loop)
window.mainloop()


# # Testing timer
#
# p = Pomodoro()
# p.start_pomodoro_timer()
# while True:
#
#     if p.state is None:
#         p.reset()
#         p.start_pomodoro_timer()
#     print(f'{p.state} | {p.timer} | {p.pomodoro_count}')
#
#     p.update()
