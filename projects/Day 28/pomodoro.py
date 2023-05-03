import time
from tkinter import Tk

# WORK_TIME = 1500
# SHORT_BREAK_TIME = 300
# LONG_BREAK_TIME = 600

WORK_TIME = 5
SHORT_BREAK_TIME = 2
LONG_BREAK_TIME = 5


class Pomodoro:

    def __init__(self):

        # Valid states 'Work', 'Short Break', 'Long Break'
        self.state = None
        self.pomodoro_count = 0
        self.timer = 0
        self.pause = False

    def start_pomodoro_timer(self):

        self.state = 'Work'
        self.timer = WORK_TIME
        self.pomodoro_count = 0

    def update(self):
        """Updates the timer and changes states"""
        # print(f'{self.state} | {self.timer} | {self.pomodoro_count} | {self.pause}')
        if self.pause:
            print('PAUSED!')
        elif self.timer != 0 and self.state is not None:
            self.timer -=1
        else:
            if self.state == 'Work' and self.pomodoro_count == 3:
                self.state = 'Long Break'
                self.timer = LONG_BREAK_TIME
                self.pomodoro_count += 1
            elif self.state == 'Work':
                self.pomodoro_count += 1
                self.state = 'Short Break'
                self.timer = SHORT_BREAK_TIME
            elif self.state == 'Long Break':
                self.reset()
            elif self.state == 'Short Break':
                self.state = 'Work'
                self.timer = WORK_TIME

    def reset(self):
        self.state = None
        self.pomodoro_count = 0
        self.timer = 0
        self.pause = False

    def get_time(self):

        minutes = self.timer // 60
        seconds = self.timer % 60
        return minutes, seconds

    def update_pause(self):
        self.pause = not self.pause