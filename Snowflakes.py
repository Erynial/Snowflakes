from grafik.canvas import Canvas
import random
import time

# SNOWFLAKE LISTS

snowflakes = []
blue_snowflakes = []
red_snowflakes = []
green_snowflakes = []
other_snowflakes = []

# COUNTERS

blue_count = 0
red_count = 0
green_count = 0

# CANVAS

canvas_width = 1000
canvas_height = 800

UPDATE_DELAY = 0.006

# SNOWFLAKES

snowflake_count = 100

snowflake_width = 25
snowflake_height = 25

snowflake_min_x = 0
snowflake_max_x = canvas_width

snowflake_y_min = -200
snowflake_y_max = -15

snowflake_speed = 5

red_snowflakes_text_x = canvas_width - 100
red_snowflakes_text_y = 10

green_snowflakes_text_x = canvas_width - 100
green_snowflakes_text_y = red_snowflakes_text_y + 20

blue_snowflakes_text_x = canvas_width - 100
blue_snowflakes_text_y = green_snowflakes_text_y + 20

snowflakes_text_x = canvas_width - 100
snowflakes_text_y = blue_snowflakes_text_y + 20

# MARIO

MARIO_EN = 100
MARIO_BOY = 100

mario_left_x = 0
mario_right_x = canvas_width - MARIO_EN

mario_left_y = canvas_height - MARIO_BOY
mario_right_y = canvas_height - MARIO_BOY

mario_speed = 5

mario_and_speed_list = []


def create_snowflakes(game, color_number, rand_x, rand_y):
    if color_number == 1:
        snowflake = game.create_oval(rand_x, rand_y, rand_x + 25, rand_y + 25)
        game.set_color(snowflake, Canvas.COLORS.Blue)
        blue_snowflakes.append(snowflake)
        snowflakes.append(snowflake)
        return snowflake
    elif color_number == 2:
        snowflake = game.create_oval(rand_x, rand_y, rand_x + 25, rand_y + 25)
        game.set_color(snowflake, Canvas.COLORS.Red)
        red_snowflakes.append(snowflake)
        snowflakes.append(snowflake)
        return snowflake
    elif color_number == 3:
        snowflake = game.create_oval(rand_x, rand_y, rand_x + 25, rand_y + 25)
        game.set_color(snowflake, Canvas.COLORS.Green4)
        green_snowflakes.append(snowflake)
        snowflakes.append(snowflake)
        return snowflake
    else:
        color = pick_random_color(game)
        snowflake = game.create_oval(rand_x, rand_y, rand_x + 25, rand_y + 25)
        game.set_color(snowflake, color)
        other_snowflakes.append(snowflake)
        snowflakes.append(snowflake)
        return snowflake


def move_snowflakes(game):
    for snowflake in snowflakes:
        game.move(snowflake, 0, snowflake_speed)


def check_snowflakes_to_send_them_back(game, blue_count_text, red_count_text, green_count_text, all_snows_count_text):
    for snowflake in blue_snowflakes:
        if game.get_top_y(snowflake) > game.get_canvas_height():
            blue_snowflakes.remove(snowflake)
            snowflakes.remove(snowflake)
            game.delete(snowflakes)
            global blue_count
            blue_count += 1

    for snowflake in green_snowflakes:
        if game.get_top_y(snowflake) > game.get_canvas_height():
            green_snowflakes.remove(snowflake)
            snowflakes.remove(snowflake)
            game.delete(snowflakes)
            global green_count
            green_count += 1

    for snowflake in red_snowflakes:
        if game.get_top_y(snowflake) > game.get_canvas_height():
            red_snowflakes.remove(snowflake)
            snowflakes.remove(snowflake)
            game.delete(snowflakes)
            global red_count
            red_count += 1

    for snowflake in other_snowflakes:
        kar_rand_y = random.randint(snowflake_y_min, snowflake_y_max)
        color = pick_random_color(game)
        if game.get_top_y(snowflake) > game.get_canvas_height():
            game.moveto(snowflake, game.get_left_x(snowflake), kar_rand_y)
            game.set_fill_color(snowflake, color)
            game.set_outline_color(snowflake, color)

    print_snowflakes_count(game, blue_count, red_count, green_count,
                           blue_count_text, red_count_text, green_count_text,
                           all_snows_count_text)


def summon_mario(canvas):
    pass


def move_mario(canvas):
    pass


