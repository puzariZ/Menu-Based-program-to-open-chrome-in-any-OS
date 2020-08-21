import time
import os
import webbrowser
import platform

user_OS = platform.system()
chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
chrome_path_linux = '/usr/bin/google-chrome %s'
chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
chrome_path = ''
game_site_link = 'https://www.instagram.com/xesthetic_avii/'

if user_OS == 'Windows':
    chrome_path = chrome_path_windows
elif user_OS == 'Linux':
    chrome_path = chrome_path_linux
elif user_OS == 'Darwin':
    chrome_path = chrome_path_mac
else:
    webbrowser.open_new_tab(game_site_link)

webbrowser.get(chrome_path).open_new_tab(game_site_link)