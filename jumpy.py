from jumpy_test_settings import *

class Game:
    def __init__(self):
        #initialize
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = False
        self.pause_show = False
        self.begin = False
        self.level = 1
        self.best_level = 1
        self.best_time = 'NUL '
        self.lives = MAX_LIVES
        self.play_time = 0
        self.portal_gone = False
        self.mouse = 0
        self.pause = False
        self.on_settings = False
        self.saw_speed = MAX_SAW_SPEED
        self.mute_sfx = False
        self.mute_music = False
        self.mute_music_settings = self.mute_music
        self.mute_sfx_settings =self.mute_sfx
        self.saw_speed_settings = self.saw_speed
        #text not buttons
        self.title_text = text(str(TITLE) + '!', 40, WIDTH/2, HEIGHT/2 - 200, self, text_color)
        self.developer_name = text(developer_name_message, 15, WIDTH/2, HEIGHT/2 - 150, self, text_color)
        self.controls_text = text(controls_text_message, 15, WIDTH/2, HEIGHT/2, self, text_color)
        self.objective_text1 = text(objective_text1_message, 15, WIDTH/2, HEIGHT/2 + 50, self, text_color)
        self.objective_text2 = text(objective_text2_message, 15, WIDTH/2, HEIGHT/2 + 100, self, text_color)
        self.start_text = text(start_text_message, 20, WIDTH/2, HEIGHT/2 + 200, self, text_color)
        self.finish_text = text(finish_text_message, 32, WIDTH/2, 150, self, text_color)
        self.again_text = text(again_text_message, 22, WIDTH/2, 300, self, text_color)
        self.info_text = text(info_text_message, 25, WIDTH/2, 450, self, text_color)
        self.level_reached_text = text(level_reached_text_message,20, WIDTH/2, 500, self, text_color)
        self.time_taken_text = text(time_taken_text_message,20, WIDTH/2, 550, self, text_color)
        self.record_level_text = text(record_level_text_message, 20, WIDTH/2, 600, self, text_color)
        self.record_time_text = text(record_time_text_message, 20, WIDTH/2, 650, self, text_color)
        self.time_text = text(time_text_message, 25, 43, 10, self, time_text_color)
        self.settings_title = text('SETTINGS', 30, 250, 30, self, text_color)
        self.saw_speed_text = text('Saw Speed', 20, 250, 150, self, text_color)
        self.saw_speed_number = text(str(self.saw_speed_settings), 15, 250, 180, self, text_color)
        self.saw_speed_number_rect = rect(self.saw_speed_number.x, self.saw_speed_number.y, self.saw_speed_number.textRect.width + 5, self.saw_speed_number.textRect.height + 5, pg.Color('white'), self)
        self.music_mute_text = text('Music', 20, 250, 250, self, text_color)
        self.sfx_mute_text = text('Sound fx', 20, 250, 325, self, text_color)
        #music and sounds
        #pg.mixer.music.load(intro_music_path)
        #pg.mixer.music.play(-1)
        #self.applause_sound = pg.mixer.Sound(applause_path)
        #self.death_sound = pg.mixer.Sound(death_path)
        #self.portal_sound = pg.mixer.Sound(portal_path)
        #self.portal_dissappear = pg.mixer.Sound(portal_dissappear_path)
        #buttons
        self.template = rect(250, 350, 150, 300, start_or_end_color, self)
        self.button_pause_rect = rect(20, 20, 40, 40, pg.Color('red'), self)
        self.button_pause = text('II', 30, self.button_pause_rect.x, self.button_pause_rect.y, self, text_color)
        self.button_resume = text('resume', 30, 250, self.template.y - self.template.height/3, self, text_color)
        self.button_restart = text('restart', 30, 250, self.template.y - self.template.height/8, self, text_color)
        self.button_quit = text('quit', 30, 250, self.template.y + self.template.height/3, self, text_color)
        self.button_settings = text('settings', 30, 250, self.template.y + self.template.height/8, self, text_color)
        self.button_play_again = text('PLAY AGAIN', 22, WIDTH/2, 275, self, text_color)
        self.button_begin = text('START', 22, WIDTH/2, HEIGHT/2 + 200, self, text_color)
        self.button_leave1 = text('EXIT', 22, WIDTH/2, HEIGHT/2 + 275, self, text_color)
        self.button_leave2 = text('EXIT', 22, WIDTH/2, 350, self, text_color)
        self.button_setting_confirm = text('CONFIRM', 22, WIDTH/2, HEIGHT - 150, self, text_color)
        self.button_setting_cancel = text('CANCEL', 22, WIDTH/2, HEIGHT - 75, self, text_color)
        self.button_saw_number_plus = text('+', 25, self.saw_speed_number.x + 2*self.saw_speed_number.textRect.width, self.saw_speed_number.y - self.saw_speed_number.textRect.height/4, self, text_color)
        self.button_saw_number_minus = text('-', 25, self.saw_speed_number.x - 2*self.saw_speed_number.textRect.width, self.saw_speed_number.y - self.saw_speed_number.textRect.height/4, self, text_color)
        self.button_music_on_rect = rect(235, 275, 30, 30, pg.Color('black'), self)
        self.button_music_off_rect = rect(265, 275, 30, 30, pg.Color('black'), self)
        self.button_music_on = text('ON', 15, self.button_music_on_rect.x , self.button_music_on_rect.y, self, pg.Color('white'))
        self.button_music_off = text('OFF', 15, self.button_music_off_rect.x, self.button_music_off_rect.y, self, pg.Color('white'))
        self.button_sfx_on_rect = rect(235, 350, 30, 30, pg.Color('black'), self)
        self.button_sfx_off_rect = rect(265, 350, 30, 30, pg.Color('black'), self)
        self.button_sfx_on = text('ON', 15, self.button_sfx_on_rect.x , self.button_sfx_on_rect.y, self, pg.Color('white'))
        self.button_sfx_off = text('OFF', 15, self.button_sfx_off_rect.x, self.button_sfx_off_rect.y, self, pg.Color('white'))

    def new(self):
        #load new game
        if self.pause == False:
            if self.level == 1 and self.lives == MAX_LIVES:
                self.start_time = int(time.time())
            self.all_sprites = pg.sprite.Group()
            self.platforms = pg.sprite.Group()
            self.saws = pg.sprite.Group()
            self.portals = pg.sprite.Group()
            self.current_level_plat = PLATFORM_LIST[self.level]
            self.current_level_saw = SAW_LIST[self.level]
            self.current_level_port = END_PORTAL_LIST[self.level]
            self.current_level_player = PLAYER_LIST[self.level]
            for plat in self.current_level_plat:
                p = Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)
            for saw in self.current_level_saw:
                s = Saw(self, *saw)
                self.all_sprites.add(s)
                self.saws.add(s)
            for portal in self.current_level_port:
                p = Portal(*portal)
                self.all_sprites.add(p)
                self.portals.add(p)
            self.player = Player(self, self.current_level_player[0], self.current_level_player[1])
            self.all_sprites.add(self.player)
            if self.level > 1 and not self.portal_gone:
                self.prev_portals = pg.sprite.Group()
                self.current_level_prev_port = START_PORTAL_LIST[self.level]
                for portal in self.current_level_prev_port:
                    p = Portal(*portal)
                    self.all_sprites.add(p)
                    self.prev_portals.add(p)
            self.level_count = 'Level ' + str(self.level)
            self.level_text = text(self.level_count, 30, 250, 20, self,lives_text_color)
        self.pause = False
        self.run()
    
    def run(self):
        #run game
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        #check for events
        for event in pg.event.get():
            self.mouse = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                self.begin = True
                self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
                pass
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.button_pause_rect.x - self.button_pause_rect.width/2 <= self.mouse[0] <= self.button_pause_rect.x + self.button_pause_rect.width/2 and self.button_pause_rect.y - self.button_pause_rect.height/2<= self.mouse[1] <= self.button_pause_rect.y + self.button_pause_rect.height/2 and self.pause_show == True:
                    pg.mixer.music.pause()
                    self.playing = False
                    self.pause = True
                    self.pause_show = False
                elif self.button_resume.textRect.x <= self.mouse[0] <= self.button_resume.textRect.x + self.button_resume.textRect.width and self.button_resume.textRect.y <= self.mouse[1] <= self.button_resume.textRect.y + self.button_resume.textRect.height and self.pause == True and self.on_settings == False:
                    if not self.mute_music:
                        pg.mixer.music.unpause()
                    self.playing = True
                elif self.button_restart.textRect.x <= self.mouse[0] <= self.button_restart.textRect.x + self.button_restart.textRect.width and self.button_restart.textRect.y <= self.mouse[1] <= self.button_restart.textRect.y + self.button_restart.textRect.height and self.pause == True and self.on_settings == False:
                    self.playing = True
                    self.pause = False
                    self.level = 1
                    self.lives = MAX_LIVES
                    if not self.mute_music:
                        pg.mixer.music.play(-1)
                elif self.button_settings.textRect.x <= self.mouse[0] <= self.button_settings.textRect.x + self.button_settings.textRect.width and self.button_settings.textRect.y <= self.mouse[1] <= self.button_settings.textRect.y + self.button_settings.textRect.height and self.pause == True and self.on_settings == False:
                    self.on_settings = True
                    self.settings()
                elif self.button_setting_confirm.textRect.x <= self.mouse[0] <= self.button_setting_confirm.textRect.x + self.button_setting_confirm.textRect.width and self.button_setting_confirm.textRect.y <= self.mouse[1] <= self.button_setting_confirm.textRect.y + self.button_setting_confirm.textRect.height and self.pause == True and self.on_settings == True:
                    self.on_settings = False 
                    self.saw_speed = self.saw_speed_settings
                    self.saw_speed_number.message = str(self.saw_speed_settings)
                    self.mute_music = self.mute_music_settings
                    self.mute_sfx = self.mute_sfx_settings
                    self.draw()
                elif self.button_setting_cancel.textRect.x <= self.mouse[0] <= self.button_setting_cancel.textRect.x + self.button_setting_cancel.textRect.width and self.button_setting_cancel.textRect.y <= self.mouse[1] <= self.button_setting_cancel.textRect.y + self.button_setting_cancel.textRect.height and self.pause == True and self.on_settings == True:
                    self.on_settings = False
                    self.saw_speed_settings = self.saw_speed
                    self.saw_speed_number.message = str(self.saw_speed_settings)
                    self.mute_music_settings = self.mute_music
                    self.mute_sfx_settings = self.mute_sfx
                    self.draw()
                elif self.button_saw_number_plus.textRect.x <= self.mouse[0] <= self.button_saw_number_plus.textRect.x + self.button_saw_number_plus.textRect.width and self.button_saw_number_plus.textRect.y <= self.mouse[1] <= self.button_saw_number_plus.textRect.y + self.button_saw_number_plus.textRect.height and self.pause == True and self.on_settings == True:
                    if self.saw_speed_settings < MAX_SAW_SPEED:
                        self.saw_speed_settings += 1
                        self.saw_speed_number.message = str(self.saw_speed_settings)
                elif self.button_saw_number_minus.textRect.x <= self.mouse[0] <= self.button_saw_number_minus.textRect.x + self.button_saw_number_minus.textRect.width and self.button_saw_number_minus.textRect.y <= self.mouse[1] <= self.button_saw_number_minus.textRect.y + self.button_saw_number_minus.textRect.height and self.pause == True and self.on_settings == True:
                    if self.saw_speed_settings > 1:
                        self.saw_speed_settings -= 1
                        self.saw_speed_number.message = str(self.saw_speed_settings)
                elif self.button_music_on_rect.x - self.button_music_on_rect.width/2 <= self.mouse[0] <= self.button_music_on_rect.x + self.button_music_on_rect.width/2 and self.button_music_on_rect.y - self.button_music_on_rect.height/2 <= self.mouse[1] <= self.button_music_on_rect.y + self.button_music_on_rect.height/2 and self.pause == True and self.on_settings == True:
                    self.mute_music_settings = False
                elif self.button_music_off_rect.x - self.button_music_off_rect.width/2 <= self.mouse[0] <= self.button_music_off_rect.x + self.button_music_off_rect.width/2 and self.button_music_off_rect.y - self.button_music_off_rect.height/2 <= self.mouse[1] <= self.button_music_off_rect.y + self.button_music_off_rect.height/2 and self.pause == True and self.on_settings == True:
                    self.mute_music_settings = True
                elif self.button_sfx_on_rect.x - self.button_sfx_on_rect.width/2 <= self.mouse[0] <= self.button_sfx_on_rect.x + self.button_sfx_on_rect.width/2 and self.button_sfx_on_rect.y - self.button_sfx_on_rect.height/2 <= self.mouse[1] <= self.button_sfx_on_rect.y + self.button_sfx_on_rect.height/2 and self.pause == True and self.on_settings == True:
                    self.mute_sfx_settings = False
                elif self.button_sfx_off_rect.x - self.button_sfx_off_rect.width/2 <= self.mouse[0] <= self.button_sfx_off_rect.x + self.button_sfx_off_rect.width/2 and self.button_sfx_off_rect.y - self.button_sfx_off_rect.height/2 <= self.mouse[1] <= self.button_sfx_off_rect.y + self.button_sfx_off_rect.height/2 and self.pause == True and self.on_settings == True:
                    self.mute_sfx_settings = True
                
                elif self.button_quit.textRect.x <= self.mouse[0] <= self.button_quit.textRect.x + self.button_quit.textRect.width and self.button_quit.textRect.y <= self.mouse[1] <= self.button_quit.textRect.y + self.button_quit.textRect.height and self.pause == True and self.on_settings == False:
                    self.playing = False
                    self.running = False
                elif self.button_begin.textRect.x <= self.mouse[0] <= self.button_begin.textRect.x + self.button_begin.textRect.width and self.button_begin.textRect.y <= self.mouse[1] <= self.button_begin.textRect.y + self.button_begin.textRect.height and self.begin == False:
                    self.begin = True
                    self.playing = True
                    self.pause_show = True
                    #pg.mixer.music.stop()
                    #pg.mixer.music.load(in_game_music_path)
                    #pg.mixer.music.play(-1)
                elif self.button_leave1.textRect.x <= self.mouse[0] <= self.button_leave1.textRect.x + self.button_leave1.textRect.width and self.button_leave1.textRect.y <= self.mouse[1] <= self.button_leave1.textRect.y + self.button_leave1.textRect.height and self.begin == False:
                    self.begin = True
                    self.playing = False
                    self.running = False
                elif self.button_leave2.textRect.x <= self.mouse[0] <= self.button_leave2.textRect.x + self.button_leave2.textRect.width and self.button_leave2.textRect.y <= self.mouse[1] <= self.button_leave2.textRect.y + self.button_leave2.textRect.height and self.playing == False and self.begin == True:
                    self.begin = True
                    self.playing = False
                    self.running = False
                elif self.button_play_again.textRect.x <= self.mouse[0] <= self.button_play_again.textRect.x + self.button_play_again.textRect.width and self.button_play_again.textRect.y <= self.mouse[1] <= self.button_play_again.textRect.y + self.button_play_again.textRect.height and self.playing == False and self.begin == True and self.pause == False:
                    pg.mixer.Sound.stop(self.applause_sound)
                    pg.mixer.Sound.stop(self.death_sound)
                    self.playing = True
                    self.level = 1
                    self.lives = MAX_LIVES
                    if not self.mute_music:
                        pg.mixer.music.play(-1)
            
            if self.button_pause_rect.x - self.button_pause_rect.width/2 <= self.mouse[0] <= self.button_pause_rect.x + self.button_pause_rect.width/2 and self.button_pause_rect.y - self.button_pause_rect.height/2<= self.mouse[1] <= self.button_pause_rect.y + self.button_pause_rect.height/2 and self.pause_show == True:
                self.button_pause_rect.color = pg.Color('white')
                self.button_pause.color = pg.Color('red')
            else:
                self.button_pause_rect.color = pg.Color('red')
                self.button_pause.color = pg.Color('white')

            if self.button_resume.textRect.x <= self.mouse[0] <= self.button_resume.textRect.x + self.button_resume.textRect.width and self.button_resume.textRect.y <= self.mouse[1] <= self.button_resume.textRect.y + self.button_resume.textRect.height and self.pause == True:
                self.button_resume.color = pg.Color('white')
            else:
                self.button_resume.color = pg.Color('black')

            if self.button_restart.textRect.x <= self.mouse[0] <= self.button_restart.textRect.x + self.button_restart.textRect.width and self.button_restart.textRect.y <= self.mouse[1] <= self.button_restart.textRect.y + self.button_restart.textRect.height and self.pause == True:
                self.button_restart.color = pg.Color('white')
            else:
                self.button_restart.color = pg.Color('black')

            if self.button_settings.textRect.x <= self.mouse[0] <= self.button_settings.textRect.x + self.button_settings.textRect.width and self.button_settings.textRect.y <= self.mouse[1] <= self.button_settings.textRect.y + self.button_settings.textRect.height and self.pause == True:
                self.button_settings.color = pg.Color('white')
            else:
                self.button_settings.color = pg.Color('black')
            
            if self.button_quit.textRect.x <= self.mouse[0] <= self.button_quit.textRect.x + self.button_quit.textRect.width and self.button_quit.textRect.y <= self.mouse[1] <= self.button_quit.textRect.y + self.button_quit.textRect.height and self.pause == True:
                self.button_quit.color = pg.Color('white')
            else:
                self.button_quit.color = pg.Color('black')

            if self.button_setting_confirm.textRect.x <= self.mouse[0] <= self.button_setting_confirm.textRect.x + self.button_setting_confirm.textRect.width and self.button_setting_confirm.textRect.y <= self.mouse[1] <= self.button_setting_confirm.textRect.y + self.button_setting_confirm.textRect.height and self.pause == True:
                self.button_setting_confirm.color = pg.Color('white')
            else:
                self.button_setting_confirm.color = pg.Color('black')

            if self.button_setting_cancel.textRect.x <= self.mouse[0] <= self.button_setting_cancel.textRect.x + self.button_setting_cancel.textRect.width and self.button_setting_cancel.textRect.y <= self.mouse[1] <= self.button_setting_cancel.textRect.y + self.button_setting_cancel.textRect.height and self.pause == True and self.on_settings == True:
                self.button_setting_cancel.color = pg.Color('white')
            else:
                self.button_setting_cancel.color = pg.Color('black')

            if self.button_saw_number_plus.textRect.x <= self.mouse[0] <= self.button_saw_number_plus.textRect.x + self.button_saw_number_plus.textRect.width and self.button_saw_number_plus.textRect.y <= self.mouse[1] <= self.button_saw_number_plus.textRect.y + self.button_saw_number_plus.textRect.height and self.pause == True and self.on_settings == True:
                self.button_saw_number_plus.color = pg.Color('white')
            else:
                self.button_saw_number_plus.color = pg.Color('black')

            if self.button_saw_number_minus.textRect.x <= self.mouse[0] <= self.button_saw_number_minus.textRect.x + self.button_saw_number_minus.textRect.width and self.button_saw_number_minus.textRect.y <= self.mouse[1] <= self.button_saw_number_minus.textRect.y + self.button_saw_number_minus.textRect.height and self.pause == True and self.on_settings == True:
                self.button_saw_number_minus.color = pg.Color('white')
            else:
                self.button_saw_number_minus.color = pg.Color('black')

            if self.button_begin.textRect.x <= self.mouse[0] <= self.button_begin.textRect.x + self.button_begin.textRect.width and self.button_begin.textRect.y <= self.mouse[1] <= self.button_begin.textRect.y + self.button_begin.textRect.height and self.begin == False:
                self.button_begin.color = pg.Color('white')
            else:
                self.button_begin.color = pg.Color('black')

            if self.button_leave1.textRect.x <= self.mouse[0] <= self.button_leave1.textRect.x + self.button_leave1.textRect.width and self.button_leave1.textRect.y <= self.mouse[1] <= self.button_leave1.textRect.y + self.button_leave1.textRect.height and self.begin == False:
                self.button_leave1.color = pg.Color('white')
            else:
                self.button_leave1.color = pg.Color('black')

            if self.button_leave2.textRect.x <= self.mouse[0] <= self.button_leave2.textRect.x + self.button_leave2.textRect.width and self.button_leave2.textRect.y <= self.mouse[1] <= self.button_leave2.textRect.y + self.button_leave2.textRect.height and self.playing == False and self.begin == True:
                self.button_leave2.color = pg.Color('white')
            else:
                self.button_leave2.color = pg.Color('black')

            if self.button_play_again.textRect.x <= self.mouse[0] <= self.button_play_again.textRect.x + self.button_play_again.textRect.width and self.button_play_again.textRect.y <= self.mouse[1] <= self.button_play_again.textRect.y + self.button_play_again.textRect.height and self.playing == False and self.begin == True:
                self.button_play_again.color = pg.Color('white')
            else:
                self.button_play_again.color = pg.Color('black')

            if self.mute_music_settings == False:
                self.button_music_on_rect.color = pg.Color('white')
                self.button_music_on.color = pg.Color('black')
                self.button_music_off_rect.color = pg.Color('black')
                self.button_music_off.color = pg.Color('white')
            else:
                self.button_music_on_rect.color = pg.Color('black')
                self.button_music_on.color = pg.Color('white')
                self.button_music_off_rect.color = pg.Color('white')
                self.button_music_off.color = pg.Color('black')
        
            if self.mute_sfx_settings == False:
                self.button_sfx_on_rect.color = pg.Color('white')
                self.button_sfx_on.color = pg.Color('black')
                self.button_sfx_off_rect.color = pg.Color('black')
                self.button_sfx_off.color = pg.Color('white')
            else:
                self.button_sfx_on_rect.color = pg.Color('black')
                self.button_sfx_on.color = pg.Color('white')
                self.button_sfx_off_rect.color = pg.Color('white')
                self.button_sfx_off.color = pg.Color('black')




    def update(self):
        #update sprites
        #try and find way to only detect if player has hit top of platform and not sides
        self.all_sprites.update()
        kill = pg.sprite.spritecollide(self.player, self.saws, False, pg.sprite.collide_mask)
        end = pg.sprite.spritecollide(self.player, self.portals, False, pg.sprite.collide_mask)
        if self.level > 1:
            Portal_kill = pg.sprite.spritecollide(self.player, self.prev_portals, False, pg.sprite.collide_mask)
            if Portal_kill:
                if not self.mute_sfx:
                    pg.mixer.Sound.play(self.portal_dissappear)
                self.prev_portals.remove(Portal_kill[0])
                self.all_sprites.remove(Portal_kill[0])
                self.portal_gone = True

        #check to see if player is on a rectangle and if it has hit the top of bottom
        #then set the position to the rectangle top or just below it so it can drop

        #run self.killed () if player has touched a saw
        if kill:
            self.killed()

        if end:
            self.ended()



        
        self.time_reconfigure()

    def draw(self):
        #draw sprites + time + level_text + lives
        self.screen.fill(playing_bg_color)
        self.all_sprites.draw(self.screen)
        self.level_text.display()
        self.time_text.display_topright()
        for i in range(0, self.lives):
            heart = Heart(WIDTH - (i+1)*(35), 5, self)
            self.screen.blit(heart.image, heart.rect)
        self.button_pause_rect.rect_draw()
        self.button_pause.display()
        pg.display.update()

    def starter_screen(self):
        #look into nicer way of doing this
        #it works but uses one more variable which could complicate things
        while not self.begin:
            self.screen.fill(start_or_end_color)
            self.title_text.display()
            self.developer_name.display()
            self.controls_text.display()
            self.objective_text1.display()
            self.objective_text2.display()
            self.button_begin.display()
            self.button_leave1.display()
            pg.display.update()
            self.events()
        

    def end_screen(self):
        #end screen
        while not self.playing and self.running:
            self.screen.fill(start_or_end_color)
            self.finish_text.display()
            self.button_play_again.display()
            self.button_leave2.display()
            self.info_update()
            self.info_text.display()
            self.level_reached_text.display()
            self.time_taken_text.display()
            self.record_level_text.display()
            self.record_time_text.display()
            pg.display.update()
            self.events()


    def pause_screen(self):
        go_time = time.time()
        while not self.playing and self.running:
            self.template.rect_draw()
            self.button_resume.display()
            self.button_restart.display()
            self.button_settings.display()
            self.button_quit.display()
            pg.display.update()
            self.events()
        end_time = time.time()
        self.start_time += (int(end_time) - int(go_time))
        self.pause_show = True

    def settings(self):
        while self.on_settings:
            self.screen.fill(start_or_end_color)
            self.settings_title.display()
            self.saw_speed_text.display()
            self.saw_speed_number_rect = rect(self.saw_speed_number.x, self.saw_speed_number.y, self.saw_speed_number.textRect.width + 5, self.saw_speed_number.textRect.height + 5, pg.Color('white'), self)
            self.saw_speed_number_rect.rect_draw()
            self.saw_speed_number.display()
            self.button_saw_number_plus.display()
            self.button_saw_number_minus.display()
            self.music_mute_text.display()
            self.button_music_on_rect.rect_draw()
            self.button_music_on.display()
            self.button_music_off_rect.rect_draw()
            self.button_music_off.display()
            self.sfx_mute_text.display()
            self.button_sfx_on_rect.rect_draw()
            self.button_sfx_on.display()
            self.button_sfx_off_rect.rect_draw()
            self.button_sfx_off.display()
            self.button_setting_confirm.display()
            self.button_setting_cancel.display()
            pg.display.update()
            self.events()


    def killed(self):
        self.lives -= 1
        if self.lives <= 0:
            self.playing = False
            self.finish_text.message = death_message
            if not self.mute_music:
                pg.mixer.music.stop()
            if not self.mute_sfx:
                pg.mixer.Sound.play(self.death_sound)
        else:
            if not self.mute_sfx:
                pg.mixer.Sound.play(self.player.hurt_sound)
            self.new()

    def ended(self):
        if self.level + 1 >= len(PLATFORM_LIST):
            self.finish_text.message = complete_message
            self.playing = False
            if not self.mute_music:
                pg.mixer.music.stop()
            if not self.mute_sfx:
                pg.mixer.Sound.play(self.applause_sound)
        else:
            self.teleport()
            self.pause_show = True
            self.level += 1
            self.lives = MAX_LIVES
            self.portal_gone = False
            if self.playing:
                self.new()


    def teleport(self):
        #teleport animation that deletes platfroms and saws one by one
        self.pause_show = False
        go_time = time.time()
        self.player.kill()
        if not self.mute_sfx:
            pg.mixer.Sound.play(self.portal_sound)
        for i in self.all_sprites:
            self.clock.tick(15)
            if self.running and self.playing:
                self.screen.fill(playing_bg_color)
                self.events()
                i.kill()
                self.all_sprites.draw(self.screen)
                pg.display.update()
            else:
                break
        end_time = time.time()

        #re-evaluate time so that time has not been gained during animation so player time is their raw gameplay
        self.start_time += (int(end_time) - int(go_time))
        if self.running and self.playing:
            if not self.mute_sfx:
                pg.mixer.Sound.play(self.portal_sound)

    def time_reconfigure(self):
        self.current_time = int(time.time())
        self.play_time = (self.current_time - self.start_time)
        if self.play_time > 999:
            self.play_time = str('999+')
        self.time_text.message = 'Time: ' + str(self.play_time) + 's'

    
    def info_update(self):
        #various conditional statements to figure what informtion to display to user
        if self.lives > 0:
            self.best_level = self.level + 1
        elif self.level > self.best_level:
            self.best_level = self.level
        if self.best_level == len(PLATFORM_LIST):
            self.record_level_text.message = 'highest level reached: completed'
        else:
            self.record_level_text.message = 'highest level reached: ' + str(self.best_level)
        if self.lives > 0:
            self.level_reached_text.message = 'level reached: completed'
        else:
            self.level_reached_text.message = 'level reached: ' + str(self.level)
        if self.lives > 0:
            if self.best_time == 'NUL ':
                self.best_time = self.play_time
            if self.play_time < self.best_time:
                self.best_time = self.play_time
        self.record_time_text.message = 'fastest completion time: ' + str(self.best_time) + 's'
        self.time_taken_text.message = 'time taken: ' + str(self.play_time) + 's'

        

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((25, 40))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.pos = vec(self.rect.midbottom[0], self.rect.midbottom[1])
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        #self.jump_sound = pg.mixer.Sound(jump_sound_path)
        #self.hurt_sound = pg.mixer.Sound(hurt_sound_path)
        self.mask = pg.mask.from_surface(self.image)

    def jump(self):
        
        #check if player is on a platform then jump if they are
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -15
            if not self.game.mute_sfx:
                pg.mixer.Sound.play(self.jump_sound)
    
    def update(self):
            
        #set new acceleration
        self.acc = vec(0, GRAVITY)
            
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_SPACE]:
            self.jump()
        
        

        #apply friction, but only for x axis movements
        self.acc.x += self.vel.x * PLAYER_FRICTION
        

        self.check_x()
        self.check_y()

        #set basic screen boundaries for x axis movements
        if self.pos.x - self.rect.width / 2< 0:
            self.pos.x = 0 + self.rect.width / 2
        elif self.pos.x + self.rect.width / 2 > WIDTH:
            self.pos.x = WIDTH - self.rect.width / 2

        #set y axis screen boundrary for top
        if self.pos.y - self.rect.height < 0:
            self.pos.y = self.rect.height
            self.vel.y = 0
            self.rect.midbottom = self.pos

        
        
        #set position of player as midbottom as we will be tracking the equivalent 'feet' of the sprite
        
        self.rect.midbottom = self.pos
        self.mask = pg.mask.from_surface(self.image)

    def check_x(self):
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.rect.midbottom = self.pos
        hits = pg.sprite.spritecollide(self, self.game.platforms, False, pg.sprite.collide_mask)
        if hits:
            if self.vel.x > 0:
                offset_x = (self.pos.x + self.rect.width/2) - hits[0].rect.x
                self.pos.x -= offset_x
            elif self.vel.x < 0:
                offset_x = (hits[0].rect.x + hits[0].rect.width) - (self.pos.x - self.rect.width/2)
                self.pos.x += offset_x
            
            self.vel.x = 0
            self.rect.midbottom = self.pos
        



    def check_y(self):
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        self.rect.midbottom = self.pos
        hits = pg.sprite.spritecollide(self, self.game.platforms, False, pg.sprite.collide_mask)
        if hits:
            if self.vel.y > 0:
                self.pos.y = hits[0].rect.top
            elif self.vel.y < 0:
                self.pos.y = hits[0].rect.bottom + self.rect.height + 1

            self.vel.y = 0
            self.rect.midbottom = self.pos




