# Libaries needed
import pyautogui
import win32api
from tkinter import *
from PIL import Image

def main():

    def MouseWheelHandler(event):
        """ This function is used to make scroll wheel functional, count is zero as at each rest point scroller is at base so to go up it needs 
        to be positive 1 and to go down it is negative 1 """

        count = 0
        def delta(event):
            if event.num == 5 or event.delta < 0:
                return -1 
            return 1 

        count += delta(event)
        
        # For Debugging purpose
        # print(count)

        C.yview_scroll(-count, "units")

        # To avoid fading of pallets
        main_window.wm_geometry("431x1000")



    def color_checker():
        """ This function uses the pyautogui to get the position of mouse and as well as take a screenshot of window to pick color from."""
        x, y = pyautogui.position() # Getting position of mouse
        screen = pyautogui.screenshot() # Screenshots current window
        pix = screen.load()

        # For Debugging purpose
        # print(screen.size)  # Window size
        # print(pix[x,y]) # RBG Value

        return pix[x, y] # Returning r g b value

    def rgb_hex(r, g, b):
        """ This function converts rbg to hex """
        rgb = (r, g, b)
        return '%02x%02x%02x' % rgb #Returns hex value without #
        

    def rgb_hsv(r, g, b):
        """ This function converts rgb to hsv """

        r, g, b = r / 255.0, g / 255.0, b / 255.0
    
        # h, s, v = hue, saturation, value

        cmax = max(r, g, b)  
        cmin = min(r, g, b)    
        diff = cmax-cmin       
    

        if cmax == cmin:
            h = 0
        

        elif cmax == r:
            h = (60 * ((g - b) / diff) + 360) % 360
    
 
        elif cmax == g:
            h = (60 * ((b - r) / diff) + 120) % 360
    

        elif cmax == b:
            h = (60 * ((r - g) / diff) + 240) % 360
    

        if cmax == 0:
            s = 0
        else:
            s = (diff / cmax) * 100
    
        v = cmax * 100
        v = round(v, 5)

        return h, s, v


    def color_picked():
        """ This function use the picked colour and use the rgb format to get other format and create a entry in window in pallete style. """

        r, g, b = color_checker()
        h, s, v = rgb_hsv(r, g, b) # Getting h s v value
        colorHex = rgb_hex(r, g, b) # Getting hex value

        # For Debugging Purpose
        # print(r, g, b)
        # print(h, s, v)
        # print(colorHex)

        displayString = "r = %f, g = %f, b = %f \nh = %f, s = %f, v = %f \nHex Value = #"%(r, g, b, h, s, v)
        displayString += str(colorHex)
        
        # Creating Pallet
        
        Height = 100
        Width = 400

        global PalletCount

        Label_hold = Listbox(master = frame, width = Width, height=Height)
        Label_hold.grid(row = PalletCount)

        Label_Main = Label(master = Label_hold)

        Label_Color = Label(master = Label_Main)
        Color_Canvas = Canvas(master = Label_Color, width = Width, height = Height)
        Color_Canvas.create_rectangle(2, 2, Width - 10, Height, fill="#"+str(colorHex))
        Color_Canvas.grid(row = 0)
        Label_Color.grid(row = 0)


        Label_Text = Label(master = Label_Main, text=displayString)
        Label_Text.grid(row = 1)

        Label_Main.grid()

        Label_Main.focus_displayof()

        PalletCount += 1

        # For Debugging 
        # print(PalletCount)
        


    # Main GUI window

    main_window = Tk()
    titlephoto = PhotoImage(file='pics/titlep.png')
    main_window.iconphoto(False, titlephoto)
    main_window.geometry("430x1000")
    main_window.title("UCP (alt+ctrl+leftClick : pick)")


    # Canvas creation
    C = Canvas(master=main_window, width=400, height=100000)
    C.configure(scrollregion=(0,0,410,100010))
    C.pack(side=LEFT, expand = True, fill = BOTH)

    # Frame creation
    frame = Frame(master = C, width = 400, height = 100000)
    frame.pack()

    # Window 
    C.create_window((0,0), window = frame, anchor = NW)

    # Scroll bar
    scroll = Scrollbar(master=main_window, orient=VERTICAL, command=C.yview)
    scroll.pack(side=RIGHT, fill=Y)

    # Attaching canvas to scroll bar
    C.configure(yscrollcommand=scroll.set)

    # Scroll binding for windows and linux
    main_window.bind("<MouseWheel>",MouseWheelHandler)
    main_window.bind("<Button-4>",MouseWheelHandler)
    main_window.bind("<Button-5>",MouseWheelHandler)

    # Pallet Count
    global PalletCount
    PalletCount = 0

    # Creating while loop without using while 

    def hotkey():

        # using virtual key to get state of the required key in the hotkey
        used = False
        
        if win32api.GetKeyState(0x12) < 0 and win32api.GetKeyState(0x11) < 0 and win32api.GetKeyState(0x01) < 0: #alt+ctrl+leftClick
            
            #print("CLicked") for debugging
            
            color_picked()
            keycheck.after(240, hotkey) # This delay is longer to make sure same color does not flood pallete due to human reaction time 
            used = True

          

        # "Used" is to change the delay since if there no hotkey press was done check every 10 ms to not miss any hotkey input
        if not used:
            keycheck.after(10, hotkey)
        

        # To Avoid fading of Pallets
        main_window.wm_geometry("430x1000")


    # label to create the loop not a visible entity
    keycheck = Label(master = main_window)
    keycheck.pack()

    # Initial Call of loop
    hotkey()


    # End of mainloop
    main_window.mainloop()
