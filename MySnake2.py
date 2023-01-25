import pymysql
import os

# подключение к базе данных
def addcolor_MySqldb():
    con = pymysql.connect(
        host= 'localhost',
        user='root',
        password='Amirka1234',
        db= 'gamedb'
    )
    
    # создадим объект курсора
    cursor = con.cursor()
    
    # закрепление после добавления
    cursor.execute( f"""INSERT INTO snakegame(colors) VALUES ({i})""" )
    con.commit()

    # закрываем все соединения
    cursor.close()
    con.close()

def output_indexColor_MySQL():
    array = [] 
    con = pymysql.connect(
        host= 'localhost',
        user='root',
        password='Amirka1234',
        db= 'gamedb'
    )
    
    # создадим объект курсора
    cursor = con.cursor()
    
    # ВЫТАСКИВАЕМ ВСЕ СОДЕРЖИМОЕ ИЗ БАЗЫ ДАННЫХ
    cursor.execute( f"""SELECT colors FROM snakegame;""" )
    con.commit()

    # ЗАКРЕПЛЯЕМ И ОКОНЧАТЕЛЬНО ВЫТАСКИВАЕМ
    rows = cursor.fetchall()

    # ПЕРЕБЕРАЕМ КОРТЕЖ ВЛОЖЕНЫМИ ЦИКЛАМИ, ДЛЯ ДОБАВЛЕНИЯ В СПИСОК
    for row in rows:
        for column in row:
            array.append(column)

    # закрываем все соединения
    cursor.close()
    con.close()
    
    return array

def addMode_MySqldb():
    con = pymysql.connect(
        host= 'localhost',
        user='root',
        password='Amirka1234',
        db= 'gamedb'
    )
    
    # создадим объект курсора
    cursor = con.cursor()
    
    # закрепление после добавления
    cursor.execute( f"""INSERT INTO snakegame(gamemode) VALUES ({j})""" )
    con.commit()

    # закрываем все соединения
    cursor.close()
    con.close()

def output_indexMode_MySQL():
    array = [] 
    con = pymysql.connect(
        host= 'localhost',
        user='root',
        password='Amirka1234',
        db= 'gamedb'
    )
    
    # создадим объект курсора
    cursor = con.cursor()
    
    # ВЫТАСКИВАЕМ ВСЕ СОДЕРЖИМОЕ ИЗ БАЗЫ ДАННЫХ
    cursor.execute( f"""SELECT gamemode FROM snakegame """ )
    con.commit()

    # ЗАКРЕПЛЯЕМ И ОКОНЧАТЕЛЬНО ВЫТАСКИВАЕМ
    rows = cursor.fetchall()

    # ПЕРЕБЕРАЕМ КОРТЕЖ ВЛОЖЕНЫМИ ЦИКЛАМИ, ДЛЯ ДОБАВЛЕНИЯ В СПИСОК
    for row in rows:
        for column in row:
            if column != None:
                array.append(column)

    # закрываем все соединения
    cursor.close()
    con.close()

    # возврашаю наш список
    return array

#импортированые модули
import dbm
import pygame
import random
import webbrowser

urlInst = 'https://www.instagram.com/self.mypy/'

def addFruit_in_Multi():
    apple_coord_in_Multi.clear()
    for i in range(3):
        apple_coord_in_Multi.append([
            random.randrange(20, windowSize[0] - 6 - 20, 10),
            random.randrange(20, windowSize[1] - 8 - 20, 10),]
            )

# расположение экрана
# C:/Users/Амирка/Desktop/Программирование/
path = os.getcwd()
files = os.listdir(path=path)
print(files)

# инициализация модуля
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Sound Eat
SoundEat = pygame.mixer.Sound(path + '/' + files[files.index('Coin.wav')])
SoundEat.set_volume(0.2)

# Sound Eat Tail
SoundEatTail = pygame.mixer.Sound(path + '/' + files[files.index('SnakeEatsTail.wav')])
SoundEatTail.set_volume(0.5)

# BGSounds
BGSound = pygame.mixer.Sound(path + '/' + files[files.index('BGSound.wav')])
valume = 0.8
BGSound.set_volume(valume)
BGSound.play()

# RectsSound
RectSound = pygame.mixer.Sound(path + '/' + files[files.index('RectRand_Sound.wav')])
RectSound.set_volume(0.8)

# проверка на звук
isSound = True

#цвета кнопки 
colorButtonIsSound = {'SoundOn':(124, 252, 0), 'SoundOff':(255, 0, 0)}

# получение высоты и ширины экрана
infoScreen = pygame.display.Info()
windowSize = (infoScreen.current_w, infoScreen.current_h)

sc = pygame.display.set_mode(windowSize, pygame.HWSURFACE)
pygame.display.set_caption('MySnake2')
pygame.display.set_icon(pygame.image.load(path + '/' +files[files.index('icon_SnakeGame2.png')]))

# Изображение
isSoundOffSurface = pygame.image.load(path + '/' +files[files.index('isSoundOff.png')])
isSoundOnSurface = pygame.image.load(path + '/' +files[files.index('isSoundOn.png')])

