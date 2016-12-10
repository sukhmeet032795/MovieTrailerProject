import webbrowser
import os
import re

# framework html template for creating the html

framework = '''

<!DOCTYPE html>
<html>
<head>

	<title>MoviesWorld</title>

	<!-- Css Files -->

	<!-- MaterializeCss -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
	<!-- Custom Css File -->
	<link rel="stylesheet" href="index.css">
	<!-- Google Icons -->
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<!-- Google Fonts -->
	<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Bree Serif">

	<!-- Scripts -->

	<!-- Jquery -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<!-- MaterializeCss -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>
	<!-- FontAwesome -->
	<script src="https://use.fontawesome.com/329b68c3d5.js"></script>
	<!-- Custom JS File -->
	<script src="index.js"></script>

</head>
<body>

	<header>
		<i class="small material-icons">movie</i>
		<span>MoviesWorld</span>
	</header>

	<div class="moviesContainer">
		{movietiles}
	</div>

	<div id = "trailerModal" class="modal">
		<div class="modal-content">
		</div>
		<div class="modal-footer">
			<a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat">Close</a>
		</div>
	</div>
</body>
</html>

'''

# single movie html template

allMovies = '''

	<div class="card">
		<div class="card-image waves-effect waves-block waves-light">
			<img class="activator" src="{movie_poster}">
		</div>
		<div class="card-content">
			<div class="card-title activator grey-text text-darken-4 movieTitle">
				<p>{movie_title}</p>
				<i class="material-icons right">more_vert</i>
			</div>
			<div class="trailerClass">
				<a href = "javascript:void(0);" id = "{movie_url}">Trailer</a>
				<i class="material-icons icon">video_library</i>
			</div>
		</div>
		<div class="card-reveal">
			<span class="card-title grey-text text-darken-4">Movie Story Line<i class="material-icons right">close</i></span>
			<p>{movie_story}</p>

			<div class="reviewHeader">
				<span class="card-title grey-text text-darken-4 reviewSpan">Movie Reviews</span>
				<i class="material-icons icon">movie_filter</i>
			</div>

			<div class="reviews">
				{all_reviews}
			</div>

			<div class="ratingHeader">
				<span class="card-title grey-text text-darken-4 ratingSpan">Movie Rating</span>
				<i class="material-icons icon">star_rate</i>
			</div>

			<div class="rating">{rating} out of 10</div>
		</div>
	</div>

'''

review = '''
			<p>
				<input type="checkbox" id="review{index}" checked="checked" disabled="disabled" />
				<label for="review{index}">{userReview}</label>
			</p>
'''

###########################


# responsible for creating the reviews tile portion

def create_reviews_tile(reviews):

    ind = 1
    allReviews = ''
    for rev in reviews:

        allReviews += review.format(

            index=ind,
            userReview=rev
        )
        ind = ind + 1
    return allReviews

# responsible for creating movie tile and merging with it the reviews tile
# portion


def create_movie_tile(movies):

    content = ''
    for movie in movies:

        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        trailer_url = "https://www.youtube.com/embed/" + \
            trailer_youtube_id + "?autoplay=1&html5=1"
        userReviews = create_reviews_tile(movie.reviews)

        content += allMovies.format(

            movie_title=movie.title,
            movie_url=trailer_url,
            movie_story=movie.story,
            all_reviews=userReviews,
            movie_poster=movie.poster_image_url,
            rating=movie.rating
        )

    return content


def open_movies_page(movies):

    output = open('index.html', 'w')

    reformattedContent = framework.format(

        movietiles=create_movie_tile(movies)
    )

    output.write(reformattedContent)
    output.close()
    url = os.path.abspath(output.name)
    webbrowser.open('file://' + url, new=2)
