import pygame
import pgzrun
import math
import random

# -~-~-~- Constants -~-~-~-
size_w = 17
size_h = 12

WIDTH = 64 * size_w
HEIGHT = 64 * size_h
TITLE = "Racing Formation"
FPS = 30

TOTAL_LAPS = 5
BASE_SPEED = 5
OFF_ROAD_SPEED = 2
SPEED = 5
SPEED_b = 2
# -------------------------

# -~-~-~- UI Elements -~-~-~-
# - buttons main -
button_play = Actor("button_red", center=(220, 320))
button_track = Actor("button_white_depth", center=(220, 400))
button_car = Actor("button_white_depth", center=(220, 480))
button_settings = Actor("button_white_depth", center=(220, 560))
button_back = Actor("button_red", center=(220, 640))

# - buttons track -
button_asphalt = Actor("button_grey_depth", center=(220, 240))
button_dirt = Actor("button_grey_depth", center=(220, 320))
button_sand = Actor("button_grey_depth", center=(220, 400))

# - buttons car -
button_car_red = Actor("button_grey_depth", center=(220, 240))
button_car_blue = Actor("button_grey_depth", center=(220, 320))
button_car_black = Actor("button_grey_depth", center=(220, 400))
button_car_green = Actor("button_grey_depth", center=(220, 480))
button_car_yellow = Actor("button_grey_depth", center=(220, 560))

# - buttons settings -
button_music = Actor("button_grey_depth", center=(220, 240))
button_game_music = Actor("button_grey_depth", center=(220, 320))
button_menu_music = Actor("button_grey_depth", center=(220, 400))
button_binds = Actor("button_grey_depth", center=(220, 480))

# - buttons binds -
button_bind_forward = Actor("button_grey_depth", center=(220, 240))
button_bind_backward = Actor("button_grey_depth", center=(220, 320))
button_bind_left = Actor("button_grey_depth", center=(220, 400))
button_bind_right = Actor("button_grey_depth", center=(220, 480))

# - input displays -
mouse_scroll_vertical = Actor("mouse_scroll_vertical", center=(button_game_music.x - 120, button_game_music.y))
mouse_scroll_vertical2 = Actor("mouse_scroll_vertical", center=(button_menu_music.x - 120, button_menu_music.y))
drive_foward_d = Actor("keyboard_w_outline", center=(375, 240))
turn_left_d = Actor("keyboard_a_outline", center=(375, 290))
drive_backward_d = Actor("keyboard_s_outline", center=(375, 340))
turn_right_d = Actor("keyboard_d_outline", center=(375, 390))

# - game logo -
logo = Actor("logo_small", center=(230, 130))

keybinds = {
    "forward": keys.W,
    "backward": keys.S,
    "left": keys.A,
    "right": keys.D
}
# ---------------------------

# -~-~-~- Variables -~-~-~-
track = "asphalt"
background = "grass"
mode = "menu"
menu_mode = "main"
car = "black"
current_checkpoint = 0
current_lap = 1

game_over = False
current_music = random.randint(1, 2)
game_music_volume = 0.5
game_music_volume_display = 5.0
menu_music_volume = 0.5
menu_music_volume_display = 5.0
music_is_on = False
# -------------------------

# -~-~-~- Objects -~-~-~-
tires_asphalt_h = [
    Actor("tires_red_small", center=(800,192)),
    Actor("tires_white_small", center=(825,192)),
    Actor("tires_red_small", center=(850,192)),
    Actor("tires_white_small", center=(875,192)),
]
tires_asphalt_v = [
    Actor("tires_red_small", center=(192,205)),
    Actor("tires_white_small", center=(192,230)),
    Actor("tires_red_small", center=(192,255)),
    Actor("tires_white_small", center=(192,280)),
    Actor("tires_red_small", center=(192,305)),
    Actor("tires_white_small", center=(702,300)),
    Actor("tires_red_small", center=(702,275)),
    Actor("tires_white_small", center=(702,250)),
    Actor("tires_red_small", center=(702,225)),
    Actor("tires_white_small", center=(702,200)),
]
asphalt_decorations = [
    Actor("tree_small", center=(390, 180)),
    Actor("tree_small", center=(900, 350)),
    Actor("tree_small", center=(510, 140)),
    Actor("barrier_red_race", center=(860, 50)),
    Actor("barrier_white_race", center=(750, 50)),
    Actor("tent_blue", center=(500, 425)),
    Actor("tent_red", center=(635, 425)),
    Actor("tribune_full3", center=(310, 425)),
    Actor("tribune_full", center=(570, 536)),
    Actor("tribune_empty", center=(708, 536)),
    Actor("barrier_red_race2", center=(980, 545)),
    Actor("barrier_red_race3", center=(775, 728)),
    Actor("barrier_white_race3", center=(665, 728)),
    Actor("barrier_red_race3", center=(535, 728)),
    Actor("barrier_white_race3", center=(425, 728)),
    Actor("barrier_red_race3", center=(295, 728)),
    Actor("barrier_white_race3", center=(185, 728)),
    Actor("rock1", center=(256, 536)),
    Actor("rock2", center=(326, 536)),
    Actor("rock3", center=(306, 500)),
]