def print_snowflakes_count(game, blue_count_numb_text, red_count, green_count, blue_count_text,
                           red_count_text, green_count_text, all_snows_count_text):
    game.set_text(blue_count_text, blue_count_numb_text)
    game.set_text(red_count_text, red_count)
    game.set_text(green_count_text, green_count)
    game.set_text(all_snows_count_text, len(snowflakes))

    return blue_count_text, red_count_text, green_count_text, all_snows_count_text


def pick_random_color(game):
    colors = [game.COLORS.Khaki3, game.COLORS.Plum1, game.COLORS.Turquoise1, game.COLORS.Yellow3,
              game.COLORS.Antiquewhite2, game.COLORS.Darksalmon, game.COLORS.Violetred3, game.COLORS.Tomato4,
              game.COLORS.Dimgray, game.COLORS.Thistle, game.COLORS.Seagreen, game.COLORS.Peachpuff,
              game.COLORS.Hotpink, game.COLORS.Violetred, game.COLORS.Azure4, game.COLORS.Darksalmon,
              game.COLORS.Brown3, game.COLORS.Cadetblue1, game.COLORS.Coral1, game.COLORS.Cornflowerblue,
              game.COLORS.Mediumorchid2]
    return random.choice(colors)


def main():
    game = Canvas(canvas_width, canvas_height)
    game.set_canvas_background_color(game.COLORS.Bisque)


    select_lang = str(input("Select language. TR-ENG : "))

    if select_lang == "TR":
        tr_start_text = game.create_text(canvas_width/2, canvas_height/2, "KAR OLUŞTURMAK İÇİN TIKLAYINIZ..")
    if select_lang == "ENG":
        eng_start_text = game.create_text(canvas_width/2, canvas_height/2, "CLICK TO CREATE SNOWFLAKES")

    game.wait_for_click()
    if select_lang == "TR":
        game.delete(tr_start_text)
    elif select_lang == "ENG":
        game.delete(eng_start_text)


    for i in range(snowflake_count):
        x = random.randint(1, game.get_canvas_width() - snowflake_width)
        y = random.randint(-2700, -15)
        pick_color = random.randint(1, 30)
        create_snowflakes(game, pick_color, x, y)
        game.update()
        time.sleep(UPDATE_DELAY)


    if select_lang == "ENG":
        game.create_text(blue_snowflakes_text_x, blue_snowflakes_text_y, "B: ")
        blue_count_text_en = game.create_text(blue_snowflakes_text_x + 15, blue_snowflakes_text_y, "0")

        game.create_text(red_snowflakes_text_x, red_snowflakes_text_y, "R: ")
        red_count_text_en = game.create_text(red_snowflakes_text_x + 15, red_snowflakes_text_y, "0")

        game.create_text(green_snowflakes_text_x, green_snowflakes_text_y, "G: ")
        green_count_text_en = game.create_text(green_snowflakes_text_x + 15, green_snowflakes_text_y, "0")

        game.create_text(snowflakes_text_x, snowflakes_text_y, "A: ")
        all_snows_count_text_en = game.create_text(snowflakes_text_x + 20, snowflakes_text_y,
                                                snowflake_count)
    elif select_lang == "TR":
        game.create_text(blue_snowflakes_text_x, blue_snowflakes_text_y, "M: ")
        blue_count_text = game.create_text(blue_snowflakes_text_x + 15, blue_snowflakes_text_y, "0")

        game.create_text(red_snowflakes_text_x, red_snowflakes_text_y, "K: ")
        red_count_text = game.create_text(red_snowflakes_text_x + 15, red_snowflakes_text_y, "0")

        game.create_text(green_snowflakes_text_x, green_snowflakes_text_y, "Y: ")
        green_count_text = game.create_text(green_snowflakes_text_x + 15, green_snowflakes_text_y, "0")

        game.create_text(snowflakes_text_x, snowflakes_text_y, "T: ")
        all_snows_count_text = game.create_text(snowflakes_text_x + 20, snowflakes_text_y,
                                                snowflake_count)



    game.wait_for_click()

    if select_lang == "TR":
        while True:
            print(len(snowflakes))
            check_snowflakes_to_send_them_back(game, blue_count_text, red_count_text, green_count_text,
                                               all_snows_count_text)
            move_snowflakes(game)
            move_mario(game)
            game.update()
            time.sleep(UPDATE_DELAY)
            print(len(snowflakes))
    elif select_lang == "ENG":
        while True:
            print(len(snowflakes))
            check_snowflakes_to_send_them_back(game, blue_count_text_en, red_count_text_en, green_count_text_en,
                                               all_snows_count_text_en)
            move_snowflakes(game)
            move_mario(game)
            game.update()
            time.sleep(UPDATE_DELAY)
            print(len(snowflakes))


if __name__ == '__main__':
    main()
