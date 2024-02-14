# Memento:
<p style="text-align: center;">
    <img src="app/static/img/memory.png" alt="Memento app icon" width="120" height="auto"/>  
</p>
Memento is a web application designed to help users learn and remember difficult concepts or words from foreign languages.  

This application is my original project, which is also the final project of the CS50x course at Harvard University.  
I have very basic knowledge of Python, so please be gentle when reading my code.  
As part of the learning process, I add further automatic tests to the application, which I also run in CI via Github Actions.  

> Live demo available [_here_](https://test-memento.onrender.com).  
> Test user: **Tester** password: **tester123**  
> _Note: The application is hosted on the free Render server and needs 3-4 minutes to wake up._

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
The Memento application was written using the following technologies:
- Backend: Python, Flask (micro web framework) and SQLite
- Frontend: HTML, CSS with Bootstrap and Jinja (page template engine). JavaScript with the JQuery library was used for dynamic elements on the pages.


## Installation and running
-


## Project file structure
```
│── app - the main project directory
│    ├── app.py - the main application file containing instructions for endpoints and application configuration
│    ├── helpers.py - the file contains methods separated from the app.py for better code readability
│    ├── memento.db - SQLite database file that stores data entered by users. It contains two tables: users and words
│    ├── requirements.txt - the file contains a list of libraries that must be downloaded for the application to run
│    ├── static - the directory with files necessary for the application frontend
│    │   ├── img - the directory contains graphic files used by the application
│    │   ├── js - the directory with scripts for individual pages
│    │   └── styles.css - the file contains custom styles added to the selected elements
│    └── templates - the directory containing the files from which the application's web pages are rendered
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
-TODO


## Continuous Integration (CI) with Github Actions
The project used GitHub Actions to build a Docker image with the Memento application. If application files are changed in the repository, the trigger will start building and releasing a new version of the image to Docker Hub.
Details are available in the [Actions tab](https://github.com/PrzemekKozakQA/Memento_flask_app_CS50x_Final_project/actions).


## Deploy to DockerHub
-TODO


## Contact
Created by [Przemysław Kozak](https://www.linkedin.com/in/przemyslaw-kozak/) - feel free to contact me!