tires_dirt_h = [
    Actor("tires_white_small", center=(885, 192)),
    Actor("tires_white_small", center=(860, 192)),
    Actor("tires_white_small", center=(835, 192)),
    Actor("tires_white_small", center=(810, 192)),
    Actor("tires_white_small", center=(785, 192)),
    Actor("tires_white_small", center=(875, 257)),
    Actor("tires_white_small", center=(850, 257)),
    Actor("tires_white_small", center=(825, 257)),
    Actor("tires_white_small", center=(800, 257)),
    Actor("tires_white_small", center=(775, 257)),
    Actor("tires_white_small", center=(760, 192)),
    Actor("tires_white_small", center=(735, 192)),
    Actor("tires_white_small", center=(710, 192)),
    Actor("tires_white_small", center=(575, 575)),
    Actor("tires_white_small", center=(600, 575)),
    Actor("tires_white_small", center=(625, 575)),
]
tires_dirt_v = [
    Actor("tires_white_small", center=(768, 280)),
    Actor("tires_white_small", center=(768, 305)),
    Actor("tires_white_small", center=(768, 330)),
    Actor("tires_white_small", center=(768, 355)),
    Actor("tires_white_small", center=(768, 380)),
    Actor("tires_white_small", center=(768, 405)),
    Actor("tires_white_small", center=(768, 430)),
    Actor("tires_white_small", center=(768, 455)),
    Actor("tires_white_small", center=(768, 480)),
    Actor("tires_white_small", center=(768, 505)),
    Actor("tires_white_small", center=(768, 530)),
    Actor("tires_white_small", center=(768, 555)),
    Actor("tires_white_small", center=(705, 280)),
    Actor("tires_white_small", center=(705, 305)),
    Actor("tires_white_small", center=(705, 330)),
    Actor("tires_white_small", center=(705, 355)),
    Actor("tires_white_small", center=(705, 380)),
    Actor("tires_white_small", center=(705, 405)),
    Actor("tires_white_small", center=(705, 430)),
    Actor("tires_white_small", center=(705, 455)),
    Actor("tires_white_small", center=(705, 480)),
    Actor("tires_white_small", center=(705, 505)),
    Actor("tires_white_small", center=(705, 530)),
    Actor("tires_white_small", center=(705, 555)),
    Actor("tires_white_small", center=(705, 255)),
    Actor("tires_white_small", center=(705, 230)),
    Actor("tires_white_small", center=(705, 205)),
]
dirt_decorations = [
    Actor("tribune_full3", center=(500, 418)),
    Actor("tribune_full2", center=(868, 390)),
    Actor("tribune_empty2", center=(868, 528)),
    Actor("tribune_full2", center=(360, 418)),
    Actor("tree_small", center=(375, 550)),
    Actor("tree_small", center=(955, 590)),
    Actor("tree_small", center=(975, 480)),
    Actor("tree_small", center=(955, 370)),
    Actor("rock1", center=(478, 225)),
    Actor("rock3", center=(548, 225)),
    Actor("tent_blue", center=(250, 650)),
    Actor("tent_red", center=(118, 650)),
    Actor("barrier_white_race3", center=(590, 728)),
    Actor("barrier_red_race3", center=(700, 728)),
    Actor("barrier_red_race4", center=(45, 435)),
    Actor("barrier_white_race4", center=(45, 325)),
    Actor("barrier_red_race4", center=(45, 215)),
]

tires_sand_h = [
    Actor("tires_white_small", center=(350,192)),
    Actor("tires_white_small", center=(325,192)),
    Actor("tires_white_small", center=(300,192)),
    Actor("tires_white_small", center=(275,192)),
    Actor("tires_white_small", center=(250,192)),
    Actor("tires_white_small", center=(225,192)),
    Actor("tires_white_small", center=(200,192)),

    Actor("tires_white_small", center=(500,127)),
    Actor("tires_white_small", center=(475,127)),
    Actor("tires_white_small", center=(450,127)),
    Actor("tires_white_small", center=(425,127)),
    Actor("tires_white_small", center=(400,127)),
    Actor("tires_white_small", center=(375,127)),
    Actor("tires_white_small", center=(350,127)),
    Actor("tires_white_small", center=(325,127)),
    Actor("tires_white_small", center=(300,127)),
    Actor("tires_white_small", center=(275,127)),
    Actor("tires_white_small", center=(250,127)),
    Actor("tires_white_small", center=(225,127)),
    Actor("tires_white_small", center=(200,127)),
    Actor("tires_white_small", center=(175,127)),
    Actor("tires_white_small", center=(150,127)),
    Actor("tires_white_small", center=(125,127)),

    Actor("tires_white_small", center=(500,65)),
    Actor("tires_white_small", center=(475,65)),
    Actor("tires_white_small", center=(450,65)),
    Actor("tires_white_small", center=(425,65)),
    Actor("tires_white_small", center=(400,65)),
    Actor("tires_white_small", center=(375,65)),
    Actor("tires_white_small", center=(350,65)),
    Actor("tires_white_small", center=(325,65)),
    Actor("tires_white_small", center=(300,65)),
    Actor("tires_white_small", center=(275,65)),
    Actor("tires_white_small", center=(250,65)),
    Actor("tires_white_small", center=(225,65)),
    Actor("tires_white_small", center=(200,65)),
    Actor("tires_white_small", center=(175,65)),
    Actor("tires_white_small", center=(150,65)),
    Actor("tires_white_small", center=(125,65)),

    Actor("tires_white_small", center=(415,450)),
    Actor("tires_white_small", center=(390,450)),
    Actor("tires_white_small", center=(365,450)),
    Actor("tires_white_small", center=(340,450)),
    Actor("tires_white_small", center=(315,450)),
]
tires_sand_v = [
    Actor("tires_white_small", center=(200,225)),
    Actor("tires_white_small", center=(125,150)),
    Actor("tires_white_small", center=(125,175)),
    Actor("tires_white_small", center=(255,335)),
    Actor("tires_white_small", center=(255,360)),
    Actor("tires_white_small", center=(390,310)),
    Actor("tires_white_small", center=(390,285)),
]
sand_decorations = [
    Actor("tribune_full4", center=(780, 300)),
    Actor("tribune_empty4", center=(780, 440)),
]
# -----------------------

# -~-~-~- collisions -~-~-~-
def check_tires_asphalt():
    global SPEED, SPEED_b
    for t in tires_asphalt_h:
        if car_player.colliderect(t) and car_player.y < t.y:
            car_player.y = t.y - 38
        elif car_player.colliderect(t) and car_player.y > t.y:
            car_player.y = t.y + 38
    for t in tires_asphalt_v:
        if car_player.colliderect(t) and car_player.x < t.x:
            car_player.x = t.x - 38
        elif car_player.colliderect(t) and car_player.x > t.x:
            car_player.x = t.x + 38
def check_tires_dirt():
    global SPEED, SPEED_b
    for t in tires_dirt_h:
        if car_player.colliderect(t) and car_player.y < t.y:
            car_player.y = t.y - 38
        elif car_player.colliderect(t) and car_player.y > t.y:
            car_player.y = t.y + 38
    for t in tires_dirt_v:
        if car_player.colliderect(t) and car_player.x < t.x:
            car_player.x = t.x - 38
        elif car_player.colliderect(t) and car_player.x > t.x:
            car_player.x = t.x + 38
def check_tires_sand():
    global SPEED, SPEED_b
    for t in tires_sand_h:
        if car_player.colliderect(t) and car_player.y < t.y:
            car_player.y = t.y - 35
        elif car_player.colliderect(t) and car_player.y > t.y:
            car_player.y = t.y + 35
    for t in tires_sand_v:
        if car_player.colliderect(t) and car_player.x < t.x:
            car_player.x = t.x - 35
        elif car_player.colliderect(t) and car_player.x > t.x:
            car_player.x = t.x + 35
# --------------------------