# из Surface в Rect
ImageSoundOff = isSoundOffSurface.get_rect(center = ((windowSize[0] // 1.5) + 180, 40))
ImageSoundOn = isSoundOnSurface.get_rect(center = ((windowSize[0] // 1.5) + 180, 40))

# иконка инстаграмма
MyInstSurface = pygame.image.load(path + '/' +files[files.index('MyInstagramm.png')])
MyInstSurface = pygame.transform.scale(MyInstSurface, (80, 80))
MyInstRect = MyInstSurface.get_rect()
MyInstRect = MyInstRect.move((windowSize[0] - MyInstSurface.get_width(), windowSize[1] - MyInstSurface.get_height()))

# Создадим счётчик FPS
clock = pygame.time.Clock()

# создадим файл в котором будет наши поинты и индексы выбраных цветов и режимов змейки с последней игры
GameFile = dbm.open('GamesFile', 'c')

# наш основной цикл
loop = True

# очки и деньги
count = 0
sum = int(GameFile['money'])

# словарь координат змейки и её возрождение
coord = {
    'x': (windowSize[0] - 6) // 2,
    'y': (windowSize[1] - 8) // 2,
    'x_col':0,
    'y_col':0
}

# цвета змейки
colors = {
    'snake_head':(50, 240, 80),
    'snake_tails':(0, 255, 0),
    'apple':(255, 0, 0)
}

#   скорость передвижения
snake_speed = 10

# координаты яблок
apple_coord = {
    'x': random.randrange(10, windowSize[0] - 10, snake_speed),
    'y': random.randrange(10, windowSize[1] - 10, snake_speed)
}
apple_coord_in_Multi = []

# наш текст
TextApplication = {'color': (255,255,255), 'x_y': (((windowSize[0] - 6) // 2) - 230, ((windowSize[1] - 8) // 2) - 300),'fontSize': 140, 'names': 'Snake2.py'}

# нажатые клавиши для блокировки движения в некоторых направлениях
keys = {'W': True, 'S': True, 'A': True, "D":True}

# цвета кнопок в состоянии фокуса и покоя
colorsMode = {'StartGame': (50, 205, 50), 'StartGame_Collidepoint':(0, 100, 0) ,'colorCollection':(255, 165, 0), 
                'Collection_Collidepoint':(255, 69, 0), 'colorText': (173, 255, 47), 'colorTextCollisions':(255, 255, 0),
                'colorMouse':(255, 255, 255), 'Collidepoint_text_shops':(184, 134, 11), 'colorTextclose':(240,0,0,), 
                'colorButtonclose':(100, 0, 0), 'colorCollideButtonClose':(255, 0, 0), 'colorTextCloseCollide':(139, 0, 0)}

# цвета в режима покупки
colorsModeShops = {'colorsStrelki':(255, 0, 0), 'colorsSetFocus': (240, 50, 0), 'moneyNotBut':(255, 0, 0), 'moneyYesBut':(127, 255, 0),
'moneyButYesFocuses':(100, 255, 100), 'moneyButCollidepoint':(127, 215, 0), 'colorsText':(139, 0, 0), 'collisionText': (0, 100, 0), 
'use_color_Text': (0, 128, 0), 'use_color_Button':(0, 255, 0), 'Byed_color_Button':(255, 165, 0), 'Byed_color_Text':(255, 69, 0),
'colorButtonMode':(255, 140, 0), 'colorButtonText':(255, 215, 0), 'colliderButtonColor':(255, 255, 0), 'colliderTextColor':(255, 69, 0),
'Buyed_in_Mode/Color':(0, 100, 0), 'colorButton_Collide_Byed':(34, 139, 34)}

# цвета которые будут в магазине змейки 1 это голова 2 хвостовая часть змеи
colorsBuy = [
            [(50, 240, 80), (0, 255, 0)], 
            [(70, 130, 180), (0, 255, 255)], 
            [(255, 165, 0), (255, 69, 0)],
            [(255, 20, 147), (255, 105, 180)],
            [(184, 134, 11), (218, 165, 32)],
            [(221, 160, 221), (188, 143, 143)],
            [(218, 165, 32), (255, 255, 0)]
            ]

# Это будут ценники на наши цвета
MoneyBuy = [0, 300, 500, 700, 850, 900, 1000]

# координаты для показа
coord_shop = {'x0': (windowSize[0] - 6) // 2,
                'y0': (windowSize[1] - 8) // 2,
                'x1': 10,
                'y2': 10
            }   

# список цветов для представления режимов
colorsSetMode = {'FruitRect': (255, 0, 0), 'StenaRect':(107, 142, 35)}

# текст для понимания что за предмет есть у них
textlistShop = ['OneFruit', 'Rects', 'MultiFruit', 'Peac']
textlistShopRus = ['Один фрукт','Стенки','Фрукты','Свободный']
# Цена за улучшение фрукта
score_Buy_Fruit = int(GameFile['count_Fruit_Buy'])
# стоимость
bonus_max = 5
MoneySetMode = [0, 300, 700, 1200, score_Buy_Fruit]

# хвоста змейки
snake_xy = []
len_snake = 1

# режим игры
GameMode = 'menu'
# мод нашей покупки
Shopmode = 'colors'
# мод нашей игры OneFruit/Multiply/RandRect/Peac/ +1 Score in Fruit
modeSnake = 'OneFruit'

# индекс цвета змейки
i = 0
use_colors_index = 0

# индекс нашего мода
j = 0
use_mode_index = 0

# вытаскивает наши купленые моды
SetMode_select = output_indexMode_MySQL()

# вытаскивает наши купленые цвета
colors_select = output_indexColor_MySQL()

# счётчик
count_Rect = 0
RectList = []

# главный цикл
while loop:
    # закрашивание всего постоянно в черный
    sc.fill((0, 0, 0,))

    if GameMode == 'menu' or GameMode == 'shop':
    # провека на включённый звук
        if isSound:
            settingSound = pygame.draw.rect(sc, colorButtonIsSound['SoundOn'], (windowSize[0] // 1.5 + 160, 20, 45, 45))
            sc.blit(isSoundOnSurface, ImageSoundOn)
            if valume <= 0.8:
                valume += 0.05
                BGSound.set_volume(valume)
        else:
            settingSound = pygame.draw.rect(sc, colorButtonIsSound['SoundOff'], (windowSize[0] // 1.5 + 160, 20, 45, 45))
            sc.blit(isSoundOffSurface, ImageSoundOff)
            if valume >= 0.0:
                valume -= 0.05
                BGSound.set_volume(valume)

        sc.blit(MyInstSurface, MyInstRect)

    ##############################################################################################################################################
    if GameMode == 'game':
        # проверка на выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                GameFile.close()
            # условия на нажатые клавиши
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and keys["A"]:
                    coord['x_col'] = -snake_speed
                    coord['y_col'] = 0
                    keys = {'W': True, 'S': True, 'A': True, "D":False}

                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and keys['D']:
                    coord['x_col'] = snake_speed
                    coord['y_col'] = 0
                    keys = {'W': True, 'S': True, 'A': False, "D":True}

                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and keys['W']:
                    coord['x_col'] = 0
                    coord['y_col'] = -snake_speed
                    keys = {'W': True, 'S': False, 'A': True, "D":True}

                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and keys['S']:
                    coord['x_col'] = 0
                    coord['y_col'] = snake_speed
                    keys = {'W': False, 'S': True, 'A': True, "D":True}
                
                elif event.key == pygame.K_ESCAPE:
                    GameMode = 'menu'
                    if isSound:
                        BGSound.play()
                    else:
                        BGSound.stop()

        # проверка накакой мод используется
        if modeSnake == 'OneFruit':
            # яблочко
            apple = pygame.draw.rect(sc, colors['apple'], (apple_coord['x'], apple_coord['y'], 10, 10))

            # проверка на съедаемость с помощью координат 
            if coord['x'] == apple_coord['x'] and coord['y'] == apple_coord['y']:
                apple_coord['x'] = random.randrange(10, windowSize[0] - 10, snake_speed)
                apple_coord['y'] = random.randrange(10, windowSize[1] - 10, snake_speed)
                count += score_Buy_Fruit // 100
                sum += 1  
                GameFile['money'] = str(sum)
                len_snake += 1
                if isSound:
                    SoundEat.play()

        # мод игры
        if modeSnake == 'MultiFruit':
            # рисование 3-х фруктов ( квадратиков )
            for cor in apple_coord_in_Multi:
                apple = pygame.draw.rect(sc, colors['apple'], (cor[0], cor[1], 10, 10))

            # проверка на не превышения колличесства фруктов на экране
            if len(apple_coord_in_Multi) > 3:
                for i in range(len(apple_coord_in_Multi) - 3):
                    apple_coord_in_Multi.pop()

            # в цикле перебераются координаты фруктов что бы проверить на столкновение, если мы фрукт "съели", то мы удаляем фрукт в списке
            # с этими координатами, и добавляем новые
            for cor in apple_coord_in_Multi:
                if coord['x'] == cor[0] and coord['y'] == cor[1]:
                    apple_coord_in_Multi.append([random.randrange(20, windowSize[0] - 6 - 20, 10),
                                                random.randrange(20, windowSize[1] - 8 - 20, 10)])
                    apple_coord_in_Multi.pop(apple_coord_in_Multi.index([cor[0], cor[1]]))
                    count += score_Buy_Fruit // 100
                    sum += 1  
                    GameFile['money'] = str(sum)
                    len_snake += 1
                    if isSound:
                        SoundEat.play()
                    break

        # Режим рандомных блоков/стенок 
        if modeSnake == 'Rects':
            # яблочко
            apple = pygame.draw.rect(sc, colors['apple'], (apple_coord['x'], apple_coord['y'], 10, 10))

            # проверка на съедаемость с помощью координат 
            if coord['x'] == apple_coord['x'] and coord['y'] == apple_coord['y']:
                apple_coord['x'] = random.randrange(10, windowSize[0] - 10, snake_speed)
                apple_coord['y'] = random.randrange(10, windowSize[1] - 10, snake_speed)
                count += score_Buy_Fruit // 100
                sum += 1  
                GameFile['money'] = str(sum)
                len_snake += 1
                count_Rect += 1
                if count_Rect >= 2:
                    count_Rect = 0
                    RectList.append( [random.randrange(10, (windowSize[0] - 6) - 10, 10), random.randrange(10, (windowSize[1] - 8) - 10, 10)] )
                    if isSound:
                        RectSound.play()
                if isSound:
                    SoundEat.play()
                
            for num in RectList:
                RectRand = pygame.draw.rect(sc, colorsSetMode['StenaRect'], (num[0], num[1], 10, 10))
                if num in snake_xy:
                    RectList.pop()
                    RectList.append( [random.randrange(10, (windowSize[0] - 6) - 10, 10), random.randrange(10, (windowSize[1] - 8) - 10, 10)] )

                if num[0] == cor[0] and num[1] == cor[1]:
                    GameMode = 'menu'
                    RectList.clear()
                    if isSound:
                        BGSound.play()
                    else:
                        BGSound.stop()
        
        # свободный режим
        if modeSnake == 'Peac':
            # яблочко
            apple = pygame.draw.rect(sc, colors['apple'], (apple_coord['x'], apple_coord['y'], 10, 10))

            # проверка на съедаемость с помощью координат 
            if coord['x'] == apple_coord['x'] and coord['y'] == apple_coord['y']:
                apple_coord['x'] = random.randrange(10, windowSize[0] - 10, snake_speed)
                apple_coord['y'] = random.randrange(10, windowSize[1] - 10, snake_speed)
                count += score_Buy_Fruit // 100
                sum += 1  
                GameFile['money'] = str(sum)
                len_snake += 1
                if isSound:
                    SoundEat.play()
                  
        # будем постоянно заполнять наш список, координатами змейки  
        snake_xy.append([coord['x'], coord['y']])

        # проверка на выход за границы экрана, выход змейки из границы экрана будет ровно поражению/окончанию игры
        if (coord['x'] < 0 or coord['x'] > windowSize[0] or coord['y'] < 0 or coord['y'] > windowSize[1]) and modeSnake != 'Peac':
            GameMode = 'menu'
            coord['x'] = (windowSize[0] - 6) / 2
            coord['y'] = (windowSize[1] - 8) / 2
            apple_coord['x'] = random.randrange(10, windowSize[0] - 10, snake_speed)
            apple_coord['y'] = random.randrange(10, windowSize[1] - 10, snake_speed)
            coord['x_col'] = 0
            coord['y_col'] = 0
            len_snake = 1    
            snake_xy.clear()
            count = 0
            keys = {'W': True, 'S': True, 'A': True, "D":True}
            RectList.clear()
            addFruit_in_Multi()
            if isSound:
                BGSound.play()
            else:
                BGSound.stop()

        # наш ипровезированный телепорт
        else:
            if coord['x'] < 0:
                coord['x'] = windowSize[0] - 6
            if coord['x'] > windowSize[0]:
                coord['x'] = 0
            if coord['y'] < 0:
                coord['y'] = windowSize[1] - 8
            if coord['y'] > windowSize[1]:
                coord['y'] = 0

        # если не будет условия, то у нас змейка будет беконечной
        if len(snake_xy) > len_snake:
            del snake_xy[0]
        
        if len_snake < len(snake_xy) and modeSnake != 'Peac':
            if isSound:
                SoundEatTail.play()
            for i in range(len(snake_xy) -  len_snake, 0, -1):
                snake_xy.pop(i)
       
        # цикл для рисования хвостов змейки
        for x_y in snake_xy:
            pygame.draw.rect(sc, colors['snake_tails'], (x_y[0], x_y[1], 10, 10))
        
        # увеличение координат с каждой итерацией цикла
        coord['x'] += coord['x_col']
        coord['y'] += coord['y_col']

        # Условие на столкновение змейки со своим хвостом, хвост будет отпадать если вдруг user переидёт через хвост
        # сделаем так что бы наши накопленые очки уменьшались
        for  num,cor in enumerate(snake_xy):
            if coord['x'] == cor[0] and coord['y'] == cor[1] and modeSnake != 'Peac':
                # snake_xy.clear()
                len_snake -= num
                count -= num
                sum -= num
                GameFile['money'] = str(sum)
            elif modeSnake == 'Peac' and coord['x'] == cor[0] and coord['y'] == cor[1] and (coord['x_col'] > 0 or coord['y_col'] > 0):
                GameMode = 'menu'
                if isSound:
                    BGSound.play()
                else:
                    BGSound.stop()

        # сама змейка
        snake = pygame.draw.rect(sc, colors['snake_head'], (coord['x'], coord['y'] ,10, 10), 2)

        # текст - очки
        f1 = pygame.font.Font(None, 36)
        score = f1.render('Очки:'+str(count), True,
                    (255, 255, 255))

        sc.blit(score, (10, 10))

    ###############################################################################################################################################
    """В этом коде будет находиться всё что связанно с меню/главного экрана игры"""
    # ослеживание нажатии мыши
    mouse = pygame.mouse.get_pressed()
    if GameMode == 'menu':
        
        # название на экране меню
        NameGame = pygame.font.Font(None, TextApplication['fontSize'])
        Surface_txt_main = NameGame.render(TextApplication['names'], False,
                    TextApplication['color'])

        sc.blit(Surface_txt_main, (TextApplication['x_y']))
        # позиция
        pos = pygame.mouse.get_pos()
        
        # текст кнопки 
        Start_txt_but = pygame.font.Font(None, 85)
        Surfase_but = Start_txt_but.render('Start', False,
                    colorsMode['colorText'])

        # кнопка старта
        GameStart = pygame.draw.rect(sc, colorsMode['StartGame'], (windowSize[0] // 2 - 150, windowSize[1] // 2 - 50, 300, 100), 10)
        sc.blit(Surfase_but, (windowSize[0] // 2 - 80, windowSize[1] // 2 - 30))
        
        # текст покупки
        Shops_bt = pygame.font.Font(None, 85)
        Surfase_but_H = Shops_bt.render('Shop', False,
                colorsMode['colorTextCollisions'])
        
        # кнопка покупки
        Shops = pygame.draw.rect(sc, colorsMode['colorCollection'], (windowSize[0] // 2 - 150, windowSize[1] // 1.5 - 50, 300, 100), 10)
        sc.blit(Surfase_but_H, (windowSize[0] // 2 - 80, windowSize[1] // 1.5 - 30))

        # текст денег
        sum_count = pygame.font.Font(None, 56)
        sum_txt = sum_count.render(str(int(GameFile['money'])) + '$', True,
                    (255, 255, 255))

        sc.blit(sum_txt, (10, 10))
        
        # условие на позицию мыши, что бы кнока меняла свой цвет ( то есть становилась в фокусе )
        if GameStart.collidepoint(pos):
            Surfase_but = Start_txt_but.render('Start', False,
                    colorsMode['colorTextCollisions'])
            sc.blit(Surfase_but, (windowSize[0] // 2 - 80, windowSize[1] // 2 - 30))
            GameStart = pygame.draw.rect(sc, colorsMode['StartGame_Collidepoint'], (windowSize[0] // 2 - 150,
                                        windowSize[1] // 2 - 50, 300, 100), 10)
        
        # условие, если наш курсор находится в зоне кнопк, то он становится в фокусе меняя свой цвет
        if Shops.collidepoint(pos): 
            Shops_bt = pygame.font.Font(None, 85)
            Surfase_but_H = Shops_bt.render('Shop', False,
                    colorsMode['Collidepoint_text_shops'])
            sc.blit(Surfase_but_H, (windowSize[0] // 2 - 80, windowSize[1] // 1.5 - 30))

            # кнопка магазина, только уже в фокусе, и другим цветом
            Shops = pygame.draw.rect(sc, colorsMode['Collection_Collidepoint'], (windowSize[0] // 2 - 150, windowSize[1] // 1.5 - 50, 300, 100), 10)
        
        # Кнопка выхода
        exitButton = pygame.draw.rect(sc, colorsMode['colorButtonclose'], (windowSize[0] - 60, 20, 50, 50))
        
        # текст кнопки выхода
        closeText_sc = pygame.font.Font(None, 65)
        Surface_close = closeText_sc.render('X', False, colorsMode['colorTextclose'])
        sc.blit(Surface_close, (windowSize[0] - 50, 25))

        # если наш курсор находиться в относительном положении кнопок И мы нажимаем левую кнопку мыши то мы
        #  начинаем игру меняя переменную мод на game      
        if GameStart.collidepoint(pos) and mouse[0]:
            GameMode = 'game'
            BGSound.stop()

        if Shops.collidepoint(pos) and mouse[0]:
            GameMode = 'shop'

        # проверка на выход из игры
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    GameFile.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop = False
                        GameFile.close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and exitButton.collidepoint(pos):
                        loop = False
                        pygame.quit()

                    # настройка
                    if event.button == 1 and settingSound.collidepoint(pos):
                        if isSound:
                            isSound = False
                        else:
                            isSound = True
                    if event.button == 1 and MyInstRect.collidepoint(pos):
                        webbrowser.open(urlInst)
                            
    # ##############################################################################################################################################
    """В данном коде будет находиться ВСЁ что связано с нашей покупкой, и многое другое"""
    #3 режим игры - это магазин, где будут цвета 
    if GameMode == 'shop':
        
        # позиция
        pos = pygame.mouse.get_pos()
        # текст денег
        sum_count = pygame.font.Font(None, 56)
        sum_txt = sum_count.render(str(int(GameFile['money'])) + '$', True,
                    (255, 255, 255))
        sc.blit(sum_txt, (10, 10))
        
        # стрелочка влево
        leftBut = pygame.draw.polygon(sc, colorsModeShops['colorsStrelki'], [[windowSize[0] * 0 + 100, windowSize[1] // 2], 
            [windowSize[0] * 0 + 150, windowSize[1] // 2 + 150],
            [windowSize[0] * 0 + 150, windowSize[1] // 2 - 150]])
        
        # наша стрелка вправо
        rightBut = pygame.draw.polygon(sc, colorsModeShops['colorsStrelki'], [[windowSize[0] - 100, windowSize[1] // 2], 
            [windowSize[0] - 150, windowSize[1] // 2 + 150],
            [windowSize[0] - 150, windowSize[1] // 2 - 150]])

        # Кнопка выхода
        exitButton = pygame.draw.rect(sc, colorsMode['colorButtonclose'], (windowSize[0] - 60, 20, 50, 50))
        
        # кнопки переключения в магазине 
        ButtonColorMode = pygame.draw.rect(sc, colorsModeShops['colorButtonMode'], (windowSize[0] / 3, 25, 140, 50))
        ButtonSetMode = pygame.draw.rect(sc, colorsModeShops['colorButtonMode'], (windowSize[0] / 1.7 , 25, 140, 50))

        # условие на нахождение в поле кнопок
        if ButtonColorMode.collidepoint(pos):
            ButtonColorMode = pygame.draw.rect(sc, colorsModeShops['colliderButtonColor'], (windowSize[0] / 3, 25, 140, 50))
            # текст кнопки магазина цвета
            ButtonColorMode_sc = pygame.font.Font(None, 60)
            Surface_mode_sc = ButtonColorMode_sc.render('color', False, colorsModeShops['colliderTextColor'])
            sc.blit(Surface_mode_sc, (windowSize[0] / 3 + 13, 28))

        elif ButtonSetMode.collidepoint(pos):
            ButtonSetMode = pygame.draw.rect(sc, colorsModeShops['colliderButtonColor'], (windowSize[0] / 1.7 , 25, 140, 50))
        
            # текст кнопки магазина модов
            ButtonSetMode_sc = pygame.font.Font(None, 60)
            Surface_SetMode_sc = ButtonSetMode_sc.render('mode', False, colorsModeShops['colliderTextColor'])
            sc.blit(Surface_SetMode_sc, (windowSize[0] / 1.7 + 13, 28))
            
        # текст кнопки выбора магазина цвета
        ButtonColorMode_sc = pygame.font.Font(None, 60)
        Surface_mode_sc = ButtonColorMode_sc.render('color', False, colorsModeShops['colorButtonText'])
        sc.blit(Surface_mode_sc, (windowSize[0] / 3 + 13, 28))

        # текст кнопки магазина модов
        ButtonSetMode_sc = pygame.font.Font(None, 60)
        Surface_SetMode_sc = ButtonSetMode_sc.render('mode', False, colorsModeShops['colorButtonText'])
        sc.blit(Surface_SetMode_sc, (windowSize[0] / 1.7 + 13, 28))
        
        # текст кнопки выхода
        closeText_sc = pygame.font.Font(None, 65)
        Surface_close = closeText_sc.render('X', False, colorsMode['colorTextclose'])
        sc.blit(Surface_close, (windowSize[0] - 50, 25))

        # ###############################################################################################################################################
        # Условие на мод, будет 2 мода, 1-ый это будет покупка цвета - 2-ой это будет покупка мода, и увеличение поинтов за фрукт
        if Shopmode == 'colors': 
            # наша змейка номер 2 которая будет показывать цвета
            Snake_Color = pygame.draw.rect(sc, colorsBuy[i][0], (coord_shop['x0'] - 55, coord_shop['y0'], 70, 70), 5)
            Snake_Color_Side = pygame.draw.rect(sc, colorsBuy[i][1], (coord_shop['x0'] + 23, coord_shop['y0'], 70, 70))
            
            # кнопка с помощью которой можно выбрать или купить цвет змейки
            BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyNotBut'], ((((windowSize[0] - 6) // 2) - 100), (windowSize[1] - 8 - 100), 240, 90))
            # проверка на надичие цвета 
            if i in colors_select:
                if use_colors_index != i:
                # отслеживаение 
                    # если не ставить это условие, то наша кнопка будет красной, тут код сделает так что бы был 
                    # эффект выбора в фокусе и нет, не забывай :) 
                    if BuyBut.collidepoint(pos):
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyButYesFocuses'], ((((windowSize[0] - 6) // 2) - 100), 
                            (windowSize[1] - 8 - 100), 240, 90))
            
                        # ТЕКСТ О ПОКУПКЕ
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render('Выбрать', False,
                                colorsModeShops['collisionText'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))
                    else:
                        # кнопка с помощью которой можно выбрать или купить цвет змейки
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['Byed_color_Button'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))

                        # ТЕКСТ О ПОКУПКЕ
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render('Выбрать', False,
                                colorsModeShops['Byed_color_Text'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))

                else:
                    # кнопка с помощью которой можно выбрать или купить цвет змейки
                    BuyBut = pygame.draw.rect(sc, colorsModeShops['use_color_Button'], ((((windowSize[0] - 6) // 2) - 100),
                    (windowSize[1] - 8 - 100), 240, 90))

                    # ТЕКСТ О ВЗЯТИИ ЦВЕТА
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render('Выбрано', False,
                            colorsModeShops['use_color_Text'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))
            else:
                # ставим условие на нужное колличество средств на покупку, если его хватает, то мы закрашиваем в слегка зелёный цвет
                # если нет, то в красный
                if sum >= MoneyBuy[i]:
                    BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100), 
                    (windowSize[1] - 8 - 100), 240, 90))      
                    # ЦЕННИК
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render(str(MoneyBuy[i]) + '$', False,
                            colorsModeShops['Buyed_in_Mode/Color'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))
                    # проверка на нахождения в поле квадрата
                    if BuyBut.collidepoint(pos):
                        # меняем квадрату цвет
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['colorButton_Collide_Byed'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))
                        # меняем цвет тексту  
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render(str(MoneyBuy[i]) + '$', False,
                            colorsModeShops['moneyYesBut'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))             
                else:
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render(str(MoneyBuy[i]) + '$', False,
                            colorsModeShops['colorsText'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))

                    if sum >= MoneyBuy[i]:
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))
            
        # режим где будут покупать режимы игры
        if Shopmode == 'setmode':
            # 1. фрукт ( авто )
            if textlistShop[j] == textlistShop[0]:
                Fruit = pygame.draw.rect(sc, colorsSetMode['FruitRect'], (windowSize[0] / 2, windowSize[1] / 2, 70, 70))

            # 2. стенки
            if textlistShop[j] == textlistShop[1]:
                Stena = pygame.draw.rect(sc, colorsSetMode['StenaRect'], (windowSize[0] / 2, windowSize[1] / 2, 70, 70))
            
            # 3. несколько фруктов
            if textlistShop[j] == textlistShop[2]:
                Fruit = pygame.draw.rect(sc, colorsSetMode['FruitRect'], (windowSize[0] / 2, windowSize[1] / 2 - 50, 70, 70))
                Fruit = pygame.draw.rect(sc, colorsSetMode['FruitRect'], (windowSize[0] / 2 - 80, windowSize[1] / 2 + 10, 70, 70))
                Fruit = pygame.draw.rect(sc, colorsSetMode['FruitRect'], (windowSize[0] / 2 + 80, windowSize[1] / 2 + 10, 70, 70))

            # 4. мирный
            if textlistShop[j] == textlistShop[3]:
                # наша змейка номер 2 которая будет показывать цвета
                Snake_Color = pygame.draw.rect(sc, colorsBuy[i][0], (coord_shop['x0'] - 55, coord_shop['y0'], 70, 70), 5)
                Snake_Color_Side = pygame.draw.rect(sc, colorsBuy[i][1], (coord_shop['x0'] + 23, coord_shop['y0'], 70, 70))
            
            # Текст для понятия что это :) 
            SetModeText_Shop = pygame.font.Font(None, 55)
            SetModeText_Shop_sc = SetModeText_Shop.render(textlistShopRus[j], True,
                        (255, 255, 255))
            sc.blit(SetModeText_Shop_sc, (windowSize[0] / 2 - 90, (windowSize[1] / 2) + 150))
            # кнопка с помощью которой можно выбрать или купить цвет змейки
            BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyNotBut'], ((((windowSize[0] - 6) // 2) - 100), (windowSize[1] - 8 - 100), 240, 90))
            
            if BuyBut.collidepoint(pos):
                BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyButYesFocuses'], ((((windowSize[0] - 6) // 2) - 100), 
                (windowSize[1] - 8 - 100), 240, 90))
            
            # проверка на колличество монет, что бы подсветить кнопку нужным цветом
            if sum >= MoneySetMode[j]:
                BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100), 
                (windowSize[1] - 8 - 100), 240, 90))

            # проверка на надичие цвета 
            if j in SetMode_select:
                if use_mode_index != j:
                    # отслеживаение 
                    # если не ставить это условие, то наша кнопка будет красной, тут код сделает так что бы был 
                    # эффект выбора в фокусе и нет, не забывай :) 
                    if BuyBut.collidepoint(pos):
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyButYesFocuses'], ((((windowSize[0] - 6) // 2) - 100), 
                            (windowSize[1] - 8 - 100), 240, 90))
            
                        # ТЕКСТ О ПОКУПКЕ
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render('Выбрать', False,
                                colorsModeShops['collisionText'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))
                    else:
                        # кнопка с помощью которой можно выбрать или купить цвет змейки
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['Byed_color_Button'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))

                        # ТЕКСТ О ПОКУПКЕ
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render('Выбрать', False,
                                colorsModeShops['Byed_color_Text'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))

                else:
                    # кнопка с помощью которой можно выбрать или купить цвет змейки
                    BuyBut = pygame.draw.rect(sc, colorsModeShops['use_color_Button'], ((((windowSize[0] - 6) // 2) - 100),
                    (windowSize[1] - 8 - 100), 240, 90))

                    # ТЕКСТ О ВЗЯТИИ ЦВЕТА
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render('Выбрано', False,
                            colorsModeShops['use_color_Text'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 80), (windowSize[1] - 8 - 75)))
            else:
                # ставим условие на нужное колличество средств на покупку, если его хватает, то мы закрашиваем в слегка зелёный цвет
                # если нет, то в красный
                if sum >= MoneySetMode[j]:
                    BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100), 
                    (windowSize[1] - 8 - 100), 240, 90))      
                    # ЦЕННИК
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render(str(MoneySetMode[j]) + '$', False,
                            colorsModeShops['Buyed_in_Mode/Color'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))
                    # проверка на нахождения в поле квадрата
                    if BuyBut.collidepoint(pos):
                        # меняем квадрату цвет
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['colorButton_Collide_Byed'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))
                        # меняем цвет тексту  
                        BuyText = pygame.font.Font(None, 65)
                        Surfase_but_Buy = BuyText.render(str(MoneySetMode[j]) + '$', False,
                            colorsModeShops['moneyYesBut'])
                        sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))             
                else:
                    BuyText = pygame.font.Font(None, 65)
                    Surfase_but_Buy = BuyText.render(str(MoneySetMode[j]) + '$', False,
                            colorsModeShops['colorsText'])
                    sc.blit(Surfase_but_Buy, ((((windowSize[0] - 6) // 2) - 31), (windowSize[1] - 8 - 75)))


                    if sum >= MoneySetMode[j]:
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100), 
                        (windowSize[1] - 8 - 100), 240, 90))

        # подсветка нашей стрелочки выбора
        if leftBut.collidepoint(pos):
            leftBut = pygame.draw.polygon(sc, colorsModeShops['colorsSetFocus'], [[windowSize[0] * 0 + 100, windowSize[1] // 2], 
                [windowSize[0] * 0 + 150, windowSize[1] // 2 + 150],
                [windowSize[0] * 0 + 150, windowSize[1] // 2 - 150]])
        
        # посветка нашей стрелочки выбора
        if rightBut.collidepoint(pos):
            rightBut = pygame.draw.polygon(sc, colorsModeShops['colorsSetFocus'], [[windowSize[0] - 100, windowSize[1] // 2], 
                [windowSize[0] - 150, windowSize[1] // 2 + 150],
                [windowSize[0] - 150, windowSize[1] // 2 - 150]])

        # проверка на выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                GameFile.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameMode = 'menu'
                    
            # остследим нажатие на кнопку мыши и покупку товара
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if BuyBut.collidepoint(pos) and event.button == 1 and not (i in colors_select) and Shopmode == 'colors':
                    if sum >= MoneyBuy[i]:
                        sum -= MoneyBuy[i]
                        GameFile['money'] = str(sum)
                        colors['snake_head'] = colorsBuy[i][0]
                        colors['snake_tails'] = colorsBuy[i][1]
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100),
                        (windowSize[1] - 8 - 100), 240, 90))
                        addcolor_MySqldb()
                
                # открытие моего профиля
                if event.button == 1 and MyInstRect.collidepoint(pos):
                        webbrowser.open(urlInst)
                    

                if BuyBut.collidepoint(pos) and event.button == 1 and not (j in SetMode_select) and Shopmode == 'setmode':
                    if sum >= MoneySetMode[j]:
                        sum -= MoneySetMode[j]
                        GameFile['money'] = str(sum)
                        BuyBut = pygame.draw.rect(sc, colorsModeShops['moneyYesBut'], ((((windowSize[0] - 6) // 2) - 100),
                        (windowSize[1] - 8 - 100), 240, 90))
                        addMode_MySqldb()
                
                # настройка
                if event.button == 1 and settingSound.collidepoint(pos):
                    if isSound:
                        isSound = False
                    else:
                        isSound = True

                # проверка на нажание кнопок влево и вправо
                if event.button == 1 and leftBut.collidepoint(pos):
                    if Shopmode == 'colors':
                        if i < 1:
                            i = len(colorsBuy) - 1
                        else:
                            i -= 1
                    elif Shopmode == 'setmode':
                        if j < 1:
                            j = len(textlistShop) - 1
                        else:
                            j -= 1

                if event.button == 1 and rightBut.collidepoint(pos):
                    if Shopmode == 'colors':
                        if i > len(colorsBuy) - 2:
                            i = 0
                        else:
                            i += 1
                    elif Shopmode == 'setmode':
                        if j > len(textlistShop) - 2:
                            j = 0
                        else:
                            j += 1

                # проверяем на наличие цвета, и его выбор
                if i in colors_select and Shopmode == 'colors':
                    if event.button == 1 and BuyBut.collidepoint(pos):    
                        colors['snake_head'] = colorsBuy[i][0]
                        colors['snake_tails'] = colorsBuy[i][1]
                        use_colors_index = i
                
                # сохранение данных
                if j in SetMode_select and Shopmode == 'setmode':
                    if event.button == 1 and BuyBut.collidepoint(pos):    
                        modeSnake = textlistShop[j]
                        addFruit_in_Multi()
                        use_mode_index = j

                # отслеживание нажатия на кнопку
                if event.button == 1 and exitButton.collidepoint(pos):
                    GameMode = 'menu'
                # отслеживание позиции кнопок
                if event.button == 1 and ButtonColorMode.collidepoint(pos):
                    Shopmode = 'colors'
                if event.button == 1 and ButtonSetMode.collidepoint(pos):
                    Shopmode = 'setmode'   
    
    if GameMode == 'menu' or GameMode == 'shop':
        # Кнопка выхода в фокусе
        if exitButton.collidepoint(pos):
            exitButton = pygame.draw.rect(sc, colorsMode['colorCollideButtonClose'], (windowSize[0] - 60, 20, 50, 50))
            # текст кнопки выхода в фокусе
            closeText_sc = pygame.font.Font(None, 65)
            Surface_close = closeText_sc.render('X', False, colorsMode['colorTextCloseCollide'])
            sc.blit(Surface_close, (windowSize[0] - 50, 25)) 

        # если мышка в фокусе
        if pygame.mouse.get_focused():
            # курсор скрыт
            pygame.mouse.set_visible(False)    
            # наша мышка
            MyMouse = pygame.draw.polygon(sc, colorsMode['colorMouse'], [[pos[0], pos[1]], 
                                                                        [pos [0] + 25, pos[1] + 10],
                                                                        [pos [0] + 10, pos[1] + 25] 
                                                                        ])

    # контроль FPS и обновление экрана и вывод счётчика FPS
    fps = clock.tick(60)
    fps_output = pygame.font.Font(None, 46)
    fps_sc = fps_output.render('FPS:'+str(fps), True,
                (255, 255, 255))
    sc.blit(fps_sc, (windowSize[0] - 170, 35))
    
    # обновление экрана
    pygame.display.update()

    # постоянно вытаскиваем наши индексы из базы данных 
    colors_select = output_indexColor_MySQL()
    SetMode_select = output_indexMode_MySQL()

# окончательный выход  из игры
GameFile.close()
exit()