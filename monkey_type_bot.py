import pyautogui
import random 
from time import sleep
from selenium import webdriver

SPEED = 500

#Path to the Chrome WebDriver and the target website
PATH = 'C:\Program Files (x86)\chromedriver.exe'
WEBSITE_URL = 'https://monkeytype.com'

#Open the Chrome browser and the site
driver = webdriver.Chrome(PATH) 
driver.get(WEBSITE_URL)
sleep(2)

#Locates and collect the set of words in html format
words = driver.find_element("id","words")
sleep(1)

#Locating and clicking the cookie button 
coords = pyautogui.locateCenterOnScreen('cookie_img.png')
pyautogui.click(coords)

#monkeytype.com uses newline character instead of spaces
corrected_text = words.text.replace('\n',' ')

#type the final text
for word in corrected_text:
    sleep(random.randint(1,10)/SPEED)
    for letter in word:
        pyautogui.write(letter)
    
#repeat the process
words2 = driver.find_element("id","words")


'''

Monkeytype shows the words in sets paragraphs
but when you grab the new paragraph 
you get text from the old paragraph inside of it


like this


first   : here is some text and this is "the extra".
secondp : "the extra" this is some thing else

as you can see "the extra" repeats

so we take up until the 10th character in the firstp => "here is so"
we split this and we can get the first word => "here"

find where the first word is located in the firstp
from from that word in first p to the end is the repeated text

replace this with "" and add a space if we are a space off
'''

#same as above..replace the newline characters with spaces int he second paragraph

corrected_text2 = words2.text.replace('\n',' ')

substring = corrected_text2.split(' ')[0]

repeater = corrected_text[corrected_text.index(substring):]

corrected_text2 = corrected_text2.replace(repeater,"")

print(corrected_text2[:10])



#type away again
for index,letter in enumerate(corrected_text2):
    print(list(letter))
    sleep(random.randint(1,10)/(SPEED))
    pyautogui.write(letter)
