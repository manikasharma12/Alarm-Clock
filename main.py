import tkinter as tk
from datetime import datetime
import pygame

pygame.mixer.init()

root = tk.Tk()

root.title("Alarm Clock")

root.geometry("500x400")

alarm_time = None

def show_time():

    current_time = datetime.now()

    current_time = current_time.strftime("%H:%M:%S")

    time_label.config(text=current_time)

    check_alarm(current_time)

    root.after(1000, show_time)


def set_alarm():

    global alarm_time

    hour = hour_entry.get()

    minute = minute_entry.get()

    second = second_entry.get()

    alarm_time = f"{hour}:{minute}:{second}"

    alarm_status.config(
        text=f"Alarm set for {alarm_time}",
        fg="green"
    )

    print(f"Alarm set for {alarm_time}")


def check_alarm(current_time):

    if alarm_time is not None:

        if current_time == alarm_time:

            alarm_status.config(
                text="⏰ TIME TO WAKE UP!",
                fg="red"
            )

            pygame.mixer.music.load("sound.wav")

            pygame.mixer.music.play(-1)

            print("⏰ Time to wake up!")


def stop_alarm():

    pygame.mixer.music.stop()

    alarm_status.config(
        text="Alarm stopped",
        fg="blue"
    )

    print("Alarm stopped")


title_label = tk.Label(
    root,
    text="Alarm Clock",
    font=("Arial", 28, "bold")
)

title_label.pack(pady=20)


time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 40, "bold")
)

time_label.pack(pady=10)


alarm_label = tk.Label(
    root,
    text="Set Alarm Time",
    font=("Arial", 18, "bold")
)

alarm_label.pack(pady=15)


input_frame = tk.Frame(root)

input_frame.pack()


hour_label = tk.Label(
    input_frame,
    text="Hour",
    font=("Arial", 12)
)

hour_label.grid(row=0, column=0, padx=10)


hour_entry = tk.Entry(
    input_frame,
    width=8,
    font=("Arial", 15)
)

hour_entry.grid(row=1, column=0, padx=10)


minute_label = tk.Label(
    input_frame,
    text="Minute",
    font=("Arial", 12)
)

minute_label.grid(row=0, column=1, padx=10)


minute_entry = tk.Entry(
    input_frame,
    width=8,
    font=("Arial", 15)
)

minute_entry.grid(row=1, column=1, padx=10)


second_label = tk.Label(
    input_frame,
    text="Second",
    font=("Arial", 12)
)

second_label.grid(row=0, column=2, padx=10)


second_entry = tk.Entry(
    input_frame,
    width=8,
    font=("Arial", 15)
)

second_entry.grid(row=1, column=2, padx=10)


alarm_status = tk.Label(
    root,
    text="No alarm set",
    font=("Arial", 14),
    fg="green"
)

alarm_status.pack(pady=15)


set_alarm_button = tk.Button(
    root,
    text="Set Alarm",
    font=("Arial", 15, "bold"),
    command=set_alarm
)

set_alarm_button.pack(pady=5)


stop_alarm_button = tk.Button(
    root,
    text="Stop Alarm",
    font=("Arial", 15, "bold"),
    command=stop_alarm
)

stop_alarm_button.pack(pady=5)


show_time()

root.mainloop()