<h2><b>Movie Trailer Website</b></h2>

The Movie Trailer Project includes server-side code to store a list of my favorite movies, including box art imagery and a movie trailer URL. It consist of the following files:

1) Media.py : Contains the framework of our application i.e. the Movie Class for creating various movie objects.

2) Entertainment_center.py : Contains a list of static movie instances and the calling function for creation of index.html

3) Imdb.py : Contains the user code for creating dynamic html content within the webpage index.html . COntains the python code for formating the html template by fitting in the necessary details at suitable locations.

4) Index.html : HTML page to be served to the user

5) Index.js : Javascript requirements for the html file

<h5>Running the Code Module</h5>

a) Open Terminal.

b) Nagivate to the folder containing all of the files.

c) Type the following command:

python entertainment_center.py    // Python 2.7  <br>
python3 entertainment_center.py   // Python 3.4

d) The code will automatically create the html file and will open the html file in your default browser. Enjoy :)

NOTE : 

1) This command is as per my local machine, you can modify it accordingly where you may just use 'python' keyword even for Python 3.4

2) The code executes properly on Windows, Linux and Macbook. Tested on all three operating systems.


