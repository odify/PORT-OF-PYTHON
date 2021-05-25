import keyboard

event = keyboard.record(until='ctrl + z')
keyboard.play(event, speed_factor=1)
print(event)
