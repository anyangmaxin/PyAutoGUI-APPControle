import time
from logging import exception

import pyautogui

# pyautogui.click(x=100, y=100)  # 在坐标(100, 100)处执行点击操作
# pyautogui.moveTo(x=200, y=200, duration=1)  # 移动鼠标到坐标(200, 200)处，持续时间为1秒

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
print("屏幕尺寸为:" + str(screen_width) + "," + str(screen_height))

region = (1440, 105, 475, 820)

import pyautogui

# 获取当前屏幕截图并保存
# pyautogui.screenshot(r"D:\MyCode\GitHub\PyAutoGUIAPPControl\Blum\Img\BlumScreen.png", region=region)
#
# print("屏幕截图已保存，检查该图片与目标图片是否一致")

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

# 定位图像
num = 0
target_imgs = [r"D:\MyCode\GitHub\PyAutoGUIAPPControl\Blum\Img\Blum01.png",
               r"D:\MyCode\GitHub\PyAutoGUIAPPControl\Blum\Img\Blum02.png",
               r"D:\MyCode\GitHub\PyAutoGUIAPPControl\Blum\Img\Blum03.png",
               r"D:\MyCode\GitHub\PyAutoGUIAPPControl\Blum\Img\Blum04.png"]
while True:
    for img in target_imgs:
        try:
            location_target_img = pyautogui.locateOnScreen(img,
                                                           region=region, confidence=0.6)
            if location_target_img is None:
                print("未能找到目标")
            else:
                # print("找到目标位置: ", location_target_img)
                pyautogui.click(location_target_img[0] + 1, location_target_img[1] + 1, clicks=1, interval=0.01,
                                duration=0)
                num += 1
                print("命中%d个" % num)
        except pyautogui.ImageNotFoundException:
            print("未能找到目标。")
