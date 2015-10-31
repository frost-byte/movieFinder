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
	  
## Running the App
From the Windows command prompt ( or OS X Terminal ) make sure you're in the project directory with virtualenv activated.<br>
Run the following command: `python entertainment_center.py`<br>

Several messages should appear indicating that the server is running on the **localhost** and port **5000**. `http://127.0.0.1:5000`<br>
A browser window should then open and the site should appear.

## Requirements
+ Python 2.7
+ pip
+ Flask
+ xmltodict
+ omdb

## Recommended
+ Sphinx
+ flake8
+ Virtualenv

##References
###Code Documentation
[Documentation](https://frost-byte.github.io/movieFinder/) for the modules was generated using Docstrings and Sphinx.<br>

[Daler's Guide to Publishing Sphinx Generated Docs to github](https://daler.github.io/sphinxdoc-test/includeme.html)<br>
Simplifies using your Sphinx generated docs on your project's github.io page.

[reStructured Text Primer](http://sphinx-doc.org/rest.html)<br>
Detailed guide for the .rst markdown format used by Sphinx.

[Python Documentation Guide](http://docs.python-guide.org/en/latest/writing/documentation/)<br>
General guide covering various tools to document Python code, including Sphinx.

[First Steps with Sphinx](http://sphinx-doc.org/tutorial.html)<br>
How to get Sphinx setup and running.

[PEP 0257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)<br>
Guidelines for using Docstrings to document your python source code.

[Documenting your Project using Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)<br>
More insights about Sphinx.

[A semi-automatic way for Sphinx to Document using Docstrings](http://sphinx-doc.org/ext/autodoc.html)<br>
This is by far the easiest way to quickly document your modules, classes and methods.

###Code Formatting
[Pep8 Online](http://pep8online.com/)<br>
An online python formatting tester.

[Flake8](https://flake8.readthedocs.org/en/2.4.1/)<br>
A Handy, command line tool for checking the formatting of your python code.

###Code Attributions  
[Python Tricks: Accessing Dictionary Items as Object Attributes by Senko Rašić](http://goodcode.io/articles/python-dict-object/)<br>
Used his method of creating a python object from a dictionary by assigning the dictionary to the object's __dict__ attribute.

[How to Check if an Enter Key is Pressed with jQuery by mkyong](http://www.mkyong.com/jquery/how-to-check-if-an-enter-key-is-pressed-with-jquery/)<br>
Checking for the Enter key's keycode in an event using jQuery.

[What is the easiest way to disable/enable buttons and links (jQuery + Bootstrap) answer from oikonomopo](http://stackoverflow.com/a/17935158)<br>
Technique for disabling a Bootstrap button using jQuery.
   
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

###Markdown
[Markdown Here](http://markdown-here.com/)<br>
[Daring Fireball - Markdown Basics](https://daringfireball.net/projects/markdown/basics)<br>
[Adam P's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)<br>
Three guides that are extremely useful when trying to create styled documents.  In particular, this README file.<br>

[Online Markdown Editor](http://markable.in/editor/)<br>
Incredibly useful for troubleshooting and learning markdown.