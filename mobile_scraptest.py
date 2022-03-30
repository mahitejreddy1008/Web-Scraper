                                                     #Web Scraping Flipkart Using Python
                                                                            
                                                                    
#importing the required libraries
import bs4
import requests
import csv
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#variable to store the webpage link 
url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=226b1834-11e5-4a63-8cac-902d4b744b2b&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove'

#headers give info such as response payload and a time limit on how long to cache the response
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

#requests is used to send HTTP request to the given url
req = requests.get(url, headers= headers)

#beautifulsoup is used to pull out data from HTML and XML files
soup = bs4.BeautifulSoup(req.text, 'html.parser')

#find_all() scans the entire webpage, finding the required HTML tags
product = soup.findAll('div', '_13oc-S')

#creating a list to store product data
datas = []

#for loop to get product details from the webpage
for x in product:
    try:
        name = x.find('div','_4rR01T').text
        rating = x.find('div','_3LWZlK').text
        desc = x.find('ul','_1xgFaf').text
        price = x.find('div', '_30jeq3 _1_WHN1').text
        offer = x.find('div', '_3Ay6Sb').text

        new_price = ''.join(char for char in price if char.isalnum())

        split_offer = offer.split("%",1)
        sub_offer = split_offer[0]
         
    except:
        offer = 'Nothing'
        
        
    #appending product details to the created list
    datas.append([name, rating, new_price, sub_offer, desc])

#writing the data into a csv file
with open('mobiledata.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ['Name', 'Rating', 'Price(in ₹)','Offer(in %)', 'Description']
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)


df = pd.read_csv("mobiledata.csv")
print("\n\n")

#creating a pandas dataframe by reading the contents of the csv file
def dataframe():
    pd.set_option('display.max_columns', None)
    print(df[['Name', 'Rating', 'Price(in ₹)', 'Offer(in %)']])
    print("\n\n")

#to display a scatterplot for Offer Vs Price    
def scatterplot():
    
    p = df["Offer(in %)"]
    r = df["Price(in ₹)"]
    

    x = []
    y = []

    x = list(p)
    y = list(r)

    fig = plt.figure(figsize =(5, 5))
    
    plt.scatter(x,y, color = 'lawngreen')
    plt.xlabel("Offer(in %)")
    plt.ylabel("Price(in ₹)")
    plt.title("Offer vs Price Scatterplot")

    plt.show()

    print("\n\n")

#to display a bar graph for rating vs offer    
def bar():
    
    p = df["Offer(in %)"]
    r = df["Price(in ₹)"]
    

    x = []
    y = []

    x = list(p)
    y = list(r)


    fig = plt.figure(figsize =(6, 6))
    
    plt.bar(x,y, color = 'slateblue')
    plt.xlabel("Offer (in %)")
    plt.ylabel("Price(in ₹)")
    plt.title("Offer vs Price Bar Graph")

    plt.show()

    print("\n\n")    

#prints information about the shape of the dataframe
def dataframeinfo():
    df.info()
    print("\n\n")

#to sort the data depending on their Price
def sortprice():
    df.sort_values("Price(in ₹)", axis = 0, ascending = True,inplace = True, na_position ='last')
    print("\n\n\t\t\tAfter Sorting by Price\n\n")
    print(df[['Name','Rating','Price(in ₹)','Offer(in %)']])
    print("\n\n")

#to sort the data depending on their Rating
def sortrating():
    df.sort_values("Rating", axis = 0, ascending = True,inplace = True, na_position ='last')
    print("\n\n\t\tAfter Sorting by Rating\n\n")
    print(df[['Name','Rating','Price(in ₹)', 'Offer(in %)']])
    print("\n\n")

#to sort the data depending on their Offer
def sortoffer():
    df.sort_values("Offer(in %)", axis = 0, ascending = True,inplace = True, na_position ='last')
    print("\n\n\t\tAfter Sorting by Offer %\n\n")
    print(df[['Name','Rating','Price(in ₹)', 'Offer(in %)']])
    print("\n\n")

#to get data of any single product
def particular_item():
    num = int(input("\nEnter the Column No. of the Required Product : "))
    print("\n\n")
    col = list(df)
    for i in col:
        print(df[i][num])
    print("\n")
    
    print("\n\n")

#using the head() function
def first_num():
    num = int(input("\n\tEnter the Number of Columns to be Printed: "))
    print(df[['Name', 'Rating', 'Price(in ₹)', 'Offer(in %)']].head(num))

#using the tail() function
def last_num():
    num = int(input("\n\tEnter the Number of Columns to be Printed: "))
    print(df[['Name', 'Rating', 'Price(in ₹)', 'Offer(in %)']].tail(num))

#using the unique() function
def unique():
    print("\n\n")
    print(np.unique(df['Rating']))
    print("\n")
    print(np.unique(df['Price(in ₹)']))
    print("\n")
    print(np.unique(df['Offer(in %)']))
    print("\n\n")


def main():

    print("\n\tWriting Contents into a CSV File ..")
    time.sleep(0.75)
    print("\n\tData Succesfully Entered!\n\n")
       
    #creating a menu driven program
    while True:
        print("\t**************************************************")
        
        print("\n\t\t\tFlipkart Web Scraping\t\n")
        
        print("\t\t1.Dataframe Information")
        print("\t\t2.HTML Body of Webpage")
        print("\t\t3.Print Dataframe")
        print("\t\t4.Print First n Columns")
        print("\t\t5.Print Last n Columns")
        print("\t\t6.Print Unique Values of Columns")
        print("\t\t7.Sort by Price")
        print("\t\t8.Sort by Rating")
        print("\t\t9.Sort by Offer %")
        print("\t\t10.Display Scatterplot")
        print("\t\t11.Display Bar Graph")
        print("\t\t12.Display a Particular Product Detail")
        print("\t\t13.Exit\n")

        print("\t**************************************************")
        
        choice = int(input("\n\n\tEnter an Option: "))
        print("\n\n\n")

        if choice == 1:
            dataframeinfo()
            print("\n\n")

        elif choice == 2:
            #to view the HTML body of the webpage
            print(soup.prettify())
            print("\n\n")
           
        elif choice == 3:
            dataframe()
            print("\n\n")
        
        elif choice == 4:
            first_num()
            print("\n\n")

        elif choice == 5:
            last_num()
            print("\n\n")

        elif choice == 6:
            unique()
            print("\n\n")

        elif choice == 7:
            sortprice()
            print("\n\n")

        elif choice == 8:
            sortrating()
            print("\n\n")

        elif choice == 9:
            sortoffer()
            print("\n\n")    
            
        elif choice == 10:
            scatterplot()
            print("\n\n")
            
        elif choice == 11:
            bar()
            print("\n\n")
            
        elif choice == 12:
            particular_item()
            print("\n\n")
            
        elif choice == 13:
            break
            
        else:
            print("\n\tInvalid Choice!\n\n")


if __name__=="__main__":
    main()    
