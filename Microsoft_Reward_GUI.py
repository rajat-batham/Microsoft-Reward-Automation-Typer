# GUI For Microsoft Reward


# Importing modules
from customtkinter import *
from PIL import Image
import time, random
import pyautogui as pg
from tkinter import messagebox
import threading
import multiprocessing
import subprocess
from pathlib import Path
import os
import sys
from pyautogui import ImageNotFoundException



# Path Function to add files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS  # when packaged by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Importing all strings as list
with open(resource_path("assets/search_list_default.txt"),"r") as a:
    data = a.read()
    data2 = data.replace("[","")
    data3 = data2.replace("]","")
    new_data = data3


# Cooldown for scroll
def cooldown(a):
    "Return Random integer from 1 to _input_"
    decimal_num = round(random.randint(1,a))
    return decimal_num

# Cooldown between typing the text in search box [to avoid suspicion]
def small_cd(a):
    "Return Random deciaml from 0.02 to _input_"
    decimal_num = round(random.uniform(0.01,a),2)
    return decimal_num

def path_taker():
    dialog = CTkInputDialog(text="Paste Path Of Browser.",title="Path Selection")
    path = dialog.get_input()
    print(path)
    return path


def browser_path_intialization():
    with open(resource_path("assets/firefox_path.txt"),"r") as firefox_path_from_file:
        firefox_path.set(firefox_path_from_file.read())
        if firefox_path.get() == "":
            firefox_select_button.configure(state="disabled")
    print(f"From File->{firefox_path.get()}")
    with open(resource_path("assets/operagx_path.txt"),"r") as operagx_path_from_file:
        operagx_path.set(operagx_path_from_file.read())
        if operagx_path.get() == "":
            operagx_select_button.configure(state="disabled")
    print(f"From File->{operagx_path.get()}")
    with open(resource_path("assets/brave_path.txt"),"r") as brave_path_from_file:
        brave_path.set(brave_path_from_file.read())
        if brave_path.get() == "":
            brave_select_button.configure(state="disabled")
    print(f"From File->{brave_path.get()}")
    with open(resource_path("assets/chrome_path.txt"),"r") as chrome_path_from_file:
        chrome_path.set(chrome_path_from_file.read())
        if chrome_path.get() == "":
            chrome_select_button.configure(state="disabled")
    print(f"From File->{chrome_path.get()}")
    with open(resource_path("assets/edge_path.txt"),"r") as edge_path_from_file:
        edge_path.set(edge_path_from_file.read())
        if edge_path.get() == "":
            edge_select_button.configure(state="disabled")
    print(f"From File->{edge_path.get()}")


def edge_path_entry():
    edge_browser_path.configure(state=NORMAL)
    edge_browser_path.configure(fg_color="#9bc987")
    edge_browser_path_save_button.place(relx=0.160,rely=0.378,anchor="n")
    edge_browser_path_button.place_forget()
def edge_path_save():
    edge_browser_path.configure(state=DISABLED)
    edge_browser_path_save_button.place_forget()
    edge_browser_path_button.place(relx=0.24,rely=0.378,anchor="n")
    edge_select_button.configure(state="normal")
    with open(resource_path("assets/edge_path.txt"),"w+") as f:
        f.write(f"{edge_path.get()}")
        print(f"Field-> {edge_path.get()}")

def chrome_path_entry():
    chrome_browser_path.configure(state=NORMAL)
    chrome_browser_path.configure(fg_color="#9bc987")
    chrome_browser_path_save_button.place(relx=0.310,rely=0.378,anchor="n")
    chrome_browser_path_button.place_forget()
def chrome_path_save():
    chrome_browser_path.configure(state=DISABLED)
    chrome_browser_path_save_button.place_forget()
    chrome_browser_path_button.place(relx=0.389,rely=0.378,anchor="n")
    chrome_select_button.configure(state="normal")
    with open(resource_path("assets/chrome_path.txt"),"w+") as f:
        f.write(f"{chrome_path.get()}")
        print(f"Field-> {chrome_path.get()}")

