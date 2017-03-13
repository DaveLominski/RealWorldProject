from tkinter import *
from random import randint
from random import uniform

""" You are the son of a great dictator!

    You have 9 town districts, 2 military base, 1 research facility, 3 elite districts, and your main capital.
    As you are now the supreme leader, you can do anything you want in your command. This game will reflect how you

    REMEMBER! ALL YOUR CHOICES RESULTS DIFFERENT CONSEQUENCES
"""


class GameGUI:
    def __init__(self, root):
        self.game_init()

        self.root = root
        self.number = 0
        self.numString = ''

        # Main Frames
        self.frame_top_bar = Frame(self.root)
        self.frame_down_info = Frame(self.root)
        self.frame_down_map = Frame(self.root)

        self.frame_top_bar.pack(fill=BOTH, expand=False)
        self.frame_down_info.pack(side=LEFT, expand=True)
        self.frame_down_map.pack(side=LEFT, fill=BOTH, expand=True)

        # TOP BAR INIT
        self.label_news = Label(self.frame_top_bar, text="NEWS: You are the son of a great dictator!")
        self.label_news.pack(fill=BOTH, expand=True)

        # INFO INIT
        self.email_message = Label(self.frame_down_info, justify=LEFT, text="FROM: -\nTIME: -\nMessage: Not available")
        self.frame_option = Frame(self.frame_down_info)
        self.frame_option_exp = Frame(self.frame_down_info)
        self.label_option_1 = Label(self.frame_option_exp, text="This is the option 1 Explanation, \nplease check commander")
        self.label_option_2 = Label(self.frame_option_exp, text="This is the option 2 Explanation, \nplease check commander")
        self.button_option_1 = Button(self.frame_option, text="Option 1")
        self.button_option_2 = Button(self.frame_option, text="Option 2")
        self.district_info = Label(self.frame_down_info, justify=LEFT,
                                   text="District Unknown\n\nHappiness   : -\nPopulation  : - / -\nLow class   : -\n"
                                        "Well-being  : -\nIncome/turn : FD. -\nFood Limit  : - / -")

        self.email_message.pack(side=TOP, fill=BOTH, expand=True)
        self.frame_option_exp.pack(side=TOP, fill=BOTH, expand=True)
        self.frame_option.pack(side=TOP, fill=BOTH, expand=True)
        self.label_option_1.pack(side=LEFT, fill=BOTH, expand=True)
        self.label_option_2.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_option_1.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_option_2.pack(side=LEFT, fill=BOTH, expand=True)
        self.district_info.pack(side=TOP, fill=BOTH, expand=True)

        # MAP INIT
        self.frame1 = Frame(self.frame_down_map)
        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2 = Frame(self.frame_down_map)
        self.frame2.pack(fill=BOTH, expand=True)
        self.frame3 = Frame(self.frame_down_map)
        self.frame3.pack(fill=BOTH, expand=True)
        self.frame4 = Frame(self.frame_down_map)
        self.frame4.pack(fill=BOTH, expand=True)
        self.frame5 = Frame(self.frame_down_map)
        self.frame5.pack(fill=BOTH, expand=True)
        self.frame6 = Frame(self.frame_down_map)
        self.frame6.pack(fill=BOTH, expand=True)

        self.button_d1 = Button(self.frame1, text='District 1',
                                command=lambda: self.district_status_update("District 1", self.district_1.show_string()))
        self.button_d2 = Button(self.frame1, text='District 2',
                                command=lambda: self.district_status_update("District 2", self.district_2.show_string()))
        self.button_d3 = Button(self.frame1, text='District 3',
                                command=lambda: self.district_status_update("District 3", self.district_3.show_string()))
        self.button_d4 = Button(self.frame2, text='District 4',
                                command=lambda: self.district_status_update("District 4", self.district_4.show_string()))
        self.button_d5 = Button(self.frame2, text='District 5',
                                command=lambda: self.district_status_update("District 5", self.district_5.show_string()))
        self.button_d6 = Button(self.frame2, text='District 6',
                                command=lambda: self.district_status_update("District 6", self.district_6.show_string()))
        self.button_d7 = Button(self.frame3, text='District 7',
                                command=lambda: self.district_status_update("District 7", self.district_7.show_string()))
        self.button_d8 = Button(self.frame3, text='District 8',
                                command=lambda: self.district_status_update("District 8", self.district_8.show_string()))
        self.button_d9 = Button(self.frame3, text='District 9',
                                command=lambda: self.district_status_update("District 9", self.district_9.show_string()))
        self.button_m1 = Button(self.frame4, text='Military 1',
                                command=lambda: self.district_status_update("Military 1", self.military_1.show_string()))
        self.button_m2 = Button(self.frame4, text='Military 2',
                                command=lambda: self.district_status_update("Military 2", self.military_2.show_string()))
        self.button_r1 = Button(self.frame4, text='Research',
                                command=lambda: self.district_status_update("Research", self.research.show_string()))
        self.button_e1 = Button(self.frame5, text='Elite 1',
                                command=lambda: self.district_status_update("Elite 1", self.elite_1.show_string()))
        self.button_e2 = Button(self.frame5, text='Elite 2',
                                command=lambda: self.district_status_update("Elite 2", self.elite_2.show_string()))
        self.button_e3 = Button(self.frame5, text='Elite 3',
                                command=lambda: self.district_status_update("Elite 3", self.elite_3.show_string()))
        self.button_capital = Button(self.frame6, text='Capital',
                                     command=lambda: self.district_status_update("Capital", self.capital.show_string()))

        self.button_d1.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d2.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d3.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d4.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d5.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d6.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d7.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d8.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_d9.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_m1.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_m2.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_r1.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_e1.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_e2.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_e3.pack(side=LEFT, fill=BOTH, expand=True)
        self.button_capital.pack(fill=BOTH, expand=True)

    def district_status_update(self, district_name, district_input):
        try:
            district_output = "%s\n\n%s" % (district_name, district_input)
            self.district_info.config(text=district_output)
        except Exception as e:
            print("ERROR: " + str(e))

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

    def game_init(self):
        early_population = randint(900000, 1000000)
        early_finance = randint(20000, 30000)

        early_pop_normal = early_population * 0.7
        early_pop_elite = early_population * 0.3
        early_fin_normal = early_finance * 0.5
        early_fin_elite = early_finance * 0.5

        # normal var
        normal_div = [0.1, 0.02, 0.18, 0.09, 0.11, 0.07, 0.12, 0.05, 0.15]
        pop_res, pop_res_cap, fin_res, food_res = [], [], [], []

        for percentage in normal_div:
            pop_res.append(round(early_pop_normal * percentage))
            pop_res_cap.append(round(early_pop_normal * percentage * uniform(1, 1.2)))
            food_res.append(round(early_pop_normal * percentage * uniform(1, 1.3)))
            fin_res.append(round(early_fin_normal * percentage, 2))

        # elite var
        el_pop = [0.26, 0.24, 0.11, 0.13, 0.11, 0.12, 0.03]
        el_fin = [0.1, 0.12, 0.2, 0.08, 0.09, 0.11, 0.3]
        el_pop_res, el_pop_res_cap, el_fin_res, el_food_res = [], [], [], []
        elite_count = 1

        for percentage in el_pop:
            el_pop_res.append(round(early_pop_elite * percentage))
            if elite_count <= 2:
                el_pop_res_cap.append(round(early_pop_elite * percentage * uniform(1.5, 2)))
                el_food_res.append(round(early_pop_elite * percentage * uniform(1, 1.7)))
            elif elite_count == 3:
                el_pop_res_cap.append(round(early_pop_elite * percentage * uniform(1.3, 1.7)))
                el_food_res.append(round(early_pop_elite * percentage * uniform(1, 1.7)))
            elif 4 <= elite_count <= 6:
                el_pop_res_cap.append(round(early_pop_elite * percentage * uniform(2, 2.8)))
                el_food_res.append(round(early_pop_elite * percentage * uniform(2, 3)))
            elif elite_count == 7:
                el_pop_res_cap.append(round(early_pop_elite * percentage * uniform(2.5, 4)))
                el_food_res.append(round(early_pop_elite * percentage * uniform(5, 8)))
            elite_count += 1

        for percentage in el_fin:
            el_fin_res.append(round(early_fin_elite * percentage, 2))

        # population, population_cap, inequalities, happiness, health, finance, food_limit
        self.district_1 = District(pop_res[0], pop_res_cap[0], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[0], food_res[0])
        self.district_2 = District(pop_res[1], pop_res_cap[1], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[1], food_res[1])
        self.district_3 = District(pop_res[2], pop_res_cap[2], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[2], food_res[2])
        self.district_4 = District(pop_res[3], pop_res_cap[3], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[3], food_res[3])
        self.district_5 = District(pop_res[4], pop_res_cap[4], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[4], food_res[4])
        self.district_6 = District(pop_res[5], pop_res_cap[5], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[5], food_res[5])
        self.district_7 = District(pop_res[6], pop_res_cap[6], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[6], food_res[6])
        self.district_8 = District(pop_res[7], pop_res_cap[7], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[7], food_res[7])
        self.district_9 = District(pop_res[8], pop_res_cap[8], randint(55, 99), randint(60, 85),
                                   randint(65, 85), fin_res[8], food_res[8])

        self.military_1 = District(el_pop_res[0], el_pop_res_cap[0], randint(3, 8), randint(80, 95),
                                   randint(90, 98), el_fin_res[0], el_food_res[0])
        self.military_2 = District(el_pop_res[1], el_pop_res_cap[1], randint(3, 8), randint(80, 95),
                                   randint(90, 98), el_fin_res[1], el_food_res[1])
        self.research = District(el_pop_res[2], el_pop_res_cap[2], randint(0, 3), randint(80, 95),
                                 randint(90, 98), el_fin_res[2], el_food_res[2])
        self.elite_1 = District(el_pop_res[3], el_pop_res_cap[3], randint(1, 5), randint(90, 95),
                                randint(90, 98), el_fin_res[3], el_food_res[3])
        self.elite_2 = District(el_pop_res[4], el_pop_res_cap[4], randint(1, 5), randint(90, 95),
                                randint(90, 98), el_fin_res[4], el_food_res[4])
        self.elite_3 = District(el_pop_res[5], el_pop_res_cap[5], randint(1, 5), randint(90, 95),
                                randint(90, 98), el_fin_res[5], el_food_res[5])
        self.capital = District(el_pop_res[6], el_pop_res_cap[6], randint(0, 1), 100,
                                randint(97, 100), el_fin_res[6], el_food_res[6])


