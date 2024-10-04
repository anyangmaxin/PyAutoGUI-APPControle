import pyautogui

print("Hello World Demo1")

pyautogui.click(x=100, y=100)  # 在坐标(100, 100)处执行点击操作
pyautogui.moveTo(x=200, y=200, duration=1)  # 移动鼠标到坐标(200, 200)处，持续时间为1秒
