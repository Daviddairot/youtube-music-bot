from selenium import webdriver
import time
import random
import tkinter.font as tkFont
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

root  = tk.Tk()
def bot():
    t = int(times.get())
    for i in range(t):
        # Path to Tor Browser executable (firefox.exe)
        tor_browser_path = "C:/Users/DAIRO/Desktop/Tor Browser/Browser/firefox.exe"  # Update with your path

        # Configure Firefox options
        firefox_options = webdriver.FirefoxOptions()

        # Set the binary location of the Tor Browser executable
        firefox_options.binary_location = tor_browser_path

        # Create a WebDriver instance with the configured options
        driver = webdriver.Firefox(options=firefox_options)

        time.sleep(3)

        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

        time.sleep(18)
        song_title = url_entry.get()
        search_url = f"https://music.youtube.com/search?q={song_title}"
        driver.get(search_url)


        time.sleep(10)
        try:
            wait = WebDriverWait(driver, 10)
            button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Accept all"]')))
            button_element.click()
        except:
            pass
        # Wait for the search results to load
        time.sleep(7)
        print("i have been passed")

        # Click on the first search result to play the song
        wait = WebDriverWait(driver, 10)
        button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="PLAY ALL"]')))
        button_element.click()

        # Wait for the song to 

        # Your Selenium actions here...
        time.sleep(random.randint(20, 90))
        # Close the browser
        driver.quit()


root.title("youtube music bot")
root.geometry("400x200")
root.overrideredirect(False)
root.resizable(False, False)
root.config(bg="black")
icon_path = "C:/Users/DAIRO/Desktop/chromeatt/image.ico"
root.iconbitmap(icon_path)


custom_font = tkFont.Font(family="Times New Romans", size=9, weight="bold")

board = tk.Frame(root, background="lime", height="160", width="350")
board.place(x=25,y=16)

board = tk.Frame(root, background="black", height="158", width="348")
board.place(x=26,y=17)

url = tk.Label(root, font=custom_font, text = "Enter your title", background="black",foreground= "lime")
url.place(x  = 154, y = 30)
url_entry =  tk.Entry(root, width = 40)
url_entry.place(x  = 85, y = 50)

ts = tk.Label(root, font=custom_font, text = "Enter number of times you want to run it", background="black",foreground= "lime")
ts.place(x  = 90, y = 75)
times = tk.Entry(root, width = 17)
times.place( x = 145, y = 100)

start_btn = tk.Button(root, text = "Start", command = bot, background="black",foreground= "lime")
start_btn.place(x  = 180, y = 130)

root.mainloop()
