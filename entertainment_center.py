import media
import imdb

'''
	Creating Instances of the Class Movie where parameters are in the follwoing order:

	MovieTitle, MovieURL, MovieStory, MovieReviews, MoviePosterURL, MovieRating
'''

bajiraoMastani = media.Movie(

		"Bajirao Mastani",
		"https://www.youtube.com/watch?v=eHOc-4D7MjY",
		"An account of the romance between the Maratha general, Baji Rao I and Mastani, a Muslim princess.",
		["A fantastic and classic epic romance", "Well-Made, Well-Acted Motion-Picture!", "surreal direction, "
		"exemplary CGI and commendable performances"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMWI3YTA1MDktYWNjOS00MTE5LTkzMTQtOWNiODY2MjIzYTQwXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_QL50_SY1000_CR0,0,691,1000_AL_.jpg",
		"7.2"
	)

pink = media.Movie(

		"Pink",
		"https://www.youtube.com/watch?v=AL2TShb6fFs",
		"When three young women are implicated in a crime; a retired lawyer steps forward to help them clear "
		"their names.",
		["Excellent, intense & gripping courtroom drama!!", "Dyeing our conscience", "Cinema's Pink Revolution"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BNGI1MTI1YTQtY2QwYi00YzUzLTg3NWYtNzExZDlhOTZmZWU0XkEyXkFqcGdeQXVyMDkwNTkwNg@@._V1_QL50_.jpg",
		"8.5"
	)

zindagiNaMilegiDubara = media.Movie(

		"Zindagi Na Milegi Dubara",
		"https://www.youtube.com/watch?v=ifIBOKCfjVs",
		"Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged.",
		["Excellent Movie", "Mind Blowing Stuff", "Mental Buoys Rockzzzz..", "Perfect summer movie about the journey "
		"of Life"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BZGFmMjM5OWMtZTRiNC00ODhlLThlYTItYTcyZDMyYmMyYjFjXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_QL50_SY1000_CR0,0,692,1000_AL_.jpg",
		"8.1"
	)

queen = media.Movie(

		"Queen",
		"https://www.youtube.com/watch?v=KGC6vl3lzf0",
		"A Delhi girl from a traditional family sets out on a solo honeymoon after her marriage gets cancelled.",
		["This 'queen' will surely rule your hearts!", "This QUEEN is ROYAL in every way!", "Queen is soul stirring",
		 "Queen of Hearts!!"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1ODUxMzA1Nl5BMl5BanBnXkFtZTgwNDk0NjMyMTE@._V1_QL50_.jpg",
		"8.4"
	)

ironMan = media.Movie(

		"Iron Man",
		"https://www.youtube.com/watch?v=8hYlB38asDY",
		"After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized"
		" suit of armor to fight evil.",
		["Delivers Intelligence & Great Acting with its Fun", "Excellent Movie, Great Plot", "Totally Entertaining", 
		"Wow, very impressive !!!!"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
		"8"
	)

piratesOfCaribbean = media.Movie(

		"Pirates of the Caribbean",
		"https://www.youtube.com/watch?v=naQr0uTrH_s",
		"Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save his love, the governor's"
		" daughter, from Jack's former pirate allies, who are now undead.",
		["Terrific!", "Laughter Guaranteed!!", "Real Swashbuckling film to make you laugh", "Most Delightful Pirates"
		" Adventure"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMjAyNDM4MTc2N15BMl5BanBnXkFtZTYwNDk0Mjc3._V1_QL50_.jpg",
		"8.3"
	)

toystory = media.Movie(
		
		"ToyStory", 
		"https://www.youtube.com/watch?v=4KPTXpQehio", 
		"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in"
		" a boy's room.", 
		["The adventure takes off!", "Guts of steel", "Buzz off!", "Oooh...3-D"], 
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_QL50_SY1000_SX670_AL_.jpg",
		"8.3"
	)

avatar = media.Movie(

		"Avatar",
		"https://www.youtube.com/watch?v=cRdxXPV9GNQ",
		"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his "
		"orders and protecting the world he feels is his home.",
		["Return to Pandora", "Enter the World", "Worth watching", "Eye-popping spectacle of conflict"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_QL50_.jpg",
		"7.9"
	)

ironman3 = media.Movie(

		"Iron Man 3",
		"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc",
		"When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey "
		"of rebuilding and retribution.",
		["Iron Man 3 delivers in spades", "Hopefully not Downey Jr's last", "Amazing Experience", "Surprising Plot "
		"Twists and Exhilarating Action"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_QL50_SY1000_SX700_AL_.jpg",
		"7.5"
	) 

hobbit = media.Movie(

		"Hobbit: Desolation of Smaug",
		"https://www.youtube.com/watch?v=fnaojlfdUbs",
		"The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their "
		"homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.",
		["Fantasy Action", "Reimagining", "Terrible"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMzU0NDY0NDEzNV5BMl5BanBnXkFtZTgwOTIxNDU1MDE@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
		"7.7"
	)

wolfofwallstreet = media.Movie(

		"The Wolf of Wall Street",
		"https://www.youtube.com/watch?v=iszwuX1AK6A",
		"Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to "
		"his fall involving crime, corruption and the federal government.",
		["DeCaprio Best Performance", "Leonardo DiCaprio's Crowning Work", "Eye-Popping Revelry", "High energy and "
		"wonderfully excessive"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
		"8.2"
	)

inception = media.Movie(

		"Inception",
		"https://www.youtube.com/watch?v=8hP9D6kZseM",
		"BA thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of " 
		"planting an idea into the mind of a CEO.",
		["Insanely Brilliant ! Nolan has outdone himself !!", "Nolan's first true masterpiece", "Inception May Be A "
		"Religion", "Christopher Nolan's masterpiece"],
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
		"8.8"
	)

# Creating an array/list of movie objects
movies = [ironman3, hobbit, wolfofwallstreet, bajiraoMastani, pink, queen, zindagiNaMilegiDubara, toystory, avatar, 
		inception , ironMan, piratesOfCaribbean]

# Calling in the python function responsible for initiating the creation of html file
imdb.open_movies_page(movies)