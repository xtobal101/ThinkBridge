import time
import re
import csv

from playwright.async_api import Playwright, async_playwright, expect
from bs4 import BeautifulSoup as bs


def WriteCounts2File(lstOfDict, fileName = "companies.csv"):

    fields = ['Name', 'Count']
    #try:
    with open(fileName,'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fields)
            writer.writeheader()
            for item in lstOfDict:
                writer.writerow(item)





async def run_getStaffCountFromUrl(playwright: Playwright, in_nest:list, email:str, password:str) -> list:
    out_nest = []
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.linkedin.com/login")
    await page.get_by_label("Email or Phone").click()
    await page.get_by_label("Email or Phone").fill(f"{email}")
    await page.get_by_label("Email or Phone").press("Tab")
    await page.get_by_label("Password").fill(f"{password}")
    await page.get_by_role("button", name="Sign in", exact=True).click()
    time.sleep(1)


    for entry in in_nest:
        await page.goto(entry['Url'])
        time.sleep(2) 
        html = await page.content()
        soup = bs(html, 'html.parser')
            
        search_term = "employees"

        #with open(f"result{entry['Name']}.html", "w", encoding='utf-8') as file:
            #file.write(str(soup))


  

        number =-1 #"Not found"
        div = soup.find(class_="ember-view org-top-card-summary-info-list__info-item")
        if div:
            items = div.find_all(string=re.compile(search_term))
            if len(items)>0:
                
                numberList = re.findall(r'\b\d+\b',items[0])
                number = ''.join(numberList) #"join individual numbers to form a single integer"

        if number == -1:
            print("not found")
        else:    
            print(number)
    
        out_nest.append({"Name":entry["Name"], "Count":number})

    await context.close()
    await browser.close()

    return out_nest



async def GetStaffCountFromUlrNameNest(in_nest:list, email:str, password:str) -> list:
    outNest = []
    async with async_playwright() as playwright:
            time.sleep(1)
            outNest = await run_getStaffCountFromUrl(playwright,in_nest,email,password)
    return outNest 