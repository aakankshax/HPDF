# HPDF
## Getting Started

The tasks in this assignment test the basic knowledge and familiarity with python and Flask framework. These tasks can be viewed [here](https://docs.google.com/document/d/1cnCbFkgn-A7pSONDTX9AlIzaqyWlZFZAT4xncfAYXcc/edit?ts=5a1e8781#). See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Python 2.7 and Flask 0.12.2


### Installing

[This](https://wiki.python.org/moin/BeginnersGuide/Download) guide can be used to install python on your system.
Flask can be installed using [this](http://flask.pocoo.org/docs/0.12/installation/) documentation.


## Description

###Task 1

The first task requires us to display a simple "Hello World" string with our name appended. First, we import the Flask class and then create its instance. The first argument is the name of the application's module, which is later declared as "__main__" to run the code. Further, we set our URL using the route() decorator, specifying the end point ('/'). The function which works for that particular URL is given a name along with the code which will display the desired output. 
This file can be saved as "task.py" and can be run on the command line using the following line of code:
```
python task.py
```

Task 1 URL: http://localhost:5000/

###Task 2

The second task requires us to fetch data using JSON API. Thus, the requests module is imported in addition to the Flask class. Now, the required information is retrieved using the requests.get() method. Further, iterating through the obtained list of data, we increment the value of “count” variable for every post by an author. The result is displayed using an HTML page which is saved in the “templates” folder at the location where task.py is. 

Task 2 URL: http://localhost:5000/authors/

###Task 3

The third task requires us to set our first name and age as cookie values. However, taking inspiration from a fellow intern, I implemented this task through user input. So, first name and age of the user is input at http://localhost:5000/inputcookie. These values are then set as cookie at http://localhost:5000/setcookie, where the setcookie function is used along with GET/POST methods creating a response object. Now, set cookie on the response object and return response.

Task 3 URL (input cookie values): http://localhost:5000/inputcookie

###Task 4

The fourth task is in continuation to the third task. In this task, we need to display the stored cookie values. This can be implemented using request.cookies.get() method.

Task 4 URL: http://localhost:5000/getcookie

###Task 5

The fifth task requires us to deny requests to a specified URL. This can easily be implemented by displaying a static message “YOU SHOULDN’T BE HERE”.

Task 5 URL: http://localhost:5000/robots.txt

###Task 6

This task requires us to render an HTML file at a specified URL. This can be done by importing render_template module from flask and then using render_template() method. The output at this URL is random text generated using [this](https://loremipsumgenerator.com) link.

Task 6 URL: http://localhost:5000/html

###Task 7
This task requires us to take input from the user and POST to any endpoint and show the input as output in command line. First, we render an HTML file on the specified URL. In this HTML file, we used the POST method at http://localhost:5000/display. In display function, we requested form data in “user” variable. 

Task 7 URL: http://localhost:5000/input


##References

http://flask.pocoo.org/docs/0.12/tutorial/ 

https://www.tutorialspoint.com/flask 

https://www.stackoverflow.com
