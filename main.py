
import asyncio
from rashmi.parser import ParseEntryFile
from rashmi.names2Urls import GetUrlFromNameLst, WriteUrlsFile 
from rashmi.urls2Count import GetStaffCountFromUlrNameNest, WriteCounts2File
 
async def main():
  
    """
    1. Give a CSV file of company names, create a python module that can find
    LinkedIn URLs for those companies.
    """
    lst_companyNames, fileName, email , password = ParseEntryFile()
    print(f"FileName: {fileName}")


    
    for item in lst_companyNames:
        print(item)


    task = asyncio.create_task(GetUrlFromNameLst(lst_companyNames))
  
    nest_NameUrls = await task 
   
    for entry in nest_NameUrls:
        print(entry)
    
    """
    The LinkedIn URLs should be stored as a
    CSV file.
    """
    WriteUrlsFile(nest_NameUrls,fileName)


    """
    And once that is done, extend the script using Playwright browser
    to find the employee count from LinkedIn 
    """
    
    task2 = asyncio.create_task(GetStaffCountFromUlrNameNest(nest_NameUrls,email,password))
  

    nest_NameCount = await task2 
   
    for entry in nest_NameCount:
        print(entry)
    
    """
    and store it in the original file
    alongside the Company Names.
    """
    WriteCounts2File(nest_NameCount,fileName)

#if __name__ == "main":
asyncio.run(main())