from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
Клавиатура для выбора команды для одной новости
"""
inkb_che = InlineKeyboardButton(text="Челси", callback_data="team_челси")
inkb_mu = InlineKeyboardButton(text="Манчестер Юнайтед", callback_data="team_манчестер юнайтед")
inkb_mc = InlineKeyboardButton(text="Манчестер Cити", callback_data="team_манчестер сити")

inkb_teams = InlineKeyboardMarkup().add(inkb_che).add(inkb_mu).add(inkb_mc)


"""
Клавиатура для выбора команды для трех новостей
"""
inkb_che_three = InlineKeyboardButton(text="Челси", callback_data="three_челси")
inkb_mu_three = InlineKeyboardButton(text="Манчестер Юнайтед", callback_data="three_манчестер юнайтед")
inkb_mc_three = InlineKeyboardButton(text="Манчестер Cити", callback_data="three_манчестер сити")

# inkb_teams_three = InlineKeyboardMarkup().add(inkb_che_three).add(inkb_mu_three).add(inkb_mc_three)
inkb_teams_three = InlineKeyboardMarkup().row(inkb_che_three, inkb_mu_three, inkb_mc_three)
"""
Клавиатура для выбора номера новости (от 1 до 3)
"""
inkb_one = InlineKeyboardButton(text="#1", callback_data="number_1")
inkb_two = InlineKeyboardButton(text="#2", callback_data="number_2")
inkb_three = InlineKeyboardButton(text="#3", callback_data="number_3")

inkb_numbers = InlineKeyboardMarkup().row(inkb_one, inkb_two, inkb_three)