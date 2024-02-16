# Memento:
<p align="center">
    <img src="app/static/img/memory.png" alt="Memento app icon" width="120" height="auto">  
</p>

**Memento is a web application designed to help users learn and remember difficult concepts or words from foreign languages.The application allows the user to create an individual account, on which they can add, edit and delete concepts or words along with their meanings. The user can also search for concepts or words that he has already added and practice his memory and knowledge by taking a quiz.**  

This application is my original project, which is also the final project of the CS50x course at Harvard University.  
I have very basic knowledge of Python, so please be gentle when reading my code.  
As part of my professional development as a tester, I add further automatic tests to the application, which I also run in CI via Github Actions. 

> Live demo available [_here_](https://test-memento.onrender.com).  
> Test user: **Tester** password: **tester123**  
> _Note: The application is hosted on the free Render server and needs 3-4 minutes to wake up. After restarting the server, all changes made will be lost_

## Table of Contents:
* [General Info](#general-information)
* [Features](#features)
* [Technical Stack](#technical-stack)
* [Installation and running](#installation-and-running)
* [Project file structure](#project-file-structure)
* [Testing](#testing)
* [Continuous Integration (CI) with Github Actions](#continuous-integration-ci-with-github-actions)
* [Deploy to DockerHub](#deploy-to-dockerhub)
* [Contact](#contact)


## General Information:
Memento is a web application that helps users learn and remember difficult definitions or learn words from foreign languages. After creating an account, the user can add words and their meanings, browse them, search them, and has access to tools supporting memory. These include a quiz and a randomization of previously added content combined with an attempt to recall the meaning.

The application is my final project for the CS50x course at Harvard University. During this course, I learned the basics of Python, the Flask framework, HTML, CSS and JS.
Even though the application was created as a final project, the idea for it and its implementation was not suggested and is entirely my idea.
More information about CS50x is available on [the course website](https://cs50.harvard.edu/x/2023/).


## Features:
- **Individual accounts**: Users can create individual accounts. Once logged in, they can manage words/concepts specific to their account.
- **Add New Word**: Users can add words/concepts and their meanings.
- **Search**: Users can search for previously added words/concepts, edit or delete them. Entering '%' in the search input displays all words/concepts added to the account.
- **Memorize**: Users practice memory recall. A randomly selected word/concept is revealed, and users trie to recall its meaning, then reveals the text with the meaning. They can mark words as well-remembered.
- **Quiz**: Users match definitions to words/concepts. Correct answers are highlighted in green, the incorrect one is highlighted in red. After clicking the button, the next question is randomly selected.
- **My Account**: Users can change their username (if available), update their password, and delete their account along with all information related to it.


## Technical stack:
* Programming language: Python
* Web framework: Flask
* Template engine: Jinja
* Database: SQLite
* Front-end framework: Bootstrap
* JavaScript framework: JQuery
* Testing tool: Postman
* Continuous Integration: Github Actions
* Deployment: Docker


## Installation and running
***To run the application, you can use one of three methods.***
1. Live demo on Render server.  

    The application is hosted on the free Render server at: https://test-memento.onrender.com. Due to the limitations of free hosting, the first application launch may take 3-4 minutes. The entered data is also not stored between sessions.
    You can use your saved user to explore the features of the Memento app. The details for the test account are:
    > username: Tester  
    > password: tester123

2. Launching the application from the Docker container.  

    The application's Docker image is available on [DockerHub](https://hub.docker.com/repository/docker/przemekqa/memento_app/general). To run the container with the application, just use the command:

    ```
    docker run -p 5000:5000 -d przemekqa/memento_app
    ```
    If Docker does not find the image file locally, it should automatically initiate its download from DockerHub.  

    The application should be available in your browser at http://localhost:5000/ 

3. Downloading the source code and installing the dependencies.  

    _Note:  
          The installation instructions below will be suitable for Ubuntu 22.04.  
          For Windows I recommend using WSL with Ubuntu 22.04 installed._  

    To launch Memento applications, execute the following commands in the terminal:  
      1. Update apt package manager:

        sudo apt update

      2. Install the necessary packages:
        
        sudo apt install -y python3 python3-pip python3-venv
        
      3. Download the source code files from GitHub:
        
        git clone https://github.com/PrzemekKozakQA/Memento-memory_helper_web_app.git
        
      4. Change to the "app" directory in the application code directory:
        
        cd Memento-memory_helper_web_app/app/
        
      5. Create a Python virtual environment:
        
        python3 -m venv venv
        
      6. Activate the previously created virtual environment:
        
        source venv/bin/activate
        
      7. Download the necessary libraries:
        
        pip3 install -r requirements.txt
         
      8. Run the application in debug mode with Flask :  
        
        flask run -p 5000

    <p>&emsp;&emsp;or using the WSGI Gunicorn server with the command:</p>

        gunicorn -b 127.0.0.1:5000 app:app

            
    The application should be available in your browser at **http://127.0.0.1:5000/**

    _Note:
          To stop the application, press **Ctrl+C**. To exit the virtual environment, enter the ```deactivate``` command.  
          If you want to run the application again, just repeat steps 4, 6 and 8._


## Project file structure
```
│── app - the main project directory
│    ├── app.py - the main application file containing instructions for endpoints and application configuration
│    ├── helpers.py - the file contains methods separated from the app.py for better code readability
│    ├── memento.db - SQLite database file that stores data entered by users. It contains two tables: users and words
│    ├── requirements.txt - the file contains a list of libraries that must be downloaded for the application to run
│    ├── templates - the directory containing the files from which the application's web pages are rendered
│    └── static - the directory with files necessary for the application frontend
│        ├── img - the directory contains graphic files used by the application
│        ├── js - the directory with scripts for individual pages
│        └── styles.css - the file contains custom styles added to the selected elements
│ 
├── Dockerfile - the file contains instructions for building a Docker image of the application
├── Postman_tests - the directory contains files with postman tests and a file with test settings
├── README.md - the file with project information
├── .gitignore - the file contains information about directories and files excluded from GIT tracking
└── .github\workflows - the directory contains configuration files for CI Github Actions
    ├── test_and_push_to_DockerHub.yml - CI configuration file used when merging changes to the main branch
    └── test_changes.yml - CI configuration file used when merging changes to a branch with planned changes
```


## Testing
- TODO


## Continuous Integration (CI) with Github Actions
- TODO
The project used GitHub Actions to build a Docker image with the Memento application. If application files are changed in the repository, the trigger will start building and releasing a new version of the image to Docker Hub.
Details are available in the [Actions tab](https://github.com/PrzemekKozakQA/Memento_flask_app_CS50x_Final_project/actions).


## Deploy to DockerHub
- TODO


## Contact
Created by [Przemysław Kozak](https://www.linkedin.com/in/przemyslaw-kozak/) - feel free to contact me!
