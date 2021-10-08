from logic_tokped import Tokopedia

# ----------------------------------Tokopedia---------------------------------------------- #
driver_path = "C:\Development\chromedriver.exe"

bot = Tokopedia(driver_path)
bot.login_tokopedia()
bot.find_item()