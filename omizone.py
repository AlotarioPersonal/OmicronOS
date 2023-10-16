from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os
import time
import programs
os.system('cls')

print("You are now leaving omicronOS. Press Shift+Q to close the application.")
app = Ursina()

stepper = True

player = FirstPersonController()
player.position=(-8, 0.2, 8)
player.cursor.color=(color.black)

def input(key):
    if key == 'escape':
        app.quit()

def makeText():
    global app
    global stepper
    text = Text('FUCK ME')
    stepper=False
    app.quit()

place = Entity(model='level', collider='mesh', texture='greyasphalt', scale=0.02, texture_scale=(2, 2))
cube = Entity(model='cube', collider='box', scale=2, on_click=makeText, texture='grass')
camera.clip_plane_far=20

app.run()