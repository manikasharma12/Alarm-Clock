import tkinter as tk
from datetime import datetime
import pygame


# --------------------------------------------------
# INITIALIZE PYGAME
# --------------------------------------------------

pygame.mixer.init()


# --------------------------------------------------
# CREATE MAIN WINDOW
# --------------------------------------------------

root = tk.Tk()

root.title("Alarm Clock")

root.geometry("500x400")


# --------------------------------------------------
# VARIABLE TO STORE ALARM TIME
# --------------------------------------------------

alarm_time = None


# --------------------------------------------------
# FUNCTION TO DISPLAY CURRENT TIME
# --------------------------------------------------

def show_time():

    # Get the current time
    current_time = datetime.now()

    # Convert time into Hour:Minute:Second format
    current_time = current_time.strftime("%H:%M:%S")

    # Display current time
    time_label.config(text=current_time)

    # Check whether alarm time has arrived
    check_alarm(current_time)

    # Run this function again after 1 second
    root.after(1000, show_time)


# --------------------------------------------------
# FUNCTION TO SET ALARM
# --------------------------------------------------

def set_alarm():

    global alarm_time

    # Get hour
    hour = hour_entry.get()

    # Get minute
    minute = minute_entry.get()

    # Get second
    second = second_entry.get()

    # Create alarm time
    alarm_time = f"{hour}:{minute}:{second}"

    # Display alarm status
    alarm_status.config(
        text=f"Alarm set for {alarm_time}",
        fg="green"
    )

    print(f"Alarm set for {alarm_time}")


# --------------------------------------------------
# FUNCTION TO CHECK ALARM
# --------------------------------------------------

def check_alarm(current_time):

    # Check whether an alarm has been set
    if alarm_time is not None:

        # Compare current time with alarm time
        if current_time == alarm_time:

            # Display alarm message
            alarm_status.config(
                text="⏰ TIME TO WAKE UP!",
                fg="red"
            )

            # Load the sound file
            pygame.mixer.music.load("sound.wav")

            # Play the sound continuously
            pygame.mixer.music.play(-1)

            # Print message in terminal
            print("⏰ Time to wake up!")


# --------------------------------------------------
# FUNCTION TO STOP ALARM
# --------------------------------------------------

def stop_alarm():

    # Stop the sound
    pygame.mixer.music.stop()

    # Change alarm status
    alarm_status.config(
        text="Alarm stopped",
        fg="blue"
    )

    print("Alarm stopped")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

title_label = tk.Label(
    root,
    text="Alarm Clock",
    font=("Arial", 28, "bold")
)

title_label.pack(pady=20)


# --------------------------------------------------
# CURRENT TIME
# --------------------------------------------------

time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 40, "bold")
)

time_label.pack(pady=10)


# --------------------------------------------------
# ALARM TITLE
# --------------------------------------------------

alarm_label = tk.Label(
    root,
    text="Set Alarm Time",
    font=("Arial", 18, "bold")
)

alarm_label.pack(pady=15)


# --------------------------------------------------
# INPUT FRAME
# --------------------------------------------------

input_frame = tk.Frame(root)

input_frame.pack()


# --------------------------------------------------
# HOUR
# --------------------------------------------------

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


# --------------------------------------------------
# MINUTE
# --------------------------------------------------

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


# --------------------------------------------------
# SECOND
# --------------------------------------------------

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


# --------------------------------------------------
# ALARM STATUS
# --------------------------------------------------

alarm_status = tk.Label(
    root,
    text="No alarm set",
    font=("Arial", 14),
    fg="green"
)

alarm_status.pack(pady=15)


# --------------------------------------------------
# SET ALARM BUTTON
# --------------------------------------------------

set_alarm_button = tk.Button(
    root,
    text="Set Alarm",
    font=("Arial", 15, "bold"),
    command=set_alarm
)

set_alarm_button.pack(pady=5)


# --------------------------------------------------
# STOP ALARM BUTTON
# --------------------------------------------------

stop_alarm_button = tk.Button(
    root,
    text="Stop Alarm",
    font=("Arial", 15, "bold"),
    command=stop_alarm
)

stop_alarm_button.pack(pady=5)


# --------------------------------------------------
# START THE CLOCK
# --------------------------------------------------

show_time()


# --------------------------------------------------
# KEEP THE WINDOW RUNNING
# --------------------------------------------------

root.mainloop()