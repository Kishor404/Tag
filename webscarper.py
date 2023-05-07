def wiki_scraper(word):
	
	import requests 
	import pandas as pd 
	from bs4 import BeautifulSoup 

  
	
	link="https://www.google.com/search?q=about+"+word
	list1=[]
	para=""

	def getdata(url): 
	    r = requests.get(url) 
	    return r.text 


	htmldata = getdata(link) 
	soup = BeautifulSoup(htmldata, 'html.parser') 
	data = '' 

	for data in soup.find_all("div"): 
	    list1.append(data.get_text())
    
	data1=list1[7]


	try:

		x=data1.split(' ')

		for i in x:
			if i=="wiki":
				ind=x.index(i)
				break
		
		data2=x[ind+2:]

		for j in data2:
			if j=="-":
				break
			else:
				para=para+" "+j
		
		
		return(para)

	except:
		return("No Search Result Found...!")
		
		
#================#==========


def dict_scraper(word):
	
	import requests 
	import pandas as pd 
	from bs4 import BeautifulSoup 

  
	
	link="https://www.google.com/search?q=cambridge+dictionary+"+word+"+meaning"
	list1=[]
	para=""
	

	def getdata(url): 
	    r = requests.get(url) 
	    return r.text 


	htmldata = getdata(link) 
	soup = BeautifulSoup(htmldata, 'html.parser') 
	data = '' 

	try:
		
		for data in soup.find_all("span"):
			list1.append(data.get_text())
		para=list1[9]
		
		z=para.split(" ")
		
		er=["days","ago"]
		
		if z[1]==er[0] and z[2]==er[1]:
			raise NameError
		else:
			return(para)
		
	except:
		
		return ("No Search Result Found")
		
#====== insta =====
		
def instascrap(id,x):
	
	def insta(id):
		try: 
			import instaloader
			L = instaloader.Instaloader()
			username = id
			profile = instaloader.Profile.from_username(L.context, username)
			return(f"Name: {profile.full_name}\nNumber of followers: {profile.followers}\nNumber of following: {profile.followees}\nNumber of posts: {profile.mediacount}\nBio : \n{profile.biography}")
		except:
			return("Private ID Or Invalid ID")

			
	if x==1:
		return(insta(id))
	else:
		return('invaild')



	
    
