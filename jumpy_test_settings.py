#imports
import pygame as pg
import sys
import math
import time
vec = pg.math.Vector2

#basic settings
TITLE = 'JUMPY'
WIDTH = 500
HEIGHT = 700
FPS = 60
MAX_LIVES = 3
TEXT_FONT = 'freesansbold.ttf'
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 40
MAX_SAW_SPEED = 10

#physics settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.10
GRAVITY = 0.8

#color settings

platform_color = pg.Color('yellow')
Portal_color = pg.Color('blue')
Portal_color_bg = pg.Color('purple')
Portal_width = 30
Portal_height = 50
player_color = pg.Color('green')
saw_color = pg.Color('red')
top_bar_color = pg.Color('blue')
playing_bg_color = pg.Color('black')
start_or_end_color = pg.Color('purple')
text_color = pg.Color('black')
lives_text_color = pg.Color('white')
time_text_color = pg.Color('white')
text_color_pause = pg.Color('white')

#text_message settings

developer_name_message = 'By Charlie Gray'
controls_text_message = 'Arrows to move, Space to jump'
objective_text1_message = 'Enter the portal to move to the next level, Each level you get 3 lives'
objective_text2_message = 'Watch out for spinning saws and other obstacles that could kill you'
start_text_message = 'Press enter to start'
finish_text_message = 'EXIT'
again_text_message = 'Press enter to play again'
death_message = 'You ran out of lives!'
complete_message = 'You completed the game!'
time_text_message = 'TBD'
level_reached_text_message = 'TBD'
time_taken_text_message = 'TBD'
record_level_text_message = 'TBD'
record_time_text_message = 'TBD'
info_text_message = 'Game Info:'



#image + audio path settings

heart_path = '/Users/charlie/Downloads/heart_sprite.png'
applause_path = '/Users/charlie/Downloads/Applause-SoundBible.com-151138312.mp3'
death_path = '/Users/charlie/Downloads/253886__themusicalnomad__negative-beeps.wav'
intro_music_path = '/Users/charlie/Downloads/521656__mrthenoronha__soft-game-them-loop.wav'
in_game_music_path = '/Users/charlie/Downloads/lsc_title.mp3'
jump_sound_path = '/Users/charlie/Downloads/350900__cabled-mess__jump-c-07.wav'
hurt_sound_path = '/Users/charlie/Downloads/retro_death.mp3'
portal_path = '/Users/charlie/Downloads/172207__leszek-szary__teleport.wav'
portal_dissappear_path = '/Users/charlie/Downloads/258020__kodack__arcade-bleep-sound.wav'
click_sound_path = '/Users/charlie/Downloads/office_keyboard_apple_key_press_single.mp3'


#platforms in each level
Level_1_PLAT = [(0, HEIGHT - 30, WIDTH, 30), (0, 560, 200, 30), (250, 450, 150, 30), (450, 350, 50, 30), (350, 250, 100, 30), (200, 150, 150, 30), (0, 100, 100, 30)]
Level_2_PLAT = [(0, HEIGHT - 30, WIDTH, 30), (300, 570, 100, 30), (200, 500,50, 30), (0, 500, 50, 30), (0, 400, 25, 30), (50, 300, WIDTH-50, 30), (400, 225, 75, 30), (300, 100, 50, 30), (175, 100, 75, 30)]
Level_3_PLAT = [(0, HEIGHT - 30, WIDTH, 30), (WIDTH - 25, 570, 25, 30), (400, 450, 50, 30), (230, 570, 100, 30), (200, 370, 300, 30), (50, 450, 75, 30), (300, 270, 100, 30), (200, 200, 75, 30), (350, 100, 50, 30), (450, 150, 50, 30)]

#saws in each level
Level_1_SAW = [(300, 250, 50), (460, 440, 65), (105, 400, 100), (350, 650, 35)]
Level_2_SAW = [(250, 625, 50) ,(125, 500, 60), (200, 275, 40), (350, 200, 60)]
Level_3_SAW = [(385, 570, 65), (200, 630, 60), (25, 425, 50), (40, 630, 60), (120, 630, 60), (450, 230, 60), (175, 125, 60), (400, 200, 30)]

#ending portal for each level
Level_1_END = [(0, 50)]
Level_2_END = [(175, 50)]
Level_3_END = [(470, 100)]

Level_1_PLAYER = (WIDTH - (PLAYER_WIDTH/2), HEIGHT - 30)
Level_2_PLAYER = (WIDTH - (PLAYER_WIDTH/2) - Portal_width - 10, HEIGHT - 30)
Level_3_PLAYER = (WIDTH - (PLAYER_WIDTH/2) - Portal_width - 10, HEIGHT - 30)

Level_1_START_PORT = [(WIDTH - Portal_width, HEIGHT - 30 - Portal_height)]
Level_2_START_PORT = [(WIDTH - Portal_width, HEIGHT - 30 - Portal_height)]
Level_3_START_PORT = [(WIDTH - Portal_width, HEIGHT - 30 - Portal_height)]
#list for portals in each level
END_PORTAL_LIST = (0, Level_1_END, Level_2_END, Level_3_END)

#list for platforms in each level
PLATFORM_LIST = (0, Level_1_PLAT, Level_2_PLAT, Level_3_PLAT)
#list for saws in each level
SAW_LIST = (0, Level_1_SAW, Level_2_SAW, Level_3_SAW)

PLAYER_LIST = (0, Level_1_PLAYER, Level_2_PLAYER, Level_3_PLAYER)

START_PORTAL_LIST = (0, Level_1_START_PORT, Level_2_START_PORT, Level_3_START_PORT)