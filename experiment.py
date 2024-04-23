# import pyautogui
# import time


# # im=pyautogui.screenshot()
# # pxl=im.getpixel((200,200))
# # print(pxl)
# a = pyautogui.locateCenterOnScreen('02.png',region=(0,0,900,1070))
# pyautogui.click(a) #1900,1070

import pyautogui
import cv2
import time
import numpy as np

# Function to find template image in the screenshot
while True:
    def find_template(template_path, screenshot):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)  # Load template as grayscale
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        if len(loc[0]) > 0:
            return True, (loc[1][0], loc[0][0]), (loc[1][0] + w/2, loc[0][0] + h/2)
        else:
            return False, None, None

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # Convert screenshot to grayscale

    # Specify the path to the template image
    template_path = '02.png'

    # Find the template image in the screenshot
    found, top_left, bottom_right = find_template(template_path, screenshot_gray)

    if found:
        print("Template found at:", top_left, bottom_right)
        pyautogui.doubleClick(bottom_right)
        # You can perform further actions here like clicking on the found image
        # pyautogui.click(top_left[0], top_left[1])
    else:
        print("Template not found")

    time.sleep(5)
