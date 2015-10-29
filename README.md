# Movie Finder (Movie Trailer Website)

# Installation on Windows

### Environment Variables
1. Push the Windows Key
- Type Environment Variables
- Click "Edit the system environment variables" to bring up System Properties, Advanced tab
- Click the "Environment Variables"" button
- Under "System variables"
- Add PYTHONPATH if it doesn't already exist
- Edit Path to include %PYTHONPATH%;%PYTHONPATH%\Scripts;
    	
### Virtualenv
If the Path variables have been set, you should be able to use pip from the Windows command line.
Press the Windows Key and r to bring up the Run Dialog and in the Open text box type: (Press the Enter key after each of the following)

```
cmd
pip install virtualenv
cd C:\Path\to\movieFinder
virtualenv venv
venv\scripts\activate
```

# Installation on Mac OS X
OS X comes with a version of Python already installed.  These instructions will assume that the default Python install will be used.<br>

1. Toggle Spotlight by pushing the Command key and spacebar at the same time.
- Type Terminal and hit enter
- The Terminal should open up to your home directory, change directory to where you unzipped the project or want to install.
- If you have git installed, then you can clone the project via the command `git clone https://github.com/frost-byte/movieFinder.git`
- Next, enter the following commands:

### Virtualenv
```
sudo easy_install pip
sudo pip install virtualenv
cd movieFinder
virtualenv venv
source venv/bin/activate
```

The command prompt will change from 'c:\path\to\movieFinder>' to '(venv) c:\path\to\movieFinder'
	  
## Python Modules and Dependencies

Make sure virtualenv is activated (see above) 
```
pip install omdb
pip install xmltodict
pip install flask
```

For Mac OS X, you might need to preface the above commands with sudo.
```
sudo pip install omdb
sudo pip install xmltodict
sudo pip install flask
```
	  

## Requirements
+ Python 2.7
+ pip
+ Flask
+ xmltodict
+ omdb

## References
    
###Movie APIs
## References
    
###Movie APIs
[Jayaprakash Garaga, Grand Valley State University, Personalized Movie Database System](http://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1205&context=cistechlib)<br>
This was very useful for understanding and learning about some of the APIs available for web sites and services for Movies.

[TrailerAddict.com API](http://www.traileraddict.com/trailerapi)<br>
Offers a way to allow the user to select a movie and then assign a trailer programmatically. The Simple API was used in this project.</p>

[OMDB Api](http://omdbapi.com)<br>
The online specification and reference for the Open Movie Database API.

###Other API and Coding References
[Stack Overflow](http://stackoverflow.com/)<br>
A go to resource for solving all problems related to coding.

[W3Schools](http://www.w3schools.com/)<br>
Great reference for all languages and specifications for programming web based content. HTML, CSS, jQuery, Javascript...

[jQuery API](http://api.jquery.com)<br>
The definitive javascript library for interacting with the Document Object Model (DOM).

[Bootstrap](http://www.getbootstrap.com)<br>
The javascript and css library of gui elements.
	
###Python

[Derrick Gilland's Python OMDB Api Wrapper](https://github.com/dgilland/omdb.py)<br>
User search's for movies generate a list of titles by querying the OMDB Api.<br>

[Martín Blech's xmltodict Python Module](https://github.com/martinblech/xmltodict)<br>
Takes the xml file retrieved using the TrailerAddict SimpleAPI and converts it into a python dictionary.<br>

[Flask - "A micro webdevelopment framework for Python"](http://flask.pocoo.org/docs/0.10/)<br>
Runs the web server that handles user requests for searching movies and adding them to the list of favorites. Leverages the OMDB and TrailerAddict.com Api's to dynamically	update the list of favorite movies.<br>

[The Traveling Coder - Building Websites in Python with Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)<br>
A handy tutorial and reference.<br>

[Virtualenv](https://virtualenv.pypa.io/en/latest/index.html)<br>
A python module for creating Virtual Environments for Python projects.

[Python-Guide.org Virtualenv Guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)<br>
Encapsulates a Python projects third party module dependencies into an environment which can be per project.

[Python Tricks: Accessing Dictionary Items as Object Attributes by Senko Rašić](http://goodcode.io/articles/python-dict-object/)<br>
Used his method of creating a python object from a dictionary by assigning the dictionary to the object's __dict__ attribute.

###Markdown
[Markdown Here](http://markdown-here.com/)<br>
[Daring Fireball - Markdown Basics](https://daringfireball.net/projects/markdown/basics)<br>
[Adam P's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)<br>
Three guides that are extremely useful when trying to create styled documents.  In particular, this README file.<br>

[Online Markdown Editor](http://markable.in/editor/)<br>
Incredibly useful for troubleshooting and learning markdown.