import pyautogui as GUI
import time


def open_fiji():
    GUI.hotkey('win')
    GUI.press('space')
    GUI.typewrite('ImageJ-win64', interval=0.25)
    GUI.press('enter')
    time.sleep(5)


def find_console():
    # console = GUI.locateCenterOnScreen(r'C:\ninja\Project\Fiji_console.png', confidence=0.9)
    console = GUI.locateCenterOnScreen('./image/fiji_console.png', confidence=0.9)
    GUI.moveTo(*console, duration=1)
    GUI.click()
    GUI.hotkey('alt', 'f4')  # close Fiji console


def find_app_fiji():
    fiji = GUI.locateCenterOnScreen('./image/Fiji_main.png', confidence=0.9)
    for loc in fiji:
        print(loc)
    GUI.moveTo(*fiji, duration=0.5)
    fijiX, fijiY = GUI.position()
    GUI.moveTo(fijiX, fijiY - 50, duration=0.5)
    GUI.click()


def find_menu_plugin():
    print('open plugins')
    fiji = GUI.locateCenterOnScreen('./image/menu_Plugins.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_menu_file():
    print('open file')
    fiji = GUI.locateCenterOnScreen('./image/menu_File.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_menu_edit():
    print('open edit')
    fiji = GUI.locateCenterOnScreen('./image/menu_Edit.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_menu_image():
    print('open image')
    fiji = GUI.locateCenterOnScreen('./image/menu_Image.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_menu_process():
    print('open process')
    fiji = GUI.locateCenterOnScreen('./image/menu_Process.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_menu_analyze():
    print('open analyze')
    fiji = GUI.locateCenterOnScreen('./image/menu_Analyze.png', confidence=0.9)
    GUI.moveTo(*fiji, duration=0.5)


def find_plugin_trackmate():
    for i in range(35):
        GUI.press('down')
        time.sleep(0.25)
    GUI.press('right')
    for i in range(3):
        GUI.press('down')
        time.sleep(0.25)


if __name__ == '__main__':
    print('starting Fiji automation...')
    open_fiji()
    find_console()
    time.sleep(2)
    find_app_fiji()
    find_menu_file()
    find_menu_edit()
    find_menu_image()
    find_menu_process()
    find_menu_analyze()
    find_menu_plugin()
    GUI.click(button='left')
    time.sleep(1)
    find_plugin_trackmate()
    GUI.press('enter')