class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(platform_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)


class Saw(pg.sprite.Sprite):
    def __init__(self, game, x, y, size = 50,):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = size
        self.game = game
        self.angle = 0
        self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)
        #draw regular shaped hexagon according to size of surface
        self.shape = pg.draw.polygon(self.image, saw_color, [(self.size/2 - self.size/2, self.size/2), (self.size/2 - self.size/4, self.size/2+(self.size/4*(math.sqrt(3)))), (self.size/2 + self.size/4, self.size/2+(self.size/4*(math.sqrt(3)))), (self.size/2 + self.size/2, self.size/2), (self.size/2 + self.size/4, self.size/2-(self.size/4*(math.sqrt(3)))), (self.size/2 - self.size/4, self.size/2-(self.size/4*(math.sqrt(3))))])
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.original = self.image
        self.original_rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pg.mask.from_surface(self.image)



    def update(self):
        self.angle += self.game.saw_speed
        self.image = pg.transform.rotozoom(self.original, self.angle, 1)
        self.rect = self.image.get_rect(center = self.original_rect.center)
        self.mask = pg.mask.from_surface(self.image)


class text():
    #find quicker and better way to display text on screen
    def __init__(self, message, size, x, y, game, color = pg.Color('white')):
        self.message = message
        self.size = size
        self.x = x
        self.y = y
        self.game = game
        self.color = color
        self.font = pg.font.Font('freesansbold.ttf', self.size)
        self.text = self.font.render(self.message, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)

    def display(self):
        self.font = pg.font.Font('freesansbold.ttf', self.size)
        self.text = self.font.render(self.message, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        self.game.screen.blit(self.text, self.textRect)

    #some texts contents are always changing so it is handy to be able to secure the text at a corner not a middle
    #this is mainly so the time can go in the top right corner of the screen without changing x co-ordinate as it changes its message
    def display_topright(self):
        self.font = pg.font.Font(TEXT_FONT, self.size)
        self.text = self.font.render(self.message, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.x, self.y)
        self.game.screen.blit(self.text, self.textRect)

    


class Heart:

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        self.image = pg.image.load(heart_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)



class Portal(pg.sprite.Sprite):
    #portal made up of two rectangles
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((Portal_width, Portal_height))
        self.image.fill(Portal_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        pg.draw.rect(self.image, Portal_color_bg, (7, 10, 17, 31))

class rect:

    def __init__(self, x, y, width, height, color, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.game = game

    def rect_draw(self):
        pg.draw.rect(self.game.screen, self.color, (self.x - self.width/2, self.y - self.height/2, self.width, self.height))


#game loop
g = Game()
g.starter_screen()
while g.running:
    g.new()
    if g.pause == True:
        g.pause_screen()
    else:
        g.end_screen()

pg.quit()
sys.exit()