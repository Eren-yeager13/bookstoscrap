import requests
from bs4 import BeautifulSoup
import csv
from time import time
start=time()
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price','Availability','Rating','description'])


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
       
            #get more data
            line=book.h3.a['href']
        for i in line:
               https="https://books.toscrape.com/catalogue/{}"
               
               https=https.format(line)
               response2=object_req.get(https)
               soup2=BeautifulSoup(response2.content,'lxml')
         
               proudict=soup2.find('article',{'class':'product_page'})
   
               desc=proudict.find('p',{'class':None}).get_text().strip()

            #    description.append(desc)
               if desc == None:
                    desc='invalide'
               else:
                    description.append(desc)
                
        for title, price,avaliable,rating,des in zip(book_titles, book_prices, instock,stars,description):
            writer.writerow([title, price, avaliable, rating,des])

print("<<<<<<<Data exported to CSV file.>>>>>>>")
end=time()
print(end-start)
