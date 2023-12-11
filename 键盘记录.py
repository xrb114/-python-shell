from pynput import keyboard, mouse
from loguru import logger
from threading import Thread

logger.add('monitor.log')


def on_press(key):
    logger.debug(f'键盘输出：{key} ')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def f1():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
        lsn.join()


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        logger.debug('鼠标左键点击')
    elif button == mouse.Button.right:
        logger.debug('鼠标右键点击')
        return False
    else:
        logger.debug('mid被点击')


def f2():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == '__main__':
    t1 = Thread(target=f1)
    t2 = Thread(target=f2)
    t1.start()
    t2.start()
print("down")