# -~-~-~- Maps -~-~-~-
grass_plain = [
    [2,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1],
    [4,5,12,5,5,5,12,5,12,5,5,12,12,5,5,12,6],
    [4,5,12,12,5,12,5,5,12,5,12,12,5,5,5,5,6],
    [4,5,5,5,5,12,12,5,12,5,5,5,12,12,5,12,6],
    [4,5,12,5,12,12,5,5,5,12,12,5,12,5,5,5,6],
    [4,5,5,12,5,12,5,5,12,5,12,12,5,5,5,12,6],
    [4,5,5,12,5,5,12,5,12,12,5,5,5,12,5,12,6],
    [4,5,5,5,5,5,12,5,12,5,12,5,5,12,12,12,6],
    [4,5,5,12,5,12,5,12,12,5,5,12,5,12,5,5,6],
    [4,5,5,12,12,5,12,5,5,5,12,12,5,12,5,5,6],
    [4,5,12,5,12,12,5,5,12,5,12,5,12,5,5,5,6],
    [7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,3]
]
sand_plain = [
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [4,5,12,5,12,5,5,5,12,5,12,5,12,12,5,5,6],
    [4,5,5,5,5,5,12,12,5,12,5,5,12,12,5,12,6],
    [4,12,12,12,5,5,5,12,5,12,5,5,5,12,5,5,6],
    [4,12,5,5,5,5,12,12,5,12,5,12,5,12,5,5,6],
    [4,12,5,12,12,5,5,5,12,5,12,5,5,12,5,5,6],
    [4,5,5,5,5,12,5,12,12,5,5,12,12,5,5,12,6],
    [4,5,12,12,5,12,5,12,5,12,5,5,12,5,5,5,6],
    [4,12,5,12,5,5,12,5,5,12,5,5,12,12,5,5,6],
    [4,5,5,5,5,12,5,12,5,5,12,12,5,12,5,12,6],
    [4,12,5,5,12,5,5,12,5,12,12,5,5,12,5,5,6],
    [7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9]
]
dirt_plain = [
    [ 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [ 4, 5,12, 5,12, 5, 5, 5,12, 5,12, 5,12,12, 5, 5, 6],
    [ 4, 5, 5, 5, 5, 5,12,12, 5,12, 5, 5,12,12, 5,12, 6],
    [ 4,12,12,12, 5, 5, 5,12, 5,12, 5, 5, 5,12, 5, 5, 6],
    [ 4,12, 5, 5, 5, 5,12,12, 5,12, 5,12, 5,12, 5, 5, 6],
    [ 4,12, 5,12,12, 5, 5, 5,12, 5,12, 5, 5,12, 5, 5, 6],
    [ 4, 5, 5, 5, 5,12, 5,12,12, 5, 5,12,12, 5, 5,12, 6],
    [ 4, 5,12,12, 5,12, 5,12, 5,12, 5, 5,12, 5, 5, 5, 6],
    [ 4,12, 5,12, 5, 5,12, 5, 5,12, 5, 5,12,12, 5, 5, 6],
    [ 4, 5, 5, 5, 5,12, 5,12, 5, 5,12,12, 5,12, 5,12, 6],
    [ 4,12, 5, 5,12, 5, 5,12, 5,12,12, 5, 5,12, 5, 5, 6],
    [ 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]
]

Track_asphalt = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 4, 5, 6, 0, 0, 0, 0, 1,27,27,27,27,32,36, 0],
    [0,12,13,14,15, 0, 0, 0, 0, 8,13,28,28,28,14,35, 0],
    [0, 8, 9, 8, 9, 0, 7,26,27,18, 9,40,44,27,18,34, 0],
    [0,20,21, 8,17,27,16,24,28,28,11,39,13,28,29,33, 0],
    [0,22,23,10,28,28,19,25, 0, 0, 0, 8, 9, 0, 0, 0, 0],
    [0,23,22, 0, 0, 0, 0, 0, 0, 0, 0,38,17,32,36, 0, 0],
    [0,22,23, 0, 0, 0, 0, 0, 0, 0, 0,37,41,14,35, 0, 0],
    [0,23,22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 0, 0],
    [0, 8,17,27,27,27,27,27,27,27,27,27,27,18,34, 0, 0],
    [0,10,28,28,28,28,28,28,28,28,28,28,28,29,33, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
Track_dirt = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6,18,38,27,13,27,13,28,38,38,38,38,38,34,30, 0],
    [0, 5,16,39,13,27,13,27,29,39,39,39,39,39,17,31, 0],
    [0,12,14, 6,18, 9,10, 0, 0, 0, 0, 2, 1,11,36,32, 0],
    [0,12,14, 5,16,21,22,38,38,34,30,40, 2,11,37,33, 0],
    [0,12,14,12,14,25,26,39,39,17,31,40,40, 0, 0, 0, 0],
    [0,12,14,12,14, 0, 0, 0, 0,12,14,40,40, 0, 0, 0, 0],
    [0, 4,35,36,32, 0, 0, 6,18,36,32,40,40, 0, 0, 0, 0],
    [0, 3,15,37,33, 0, 0, 5,16,37,33,40,40, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4,35,38,38,36,32, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3,15,39,39,37,33, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
Track_sand = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0,34,33,33,33,33,33, 8,10,10,35,35,35,35, 4, 5, 0],
    [0,32,34,33,33,33,33, 8,10,10,36,36,36,15,10,16, 0],
    [0, 9,11, 1, 4, 5, 0, 0, 0, 0, 0, 0, 0, 9,10,11, 0],
    [0,19,10,10,10,16, 6, 7, 4, 5, 0, 0, 0, 9,10,11, 0],
    [0,25,26,12,19,20,17,18,15,16, 0, 0, 0, 9,10,11, 0],
    [0, 0, 0, 0,25,26,23,24, 9,11, 0, 0, 0, 9,10,11, 0],
    [0, 2, 3,35,35,35,35,35,21,22, 0, 0, 0, 9,10,11, 0],
    [0,13,14,36,36,36,36,36,27,28, 0, 0, 0, 9,10,11, 0],
    [0,19,20,35,29,10,29,10,30,35,35,35,35,21,10,22, 0],
    [0,25,26,36,10,29,10,29,31,36,36,36,36,36,27,28, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

checkpoints_asphalt = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
    [0,99,99, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
checkpoints_dirt = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 9, 0, 0, 0, 0, 0,99, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 9, 9, 0, 0, 0, 0, 0,99, 0, 0, 0, 1, 0, 2, 2, 0],
    [0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
    [0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
checkpoints_sand = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 6, 0, 0, 7, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 9, 0, 0, 0, 0, 0,99, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0,99, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# --------------------

# -~-~-~- Preparing the Map Surface -~-~-~-
map_surface = pygame.Surface((WIDTH, HEIGHT))
# - seting background acording to the selected track -
def set_track(selected_track):
    global track, background
    track = selected_track
    if track == "asphalt":
        background = "grass"
    elif track == "dirt":
        background = "sand"
    elif track == "sand":
        background = "dirt"
    prepare_map()

def prepare_map():
    if background == "grass":
        for i in range(len(grass_plain)):
            for j in range(len(grass_plain[0])):
                val = grass_plain[i][j]
                # Seleciona o ator correto de acordo com a matriz
                tile = None
                if val == 1: tile = Actor("land_grass1")
                elif val == 2: tile = Actor("land_grass2")
                elif val == 3: tile = Actor("land_grass3")
                elif val == 4: tile = Actor("land_grass4")
                elif val == 5: tile = Actor("land_grass5")
                elif val == 6: tile = Actor("land_grass6")
                elif val == 7: tile = Actor("land_grass7")
                elif val == 8: tile = Actor("land_grass8")
                elif val == 9: tile = Actor("land_grass9")
                elif val == 10: tile = Actor("land_grass10")
                elif val == 11: tile = Actor("land_grass11")
                elif val == 12: tile = Actor("land_grass12")
                elif val == 13: tile = Actor("land_grass13")
                elif val == 14: tile = Actor("land_grass14")

                if tile:
                    tile.left = tile.width * j
                    tile.top = tile.height * i
                    # Blit copia o gráfico do ator para a nossa superfície do mapa
                    map_surface.blit(tile._surf, tile.topleft)
    if background == "sand":
            for i in range(len(sand_plain)):
                for j in range(len(sand_plain[0])):
                    val = sand_plain[i][j]
                    # Seleciona o ator correto de acordo com a matriz
                    tile = None
                    if val == 1: tile = Actor("land_sand1")
                    elif val == 2: tile = Actor("land_sand2")
                    elif val == 3: tile = Actor("land_sand3")
                    elif val == 4: tile = Actor("land_sand4")
                    elif val == 5: tile = Actor("land_sand5")
                    elif val == 6: tile = Actor("land_sand6")
                    elif val == 7: tile = Actor("land_sand7")
                    elif val == 8: tile = Actor("land_sand8")
                    elif val == 9: tile = Actor("land_sand9")
                    elif val == 10: tile = Actor("land_sand10")
                    elif val == 11: tile = Actor("land_sand11")
                    elif val == 12: tile = Actor("land_sand12")
                    elif val == 13: tile = Actor("land_sand13")
                    elif val == 14: tile = Actor("land_sand14")

                    if tile:
                        tile.left = tile.width * j
                        tile.top = tile.height * i
                        # Blit copia o gráfico do ator para a nossa superfície do mapa
                        map_surface.blit(tile._surf, tile.topleft)
    if background == "dirt":
                for i in range(len(dirt_plain)):
                    for j in range(len(dirt_plain[0])):
                        val = dirt_plain[i][j]
                        # Seleciona o ator correto de acordo com a matriz
                        tile = None
                        if val == 1: tile = Actor("land_dirt1")
                        elif val == 2: tile = Actor("land_dirt2")
                        elif val == 3: tile = Actor("land_dirt3")
                        elif val == 4: tile = Actor("land_dirt4")
                        elif val == 5: tile = Actor("land_dirt5")
                        elif val == 6: tile = Actor("land_dirt6")
                        elif val == 7: tile = Actor("land_dirt7")
                        elif val == 8: tile = Actor("land_dirt8")
                        elif val == 9: tile = Actor("land_dirt9")
                        elif val == 10: tile = Actor("land_dirt10")
                        elif val == 11: tile = Actor("land_dirt11")
                        elif val == 12: tile = Actor("land_dirt12")
                        elif val == 13: tile = Actor("land_dirt13")
                        elif val == 14: tile = Actor("land_dirt14")

                        if tile:
                            tile.left = tile.width * j
                            tile.top = tile.height * i
                            # Blit copia o gráfico do ator para a nossa superfície do mapa
                            map_surface.blit(tile._surf, tile.topleft)

    if track == "asphalt":
            for i in range(len(Track_asphalt)):
                for j in range(len(Track_asphalt[0])):
                    val = Track_asphalt[i][j]
                    tile = None
                    if val == 1: tile = Actor("road_asphalt01")
                    elif val == 2: tile = Actor("road_asphalt02")
                    elif val == 3: tile = Actor("road_asphalt03")
                    elif val == 4: tile = Actor("road_asphalt04")
                    elif val == 5: tile = Actor("road_asphalt05")
                    elif val == 6: tile = Actor("road_asphalt06")
                    elif val == 7: tile = Actor("road_asphalt07")
                    elif val == 8: tile = Actor("road_asphalt08")
                    elif val == 9: tile = Actor("road_asphalt09")
                    elif val == 10: tile = Actor("road_asphalt10")
                    elif val == 11: tile = Actor("road_asphalt11")
                    elif val == 12: tile = Actor("road_asphalt12")
                    elif val == 13: tile = Actor("road_asphalt13")
                    elif val == 14: tile = Actor("road_asphalt14")
                    elif val == 15: tile = Actor("road_asphalt15")
                    elif val == 16: tile = Actor("road_asphalt16")
                    elif val == 17: tile = Actor("road_asphalt17")
                    elif val == 18: tile = Actor("road_asphalt18")
                    elif val == 19: tile = Actor("road_asphalt19")
                    elif val == 20: tile = Actor("road_asphalt20")
                    elif val == 21: tile = Actor("road_asphalt21")
                    elif val == 22: tile = Actor("road_asphalt22")
                    elif val == 23: tile = Actor("road_asphalt23")
                    elif val == 24: tile = Actor("road_asphalt24")
                    elif val == 25: tile = Actor("road_asphalt25")
                    elif val == 26: tile = Actor("road_asphalt26")
                    elif val == 27: tile = Actor("road_asphalt27")
                    elif val == 28: tile = Actor("road_asphalt28")
                    elif val == 29: tile = Actor("road_asphalt29")
                    elif val == 32: tile = Actor("road_asphalt32")
                    elif val == 33: tile = Actor("road_asphalt33")
                    elif val == 34: tile = Actor("road_asphalt34")
                    elif val == 35: tile = Actor("road_asphalt35")
                    elif val == 36: tile = Actor("road_asphalt36")
                    elif val == 37: tile = Actor("road_asphalt37")
                    elif val == 38: tile = Actor("road_asphalt38")
                    elif val == 39: tile = Actor("road_asphalt39")
                    elif val == 40: tile = Actor("road_asphalt40")
                    elif val == 41: tile = Actor("road_asphalt41")
                    elif val == 44: tile = Actor("road_asphalt44")


                    if tile:
                        tile.left = tile.width * j
                        tile.top = tile.height * i
                        map_surface.blit(tile._surf, tile.topleft)
    if track == "dirt":
            for i in range(len(Track_dirt)):
                for j in range(len(Track_dirt[0])):
                    val = Track_dirt[i][j]
                    
                    tile = None
                    if val == 1: tile = Actor("road_dirt1")
                    elif val == 2: tile = Actor("road_dirt2")
                    elif val == 3: tile = Actor("road_dirt3")
                    elif val == 4: tile = Actor("road_dirt4")
                    elif val == 5: tile = Actor("road_dirt5")
                    elif val == 6: tile = Actor("road_dirt6")
                    elif val == 7: tile = Actor("road_dirt7")
                    elif val == 8: tile = Actor("road_dirt8")
                    elif val == 9: tile = Actor("road_dirt9")
                    elif val == 10: tile = Actor("road_dirt10")
                    elif val == 11: tile = Actor("road_dirt11")
                    elif val == 12: tile = Actor("road_dirt12")
                    elif val == 13: tile = Actor("road_dirt13")
                    elif val == 14: tile = Actor("road_dirt14")
                    elif val == 15: tile = Actor("road_dirt15")
                    elif val == 16: tile = Actor("road_dirt16")
                    elif val == 17: tile = Actor("road_dirt17")
                    elif val == 18: tile = Actor("road_dirt18")
                    elif val == 19: tile = Actor("road_dirt19")
                    elif val == 20: tile = Actor("road_dirt20")
                    elif val == 21: tile = Actor("road_dirt21")
                    elif val == 22: tile = Actor("road_dirt22")
                    elif val == 23: tile = Actor("road_dirt23")
                    elif val == 24: tile = Actor("road_dirt24")
                    elif val == 25: tile = Actor("road_dirt25")
                    elif val == 26: tile = Actor("road_dirt26")
                    elif val == 27: tile = Actor("road_dirt27")
                    elif val == 28: tile = Actor("road_dirt28")
                    elif val == 29: tile = Actor("road_dirt29")
                    elif val == 30: tile = Actor("road_dirt30")
                    elif val == 31: tile = Actor("road_dirt31")
                    elif val == 32: tile = Actor("road_dirt32")
                    elif val == 33: tile = Actor("road_dirt33")
                    elif val == 34: tile = Actor("road_dirt34")
                    elif val == 35: tile = Actor("road_dirt35")
                    elif val == 36: tile = Actor("road_dirt36")
                    elif val == 37: tile = Actor("road_dirt37")
                    elif val == 38: tile = Actor("road_dirt38")
                    elif val == 39: tile = Actor("road_dirt39")
                    elif val == 40: tile = Actor("road_dirt40")

                    if tile:
                        tile.left = tile.width * j
                        tile.top = tile.height * i
                        map_surface.blit(tile._surf, tile.topleft)
    if track == "sand":
                for i in range(len(Track_sand)):
                    for j in range(len(Track_sand[0])):
                        val = Track_sand[i][j]

                        tile = None
                        if val == 1: tile = Actor("road_sand1")
                        elif val == 2: tile = Actor("road_sand2")
                        elif val == 3: tile = Actor("road_sand3")
                        elif val == 4: tile = Actor("road_sand4")
                        elif val == 5: tile = Actor("road_sand5")
                        elif val == 6: tile = Actor("road_sand6")
                        elif val == 7: tile = Actor("road_sand7")
                        elif val == 8: tile = Actor("road_sand8")
                        elif val == 9: tile = Actor("road_sand9")
                        elif val == 10: tile = Actor("road_sand10")
                        elif val == 11: tile = Actor("road_sand11")
                        elif val == 12: tile = Actor("road_sand12")
                        elif val == 13: tile = Actor("road_sand13")
                        elif val == 14: tile = Actor("road_sand14")
                        elif val == 15: tile = Actor("road_sand15")
                        elif val == 16: tile = Actor("road_sand16")
                        elif val == 17: tile = Actor("road_sand17")
                        elif val == 18: tile = Actor("road_sand18")
                        elif val == 19: tile = Actor("road_sand19")
                        elif val == 20: tile = Actor("road_sand20")
                        elif val == 21: tile = Actor("road_sand21")
                        elif val == 22: tile = Actor("road_sand22")
                        elif val == 23: tile = Actor("road_sand23")
                        elif val == 24: tile = Actor("road_sand24")
                        elif val == 25: tile = Actor("road_sand25")
                        elif val == 26: tile = Actor("road_sand26")
                        elif val == 27: tile = Actor("road_sand27")
                        elif val == 28: tile = Actor("road_sand28")
                        elif val == 29: tile = Actor("road_sand29")
                        elif val == 30: tile = Actor("road_sand30")
                        elif val == 31: tile = Actor("road_sand31")
                        elif val == 32: tile = Actor("road_sand32")
                        elif val == 33: tile = Actor("road_sand33")
                        elif val == 34: tile = Actor("road_sand34")
                        elif val == 35: tile = Actor("road_sand35")
                        elif val == 36: tile = Actor("road_sand36")
    
                        if tile:
                            tile.left = tile.width * j
                            tile.top = tile.height * i
                            map_surface.blit(tile._surf, tile.topleft)
prepare_map()
if mode == "menu":
    if current_music == 1 and music_is_on:
        music.play("background_1")
        music.set_volume(game_music_volume)
    elif current_music == 2 and music_is_on:
        music.play("background_2")
        music.set_volume(game_music_volume)

def check_checkpoints(grid_x, grid_y):
    global current_checkpoint, current_lap, game_over
    
    if game_over:
        return

    # Seleciona o mapa de checkpoints correto
    cp_map = checkpoints_asphalt
    if track == "dirt":
        cp_map = checkpoints_dirt
    elif track == "sand":
        cp_map = checkpoints_sand

    # Pega o valor do checkpoint na posição atual do carro
    tile_cp = cp_map[grid_y][grid_x]
    
    # 1. Se passou no próximo checkpoint intermediário esperado
    if tile_cp == current_checkpoint + 1:
        current_checkpoint += 1
        
    # 2. Se completou todos os checkpoints e cruzou a linha de chegada (99)
    elif tile_cp == 99 and current_checkpoint == 9:
        if current_lap < TOTAL_LAPS:
            current_lap += 1
            current_checkpoint = 0  # Reseta para validar a próxima volta
        else:
            game_over = True
# ----------------------------------------

# -~-~-~- Cars -~-~-~-
car_player = Actor("car_black_small_5", pos=(160, 360))
menu_car_red = Actor("car_red_small_5", center=(button_car_red.x + 150, button_car_red.y))
menu_car_blue = Actor("car_blue_small_5", center=(button_car_blue.x + 150, button_car_blue.y))
menu_car_black = Actor("car_black_small_5", center=(button_car_black.x + 150, button_car_black.y))
menu_car_green = Actor("car_green_small_5", center=(button_car_green.x + 150, button_car_green.y))
menu_car_yellow = Actor("car_yellow_small_5", center=(button_car_yellow.x + 150, button_car_yellow.y))
# --------------------

# -~-~-~- Functions -~-~-~-
def draw():
    global button_asphalt, button_dirt, button_sand, button_car_red, button_car_blue, button_car_black, button_car_green, button_car_yellow, button_play, button_track, button_car, button_back, drive_foward_d, drive_backward_d, turn_left_d, turn_right_d
    screen.clear()

    # - In menu graphics -
    if mode == "menu":
        if track == "asphalt":
            for i in range(len(tires_asphalt_h)):
                tires_asphalt_h[i].draw()
            for i in range(len(tires_asphalt_v)):
                tires_asphalt_v[i].draw()
            screen.blit(map_surface, (0, 0))

            for i in range(len(asphalt_decorations)):
                asphalt_decorations[i].draw()

        elif track == "dirt":
            for i in range(len(tires_dirt_h)):
                tires_dirt_h[i].draw()
            for i in range(len(tires_dirt_v)):
                tires_dirt_v[i].draw()
            screen.blit(map_surface, (0, 0))
            
            for i in range(len(dirt_decorations)):
                dirt_decorations[i].draw()
        elif track == "sand":
            for i in range(len(tires_sand_h)):
                tires_sand_h[i].draw()
            for i in range(len(tires_sand_v)):
                tires_sand_v[i].draw()
            screen.blit(map_surface, (0, 0))
            
            for i in range(len(sand_decorations)):
                sand_decorations[i].draw()

        quadrado = pygame.Rect((0, 0), (WIDTH/2, HEIGHT))
        screen.draw.filled_rect(quadrado, (0, 0, 0))

        if menu_mode == "main":
            # - logo -
            logo.draw()

            # - main menu buttons -
            button_play.draw()
            button_track.draw()
            button_car.draw()
            button_settings.draw()
    
            screen.draw.text("PLAY", center=button_play.pos, fontsize=40, fontname="kenney_future", color="black")
            screen.draw.text("TRACK", center=button_track.pos, fontsize=38, fontname="kenney_future", color="black")
            screen.draw.text("CAR", center=button_car.pos, fontsize=40, fontname="kenney_future", color="black")
            screen.draw.text("SETTINGS", center=button_settings.pos, fontsize=28, fontname="kenney_future", color="black")         
        elif menu_mode == "track":
            # - track selection buttons -
            button_asphalt = Actor("button_grey", center=(220, 240)) if track == "asphalt" else Actor("button_grey_depth", center=(220, 240))
            button_dirt = Actor("button_grey", center=(220, 320)) if track == "dirt" else Actor("button_grey_depth", center=(220, 320))
            button_sand = Actor("button_grey", center=(220, 400)) if track == "sand" else Actor("button_grey_depth", center=(220, 400))
            # - check marks -
            check_button_asphalt = Actor("checked_square_grey", center=(100, 240)) if track == "asphalt" else Actor("check_square_grey", center=(100, 240))
            check_button_dirt = Actor("checked_square_grey", center=(100, 320)) if track == "dirt" else Actor("check_square_grey", center=(100, 320))
            check_button_sand = Actor("checked_square_grey", center=(100, 400)) if track == "sand" else Actor("check_square_grey", center=(100, 400))

            # - track selection buttons -
            button_asphalt.draw()
            button_dirt.draw()
            button_sand.draw()
            button_back.draw()

            check_button_asphalt.draw()
            check_button_dirt.draw()
            check_button_sand.draw()

            screen.draw.text("ASPHALT", center=button_asphalt.pos, fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("DIRT", center=button_dirt.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("SAND", center=button_sand.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("BACK", center=button_back.pos, fontsize=30, fontname="kenney_future", color="black")

            screen.draw.text("- fundo = grama", pos=(340, 210), fontsize=24, color="white")
            screen.draw.text("- dificuldade = fácil", pos=(340, 230), fontsize=24, color="white")
            screen.draw.text("- fundo = terra", pos=(340, 290), fontsize=24, color="white")
            screen.draw.text("- dificuldade = média", pos=(340, 310), fontsize=24, color="white")
            screen.draw.text("- fundo = areia", pos=(340, 370), fontsize=24, color="white")
            screen.draw.text("- dificuldade = difícil", pos=(340, 390), fontsize=24, color="white")
        elif menu_mode == "car":
            check_button_red = Actor("checked_square_grey", center=(100, 240)) if car == "red" else Actor("check_square_grey", center=(100, 240))
            check_button_blue = Actor("checked_square_grey", center=(100, 320)) if car == "blue" else Actor("check_square_grey", center=(100, 320))
            check_button_black = Actor("checked_square_grey", center=(100, 400)) if car == "black" else Actor("check_square_grey", center=(100, 400))
            check_button_green = Actor("checked_square_grey", center=(100, 480)) if car == "green" else Actor("check_square_grey", center=(100, 480))
            check_button_yellow = Actor("checked_square_grey", center=(100, 560)) if car == "yellow" else Actor("check_square_grey", center=(100, 560))

            # - car selection buttons -
            button_car_red.draw()
            button_car_blue.draw()
            button_car_black.draw()
            button_car_green.draw()
            button_car_yellow.draw()
            button_back.draw()

            check_button_red.draw()
            check_button_blue.draw()
            check_button_black.draw()
            check_button_green.draw()
            check_button_yellow.draw()

            menu_car_red.draw()
            menu_car_blue.draw()
            menu_car_black.draw()
            menu_car_green.draw()
            menu_car_yellow.draw()

            button_car_red = Actor("button_grey", center=(220, 240)) if car == "red" else Actor("button_grey_depth", center=(220, 240))
            button_car_blue = Actor("button_grey", center=(220, 320)) if car == "blue" else Actor("button_grey_depth", center=(220, 320))
            button_car_black = Actor("button_grey", center=(220, 400)) if car == "black" else Actor("button_grey_depth", center=(220, 400))
            button_car_green = Actor("button_grey", center=(220, 480)) if car == "green" else Actor("button_grey_depth", center=(220, 480))
            button_car_yellow = Actor("button_grey", center=(220, 560)) if car == "yellow" else Actor("button_grey_depth", center=(220, 560))

            screen.draw.text("RED", center=button_car_red.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("BLUE", center=button_car_blue.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("BLACK", center=button_car_black.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("GREEN", center=button_car_green.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("YELLOW", center=button_car_yellow.pos, fontsize=30, fontname="kenney_future", color="black")
            screen.draw.text("BACK", center=button_back.pos, fontsize=30, fontname="kenney_future", color="black")
        elif menu_mode == "settings":
            button_music = Actor("button_grey", center=(220, 240)) if music_is_on else Actor("button_grey_depth", center=(220, 240))
            check_button_music = Actor("checked_square_grey", center=(100, 240)) if music_is_on else Actor("check_square_grey", center=(100, 240))

            button_music.draw()
            button_game_music.draw()
            button_menu_music.draw()
            button_binds.draw()
            button_back.draw()

            mouse_scroll_vertical.draw()
            mouse_scroll_vertical2.draw()

            check_button_music.draw()

            screen.draw.text("MUSIC", center=button_music.pos, fontsize=40, fontname="kenney_future", color="black")
            screen.draw.text("game", center=(button_game_music.x - 20, button_game_music.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("music", center=(button_game_music.x + 20, button_game_music.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("menu", center=(button_menu_music.x - 20, button_menu_music.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("music", center=(button_menu_music.x + 20, button_menu_music.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("BINDS", center=button_binds.pos, fontsize=40, fontname="kenney_future", color="black")
            screen.draw.text("BACK", center=button_back.pos, fontsize=40, fontname="kenney_future", color="black")

            screen.draw.text("- volume: " + str(game_music_volume_display), pos=(button_game_music.x + 105, button_game_music.y - 10), fontsize=30, color="white")
            screen.draw.text("- volume: " + str(menu_music_volume_display), pos=(button_menu_music.x + 105, button_menu_music.y - 10), fontsize=30, color="white")
        elif menu_mode == "binds":
            button_bind_forward.draw()
            button_bind_backward.draw()
            button_bind_left.draw()
            button_bind_right.draw()
            button_back.draw()

            drive_foward_d.draw()
            drive_backward_d.draw()
            turn_left_d.draw()
            turn_right_d.draw()

            screen.draw.text("drive", center=(button_bind_forward.x - 20, button_bind_forward.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("forward", center=(button_bind_forward.x + 5, button_bind_forward.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("drive", center=(button_bind_backward.x - 20, button_bind_backward.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("back", center=(button_bind_backward.x + 20, button_bind_backward.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("turn", center=(button_bind_left.x - 20, button_bind_left.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("left", center=(button_bind_left.x + 20, button_bind_left.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("turn", center=(button_bind_right.x - 20, button_bind_right.y - 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("right", center=(button_bind_right.x + 20, button_bind_right.y + 10), fontsize=28, fontname="kenney_future", color="black")
            screen.draw.text("BACK", center=button_back.pos, fontsize=40, fontname="kenney_future", color="black")

    # - In game graphics -
    elif mode == "game":
        if track == "asphalt":
            for i in range(len(tires_asphalt_h)):
                tires_asphalt_h[i].draw()
            for i in range(len(tires_asphalt_v)):
                tires_asphalt_v[i].draw()
            screen.blit(map_surface, (0, 0))
            
            car_player.draw()
            for i in range(len(asphalt_decorations)):
                asphalt_decorations[i].draw()

        elif track == "dirt":
            for i in range(len(tires_dirt_h)):
                tires_dirt_h[i].draw()
            for i in range(len(tires_dirt_v)):
                tires_dirt_v[i].draw()
            screen.blit(map_surface, (0, 0))
            
            car_player.draw()
            for i in range(len(dirt_decorations)):
                dirt_decorations[i].draw()

        elif track == "sand":
            for i in range(len(tires_sand_h)):
                tires_sand_h[i].draw()
            for i in range(len(tires_sand_v)):
                tires_sand_v[i].draw()
            screen.blit(map_surface, (0, 0))
            
            car_player.draw()
            for i in range(len(sand_decorations)):
                sand_decorations[i].draw()

        # - Laps interface -
        if not game_over:
            screen.draw.text(f"Volta: {current_lap}/{TOTAL_LAPS}", (10, 10), fontsize=30, color="yellow", owidth=1, ocolor="black")
            screen.draw.text(f"CP: {current_checkpoint}/9", (10, 40), fontsize=20, color="white", owidth=1, ocolor="black")
        else:
            screen.draw.text("CORRIDA FINALIZADA!", center=(WIDTH/2, HEIGHT/2 - 20), fontsize=60, color="gold", owidth=2, ocolor="black")
            screen.draw.text("Pressione ESC para voltar ao Menu", center=(WIDTH/2, HEIGHT/2 + 40), fontsize=30, color="white", owidth=1, ocolor="black")

def update(dt):
    global SPEED, SPEED_b, track, background, mode, car, game_over, drive_foward_d, turn_left_d, turn_right_d, drive_backward_d
    if mode == "game":

        # - Get the grid position of the car -
        grid_x = int(car_player.x // 64)
        grid_y = int(car_player.y // 64)

        grid_x = max(0, min(grid_x, size_w - 1))
        grid_y = max(0, min(grid_y, size_h - 1))

        # - Check checkpoints -
        check_checkpoints(grid_x, grid_y)

        # - Check the track type and adjust speed accordingly -
        if track == "asphalt":
            if Track_asphalt[grid_y][grid_x] == 0:
                SPEED = OFF_ROAD_SPEED
            else:
                SPEED = BASE_SPEED
        elif track == "dirt":
            if Track_dirt[grid_y][grid_x] == 0:
                SPEED = OFF_ROAD_SPEED
            else:
                SPEED = BASE_SPEED
        elif track == "sand":
            if Track_sand[grid_y][grid_x] == 0:
                SPEED = OFF_ROAD_SPEED
            else:
                SPEED = BASE_SPEED
        
        SPEED_b = 3
        if track == "asphalt":
            check_tires_asphalt()
        elif track == "dirt":
            check_tires_dirt()
        elif track == "sand":
            check_tires_sand()

        if game_over == False:
            # - Turn -
            if keyboard[keybinds["left"]]:
                car_player.angle += 3
            if keyboard[keybinds["right"]]:
                car_player.angle -= 3

            # - Drive forward -
            if keyboard[keybinds["forward"]]:
                radians = math.radians(car_player.angle)
                
                car_player.x -= SPEED * math.sin(radians)
                car_player.y -= SPEED * math.cos(radians)
                
            # - Drive backward -
            if keyboard[keybinds["backward"]]:
                radians = math.radians(car_player.angle)

                car_player.x += SPEED_b * math.sin(radians)
                car_player.y += SPEED_b * math.cos(radians)   

        # - Check boundaries -
        if car_player.left < 0:
            car_player.left = 0
        if car_player.right > WIDTH:
            car_player.right = WIDTH
        if car_player.top < 0:
            car_player.top = 0
        if car_player.bottom > HEIGHT:
            car_player.bottom = HEIGHT

    elif mode == "menu":
        if menu_mode == "main":
            if keyboard[keybinds["forward"]]:
                drive_foward_d = Actor("keyboard_w", center=(375, 240))
            else:
                drive_foward_d = Actor("keyboard_w_outline", center=(375, 240))
            if keyboard[keybinds["left"]]:
                turn_left_d = Actor("keyboard_a", center=(375, 290))
            else:
                turn_left_d = Actor("keyboard_a_outline", center=(375, 290))
            if keyboard[keybinds["right"]]:
                turn_right_d = Actor("keyboard_d", center=(375, 390))
            else:
                turn_right_d = Actor("keyboard_d_outline", center=(375, 390))
            if keyboard[keybinds["backward"]]:
                drive_backward_d = Actor("keyboard_s", center=(375, 340))
            else:
                drive_backward_d = Actor("keyboard_s_outline", center=(375, 340))
        elif menu_mode == "binds":
            if keyboard[keybinds["forward"]]:
                drive_foward_d = Actor("keyboard_w", center=(button_bind_forward.x + 140, button_bind_forward.y))
            else:
                drive_foward_d = Actor("keyboard_w_outline", center=(button_bind_forward.x + 140, button_bind_forward.y))
            if keyboard[keybinds["left"]]:
                turn_left_d = Actor("keyboard_a", center=(button_bind_left.x + 140, button_bind_left.y))
            else:
                turn_left_d = Actor("keyboard_a_outline", center=(button_bind_left.x + 140, button_bind_left.y))
            if keyboard[keybinds["right"]]:
                turn_right_d = Actor("keyboard_d", center=(button_bind_right.x + 140, button_bind_right.y))
            else:
                turn_right_d = Actor("keyboard_d_outline", center=(button_bind_right.x + 140, button_bind_right.y))
            if keyboard[keybinds["backward"]]:
                drive_backward_d = Actor("keyboard_s", center=(button_bind_backward.x + 140, button_bind_backward.y))
            else:
                drive_backward_d = Actor("keyboard_s_outline", center=(button_bind_backward.x + 140, button_bind_backward.y))

        if car == "red":
            car_player.image = "car_red_small_5"
        elif car == "blue":
            car_player.image = "car_blue_small_5"
        elif car == "black":
            car_player.image = "car_black_small_5"
        elif car == "green":
            car_player.image = "car_green_small_5"
        elif car == "yellow":
            car_player.image = "car_yellow_small_5"

        if track == "asphalt":
            car_player.pos = 160, 360
            car_player.angle = 0
        if track == "dirt":
            car_player.pos = 475, 160
            car_player.angle = -90
        if track == "sand":
            car_player.pos = 475, 673
            car_player.angle = -90
    
# -------------------------

# -~-~-~- Key Press Events -~-~-~-
def on_key_down(key):
    global track, background, mode, car, current_music, binding_action
    if mode == "game":
        if key == keys.ESCAPE:
            mode = "menu"
            music.stop()
            current_music = random.randint(1, 2)
            if current_music == 1 and music_is_on:
                music.play("background_1")
                music.set_volume(menu_music_volume)
            elif current_music == 2 and music_is_on:
                music.play("background_2")
                music.set_volume(menu_music_volume)

# -~-~-~- Mouse Click Events -~-~-~-
def on_mouse_down(pos, button):
    global mode, menu_mode, track, car, car_player, current_lap, current_checkpoint, game_over, button_track, music_is_on, current_music, menu_music_volume, menu_music_volume_display, game_music_volume, game_music_volume_display
    if mode == "menu":
        if menu_mode == "main":
            if button_play.collidepoint(pos):
                mode = "game"
                sounds.tap_a.play()
                music.stop()
                if current_music == 1 and music_is_on:
                    music.play("gameplay_1")
                    music.set_volume(game_music_volume)
                elif current_music == 2 and music_is_on:
                    music.play("gameplay_2")
                    music.set_volume(game_music_volume)
                current_lap = 1
                current_checkpoint = 0
                game_over = False
            elif button_track.collidepoint(pos):
                menu_mode = "track"
                sounds.tap_a.play()
            elif button_car.collidepoint(pos):
                menu_mode = "car"
                sounds.tap_a.play()
            elif button_settings.collidepoint(pos):
                menu_mode = "settings"
                sounds.tap_a.play()

        elif menu_mode == "track":
            if button_asphalt.collidepoint(pos):
                if track == "asphalt":
                    sounds.switch_b.play()
                else:
                    set_track("asphalt")
                    sounds.tap_a.play()
            elif button_dirt.collidepoint(pos):
                if track == "dirt":
                    sounds.switch_b.play()
                else:
                    set_track("dirt")
                    sounds.tap_a.play()
            elif button_sand.collidepoint(pos):
                if track == "sand":
                    sounds.switch_b.play()
                else:
                    set_track("sand")
                    sounds.tap_a.play()
                car_player.pos = 930, 550
            elif button_back.collidepoint(pos):
                menu_mode = "main"
                sounds.tap_a.play()

        elif menu_mode == "car":
            if button_car_red.collidepoint(pos):
                if car == "red":
                    sounds.switch_b.play()
                else:
                    car = "red"
                    sounds.tap_a.play()
            elif button_car_blue.collidepoint(pos):
                if car == "blue":
                    sounds.switch_b.play()
                else:
                    car = "blue"
                    sounds.tap_a.play()
            elif button_car_black.collidepoint(pos):
                if car == "black":
                    sounds.switch_b.play()
                else:
                    car = "black"
                    sounds.tap_a.play()
            elif button_car_green.collidepoint(pos):
                if car == "green":
                    sounds.switch_b.play()
                else:
                    car = "green"
                    sounds.tap_a.play()
            elif button_car_yellow.collidepoint(pos):
                if car == "yellow":
                    sounds.switch_b.play()
                else:
                    car = "yellow"
                    sounds.tap_a.play()
            elif button_back.collidepoint(pos):
                menu_mode = "main"
                sounds.tap_a.play()

        elif menu_mode == "settings":
            if button_menu_music.collidepoint(pos) and button == mouse.WHEEL_UP:
                menu_music_volume += 0.05
                menu_music_volume_display += 0.5
                music.set_volume(menu_music_volume)
            elif button_menu_music.collidepoint(pos) and button == mouse.WHEEL_DOWN:
                menu_music_volume -= 0.05
                menu_music_volume_display -= 0.5
                music.set_volume(menu_music_volume)

            if button_game_music.collidepoint(pos) and button == mouse.WHEEL_UP:
                game_music_volume += 0.05
                game_music_volume_display += 0.5
            elif button_game_music.collidepoint(pos) and button == mouse.WHEEL_DOWN:
                game_music_volume -= 0.05
                game_music_volume_display -= 0.5

            if button_music.collidepoint(pos) and music_is_on and button == mouse.LEFT:
                music_is_on = False
                music.stop()
                sounds.tap_a.play()
            elif button_music.collidepoint(pos) and not music_is_on and button == mouse.LEFT:
                music_is_on = True
                current_music = random.randint(1, 2)
                if current_music == 1:
                    music.play("background_1")
                    music.set_volume(menu_music_volume)
                elif current_music == 2:
                    music.play("background_2")
                    music.set_volume(menu_music_volume)
                sounds.tap_a.play()
            elif button_binds.collidepoint(pos):
                menu_mode = "binds"
                sounds.tap_a.play()

            elif button_back.collidepoint(pos):
                menu_mode = "main"
                sounds.tap_a.play()

        elif menu_mode == "binds":
            if button_back.collidepoint(pos):
                menu_mode = "settings"
                sounds.tap_a.play()
# ----------------------------------

pgzrun.go()
