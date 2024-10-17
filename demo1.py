import time
from logging import exception

import pyautogui

print("Hello World Demo1")

# pyautogui.click(x=100, y=100)  # 在坐标(100, 100)处执行点击操作
# pyautogui.moveTo(x=200, y=200, duration=1)  # 移动鼠标到坐标(200, 200)处，持续时间为1秒

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
print("屏幕尺寸为:" + str(screen_width) + "," + str(screen_height))

region = (1420, 126, 480, 739)

import pyautogui

# 获取当前屏幕截图并保存
pyautogui.screenshot(r"D:\MyCode\GitHub\PyAutoGUIAPPControl\targetImg\current_screenshot.png", region=region)

print("屏幕截图已保存，检查该图片与目标图片是否一致")

# 定位图像


try:
    palyAgainLocation = pyautogui.locateOnScreen(r"D:\MyCode\GitHub\PyAutoGUIAPPControl\targetImg\PlayAgain.png",
                                                 region=region, confidence=0.7)
    if palyAgainLocation is None:
        print("未能找到重新开始游戏图片位置")
    else:
        print("找到重新开始游戏图片位置: ", palyAgainLocation)
        pyautogui.moveTo(palyAgainLocation[0], palyAgainLocation[1])
        time.sleep(1)
        pyautogui.click(palyAgainLocation[0], palyAgainLocation[1])
except pyautogui.ImageNotFoundException:
    print("未能找到重新开始游戏图片位置，确认图片路径及其存在性。")

try:
    continueLocation = pyautogui.locateOnScreen(r"D:\MyCode\GitHub\PyAutoGUIAPPControl\targetImg\Continue.png",
                                                region=region, confidence=0.7)
    if continueLocation is None:
        print("未能找到继续游戏图片位置")
    else:
        print("找到继续游戏图片位置: ", continueLocation)
        pyautogui.moveTo(continueLocation[0], continueLocation[1])
        time.sleep(1)
        pyautogui.click(continueLocation[0], continueLocation[1])
except pyautogui.ImageNotFoundException:
    print("未能找到继续游戏图片位置，确认图片路径及其存在性。")

try:
    location = pyautogui.locateOnScreen(r"D:\MyCode\GitHub\PyAutoGUIAPPControl\targetImg\PlayGame.png", region=region,
                                        confidence=0.7)
    if location is None:
        print("未能找到开始游戏图片位置")
    else:
        print("找到开始游戏图片位置: ", location)
        pyautogui.moveTo(location[0], location[1])
        time.sleep(1)
        pyautogui.click(location[0], location[1])
except pyautogui.ImageNotFoundException:
    print("未能找到开始游戏图片位置，确认图片路径及其存在性。")