def brave_path_entry():
    brave_browser_path.configure(state=NORMAL)
    brave_browser_path.configure(fg_color="#9bc987")
    brave_browser_path_save_button.place(relx=0.461,rely=0.378,anchor="n")
    brave_browser_path_button.place_forget()
def brave_path_save():
    brave_browser_path.configure(state=DISABLED)
    brave_browser_path_save_button.place_forget()
    brave_browser_path_button.place(relx=0.539,rely=0.378,anchor="n")
    brave_select_button.configure(state="normal")
    with open(resource_path("assets/brave_path.txt"),"w+") as f:
        f.write(f"{brave_path.get()}")
        print(f"Field-> {brave_path.get()}")

def operagx_path_entry():
    operagx_browser_path.configure(state=NORMAL)
    operagx_browser_path.configure(fg_color="#9bc987")
    operagx_browser_path_save_button.place(relx=0.610,rely=0.378,anchor="n")
    operagx_browser_path_button.place_forget()
def operagx_path_save():
    operagx_browser_path.configure(state=DISABLED)
    operagx_browser_path_save_button.place_forget()
    operagx_browser_path_button.place(relx=0.69,rely=0.378,anchor="n")
    operagx_select_button.configure(state="normal")
    with open(resource_path("assets/operagx_path.txt"),"w+") as f:
        f.write(f"{operagx_path.get()}")
        print(f"Field-> {operagx_path.get()}")

def firefox_path_entry():
    firefox_browser_path.configure(state=NORMAL)
    firefox_browser_path.configure(fg_color="#9bc987")
    firefox_browser_path_save_button.place(relx=0.76,rely=0.378,anchor="n")
    firefox_browser_path_button.place_forget()
def firefox_path_save():
    firefox_browser_path.configure(state=DISABLED)
    firefox_browser_path_save_button.place_forget()
    firefox_browser_path_button.place(relx=0.84,rely=0.378,anchor="n")
    firefox_select_button.configure(state="normal")
    with open(resource_path("assets/firefox_path.txt"),"w+") as f:
        f.write(f"{firefox_path.get()}")
        print(f"Field-> {firefox_path.get()}")
    
def give_selected_browser_path():
    match selected_browser_tk.get():
        case "FIREFOX":
            with open(resource_path("assets/firefox_path.txt"),"r") as f:
                path = f"\"{f.read()}\""
                return path
        case "OPERA GX":
            with open(resource_path("assets/operagx_path.txt"),"r") as f:
                path = f"\"{f.read()}\""
                return path
        case "BRAVE": 
            with open(resource_path("assets/brave_path.txt"),"r") as f:
                path = f"\"{f.read()}\""
                return path
        case "CHROME":
            with open(resource_path("assets/chrome_path.txt"),"r") as f:
                path = f"\"{f.read()}\""
                return path
        case "EDGE":
            with open(resource_path("assets/edge_path.txt"),"r") as f:
                path = f"\"{f.read()}\""
                return path
        

