#========= 1. 导入库 =========
import pygame
import sys
import random
#========= 2. 初始化pygame所有模块 ==========
pygame.init()
#========= 3. 创建一个宽800，高600的窗口 =========
screen = pygame.display.set_mode((800, 600))
#========= 4. 窗口命名 =========
pygame.display.set_caption('贪吃蛇小游戏')
#========= 5. 变量配置 =========
#1.定义一个坐标列表
snake = [(100,100),(80,100),(60,100)]
# print(snake[0][0])
#2.定义一个外循环
clock = pygame.time.Clock()
#3.定义一个窗口状态变量，默认为True
game = True
#4.定义移动初始值·默认向右移动
dx = 20
dy = 0
#5.分数变量
score = 0
#6.创建字体·大小为20
font = pygame.font.Font('hpsimplifiedhans-light.ttf',20)
#7.游戏状态变量
state = 'playing'
#8.食物坐标
food_x = random.randrange(0, 40) * 20   # 0~39 乘以 20，得到 0~780
food_y = random.randrange(0, 30) * 20   # 0~29 乘以 20，得到 0~580
#========= 6. 循环开启 =========
while game:
    #1.限制为每秒循环八次
    clock.tick(8)
    #2.创建事件循环
    for event in pygame.event.get():
        #3.如果点击了叉号就将窗口循环状态更改为False·关闭窗口
        if event.type == pygame.QUIT:
            game = False
        #4.让方块跟随按键移动
        #只有在游戏进行中的时候才触发检测
        if state == 'playing' and  event.type == pygame.KEYDOWN:
            #如果按了⬆️
            if event.key == pygame.K_UP:
                dy = -20
                dx = 0
            #如果按了⬇️
            elif event.key == pygame.K_DOWN:
                dy = 20
                dx = 0
            #⬅️
            elif event.key == pygame.K_LEFT:
                dx = -20
                dy = 0
            #➡️
            elif event.key == pygame.K_RIGHT:
                dx = 20
                dy = 0
        #5.如果游戏已结束
        if state == 'gameover' and event.type == pygame.KEYDOWN:
            #如果按了r，则重新开始游戏
            if event.key == pygame.K_r:
                #需要重置所有变量
                snake = [(100, 100), (80, 100), (60, 100)]      #初始坐标
                dx,dy = 20,0                                    #移动值
                score = 0                                       #分数
                food_x = random.randrange(0, 40) * 20  # 0~39 乘以 20，得到 0~780
                food_y = random.randrange(0, 30) * 20  # 0~29 乘以 20，得到 0~580
                state = 'playing'                               #游戏状态
    #6.填充背景色
    screen.fill((255,255,255))
    #7.创建分数面板
    text = font.render(f'分数: {score}', True, (0,0,0))
    #将分数面板放到左上角10,10的位置
    screen.blit(text, (10,10))
    #8.在窗口内绘制贪吃蛇与食物
    for sn in snake:
        #贪吃蛇
        pygame.draw.rect(screen, (0,255,0),(sn[0],sn[1],20,20))
    #食物
    pygame.draw.rect(screen, (255,0,0),(food_x,food_y,20,20))
    #生成新的蛇头
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)
    #9.吃到食物就+1
    if snake[0] == (food_x,food_y):
        score += 1
        food_x = random.randrange(0, 800,20)
        food_y = random.randrange(0, 600,20)
    else:
        #删除尾部
        snake.pop()
    #10.游戏失败，触发判定
    if state == 'playing':
        # 碰到墙壁游戏结束
        if snake[0][0] < 0 or snake[0][0] >= 800 or snake[0][1] < 0 or snake[0][1] >= 600:
            state = 'gameover'
        # 碰到自己游戏退出
        if snake[0] in snake[1:]:
            state = 'gameover'
    if state == 'gameover':
        over_text = font.render('游戏结束，按 R 重开', True, (255, 0, 0))
        screen.blit(over_text, (250, 280))
    #11.更新画面，刷新窗口
    pygame.display.flip()
#========= 7. 关闭窗口 =========
pygame.quit()
sys.exit()