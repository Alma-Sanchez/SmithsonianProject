import web
import sqlite3
import DBManager

class WebpyServer:
	def __init__(self):
		"""
		The WebpyServer class is the blueprint for the server which will be called whenever a client begins a session.
		This is how the server is initialized and how it is able to react to the client.
		"""

		self.urls = ('/', 'WebpyServer') #The structure of the url and the name of the class to send the request to.
		self.app = web.application(self.urls, globals()) #The application object that needs to be created for the app to run.
		self.render = web.template.render('templates/') #The file path for HTML templates.

	def GET(self):
		"""
		The GET function is a HTTP method which will help create the initial server/client session.
		This is the initial handshake.
		This specific GET function will check to see if the player has played before via IP.
		If not then the player will be given a 'new player' path.

		Examples:
		Player enters the URL for the game. This begins the GET function which will serve up the player the correct HTML page.

		Parameters:
		None

		Returns:
		Rendered HTML page
		"""
		return self.render.main() #Uses the template path that was defined earlier to find the correct HTML template. In this case, it is 'main.'

	def POST(self):
		"""
		The POST function is a HTTP method which allows for data to be sent from the client to the server.
		The main purpose of this POST is to make sure that the player's input will have an appropriate response.
		
		Examples:
		Player inputs an incorrect accession number. Receives the hint screen template with the correct information.
		Player inputs a correct accession number. Receives next part of the correct story.

		Parameters:
		None

		Returns:
		Rendered HTML page
		"""
		return "post" #This is just a test for the moment.

class PlayerState:
	def __init__(self, character = None, story = None):
		"""
		The player state class is initialized for each player which keeps a record of the player within the DB.
		This allows for easy access to the player's information through DBManager.

		Parameters:
		Character: The player's chosen character.
		Story: The player's chosen story.

		Returns:
		Something.
		"""
		player_ip = DBManager.getIP() #Uses a DBManager function to return the player's IP

		player_character = DBManager.getCharacter() #Uses a DBManager function to return the player's character.

		player_story = DBManager.getStory() #Uses a DBManager function to return the player's current story.

		player_current_step = DBManager.getStep() #Uses a DBManager function to return the player's current step.