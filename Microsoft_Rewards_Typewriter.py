'''
This is a first automation project to automate microsoft search rewards on pc
 ~ Browser supported: Microsoft Edge, Tor, Opera GX, Chrome
 ~ Still Non GUI {Will add soon}
 '''

# importing modules & files
import time, random
import pyautogui as pg 
from AppOpener import open,close
import mouse
# from search_list.txt import search_list_list

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

def mouse_middle_clicked():
    if mouse.is_pressed("middle") == True:
        cancel = False
        pg.alert(title="Cancelled",text="Process Aborted By User")
        raise InterruptedError("Process Aborted By User")
    

# Add search item in this list 
text = [
    'compaq','digita crime','digital arrest','date','date today','next valorant update','dell optix','syrotech','net logs','import duty',
    'ali baba','aliexpress','random module','module in python','colgate','random module','encourage','jack of all trades','tony robbins',
    'financial literacy','meta','facebook pexels','wings','micrrosoft','microsoft rewards','optimumtech','thomas shelby','vga','resolution',
    'ration best for monitors','ultra wide monitors','mrwhoistheboss','python latest updates','nvidia next gpu','amd next launches','twitch',
    'next cs2 major','cs2 teams from india','death bed part 2','bandar mama','fairy tails','shi ching ping','espresso','get paid',
    'falling','oops','cool python projects','notes books','list','dictionaries','asus rog','steam deck','steam','epic games','steam db',
    'what is arm 64','mechanical keyboard','cs2 drops rate','gta online best cars to get','japanese culture','beauty of asia','elon musk',
    'I love india','Independece day of America','Pylance','Is C hard','Is C++ Easy ?','Latest laptops','Rockstar games',
    'GTA online new update','red dead redemption 2','RDR 2','Business in gta','Friday AI','Iron man in real life',
    'New cars in india','New GPU in India','Next CES date','RTX 2060','Ryzen 5 5500','DDR4 16Gig ram','RGB PC','Game nation',
    'Modx computers','MD computers','Techpc7 store','Gaming PC','Asus tuf','Budget gaming gpu','Budget gaming pc','Pm of china',
    'Is is worth','apple air','galaxy pro max','write down','big dawgs','cocomelon','most viewed channel on yt','most viewed video on yt',
    'Entropy','Anthalpy','Python Functions','PyQT','Make Mobile Applications','Pyton GUI modules','Easy GUI','CSS vs PyQT','Python vs Javascript',
    'Internal Energy'
    
    ]



if __name__ == "__main__":


    # Asking confirmation to not interrupt in between
    condition1 = pg.confirm(title='Acknoledgement',text="Do not interrupt the proccess in between\nto avoid any account ban issue.\nI do not give gurantee about your account,\nit may get suspended...\nDo you copy?")
    condition2 = pg.confirm(title='Warning',text="Make sure to update your search list weekly with atleast 5 or more strings to avoid detection.")
    
    # If User Cancel Action
    if condition1 == "Candel" or condition2 == "Cancel":
        raise InterruptedError("Accept Conditions to proceed further")


    # Giving prompt to enter number of searches
    searches = int((pg.prompt(title='Searches',text='Enter number of Searches\n[Preferred - 35]')))

    # Dialog Box For Confirmation Of Browser
    browser = pg.confirm(title='Browser',text="Choose The Browser", buttons=['CHROME','EDGE','OPERA GX','TOR'])

    # Giving Browser Names
    if browser == 'CHROME':
        browser_name = "Google Chrome"
        try:      
            open(browser_name,throw_error=True)
        except:
            print("Please Install Browser First")
            raise InterruptedError("Browser Doesn't Exist")
    if browser == 'EDGE':
        browser_name = "Microsoft Edge"
        try:      
            open(browser_name,throw_error=True)
        except:
            print("Please Install Browser First")
            raise InterruptedError("Browser Doesn't Exist")
    if browser == 'OPERA GX':
        browser_name = "Opera GX Browser"
        try:      
            open(browser_name,throw_error=True)
        except:
            print("Please Install Browser First")
            raise InterruptedError("Browser Doesn't Exist")
    if browser == 'TOR':
        browser_name = "Tor"
        try:      
            open(browser_name,throw_error=True)
        except:
            print("Please Install Browser First")
            raise InterruptedError("Browser Doesn't Exist")
   

    # Getting Monitor Size
    screen_size = pg.size()

    # Moving Mouse To Middle Of Screen
    current_mouse_pos = pg.position()
    pg.moveTo(2,2, 2)
    pg.moveTo(screen_size[0]//2, screen_size[1]//2, 2)

    time.sleep(3)
    mouse_middle_clicked()

    cancel = True
    # Searching loop with list above
    while cancel == True:
        for i in range(searches):
            mouse_middle_clicked()
            pg.write(text[random.randint(0,(len(text)-1))], interval=small_cd(0.7))
            mouse_middle_clicked()
            time.sleep(cooldown(3))
            mouse_middle_clicked()
            pg.press('enter')
            random_cd = small_cd(1)
            mouse_middle_clicked()
            if random_cd<0.03:
                mouse_middle_clicked()
                for i in range(30,random.randint(30,111)):
                    mouse_middle_clicked()
                    time.sleep(small_cd(0.1))
                    mouse_middle_clicked()
                    pg.scroll(-random.randint(20,150),x=250,y=250)
                    mouse_middle_clicked()
                for i in range(30,random.randint(30,111)):
                    mouse_middle_clicked()
                    time.sleep(small_cd(0.1))
                    mouse_middle_clicked()
                    pg.scroll(random.randint(20,150),x=250,y=250)
                    mouse_middle_clicked()
            mouse_middle_clicked()
            time.sleep(cooldown(4))
            mouse_middle_clicked()
            pg.typewrite('/')
            mouse_middle_clicked()
            time.sleep(0.5)
            mouse_middle_clicked()
            pg.press('backspace')
            mouse_middle_clicked()
            time.sleep(2)
            mouse_middle_clicked()

    # Closing after search
    close(browser_name)
    time.sleep(2)
    pg.alert(title="FINISHED",text=f'Process Completed with {searches} searches')



