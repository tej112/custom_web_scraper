from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com/")
driver.implicitly_wait(20)
num = True
with open("quotes.csv", 'w') as csvfile:
    csvfile.write("Author,Quote\n")

while num:
    quotes = driver.find_elements(by=By.CLASS_NAME, value="text")
    quotes = [quote.text for quote in quotes]
    author_names = driver.find_elements(by=By.CLASS_NAME, value="author")
    author_names = [author.text for author in author_names]

    next_button = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/nav/ul/li/a")
    if next_button.text == "Next →":
        next_button.click()
    else:
        try:
            next_button = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/nav/ul/li[2]/a")
            next_button.click()
        except Exception as e:
            # print(e)
            num = False
            pass
    for quote, author_name in zip(quotes, author_names):
        with open("quotes.csv", 'a') as csvfile:
            csvfile.write(author_name + "," + quote + "\n")


driver.quit()