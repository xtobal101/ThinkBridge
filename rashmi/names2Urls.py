import csv
import time
from bs4 import BeautifulSoup as bs 
from playwright.async_api import Playwright, async_playwright, expect

def WriteUrlsFile(lstOfEntries, fileName = ""):
    """
    The LinkedIn URLs should be stored as a
    CSV file.
    """

    fileName = fileName+".urls.csv"
    fields = ['Name', 'Url']
    # fields = ['Url'] ###-> I decided to add the Name column to the Url column to make file usefu
    with open(fileName,'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fields)
            writer.writeheader()
            for entry in lstOfEntries:
                writer.writerow(entry)



async def run_getUrlFromName(playwright: Playwright, name: str) -> str:
    foundUrl = "not_found"
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.google.com/ncr")
    await page.get_by_role("combobox", name="Search").click()
    await page.get_by_role("combobox", name="Search").fill(f"linkedIn {name}")
    await page.get_by_role("combobox", name="Search").press("Enter")
    time.sleep(1)
  

    html = await page.content()
    soup = bs(html, 'html.parser')

    
    allData = soup.find_all("div",{"class":"g"})
    g=0
    Data = []
    l={}
    foundUrl = "UnableToFind"
    for i in range(0,len(allData)):
        link = allData[i].find('a').get('href')

        if(link is not None):
            if(link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
                g=g+1
                l["link"]=link
                try:
                    l["title"]=allData[i].find('h3').text
                except:
                    l["title"]=None  

                try:
                    l["description"]=allData[i].find("span",{"class":"aCOpRe"}).text
                except:
                    l["description"]=None 

                l["position"]=g 

                Data.append(l)  

                l={}   

            else:
                continue 

        else:
            continue

        foundUrl ="notfound" 
        for item in Data: #filter local results that include '?' 
            if '?' not in item["link"] and '//www.' in item["link"]:
                foundUrl = item["link"]
                break
            
    print(foundUrl)
    return foundUrl


    # ---------------------
    await context.close()
    await browser.close()


async def GetUrlFromNameLst(nameLst:list) -> list:
    outNest = []
    async with async_playwright() as playwright:

        for name in nameLst:
            time.sleep(1)
            url = await run_getUrlFromName(playwright, name)
            outNest.append({"Name":name, "Url": url})

    return outNest 

    