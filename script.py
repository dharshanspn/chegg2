from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# Define functions to send messages via Telegram
def telegram_bot_sendques(bot_message):
    bot_token = '6283203048:AAGgOl-o6Itm3D1mw4_Omcf-g4t260vixN8'
    bot_chatID = '1155462778'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()

def telegram_bot_sendtext(bot_message):
    bot_token = '6151330973:AAHuzkvwRjN9MfaFZ0LiiNUNdI0bgZqppQk'
    bot_chatID = '1155462778'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()


# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Open the Chegg website and log in
driver.get("https://expert.chegg.com/auth")
time.sleep(3)

#print(driver.find_element(By.XPATH, "/html/body").text)

# Username
element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/div[1]/div[2]/div/div/input")  # Replace with the correct XPath
element.send_keys("nirupeshcs@icloud.com")
element.send_keys(Keys.ENTER)
time.sleep(3)

# Password
passw = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/form/div[1]/div[2]/div[2]/div/div/input")  # Replace with the correct XPath
passw.send_keys("#Hitlin3945")
passw.send_keys(Keys.ENTER)
time.sleep(3)

telegram_bot_sendtext("Logged CSN")

# Navigate to the authoring page
driver.get("https://expert.chegg.com/qna/authoring/answer")
time.sleep(3)

i = 1
while True:
    try:
        driver.get("https://expert.chegg.com/qna/authoring/answer")
        time.sleep(8)
        message = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[1]")
        text_to_copy = message.text
        if text_to_copy == "Thank you for your efforts on Chegg Q&A! Unfortunately, no Qs are available in your queue at the moment.":
            driver.refresh()
            if i <= 1:
                telegram_bot_sendtext(i)
            elif i % 100 == 0:
                status = f"UP Running...  {i/10} CSN"
                telegram_bot_sendtext(status)
            i += 1
        else:
            telegram_bot_sendques("CSN")
            time.sleep(660)
    except Exception as e:
        telegram_bot_sendtext("An error occurred CSN")
# Quit the WebDriver
driver.quit()
