# ThinkBridge

Read the following to run the solutions...

Requirements:
1. Give a CSV file of company names, 
 
 [.\companies.csv] 
 
 create a python module that can find LinkedIn URLs for those companies 
 
  [
   from rashmi.names2Urls import GetUrlFromNameLst, WriteUrlsFile 
  ]. 
 
The LinkedIn URLs should be stored as a CSV file

 [.\companies.cvs.urls.csv] 
 
. And once that is done, extend the script using Playwright browser to find the employee count from LinkedIn  

   [
         from rashmi.urls2Count import GetStaffCountFromUlrNameNest
      
   ]

. And store it in the original file alongside the Company Names 

[
    from rashmi.urls2Count import
] modifies -> [.\companies.csv]

.
2. Use any csv reader you want and any scraper you want to
accomplish this...
        
         [
            import argparse
            import csv
            from bs4 import BeautifulSoup
            import playwright
         ]


3. The module entry point can be a POST API endpoint that accepts
csv files and returns the file with company name and employee count
or a CLI program.

         
   [
      Cli ->  python3 .\thinkBrigde.py .\companies.csv  email  password
   ] will produce -> [.\companies.cvs.urls.csv] 
     and modify -> [.\companies.csv]

     Note provide with email and password from a valid linkedIn account 

4. Please ensure the following points as well:

4.1. All API calls should be asynchronous.

   [ 
      #Note the use of 
      import asyncio

      ...
      and the call of the main function at main.py should require the following...
      asyncio.run(main())
   ]


4.2. Include data validations wherever needed for all endpoints taking
inputs. 
    
     [
      Note due to time constraints just a few validations were taking into account. 
      This code is not production ready.
     ] 

4.3. Exception handling needs to be present wherever applicable.

     [
      Note due to time constraints elementary Exception handling was included.  
      This code is not production ready.
     ]


Submission Requirements:
1. The code should be submitted via GitHub/BitBucket in a public repository.
    [ 
      Find my code solution at: https://www.github.com/xtobal101/ThinkBridge 
    ]
    
2. Simple and minimal design, you can use any extra packages you want to.
   [
      Extra packages: BeutifulSoup, Playwright, CSV, argparse, requests
   ]

3. The code repo should have all supporting/relevant documentation
showing all endpoints and detailed steps on how to run the solutions.
    
    [
     Use this file as documentation.  
     Note that the module can be run as Cli 
     therefore not endpoints were defined
    ] 

    [
      How to run the solution:
      #Ensure that python 3.8 or above and that the following packages are present 
      in your local system.
       
       pip install BeutifulSoup
       pip install argparse
       pip install playwright
       pip install csv
       pip install requests
         

       #Clone to your local repository.
       git clone https://www.github.com/xtobal101/ThinkBridge
       
       # get into your local repository folder and type ...
       
        
       python .\thinkBrigde.py .\companies.csv  email password

       #Note: you most provide a valid linkedIn email and password combo


       #This should produce the a new companies.csv.urls.csv file and also 
       should modify the original companies.csv file to include an employees count column.
     ]


4. Please include any extra steps required to create/run any external
integrations.


    [
      The module ThinkBridge includes several functions to cover each step of the requirements. 
      Please have a look of the steps 1 to 3 of the requirements portion of this document to find
      which function is used for each step and what file is produced after every call.  
      This will help to choose the proper function to accomplish any step in isolation.

      The included file main.py assembles all the components to form a CLI.

      Note: There is a delay of a second on every page visit.
      Also if the page is not found the "Not found" string entry would be added to the csv file.
      Finally: If the amount of employees is not found the number stored would be -1 
    ]

