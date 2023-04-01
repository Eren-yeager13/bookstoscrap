import requests
from bs4 import BeautifulSoup
import csv
from time import time


#get url for the website
start=time()
base_url = "https://books.toscrape.com/catalogue/page-{}.html"


#creat csv file
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price','Availability','Rating','description'])

    #loop for import countent from site for every page (10)
    for i in range(1, 11): 

        url = base_url.format(i)
        object_req=requests.session()
        response = object_req.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        cards=soup.find_all('article', {'class':'product_pod'})

        book_titles = []
        book_prices = []
        instock= []
        stars=[]
        description=[]

        #loop to get the countent of cards 
        for book in cards:
            #get card data
            book_title = book.h3.a['title']
            book_price = book.find('p',{'class':'price_color'}).get_text()
            availability = book.find('p',{'class':'availability'}).get_text().strip()
            star=book.p['class'][1]
            book_titles.append(book_title)
            book_prices.append(book_price)
            instock.append(availability)
            stars.append(star)
       
            #get url from every single book 
            line=book.h3.a['href']
        for i in line:
               https="https://books.toscrape.com/catalogue/{}"
               https=https.format(line)
               response2=object_req.get(https)
               soup2=BeautifulSoup(response2.content,'lxml')


                #  get description of books
               proudict=soup2.find('article',{'class':'product_page'})
   
               desc=proudict.find('p',{'class':None}).get_text().strip()

                # if book have no description 
               if desc == None:
                    desc='invalide'
               else:
                    description.append(desc)
         #append data to csv file       
        for title, price,avaliable,rating,des in zip(book_titles, book_prices, instock,stars,description):
            writer.writerow([title, price, avaliable, rating,des])

print("<<<<<<<Data exported to CSV file.>>>>>>>")
end=time()
print(end-start)
