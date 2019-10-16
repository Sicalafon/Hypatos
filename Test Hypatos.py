import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install("Selenium")
install("bs4")


# Coding challange:

# Test Hypatos.ai website
# Our website (https://hypatos.ai) is really simple, so we would like to check
# whether on everypage, when we scroll down, we can see Request a Demo in
# the right upper corner of the page:
# 1. Write a script that checks on main page whether it holds true.

# -please use FindDemo()

# 2. Extend the script to cover the subpages Request a Demo.

# -please use FindDemo()

# 3. Write a script that extracts the name and surname of our VP of Machine
# Learning.

# -please use FindPresident()

# 4. How would you write this task in a form of a test scenario.

# Requirements: Windows, Python 3.7, Google Chrome (latest version) , Chrome Web Driver-
# download ChromeDriver from https://chromedriver.chromium.org/downloads
# and save it into the local computer

# External Libraries - BeautifullSoup4, Selenium


def FindLinks(URL):  # Insert your URL to extract

    # Function which extracts all links from the URL to the list

    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    links_list = []
    html = urlopen(URL)
    bsObj = BeautifulSoup(html.read(),features="lxml");

    for link in bsObj.find_all('a'):
        links_list.append(link.get('href'))

    return links_list


def FindDemo(URL='https://hypatos.ai',chrome_driver= r'C:\\'): # Insert your URL and path to chromedriver


    # Autor: Bartosz Tyrała 2019-10-15
    # Output: Console
    # Function which checks on everypage of whether it holds Request a Demo Button
    # on the right upper corner of the page after it scrolls down.
    # Parameters - URL to search, path to chromedriver
    # Please install Google Chrome and download ChromeDriver First from https://chromedriver.chromium.org/downloads

    from selenium import webdriver
    import time

    AllLinks = FindLinks(URL)

    for link in AllLinks:
        browser = webdriver.Chrome(executable_path=chrome_driver)
        # browser.minimize_window()
        browser.get(link)
        try:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            print(link + ": there is no possibility to scroll down")

        time.sleep(3)
        try:
            request_demo = browser.find_element_by_xpath("/html/body/header/div/div/div/nav/button")
            print("Correct " + link + ": " + request_demo.text + " on the right upper corner after scrolling down.")
        except:
            print(link + ": No request demo")

        browser.quit()

def FindPresident(URL, pattern, sensitiveness, analysis_type='only result'):

    # Autor: Bartosz Tyrała 2019-10-15
    # Output: Console
    # Function which search for specific pattern inside of liked sites
    # Parameters - URL, regex pattern please refer to https://regexr.com/
    # sensitiveness: represents number of letters around matched pattern
    # analysis_type: by default only result of matched condition, if you change
    # analysis type this function should show all results of the search

    import re
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    List_of_Links = FindLinks(URL)

    for Link in List_of_Links:
        try:

            html = urlopen(Link)
            soup = BeautifulSoup(html.read(),features="lxml")
            text = soup.get_text()
            text_without_space = " ".join(text.split())



            r1 = re.search(pattern,text_without_space)
            if r1 != None:
                VP_position = r1.span()[0]
                print(Link + " >> The name of VP of MachineLearning is probably: " + text_without_space[VP_position-sensitiveness[0]:VP_position+sensitiveness[1]])
            else:
                if analysis_type != 'only result':
                    print(Link + ": there is no pattern")

        except:
            if analysis_type != 'only result':
                print(Link + ": some problem occurred with parsing website")
                continue

print("-----------STARTING TASK 1: Find Request a Demo---------------")
print("-Please do not interrupt Google Chrome until it ends its work-")
try:
    FindDemo(URL='https://hypatos.ai', chrome_driver=r"C:\Users\Bartosz.Tyrala\Desktop\Ladowacz do GUS\chromedriver.exe")
    print("-----------DONE-----------")
except:
    print("TASK 1: Something went wrong.")


print("-----------STARTING TASK 2: Find a VP-----------")

try:
    FindPresident(URL='https://hypatos.ai' ,pattern = 'VP.*Machine.*Learning',sensitiveness = [15,5])
    print("-----------DONE-----------")
except:
    print("TASK 2: Something went wrong.")