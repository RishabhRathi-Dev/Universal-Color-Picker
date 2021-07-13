# About
Universal Color Picker is project aimed to create a color picker tool for artist, which works on whole window (not bounded by the boundaries of software) and create a selected color pallet with their rgb, hsv and hex value. If you want to run this then the start script is entry.py

# Working 
When the hotkey (alt+ctrl+LeftClick) is pressed, program takes screenshot of screen (_Screenshot is not saved_) while noting the position of cursor. Using pillow library program finds out the rgb value of the pixel at which cursor was pointing. With this rgb, We can easily find out hex and hsv value. This color is then displayed in pallet style in the program window with rgb, hsv and hex value. Program can hold approx 400 colors each session. There is currently no method to save the pallet, each session starts with blank window.

# Pictures
| At Start | After Few Entries |
| :---------: |:------------------: |
|![startpic](https://github.com/RishabhRathi-Dev/Universal-Color-Picker/blob/main/pics/startpic.jpg)|![AfterPic](https://github.com/RishabhRathi-Dev/Universal-Color-Picker/blob/main/pics/aftercollectionpic.jpg)|


# Technologies
This project is built using Python 3.9.1. Following libaries were used:
* pyautogui
* win32api
* tkinter
* pillow

## pyautogui
This library is used to take screenshot of window and find the current position of cursor.

## win32api
This library is used to create hotkey (alt+ctrl+LeftClick).

## tkinter
This library is the base of the project as it is used to make the GUI for the project.

## pillow
From this library only Image is used for titlephoto.

# Challenges
Few challenging tasks faced during this project:
* Making scroll function to work with scroll wheel
* Making executable of this project