def is_windows_app_running(process_name):
    try:
        cmd = f'tasklist /fi "imagename eq {process_name}"'
        output = subprocess.check_output(cmd, shell=True).decode()
        if process_name.lower() in output.lower():
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        print(f"Error executing tasklist command. Make sure it's available in your PATH.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

             
def active_gui_search(searchvalue,search_counter):
    """This is the main which moves Mouse & Keyboard to immitate human"""
    time.sleep(7)    
    pg.typewrite('bing.com')
    time.sleep(small_cd(0.03))
    pg.press("enter")
    time.sleep(3)
    image_list = [
        ["Bing Full Search Bar Dark.JPG",
        "Bing Full Search Bar Light.JPG"],
        ["Bing Engine Search Bar Dark.JPG","Bing Engine Search Bar Light.JPG"],
    ]

    # messagebox.showerror("Error","Image Not Found on screen!")
    screen_width, screen_height = pg.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    for i in range(searchvalue):
            search_counter = i
            for image_path in image_list[0]:
                try:
                    chords = pg.locateCenterOnScreen(f"{image_path}",confidence=0.7)
                    print("Found It")
                except ImageNotFoundException:
                    pass
                else:
                    pg.moveTo(chords,duration=0.5)
                    pg.click()
                    break
            word_list = data3.split(",")
            word = random.choice(word_list)
            word2 = word.lstrip("'")
            word_final = word2.rstrip("'")
            for letter in word_final:
                pg.typewrite(letter)
                small_cd(0.05)
            pg.press("Enter")
            time.sleep(cooldown(5))
            pg.moveTo(center_x,center_y,duration=1)
            scroll_lines = random.randrange(30,50)
            scroll_amount = random.randrange(30,70)
            for i in range(scroll_amount):
                pg.scroll(-scroll_lines)
            time.sleep(cooldown(2))
            for i in range(scroll_amount):
                pg.scroll(scroll_lines+2)
            time.sleep(cooldown(5))
            for image_path in image_list[1]:
                try:
                    chords2 = pg.locateCenterOnScreen(f"{image_path}",confidence=0.4)
                except:
                    pass
                else:
                    pg.click(chords2,duration=0.5)
            time.sleep(cooldown(3))
            pg.keyDown("Ctrl")
            for i in range(10):
                pg.press("backspace")
            pg.keyUp("Ctrl")
            print(i)
    messagebox.showinfo("Completed","Searches Completed Successfully!")
        






    


            


def start_progress_switch():
    if start_button.winfo_viewable():
        start_button.place_forget()
        progressbar.place(anchor="n",relx=0.5,rely=0.8)
        progress_text.place(anchor="n",relx=0.5,rely=0.85)
    elif progressbar.winfo_viewable():
        progressbar.pack_forget()
        progress_text.pack_forget()
        start_button.place(relx=0.5, rely=0.92, anchor="s")

def searching_and_progress():
    p1 = threading.Thread(target=Searchstart)
    p2 = threading.Thread(target=terminate_on_user_input,args=(p1,))
    p1.start()
    p2.start()

stop_event = threading.Event()

def Searchstart():
    """Main Searching Loop"""
    global search_counter,searchvalue
    try:      
        if selected_browser_tk.get() == "":
            raise IOError
        if searches.get().isnumeric() == False:
            raise ValueError
        if int(searches.get()) == 0:
            raise ValueError
        print(f"Path-> {give_selected_browser_path()}")
        subprocess.Popen(give_selected_browser_path(), creationflags=subprocess.CREATE_NEW_CONSOLE)
        # start_progress_switch() 
    except IOError:
        messagebox.showwarning("Warning","Select Browser First")
        condition_accept.deselect()
        start_button.configure(state="disabled")
    except ValueError:
        messagebox.showwarning("Warning","Please Enter Proper Search Value")
        condition_accept.deselect()
        start_button.configure(state="disabled")
    except:
        print("Please Install Browser First")
        messagebox.showwarning("Warning","Install Browser First")
        condition_accept.deselect()
        start_button.configure(state="disabled")
    try:
        searchvalue = int(searches.get())
    except:
        pass
    else:
        active_gui_search(searchvalue,search_counter)

def terminate_on_user_input(p1):
    pass
    # while True:
    #     user_input = input().lower()
    #     if user_input.lower() == "q" and user_input.lower("p"):
    #         print("Stopping worker...")
    #         stop_event.set()
    #         break



def enable_start_button():
    if terms_cond.get() == "check":
        start_button.configure(state="normal")
    else:
        start_button.configure(state="disabled")


global counter
counter = 1


def enable_string_editing():
    text_editor.configure(state='normal')
    string_save_button.configure(state='normal')
    string_edit_button.configure(state='disabled')

# Reset String To Default
def reset_strings():
    global default_string
    confirmation = messagebox.askyesno(title='RESET',message='Are you sure you want to reset strings ?')
    if confirmation==True:
        with open(resource_path("assets/search_list_default.txt"),"r") as a:
            default_string = a.read()
        with open(resource_path("assets/search_list.txt"),"w") as a:
            a.write(default_string)


# Saving new text in string editor
def save_new_text():
    global new_data
    new_data = "["+text_editor.get(1.0,END)+"]"
    print(new_data)
    with open(resource_path("assets/search_list.txt"),"w") as a:
        a.write(new_data)
    messagebox.showinfo(title='SAVED',message='Your Strings Are SAVED SUCCESSFULLY')
    text_editor.configure(state='disabled')
    string_edit_button.configure(state='normal')
    string_save_button.configure(state='disabled')
      

# Selecting Browser
def browser_selection(button):
    global edge_browser_var,brave_browser_var,chrome_browser_var,operagx_browser_var,firefox_browser_var,selected_browser,sel_browser_location,selected_browser_tk
    browser_nd_variable_list = {edge_select_button:edge_browser_var,chrome_select_button:chrome_browser_var,operagx_select_button:operagx_browser_var,firefox_select_button:firefox_browser_var,brave_select_button:brave_browser_var}
    for browserbutton in browser_nd_variable_list:
        if browserbutton == button:
            browserbutton.configure(fg_color="#38b528")
            browser_nd_variable_list[browserbutton].set("SELECTED")
        if browserbutton != button:
            browserbutton.configure(fg_color=("#D3463E","#F1F1F1"))
            browser_nd_variable_list[browserbutton].set("SELECT")
    if str(button) == ".!ctkbutton":
        selected_browser_tk.set("EDGE")
        if edge_browser_path == "":
            messagebox.showwarning("Warning","Please, Provide Browser Path!")
            edge_select_button.configure(state="disabled")
            selected_browser_tk.set("")
        elif not(os.path.exists(edge_browser_path.get())):
            messagebox.showwarning("Warning","Wrong Path!\nPlease Rectify It!")
            edge_select_button.configure(state="disabled")
            selected_browser_tk.set("")
    if str(button) == ".!ctkbutton4":
        selected_browser_tk.set("CHROME")
        if chrome_browser_path.get() == "":
            messagebox.showwarning("Warning","Please, Provide Browser Path!")
            chrome_select_button.configure(state="disabled")
            selected_browser_tk.set("")
        elif not(os.path.exists(chrome_browser_path.get())):
            messagebox.showwarning("Warning","Wrong Path!\nPlease Rectify It!")
            chrome_select_button.configure(state="disabled")
            selected_browser_tk.set("")
    if str(button) == ".!ctkbutton7":
        selected_browser_tk.set("BRAVE")
        if brave_browser_path.get() == "":
            messagebox.showwarning("Warning","Please, Provide Browser Path!")
            brave_select_button.configure(state="disabled")
            selected_browser_tk.set("")
        elif not(os.path.exists(brave_browser_path.get())):
            messagebox.showwarning("Warning","Wrong Path!\nPlease Rectify It!")
            brave_select_button.configure(state="disabled")
            selected_browser_tk.set("")
    if str(button) == ".!ctkbutton10":
        selected_browser_tk.set("OPERA GX")
        if operagx_browser_path.get() == "":
            messagebox.showwarning("Warning","Please, Provide Browser Path!")
            operagx_select_button.configure(state="disabled")
            selected_browser_tk.set("")
        elif not(os.path.exists(operagx_browser_path.get())):
            messagebox.showwarning("Warning","Wrong Path!\nPlease Rectify It!")
            operagx_select_button.configure(state="disabled")
            selected_browser_tk.set("")
    if str(button) == ".!ctkbutton13":
        selected_browser_tk.set("FIREFOX")
        if firefox_browser_path.get() == "":
            messagebox.showwarning("Warning","Please, Provide Browser Path!")
            firefox_select_button.configure(state="disabled")
            selected_browser_tk.set("")
        elif not(os.path.exists(firefox_browser_path.get())):
            messagebox.showwarning("Warning","Wrong Path!\nPlease Rectify It!")
            firefox_select_button.configure(state="disabled")
            selected_browser_tk.set("")
    
    
# String Editor Window
def string_editor():
    global counter, text_editor, string_edit_button, string_save_button
    if counter < 2:
        # Initializing Top Level Gui
        stringeditor = CTkToplevel(app)
        stringeditor.title("String Editor")
        stringeditor.resizable(0,0)
        stringeditor.grab_set()
        stringeditor.transient(app)

        # Gui Width & Height
        gui_width = 400
        gui_height = 350

        # Creating Backgorund
        background_frame = CTkFrame(master=stringeditor,width=gui_width,height=gui_height,bg_color="#32FCD4")
        background_frame.pack()

        stringeditor_heading_text = CTkLabel(background_frame,text="STRING EDITOR",font=("Anton SC",25),bg_color="#32FCD4",text_color="#EC221F")
        stringeditor_heading_text.grid(row=0,column=1,sticky="we")

        text_editor = CTkTextbox(background_frame, width=390, height=266, font=("Helvetica",15), corner_radius=2, border_color="#828282")
        text_editor.insert(0.0, new_data)
        text_editor.configure(state='disabled')
        text_editor.grid(row=1, column=1, padx=5, pady=5)

        string_edit_button = CTkButton(background_frame,text="EDIT",command=enable_string_editing, width=100, height=30, font=("Hevitas",15), corner_radius=2, bg_color="#828282",anchor="n")
        string_edit_button.grid(row=2,column=1, sticky="w",padx=15)

        string_save_button = CTkButton(background_frame,text="SAVE",state='disabled',command=save_new_text, width=100, height=30, font=("Hevitas",15), corner_radius=2, bg_color="#828282",anchor="n")
        string_save_button.grid(row=2,column=1, sticky="e",padx=15)

        string_reset_button = CTkButton(background_frame,text="RESET",command=reset_strings, width=100, height=30, font=("Hevitas",15), corner_radius=2, bg_color="#828282",anchor="n")
        string_reset_button.grid(row=2,column=1, sticky="n",padx=15)

        stringeditor.geometry(f"{gui_width}x{gui_height}")
        stringeditor.minsize(gui_width,gui_height)
        stringeditor.maxsize(gui_width,gui_height)

        # counter = 1

def search_progress():
    progressbar.set(0)
    


# GUI Window Settings
app = CTk()

app.title("Microsoft Rewards Automation")
app.resizable(0,0)
app.wm_iconbitmap(resource_path("assets/app icon.ico"))


theme = set_appearance_mode("Light")
color_theme = set_default_color_theme("green")

gui_width = 800
gui_height = 550

app.geometry(f"{gui_width}x{gui_height}")
app.minsize(gui_width,gui_height)
app.maxsize(gui_width,gui_height)


# Variables Init
search_counter = 0


# Tkinter Variables
searches = StringVar()
terms_cond = StringVar()
edge_browser_var = StringVar(app,value="SELECT")
brave_browser_var = StringVar(app,value="SELECT")
firefox_browser_var = StringVar(app,value="SELECT")
chrome_browser_var = StringVar(app,value="SELECT")
operagx_browser_var = StringVar(app,value="SELECT")

firefox_path = StringVar(app)
brave_path = StringVar(app)
operagx_path = StringVar(app)
chrome_path = StringVar(app)
edge_path = StringVar(app)
selected_browser_tk = StringVar(app)

progressbar_text_var = StringVar(app,value=f"{search_counter}/{searches.get()}")




# Top Heading
frame0 = CTkFrame(master=app,width=800,height=50,fg_color="#EC221F",corner_radius=0).pack(side="top",fill="x",anchor="n")
top_title = CTkLabel(master=frame0,text="MICROSOFT AUTOMATION TYPER",font=("Anton SC",25),bg_color="#EC221F",text_color="#32FCD4").place(relx=0.01,rely=0.001)

# Progress Bar
progressbar = CTkProgressBar(master=app,width=700,height=20,corner_radius=3)
#progressbar.place(anchor="n",relx=0.5,rely=0.8)
progress_text = CTkLabel(app, width=700, height=30,corner_radius=3,textvariable=progressbar_text_var)
#progress_text.place(anchor="n",relx=0.5,rely=0.85)


# Main Frame
frame1 = CTkFrame(master=app,width=700,height=200,corner_radius=5,fg_color="#D0C1F3",bg_color="transparent").place(anchor="n",relx=0.5,rely=0.12)

# Edge 
edge_select_button = CTkButton(master=frame1,command=lambda:browser_selection(edge_select_button),textvariable=edge_browser_var,font=("IBM Plex Mono bold",15),width=100,fg_color=("#D3463E","#F1F1F1"),bg_color="#D0C1F3",hover_color="#237a17")
edge_select_button.place(relx=0.2,rely=0.44,anchor="center")
edge_icon = CTkImage(light_image=Image.open(resource_path("assets/Edge icon.png")),size=(100,100))
edge_icon_show = CTkLabel(master=frame1,image=edge_icon,text="",bg_color="#D0C1F3").place(anchor="n",relx=0.2,rely=0.145)
edge_browser_path_button = CTkButton(master=frame1,command=edge_path_entry,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Edit]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
edge_browser_path_button.place(relx=0.24,rely=0.378,anchor="n")
edge_browser_path_save_button = CTkButton(master=frame1,command=edge_path_save,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Save]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
edge_browser_path = CTkEntry(app,width=100,height=20,textvariable=edge_path,text_color="#3F3F3F",fg_color="#B6B4B4",font=("Roboto",10),bg_color="#D0C1F3",corner_radius=0,state=DISABLED)
edge_browser_path.place(anchor="n",relx=0.2,rely=0.345)


# Chrome
chrome_select_button = CTkButton(master=frame1,command=lambda:browser_selection(chrome_select_button),textvariable=chrome_browser_var,font=("IBM Plex Mono bold",15),width=100,fg_color=("#D3463E","#F1F1F1"),bg_color="#D0C1F3",hover_color="#237a17")
chrome_select_button.place(relx=0.35,rely=0.44,anchor="center")
chrome_icon = CTkImage(light_image=Image.open(resource_path("assets/Chrome icon.png")),size=(100,100))
chrome_icon_show = CTkLabel(master=frame1,image=chrome_icon,text="",bg_color="#D0C1F3").place(anchor="n",relx=0.35,rely=0.145)
chrome_browser_path_button = CTkButton(master=frame1,command=chrome_path_entry,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Edit]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
chrome_browser_path_button.place(relx=0.389,rely=0.378,anchor="n")
chrome_browser_path_save_button = CTkButton(master=frame1,command=chrome_path_save,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Save]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
chrome_browser_path = CTkEntry(app,width=100,height=20,textvariable=chrome_path,text_color="#3F3F3F",fg_color="#B6B4B4",font=("Roboto",10),bg_color="#D0C1F3",corner_radius=0,state=DISABLED)
chrome_browser_path.place(anchor="n",relx=0.35,rely=0.345)


# Brave
brave_select_button = CTkButton(master=frame1,command=lambda: browser_selection(brave_select_button),textvariable=brave_browser_var,font=("IBM Plex Mono bold",15),width=100,fg_color=("#D3463E","#F1F1F1"),bg_color="#D0C1F3",hover_color="#237a17")
brave_select_button.place(relx=0.50,rely=0.44,anchor="center")
brave_icon = CTkImage(light_image=Image.open(resource_path("assets/Brave Icon.png")),size=(100,100))
brave_icon_show = CTkLabel(master=frame1,image=brave_icon,text="",bg_color="#D0C1F3").place(anchor="n",relx=0.50,rely=0.145)
brave_browser_path_button = CTkButton(master=frame1,command=brave_path_entry,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Edit]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
brave_browser_path_button.place(relx=0.539,rely=0.378,anchor="n")
brave_browser_path_save_button = CTkButton(master=frame1,command=brave_path_save,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Save]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
brave_browser_path = CTkEntry(app,width=100,height=20,textvariable=brave_path,text_color="#3F3F3F",fg_color="#B6B4B4",font=("Roboto",10),bg_color="#D0C1F3",corner_radius=0,state=DISABLED)
brave_browser_path.place(anchor="n",relx=0.50,rely=0.345)


# OperaGX
operagx_select_button = CTkButton(master=frame1,command=lambda: browser_selection(operagx_select_button),textvariable=operagx_browser_var,font=("IBM Plex Mono bold",15),width=100,fg_color=("#D3463E","#F1F1F1"),bg_color="#D0C1F3",hover_color="#237a17")
operagx_select_button.place(relx=0.65,rely=0.44,anchor="center")
operagx_icon = CTkImage(light_image=Image.open(resource_path("assets/Operagx icon.png")),size=(100,100))
operagx_icon_show = CTkLabel(master=frame1,image=operagx_icon,text="",bg_color="#D0C1F3").place(anchor="n",relx=0.65,rely=0.145)
operagx_browser_path_button = CTkButton(master=frame1,command=operagx_path_entry,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Edit]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
operagx_browser_path_button.place(relx=0.69,rely=0.378,anchor="n")
operagx_browser_path_save_button = CTkButton(master=frame1,command=operagx_path_save,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Save]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
operagx_browser_path = CTkEntry(app,width=100,height=20,textvariable=operagx_path,text_color="#3F3F3F",fg_color="#B6B4B4",font=("Roboto",10),bg_color="#D0C1F3",corner_radius=0,state=DISABLED)
operagx_browser_path.place(anchor="n",relx=0.65,rely=0.345)



# Firefox
firefox_select_button = CTkButton(master=frame1,command=lambda: browser_selection(firefox_select_button),textvariable=firefox_browser_var,font=("IBM Plex Mono bold",15),width=100,fg_color=("#D3463E","#F1F1F1"),bg_color="#D0C1F3",hover_color="#237a17")
firefox_select_button.place(relx=0.8,rely=0.44,anchor="center")
firefox_icon = CTkImage(light_image=Image.open(resource_path("assets/Firefox icon.png")),size=(100,100))
firefox_icon_show = CTkLabel(master=frame1,image=firefox_icon,text="",bg_color="#D0C1F3").place(anchor="n",relx=0.8,rely=0.145)
firefox_browser_path_button = CTkButton(master=frame1,command=firefox_path_entry,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Edit]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
firefox_browser_path_button.place(relx=0.84,rely=0.378,anchor="n")
firefox_browser_path_save_button = CTkButton(master=frame1,command=firefox_path_save,height=2,width=5,font=("IBM Plex Mono bold",9),fg_color="#D0C1F3",text="[Save]",text_color="#383838",bg_color="#D0C1F3",hover_color="#E6E1E1")
firefox_browser_path = CTkEntry(app,width=100,height=20,textvariable=firefox_path,text_color="#3F3F3F",fg_color="#B6B4B4",font=("Roboto",10),bg_color="#D0C1F3",corner_radius=0,state=DISABLED)
firefox_browser_path.place(anchor="n",relx=0.8,rely=0.345)



# Search Number Frame
frame2 = CTkFrame(app, width=220,height=40,fg_color="#D0C1F3",corner_radius=5,bg_color="transparent").place(anchor="w",relx=0.06,rely=0.53)
search_number_text = CTkLabel(frame2, text="Searches:",text_color="#221D1D",font=("IBM Plex Mono bold",17),bg_color="#D0C1F3").place(anchor="n",relx=0.135,rely=0.5045)
search_entry = CTkEntry(frame2, width=100,height=25,font=("Roboto",12),text_color="#3F3F3F",bg_color="#D0C1F3",fg_color="#B6B4B4",corner_radius=0,border_color="#A0A0A0",textvariable=searches).place(anchor="n",relx=0.26,rely=0.507)

# Selected Browser Info
frame5 = CTkFrame(app, width=250,height=40,fg_color="#D0C1F3",corner_radius=5,bg_color="transparent").place(anchor="n",relx=0.5,rely=0.494)
selected_browser_text = CTkLabel(frame5, text="Browser:",text_color="#221D1D",font=("IBM Plex Mono bold",17),bg_color="#D0C1F3").place(anchor="n",relx=0.41,rely=0.5045)
selected_browser_preview = CTkEntry(frame2, width=140,height=25,font=("Roboto",13),text_color="#3F3F3F",bg_color="#D0C1F3",fg_color="#C2ADF0",border_width=1,corner_radius=1,border_color="#9E9B9B",textvariable=selected_browser_tk,state="disabled")
selected_browser_preview.place(anchor="n",relx=0.555,rely=0.507)

# Edit String 
frame3 = CTkFrame(app, width=220,height=40,fg_color="#D0C1F3",corner_radius=5,bg_color="transparent").place(anchor="e",relx=0.94,rely=0.53)
edit_string_button = CTkButton(frame3, width=60
,height=30,text="EDIT",bg_color="#D0C1F3",fg_color="#6035AD",hover_color="#5718CB",font=("IBM Plex Mono bold",16),command=string_editor)
edit_string_button.place(anchor="n",relx=0.88,rely=0.503)
edit_string_text = CTkLabel(frame3, text="Edit String:",text_color="#221D1D",font=("IBM Plex Mono bold",17),bg_color="#D0C1F3").place(anchor="n",relx=0.755,rely=0.5045)


# Inststructions Frame
frame4 = CTkFrame(master=app,width=700,height=120,fg_color="#C2C2C2",corner_radius=0,bg_color="transparent").place(anchor="n",relx=0.5,rely=0.58)
instructions_text = CTkLabel(frame4,
                             text="-->  I will recommend this app to use on alternate days.\n-->  DO NOT use it consecutively for more than 3days. \n-->  Also update your search list at least every week to be undetected with minimum 5 strings (by going in search_list.py file). \n-->  If your accounts gets suspended after using this app then I am not responsible for that. I have provided the optimal use \n       above so be responsible for your any bad luck.",
                             font=("Roboto",10,"bold"),text_color="#1D1B20",bg_color="#C2C2C2",justify="left").place(anchor="n",relx=0.5,rely=0.6)
condition_accept = CTkCheckBox(frame4,checkbox_width=12,checkbox_height=12,fg_color="#6035AD",hover_color="#4300BC",corner_radius=0,border_width=1,text="I happily accept above conditions and creator will not be responsible for any damage.",text_color="#1D1B20",variable=terms_cond,bg_color="#C2C2C2",command=enable_start_button,onvalue="check",offvalue="uncheck")
condition_accept.place(anchor="n",relx=0.5,rely=0.73)


# Start Button
start_button = CTkButton(master=app,text="START SEARCH",width=350,height=40,corner_radius=5,fg_color=("#06ADAD","#834EFF"),hover_color="#797C7C",font=("Anonymous Pro",23,"bold"),state="disabled",command=searching_and_progress)
start_button.place(relx=0.5, rely=0.92, anchor="s")


# Credit Text
credit_text = CTkLabel(master=app,text="Made With      By Muffin",font=("caveat",12),text_color="#999898").place(anchor="n",relx=0.5,rely=0.95)
py_icon = CTkImage(light_image=Image.open(resource_path("assets/Python icon.png")),size=(10,10))
py_icon_show = CTkLabel(master=frame1,image=py_icon,text="",bg_color="transparent").place(anchor="n",relx=0.505,rely=0.95)


browser_path_intialization()


app.mainloop()



