import random
import arcade
import time
import math
import threading

SCREEN_WIDTH =800
SCREEN_HIGHT =600

class starship(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x =SCREEN_WIDTH//2
        self.center_y =32
        self.width =40
        self.heigth=40
        self.angle=0
        self.speed =4
        self.change_angle =3
        self.bulet_list=[]
        self.score =10
        
    def fire(self):
        self.bulet_list.append(Bullet(self))  

    def rotate(self, dir):
        self.angle += self.change_angle * dir
        
    

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randint(0,SCREEN_WIDTH)
        self.center_y = SCREEN_HIGHT+20
        self.change_y=0
        self.width =40
        self.heigth=40
        self.speed =4
        self.score =10
    def move(self):
        self.center_y -=self.speed   

class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed =6
        self.angle =host.angle
        self.center_x = host.center_x
        self.center_y =host.center_y
    def move(self):
        a=math.radians(self.angle)
        self.center_x +=self.speed * math.sin(-a)
        self.center_y +=self.speed * math.cos(a)
            

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HIGHT,"STAR WAR GAME 🚀")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.laser = arcade.sound.Sound(":resources:sounds/laser5.wav")
        self.hit = arcade.sound.Sound(":resources:sounds/hit3.wav")
        self.me=starship()
        self.enemy_list =[]
        self.start_time= time.time()
        self.next_time = random.uniform(4, 6)
        self.score = 0
        self.health = 3
        self.game_over = False
        self.enemy_speed = 4
        self.dir = 1
        self.start_thread=True
        self.my_thread=threading.Thread(target=self.add_enemy)
        self.my_thread.start()
        


    def on_draw(self): 
        arcade.start_render() 
        arcade.draw_text("Score: " + str(self.score), 700, 32)
        if self.health > 0:
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HIGHT,self.background_image)
            for i in range(self.health):
                arcade.draw_lrwh_rectangle_textured(32 + i * 30, 32, 25, 25, arcade.load_texture("heart.png"))
        else:
            # Game Over
            self.game_over = True
            arcade.draw_text('GAME OVER', SCREEN_WIDTH/2 - 100, SCREEN_HIGHT/2, font_size=25)
            

        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for bullet in self.me.bulet_list:
            bullet.draw()    
    

    def add_enemy(self):
        while not self.game_over:
            time.sleep(5)
            if not self.game_over:
                self.enemy_list.append(Enemy())
            
      

    def on_update(self,delta_time:float):
        if not self.game_over:
            self.end_time =time.time()
            self.me.rotate(self.dir) 

            for enemy in self.enemy_list:
                enemy.speed = self.enemy_speed
                enemy.move()
                if enemy.center_y < 0:
                    self.enemy_list.remove(enemy)
                    self.health -= 1
                    if self.health <= 0:
                        self.health = 0

            for bullet in self.me.bulet_list:
                bullet.move() 
                for enemy in self.enemy_list:
                    if arcade.check_for_collision(bullet, enemy):
                        # Collision Detection
                        self.enemy_list.remove(enemy)
                        self.me.bulet_list.remove(bullet)
                        self.score += 1
                        self.enemy_speed += 0.1
                        arcade.play_sound(self.laser)
                if bullet.center_y > SCREEN_HIGHT + 5:
                    if bullet in self.me.bulet_list:
                        self.me.bulet_list.remove(bullet)
                
    def on_key_press(self, symbol: int, modifiers: int):
        # Space: shoot, A: rotate to left, S: rotate to right
        if not self.game_over:
            if symbol==arcade.key.SPACE:
                self.me.fire()
                arcade.play_sound(self.hit)
            if symbol==arcade.key.A:
                self.dir = 1
            if symbol==arcade.key.S:
                self.dir = -1


game=Game()            
arcade.run()
 