'''
This is a first automation project to automate microsoft search rewards on pc
Browser: Chromebrowser
'''


# importing modules
import time, random
import pyautogui as pg 
from AppOpener import open,close

# Cooldown between typing the text in search box [to avoid suspicion]
def text_cd(a):
    decimal_num = round(random.uniform(0.01,a),2)
    return decimal_num

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
    'Is is worth','apple air','galaxy pro max','write down','big dawgs','cocomelon','most viewed channel on yt','most viewed video on yt'
    
    ]

# Giving prompt to enter number of searches
searches = int((pg.prompt('Enter number of Searches\n[Preferred - 50]')))

# Asking confirmation to not interrupt in between
pg.confirm("Do not interrupt the proccess in between\nto avoid any account ban issue.\nI do not give gurantee about your account,\nit may get suspended...\nDo you copy?")

# Opening microsoft edge with a cooldown
time.sleep(2)
open('Microsoft Edge')
time.sleep(2)

# Searching loop with list above
for i in range(searches):
    pg.write(text[random.randint(0,(len(text)-1))], interval=text_cd(0.7))
    time.sleep(random.randint(1,3))
    pg.press('enter')
    time.sleep(random.randint(3,7))
    pg.typewrite('/')
    time.sleep(0.5)
    pg.press('backspace')
    time.sleep(2)

# Closing after search
close('Microsoft Edge')
time.sleep(2)
pg.alert(f'Process Completed with {searches} searches')



