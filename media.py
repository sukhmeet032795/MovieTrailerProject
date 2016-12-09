import webbrowser

class Movie(object):

	'''Class which helps me to create various movie objects and check their corresponding parameters like youtube url, 
		poster url, reviews etc..'''

	def __init__(self, movie_title, movie_url, movie_storyLine, movie_reviews, movie_posterUrl, movie_rating):

		self.title = movie_title
		self.trailer_youtube_url = movie_url
		self.story = movie_storyLine
		self.poster_image_url = movie_posterUrl
		self.rating = movie_rating
		self.reviews = []
		
		for review in movie_reviews:
			self.reviews.append(review)

	def showTitle(self):
		return self.title

	def showRating(self):
		return self.rating	

	def showStory(self):
		return self.story

	def showReviews(self):
		return self.reviews

	def showPoster(self):
		webbrowser.open(self.poster_image_url)	
		return self.poster_image_url
		
	def showTrailer(self):
		webbrowser.open(self.trailer_youtube_url)
		return self.trailer_youtube_url					

