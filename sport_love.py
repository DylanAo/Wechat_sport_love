import pyautogui
import time


def me():
    # 如果没人给你点赞进入这里
    # 不会真的没人给你点赞吧
    # 不会吧，不会吧
    # 没人给你点赞你还给别人点什么
    time.sleep(0.5)
    if pyautogui.locateOnScreen('none.png', confidence=0.90):
        left, top, width, height = pyautogui.locateOnScreen('back.png', confidence=0.90)
        center = pyautogui.center((left, top, width, height))
        pyautogui.click(center)
        pyautogui.moveRel(0, 100)  # 向下移一下，要不然不能滑动
        pyautogui.scroll(-1000)
        print('没人给你点赞真可怜')
        return True
    else:
        return False


def dian_zan():
    time.sleep(0.5)
    try:
        left, top, width, height = pyautogui.locateOnScreen('heart.png', confidence=0.90)
    except TypeError:  # 这里不加可能会抛出异常，我也不知道为什么
        print("不是，我怎么没找到")
    center = pyautogui.center((left, top, width, height))
    pyautogui.click(center)
    me()


scroll_num = 0
while True:
    if pyautogui.locateOnScreen('heart.png', confidence=0.90):
        dian_zan()
        print('点赞了')
        scroll_num = 0
    else:
        pyautogui.moveRel(0, -10)  # 先向上移动一下，防止出去屏幕
        pyautogui.scroll(-1000)  # 没找到滚动鼠标
        scroll_num += 1
        if scroll_num == 2:
            try:
                left, top, width, height = pyautogui.locateOnScreen('over.png', confidence=0.90)
            except TypeError:
                print('看来还没到最后啊')
                continue
            break
print('点完了')