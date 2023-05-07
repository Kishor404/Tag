from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.utils import asynckivy
import webbrowser
import chartbot as bot


Window.keyboard_anim_args={"d":.2,"t":"in_out_expo"}
Window.softinput_mode="below_target"
#Window.clearcolor = (1, 0, 0, 1)
#Window.size=(350,550)


class Command(MDLabel):
	
	text=StringProperty()
	size_hint_x=NumericProperty()
	halign=StringProperty()
	font_name="Poppins"
	font_size=20
	
class Response(MDLabel):
	
	text=StringProperty()
	#drop_button=ObjectProperty()
	size_hint_x=NumericProperty()
	halign=StringProperty()
	font_name="Poppins"
	font_size=20
	
	
class botApp(MDApp):
	
	Name="Tag"
	BotN=bot.theme(1)
	
	up=0
	arr=1.5

	
	def ok(self,*args):
		screen_manager.get_screen('Chatbot').chat_list.add_widget(Response(text="ok", size_hint_x=.22, halign="center"))
		
	
	yellow=1,170/255,23/255,1
	red=1,0,0,1
	blue=0,0,1,1
	green=0/255,92/255,74/255,1
	white=1,1,1,1
	black=0,0,0,1
	plat=225/255,225/255,235/255,1
	milk=230/255,230/255,230/255,1
	them=bot.theme_geter(bot.theme(0))
	inptext=bot.settings()
	
	
	
	def bot_id(self):
		x=screen_manager.get_screen("BotID").text_input.text
		screen_manager.get_screen("BotID").text_input.text=""
		txt="The Bot Name Was Changed Succesfully.\nOnce You Close App And Open Again To See The Changes.\n\nTap Anywhere To Continue..."
		dialog=MDDialog(text=txt)
		dialog.open()
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		a.close()
		d=open("theme.txt","w")
		if x!="":
			d.write(c[0]+"\n"+x+"\n"+c[2])
		else:
			pass
	
	def lang_code(self):
		a="001 - English\n002 - Tamil\n003 - Arabic\n004 - Bengali\n005 - Chinese\n006 - French\n007 - German\n008 - Greek\n009 - Gujarati\n010 - Hindi\n011 - Indonesian\n012 - Italian\n013 - Japanese\n014 - Kannada\n015 - Korean\n016 - Malayalam\n017 - Marathi\n018 - Portuguese\n019 - Russian\n020 - Spanish\n021 - Telugu\n022 - Thai\n023 - Turkish\n024 - Urdu\n025 - Vietnamese"
		dialog=MDDialog(text=a)
		dialog.open()
		
	def change_lang(self):
		x=screen_manager.get_screen("Lang").text_input.text
		screen_manager.get_screen("Lang").text_input.text=""
		txt="The Replay Language Was Changed Succesfully.\nOnce You Close And Open Again To See The Changes.\n\nTap Anywhere To Continue..."
		dialog=MDDialog(text=txt)
		dialog.open()
		if x!="":
			y=""
			for i in x:
				if i == 0:
					pass
				else:
					y=y+i
			a=open("settings.txt","r")
			b=a.read()
			for j in b:
				c=b.split("\n")
			z=int(y)
			if z<26 and z>0:
				z=z
			else:
				z=1
			d=c[z-1]
			a.close()
			m=open("settings.txt","a")
			m.write("\n"+d)
			m.close()
				
	
	
	def coffee(self):
		webbrowser.open("https://www.buymeacoffee.com/Blackjack404")
	
	
	def Change_Screen(self,name):
		
		screen_manager.current=name
		
	def change_color(self,id):
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		a.close()
		d=open("theme.txt","w")
		if id==1:
			d.write("Red"+"\n"+c[1]+"\n"+c[2])
			dialog="Red Color Theme Applied Succefully. Close The App And Open Again For View The Changes.\n\nTap Anywhere To Continue..."
			comet=MDDialog(text=dialog)
			comet.open()
		elif id==2:
			d.write("Black"+"\n"+c[1]+"\n"+c[2])
			dialog="Black Color Theme Applied Succefully. Close The App And Open Again For View The Changes.\n\nTap Anywhere To Continue..."
			comet=MDDialog(text=dialog)
			comet.open()
		elif id==3:
			d.write("Green"+"\n"+c[1]+"\n"+c[2])
			dialog="Green Color Theme Applied Succefully. Close The App And Open Again For View The Changes.\n\nTap Anywhere To Continue..."
			comet=MDDialog(text=dialog)
			comet.open()
		elif id==4:
			d.write("Yellow"+"\n"+c[1]+"\n"+c[2])
			dialog="Yellow Color Theme Applied Succefully. Close The App And Open Again For View The Changes.\n\nTap Anywhere To Continue..."
			comet=MDDialog(text=dialog)
			comet.open()
		elif id==5:
			d.write("Blue"+"\n"+c[1]+"\n"+c[2])
			dialog="Blue Color Theme Applied Succefully. Close The App And Open Again For View The Changes.\n\nTap Anywhere To Continue..."
			comet=MDDialog(text=dialog)
			comet.open()

		
		
		
	def build(self):
		
		global screen_manager
		
		self.icon="tagicon.png"
		
		screen_manager=ScreenManager()
		screen_manager.add_widget(Builder.load_file("Home.kv"))
		screen_manager.add_widget(Builder.load_file("Chatbot.kv"))
		screen_manager.add_widget(Builder.load_file("Question.kv"))
		screen_manager.add_widget(Builder.load_file("Info.kv"))
		screen_manager.add_widget(Builder.load_file("Settings.kv"))
		screen_manager.add_widget(Builder.load_file("Coffee.kv"))
		screen_manager.add_widget(Builder.load_file("Editdata.kv"))
		screen_manager.add_widget(Builder.load_file("lang.kv"))
		screen_manager.add_widget(Builder.load_file("Botid.kv"))
		screen_manager.add_widget(Builder.load_file("Deldata.kv"))
		#self.refresher()
		return screen_manager
	
		
		####
	#def refresher(self):
	#	async def refresher():
	#		await asynckivy.sleep(1)
	#		self.inptext=bot.settings()
	#	asynckivy.start(refresher())
	unlockid=0
	
	def unlock(self):
		self.su=MDDialog(text="Unlocked !")
		self.dialog=MDDialog(text="By Sloving The Problem Unlock The Button !\n\nSlove : 8+3\n\n",buttons=[MDFlatButton(text="10",on_release=self.dish),MDFlatButton(text="11",on_release=self.wish),MDFlatButton(text="83",on_release=self.dish),MDFlatButton(text="9",on_release=self.dish)])
		
		self.dialog.open()
		
	def dish(self,obj):
		self.dialog.dismiss()
	def wish(self,obj):
		self.unlockid=1
		self.dialog.dismiss()
		self.su.open()
		
	def deldatacon(self):
		if self.unlockid==1:
			self.dialogs=MDDialog(text="The Data Are Never Restorable, Are You Sure To Delete It..?",buttons=[MDFlatButton(text="Cancel",on_release=self.dih),MDFlatButton(text="Confirm",on_release=self.deldata)])
			self.dialogs.open()
			self.unlockid=0
		else:
			a=MDDialog(text="You Need To Unlock The Button !")
			a.open()
	def dih(self,obj):
		self.dialogs.dismiss()
		
		self.dialogs.open()
	def deldata(self,obj):
		a=open("input.txt","w")
		b=open("output.txt","w")
		a.write("ester egg")
		b.write("You Are Master Of Egg Finder...")
		a.close()
		b.close()
		self.dialogs.dismiss()
		txt="The Memory Of Your Bot Where Deleted Succefully.\n\nTap Anywhere To Continue..."
		dialog=MDDialog(text=txt)
		dialog.open()
		
	def response(self,*args):
		
		global x
		
		x=value
		
		respose=bot.cbin(value)
		
		if respose==0:
			respose=self.inptext
			siz=.32
			halig="center"
			self.up=1
			
		if len(respose)<6:
			siz=.22
			halig="center"
				
		elif len(respose)<11:
			siz=.32
			halig="center"
				
		elif len(respose)<16:
			siz=.45
			halig="center"
				
		elif len(respose)<21:
			siz=.45
			halig="center"
				
		elif len(respose)<26:
			siz=.45
			halig="center"
					
		else:
			siz=.45
			halig="center"
			
		
		screen_manager.get_screen('Chatbot').chat_list.add_widget(Response(text=respose, size_hint_x=siz, halign=halig))
		
		#######
		
	def repedit(self):
		x=screen_manager.get_screen("Editdata").text_input.text
		bot.adset(x)
		screen_manager.get_screen('Editdata').text_input.text=""
		a="The Replay Of Unknown Chat Was Set Succefully.\nOnce You Close And Open Again To See The Changes.\n\nTap Anywhere To Continue..."
		dialog=MDDialog(text=a)
		dialog.open()
		
	def add(self):
		if self.up==1:
			
			y = screen_manager.get_screen("Chatbot").text_input.text
			
			bot.cbout(x,y)
			
			screen_manager.get_screen('Chatbot').chat_list.add_widget(Command(text=y, size_hint_x=.32, halign="center"))
			
			
			screen_manager.get_screen('Chatbot').text_input.text=""
			
			Clock.schedule_once(self.ok, 2)
			
			
			
			self.up=0
			
		else:
			self.send()
			
	def font_changer(self,x):
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		a.close()
		d=open("theme.txt","w")
		if x==0:
			c[2]="Poppins-Regular.ttf"
		elif x==1:
			c[2]="Qlassik_TB.ttf"
		d.write(c[0]+"\n"+c[1]+"\n"+c[2])
		d.close
		m=MDDialog(text="The Font Was Changed Succesfully.\n\nOnce You Close App And Open Again To See The Changes.\n\nTap Anywhere To Continue...")
		m.open()
			
		
	def font(self):
		a=open("theme.txt","r")
		b=a.read()
		for i in b:
			c=b.split("\n")
		a.close()
		return c[2]
		
	def send(self):
		global size, halign, value,x
		
		if screen_manager.get_screen("Chatbot").text_input!="":
			
			value = screen_manager.get_screen("Chatbot").text_input.text
			
			if len(value)<6:
				size=.22
				halign="center"
				
			elif len(value)<11:
				size=.32
				halign="center"
				
			elif len(value)<16:
				size=.45
				halign="center"
				
			elif len(value)<21:
				size=.45
				halign="center"
			
			elif len(value)<26:
				size=.45
				halign="center"
				
			else:
				size=.45
				halign="center"
			
			screen_manager.get_screen('Chatbot').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
			
			Clock.schedule_once(self.response, 2)
			screen_manager.get_screen('Chatbot').text_input.text=""
		

if __name__ == "__main__":
	LabelBase.register(name="Poppins",fn_regular=botApp.font(1))
	
	botApp().run()