from random import randint
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime as dt
from time import sleep
print("++++++++++++++++++++++\n"
	"Dubizzle Scrapper Ads and their Prices\n"
	"Feel Free to modify or change the code\n"
	"For your data need or contact me for modifications\n"
	"mushrafmustafa@gmail.com\n"
	"Mob:+971521287752\n"
	"++++++++++++++++++++++\n")
sleep(2)#To make sure u read ;)
search_input = input("What You want to search: ")
search_tune = str(search_input.replace(" ","+"))
end = int(input("Number of Pages for scrapping: "))
end +=1
pages = list(range(1,end))
sleep(1)
print("---------------------\n"
 " 1 - Dubai\n"
 " 2 - Abu Dhabi\n"
 " 3 - Ras Al Khaimah\n"
 " 4 - Sharjah\n"
 " 5 - Ajman\n"
 " 6 - Al Ain\n"
 " 7 - Fujairah\n"
 " 8 - Ummal Quawin\n"
 "---------------------")
area_raw =input("Choose the Area Number: 1 - 8\n")
def area():
	if area_raw == "1":
		return "dubai"
	elif area_raw=="2":
		return "abudhabi"
	elif area_raw=="3":
		return "rak"
	elif area_raw=="4":
		return "sharjah"
	elif area_raw=="5":
		return "ajman"
	elif area_raw=="6":
		return "alain"
	elif area_raw=="7":
		return "fujairah"
	elif area_raw=="8":
		return "uaq"
#area1 = area()
def PriceName():
	start_time = dt.now()
	print("Search Started at "+str(start_time))
	for page in pages:
		url  = urllib.request.urlopen('https://'+area()+'.dubizzle.com/search/?page='+str(page)+'&keywords='+search_tune+'&is_basic_search_widget=1&is_search=1')
		soup = BeautifulSoup(url,"html.parser")
		item_container = soup.findAll('div',{'class':'list-item-wrapper'})
		contain = item_container[0]
		file_name = area()+" page no "+str(page)+".csv"
		f = open(file_name, "w")
		headers = "Ad Name, Price AED\n"
		f.write(headers)

		for container in item_container:
			title = container.findAll('span',{'class':'title'})[0].a.text.strip()
			price  = container.findAll('div',{'class':'price'})[0].text.strip()
#print("Title: " +title) //unhide for testing
#print("Price: " +price) //unhide for testing
			f.write(title.replace(",","|") + "," + price.replace(",","") + "\n")
		f.close()
	end_time =dt.now()-start_time
	print("Completed!\n Time Taken: "+str(end_time))	

PriceName()