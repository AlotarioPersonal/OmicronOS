from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
import os
import time
import programs
os.system('cls')


print("You are now leaving omicronOS. Press Shift+Q to close the application.")
app = Ursina()

stepper = True


def disableBox():
    global boxOne
    if boxOne==True:
        dragbox.parent=globalpos
        temppos.position=globalpos.position
        boxOne=False
        dragbox.parent=temppos
        dragbox.x = player.camera_pivot.x
        dragbox.y = 0.4
        dragbox.z = player.camera_pivot.z
        print(dragbox.position)
        print(player.forward)
        dragbox.collider='box'
        distancemodifier = 0.6
        #CHANGE NONE OF THE FOLLOWING 9 LINES OF CODE. I am fully aware it jank as all hell, but this is so the player doesn't get stuck inside the box and frankly I don't want to do any more god damn calculations over this fucking dumbshit box
        if player.forward.x > 0:
            dragbox.x += player.forward.x + distancemodifier
        elif player.forward.x < 0:
            dragbox.x += player.forward.x - distancemodifier
            
        if player.forward.z > 0:
            dragbox.z += player.forward.z + distancemodifier
        elif player.forward.z < 0:
            dragbox.z += player.forward.z - distancemodifier
        print("BB")
        #alright, from here on out you're good to edit what you please.
    else:
        pass
    

place = Entity(model='level', collider='mesh', shader=basic_lighting_shader, texture='placetexture', scale=0.02)
place2 = Entity(model='level2', collider='mesh', shader=basic_lighting_shader, texture=place.texture, scale=0.02, position=(0, 10, 0))
player = FirstPersonController()
player.position=(-8, 0.2, 8)
player.cursor.color=(color.black)

def makeText():
    global app
    global stepper
    stepper=False
    quit()

def update():
    globalpos.position = player.position
    if held_keys['shift']:
        player.speed = 10
    if not held_keys['shift']:
        player.speed = 5
        
    if player.y > 20:
        player.y = 0
    
    if player.y < -10:
        player.y = 0
    
    if held_keys['right mouse']:
        disableBox()
        
        

boxOne = False

def startVideo():
    global lobbytvscreen
    global vid
    hearing = Audio('ham.mp3')
    lobbytvscreen.color=color.white
    lobbytvscreen.texture=vid
    hearing.play()

def travelPortalToFirst():
    player.y = -0.3

def travelPortalToSecond():
    player.y = 9
    player.z = 7

def enableBoxText():
    global boxtext
    boxtext = Text("Left Click to Pick Up")

def disableBoxText():
    global boxtext
    destroy(boxtext)

def enableBox():
    global boxOne
    if boxOne==False:
        dragbox.parent=camera
        dragbox.x = 1
        dragbox.y = -0.5
        dragbox.z = 0.5
        print("AA")
        boxOne=True
        dragbox.collider='none'
    else:
        pass

vid = 'smokedham.mp4'
globalpos = Entity(position=(0,0,0), rotation=(0,0,0))
temppos = Entity(position=(0,0,0), rotation=(0,0,0))
button = Entity(model='leavebutton', collider='mesh', scale=0.5, on_click=makeText, texture='leavebutton', rotation=(90,0,90), position=(0, 0, 0))
poster = Entity(model='cube', collider='box', texture='controls', position=(-15.1,0,12), scale_y=1.3)
dragbox = Entity(model='cube', collider='box', shader=basic_lighting_shader, texture='redconcrete', position=(1,-2,1), on_click=enableBox, on_mouse_enter=enableBoxText, on_mouse_exit=disableBoxText)
couch = Entity(model="couch", color=color.brown, texture='couchtexture', collider='mesh', shader=basic_lighting_shader, scale=0.2, position=(0.8,-2.2,9), rotation=(0, 90, 0))
coffeetable = Entity(model="table", texture='table', collider='mesh', shader=basic_lighting_shader, scale=0.5, position=(2.8,-2.6,9), rotation=(0, 0, 0))
officetable = Entity(model='table', collider='mesh', color=color.brown, shader=basic_lighting_shader, scale=0.5, position=(-13, -2.4, -12))
officemonitor = Entity(model='monitor.obj', collider='mesh', texture='monitor', shader=basic_lighting_shader, position=(-13, -1.2, -12), scale=0.4, rotation=(0, -90, 0))
lobbytvtable = Entity(model="table", texture='table', collider='mesh', shader=basic_lighting_shader, scale=0.5, position=(10,-2.6,9), rotation=(0, 0, 0))
lobbytv = Entity(model="tv", texture='brick', collider='mesh', shader=basic_lighting_shader, scale=0.5, position=(9.5,-1.4,9), rotation=(0, 0, 0))
lobbytvscreen = Entity(model='cube', collider='box', texture=None, color=color.black, position=(9.4,-0.48,9), scale_z=1.8, scale_x=0.1, scale_y=1.2, on_click=startVideo)
portal = Entity(model='portal', texture='portal', collider='mesh', shader=basic_lighting_shader, position=(6, -2.2, 12.8), rotation=(0, 90, 0), on_click=travelPortalToSecond)
portal2 = Entity(model='portal', texture='portal', collider='mesh', shader=basic_lighting_shader, position=(6, 8, 9.7), rotation=(0, 90, 0), on_click=travelPortalToFirst)
camera.clip_plane_far=20

#camera.ui.disable()
app.run()