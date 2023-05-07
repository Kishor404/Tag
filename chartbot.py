def cbin(z):
	
	import webscarper as ws
	import webbrowser
	
	ex="Sorry An Error Occurs"
	
	def check(o):
		
		x=o.lower()
		key=["<do>","wiki","dict","abt","insta","<for>","browse"]
		
		ip=open("input.txt","r")
		c=ip.read()
		cont=c.split("\n")
		
		z=x.split(" ")
		
		if key[0] in z:
			return(dosum(z,key,x,cont))
		if key[1] in z:
			return(wiki_scrap(z,key,1))
		if key[2] in z:
			return(dict_scrap(z,key,2))
		if key[3] in z:
			return(all_scrap(z,key,3))
		if key[4] in z:
			return(insta_scrap(z,key,4,1))
		if key[5] in z:
			return(edit(x))
		if key[6] in z:
			return(browse(x))
		else:
			return(elsepre(x,cont))
		
		ip.close()
		
	def elsepre(x,cont):
		y="<"+x+">"#
		if y in cont:
			id=cont.index(y)
			return(show(id))
		else:
			return 0
		
	def browse(x):
		a=x.split(" ")
		b=""
		a.pop(0)
		for i in a:
			b=b+i
		webbrowser.open("https://www.google.com/search?q="+b)
		return ("Link : https://www.google.com/search?q="+b)

	def show(id):
		
		op=open("output.txt","r")
		c=op.read()
		out=c.split("\n")
		v=out[id]
		z=v[1:-1]#
		
		op.close()
		
		return(z)
		
	# - - - Modules  DO - - -
		
	def dosum(z,key,x,cont):
		
		try:
			d=z.index(key[0])
			g=eval(z[d+1])
			return (str(g))
		except:
			return(elsepre(x,cont))
			
	# - - - Modules Web Scrap - - -
	
	def wiki_scrap(z,key,x):
		try:
			word=""
			d=z.index(key[x])
			wordlis=z[d+1:]
			for i in wordlis:
				word=word+" "+i
			para=ws.wiki_scraper(word)
			return(para)
		except:
			return("No Internet Connection...!")
	
	def dict_scrap(z,key,x):
		try:
			word=""
			d=z.index(key[x])
			wordlis=z[d+1:]
			for i in wordlis:
				word=word+" "+i
			para=ws.dict_scraper(word)
			return(para)
		except:
			return("No Internet Connection...!")
			
	def all_scrap(z,key,x):
		try:
			word=""
			d=z.index(key[x])
			wordlis=z[d+1:]
			for i in wordlis:
				word=word+" "+i
			para=ws.dict_scraper(word)
			if para=="No Search Result Found":
				para=ws.wiki_scraper(word)
			return para
		except:
			return("No Internet Connection...!")
			
	def insta_scrap(z,key,x,y):
		try:
			id=""
			d=z.index(key[x])
			id=z[d+1]
			cont=ws.instascrap(id,y)
			return cont
		except:
			return("No Internet Connection...!")
			
	def edit(x):
		
		try:
			c=x.split("<for>")
			c1=c[1]
			d=c1.split("<replay>")
			print(d)
			d1=d[0]
			x=[i for i in d1]
			d2=d[1]
			y=[j for j in d2]
			if x[0]==" ":
				x.pop(0)
			if x[-1]==" ":
				x.pop(-1)
			if y[0]==" ":
				y.pop(0)
			if y[-1]==" ":
				y.pop(-1)
			print(x)
			print(y)
			m=""
			for i in x:
				m=m+i
			n=""
			for j in y:
				n=n+j
			
			#replace in file
			
			inf=open("input.txt","r")
			outf=open("output.txt","r")
			outfc=outf.read()
			infc=inf.read()
			for i in infc:
				infcl=infc.split("\n")
			for j in outfc:
				outfcl=outfc.split("\n")
			inf.close()
			outf.close()
			outlist=outfcl
				
			mu="<"+m+">"
			if mu in infcl:
				id=infcl.index(mu)
				with open('input.txt', 'r') as fr:
					lines = fr.readlines()
					ptr = 1
					with open('input.txt', 'w') as fw:
						for line in lines:
							if ptr != id+1:
								fw.write(line)
							ptr += 1
							
				with open('output.txt', 'r') as ofr:
					olines = ofr.readlines()
					optr = 1
					with open('output.txt', 'w') as ofw:
						for oline in olines:
							if optr != id+1:
								ofw.write(oline)
							optr += 1
             			  
				
			else:
				pass
			infa=open("input.txt","a")
			outfa=open("output.txt","a")
			infa.write("\n<"+m+">")
			outfa.write("\n<"+n+">")
			infa.close()
			outfa.close()
			
			return("Replay For "+m+" is "+n)
			
		except:
			return("Succefully Error Occurs...!")
		
	return(check(z))
	

	

#---------+-----------+-----------+---------+

def cbout(x,n):
	
	a=open("input.txt","a")
	y=x.lower()#
	a.write("\n<"+y+">")
	a.close()
	
	b=open("output.txt","a")
	m=n.lower()#
	b.write("\n<"+n+">")
	b.close
	
#----------------------------

def settings():
	a=open("settings.txt","r")
	b=a.read()
	for i in b:
		c=b.split("\n")
	d=len(c)
	e=c[d-1]
	a.close()
	return e
	
def adset(x):
	a=open("settings.txt","a")
	a.write("\n"+x)
	a.close()
	
def theme(x):
	if x==0:
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		return c[0]
	elif(x==1):
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		return c[1]
	
def theme_geter(x):
	if x=="Yellow":
		y=1,170/255,23/255,1
	elif x=="Green":
		y=0/255,92/255,74/255,1
	elif x=="Red":
		y=1,0,0,1
	elif x=="Black":
		y=0,0,0,1
	elif x=="Blue":
		y=0,0,1,1
	else:
		y=0/255,92/255,74/255,1
	return y
	
#-------------------------------