class District:
    def __init__(self, population, population_cap, inequalities, happiness, health, finance, food_limit):
        self.population = population
        self.population_cap = population_cap
        self.inequalities = inequalities
        self.happiness = happiness
        self.health = health
        self.finance = finance
        self.food_limit = food_limit
        self.property_values = [self.population, self.population_cap, self.inequalities, self.happiness, self.health,
                                self.finance, self.food_limit]

    def edit_population(self, state, value):
        if state:
            self.population += value
        elif not state:
            self.population -= value

    def edit_inequalities(self, state, value):
        if state:
            self.inequalities += value
        elif not state:
            self.inequalities -= value

    def edit_happiness(self, state, value):
        if state:
            self.happiness += value
        elif not state:
            self.happiness -= value

    def edit_health(self, state, value):
        if state:
            self.health += value
        elif not state:
            self.health -= value

    def edit_finance(self, state, value):
        if state:
            self.happiness += value
        elif not state:
            self.happiness -= value

    def edit_food_limit(self, state, value):
        if state:
            self.food_limit += value
        elif not state:
            self.food_limit -= value

    def show_stats(self):
        return self.property_values

    def show_string(self):
        property_string = "Happiness     : %s%%\n" \
                          "Population    : %s / %s\n" \
                          "Low class       : %s%%\n" \
                          "Well-being    : %s%%\n" \
                          "Income/turn : FD. %s\n" \
                          "Food Limit     : %s" % (self.happiness, self.population, self.population_cap,
                                                   self.inequalities, self.health, self.finance, self.food_limit)
        return property_string


def main():
    root = Tk()
    # set the starting size of the window
    root.geometry('%dx%d' % (700, 400))
    gui = GameGUI(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
