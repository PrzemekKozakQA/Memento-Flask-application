# Memento

<p align="center">
    <img src="app/static/img/memory.png" alt="Memento app icon" width="120" height="auto">
</p>

**Memento is a web application that helps users learn and remember difficult concepts or words from foreign languages. The application allows the user to add, edit and delete words along with their meaning and practice memory by participating in a quiz.**  

This application is my original project, which is also the final project of the [CS50x course](https://cs50.harvard.edu/x/2023/) at Harvard University.  
_During the course, I quickly learned programming in Python from scratch to the basic level, so I am aware that my code is not very sophisticated._ 😊  
**As part of my professional development as a tester, I add further automatic tests to the application, which I also run in CI via Github Actions.**  

> Live demo available [_here_](https://test-memento.onrender.com).  
> Test user: **Tester** password: **tester123**  
> _Note: The application is hosted on the free Render server and needs 3-4 minutes to wake up. After restarting the server, all changes made will be lost_

## Table of Contents

* [General Info](#general-information)
* [Features](#features)
* [Technical Stack](#technical-stack)
* [Installation and running](#installation-and-running)
* [Project file structure](#project-file-structure)
* [Database](#database)
* [Continuous Integration (CI) with Github Actions](#continuous-integration-ci-with-github-actions)
* [Testing](#testing)
* [Contact](#contact)

## General Information

Memento is a web application that helps users learn and remember difficult concepts or learn words from foreign languages. After creating an account, the user can add words and their meanings, browse them, search them, and has access to tools supporting memory. These include a quiz and a randomization of previously added content combined with an attempt to recall the meaning.

The application is my final project for the CS50x course at Harvard University. During this course, I learned the basics of Python, the Flask framework, HTML, CSS and JS.
Even though the application was created as a final project, the idea for it and its implementation was not suggested and is entirely my idea.
More information about CS50x is available on [the course website](https://cs50.harvard.edu/x/2023/ ).

## Features

* **Individual accounts**: Users can create individual accounts. Once logged in, they can manage words/concepts specific to their account.

<p align="center">
    <img src="gif_files\register_and_login.gif" alt="GIF shows user registrations and logins" style="display: block; margin: auto; max-width: 800px;">
</p>  

* **Add New Word**: Users can add words/concepts and their meanings.

<p align="center">
    <img src="gif_files\add_new_word.gif" alt="GIF showing the addition of a new word" style="display: block; margin: auto; max-width: 800px;">
</p>  

* **Search**: Users can search for previously added words/concepts, edit or delete them. Entering '%' in the search input displays all words/concepts added to the account.

<p align="center">
    <img src="gif_files\search.gif" alt="GIF showing the search" style="display: block; margin: auto; max-width: 800px;">
</p>  

* **Memorize**: Users practice memory recall. A randomly selected word/concept is revealed, and users trie to recall its meaning, then reveals the text with the meaning. Users can mark words as well-remembered.

<p align="center">
    <img src="gif_files\memorize_tab.gif" alt="GIF showing a tab for practice memorization" style="display: block; margin: auto; max-width: 800px;">
</p>  

* **Quiz**: Users match definitions to words/concepts. Correct answers are highlighted in green, the incorrect one is highlighted in red. After clicking the button, the next question is randomly selected.

<p align="center">
    <img src="gif_files\quiz_tab.gif" alt="GIF showing the quiz tab" style="display: block; margin: auto; max-width: 800px;">
</p>  

* **My Account**: Users can change their username (if available), update their password, and delete their account along with all information related to it.

<p align="center">
    <img src="gif_files\account.gif" alt="GIF showing my account tab options" style="display: block; margin: auto; max-width: 800px;">
</p>  

## Technical stack

* Programming language: Python
* Web framework: Flask
* Template engine: Jinja
* Database: SQLite
* Front-end framework: Bootstrap
* JavaScript library: JQuery
* Continuous Integration: Github Actions
* Testing tools: Postman, Newman
* Generating a test report: Newman HTML reporter
* Deployment: Docker

## Installation and running

***To run the application, you can use one of three methods.***

1. Live demo on Render server.  

    The application is hosted on the free Render server at: <https://test-memento.onrender.com>. Due to the limitations of free hosting, the first application launch may take 3-4 minutes. The entered data is also not stored between sessions.
    You can use saved user to explore the features of the Memento app.  
    The details for the test account are:
    > username: Tester  
    > password: tester123

2. Launching the application from the Docker container.  

    The application's Docker image is available on [DockerHub](https://hub.docker.com/repository/docker/przemekqa/memento_app/general). To run the container with the application, just use the command:

    ```bash
    docker run -p 5000:5000 -d przemekqa/memento_app  
    ```

    If Docker does not find the image file locally, it should automatically initiate its download from DockerHub.  

    The application should be available in your browser at <http://localhost:5000/>

3. Downloading the source code and installing the dependencies.  

    _Note:  
          The installation instructions below will be suitable for Ubuntu 22.04.  
          For Windows I recommend using WSL with Ubuntu 22.04 installed._  

    To launch Memento applications, execute the following commands in the terminal:  

    3.1 Update apt package manager:

    ```bash
    sudo apt update
    ```

    3.2 Install the necessary packages:

    ```bash
    sudo apt install -y python3 python3-pip python3-venv
    ```

    3.3 Download the source code files from GitHub:

    ```bash
    git clone https://github.com/PrzemekKozakQA/Memento-memory_helper_web_app.git
    ```

    3.4 Change to the "app" directory in the application code directory:

    ```bash
    cd Memento-memory_helper_web_app/app/
    ```

    3.5 Create a Python virtual environment:

    ```bash
    python3 -m venv venv
    ```

    3.6 Activate the previously created virtual environment:

    ```bash
    source venv/bin/activate
    ```

    3.7 Download the necessary libraries:

    ```bash
    pip3 install -r requirements.txt
    ```

    3.8 Run the application in debug mode with Flask:  

    ```bash
    flask run -p 5000
    ```

    <p>&emsp;or using the WSGI Gunicorn server with the command:</p>

    ```bash
    gunicorn -b 127.0.0.1:5000 app:app
    ```

    The application should be available in your browser at **<http://127.0.0.1:5000/>**

    _Note:
          To stop the application, press **Ctrl+C**. To exit the virtual environment, enter the ```deactivate``` command.  
          If you want to run the application again, just repeat steps 3.4, 3.6 and 3.8 ._

## Project file structure

```text
│── app - the main project directory
│    ├── app.py - the main application file containing instructions for endpoints and application configuration
│    ├── helpers.py - the file contains methods separated from the app.py for better code readability
│    ├── memento.db - SQLite database file that stores data entered by users.
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

## Database

In the project I used the SQLite database engine. To connect to the database, I used the cs50 library, which uses SQLAlchemy.
There are two tables in the database:

* users - stores user data.  
  Below is the query creating users table:

    ```sql
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    username TEXT NOT NULL, 
    hash TEXT NOT NULL, 
    UNIQUE(username)
    );
    ```

* words - stores data with words and their definitions written by users.  
  Below is the query creating words table:

    ```sql
    CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    word varchar(100) NOT NULL, 
    definition TEXT NOT NULL, 
    userId INTEGER, 
    isMemorized INTEGER DEFAULT 0, 
    FOREIGN KEY(userId) REFERENCES users(id),
    UNIQUE(word, userId)
    );
    ```

## Continuous Integration (CI) with Github Actions

In the project, I used GitHub Actions to run tests, get test reports, publish it and upload a new version of the application image to DockerHub.  
The Docker container with the application is built based on the settings from the [Dockerfile file](./Dockerfile).  
Integration tests written in Postman are run using the Newman command line tool. After performing the tests, a report is generated in an .html file.
Test report file can be downloaded from GitHub by going to the [Actions tab](https://github.com/PrzemekKozakQA/Memento-memory_helper_web_app/actions), details of a specific run in the Artifacts section.  

<p align="center">
    <img src="gif_files\report.gif" alt="GIF showing where to find the test report file" style="display: block; margin: auto; max-width: 800px;">
</p>

After each change merged to main, a report is also created and automatically published via GitHub Pages.  
The latest report available at: <https://przemekkozakqa.github.io/Memento-memory_helper_web_app/test-report.html>

Sample report view:
<p align="center">
    <img src="gif_files\report-gh-page.gif" alt="GIF showing sample report" style="display: block; margin: auto; max-width: 800px;">
</p>

**CI for development branches**  
After pushing the changes to development branches (all except main), CI is launched with the configuration from the [test_changes.yml](/.github/workflows/test_changes.yml) file. First, a container with the application is built, then tests are run and a test report is generated. The report file is named test_report_from_branch_{branch name}.  

**CI for main branch**  
When changes are merged to the main branch, CI is launched with the configuration from the [test_and_push_to_DockerHub.yml](.github/workflows/test_and_push_to_DockerHub.yml) file. In addition to performing tests, this configuration includes instructions for releasing a version on DockerHub.  

## Testing

### Integration tests in Postman

The frontend of the application uses the JQuery library to send requests to the backend. Data from the responses to these requests are necessary to dynamically change some of the displayed content. To check this mechanism, I wrote integration tests in Postman.
Files containing the test code and the file with environment variables are located in the [Postman_tests director](/Postman_tests/).

Scope of tested functionalities:

* Providing information whether the username is already used or not when registering a new user.
* Providing JSON with data when searching by the name of the saved word
* Marking a word in the database as remembered
* Deleting a word from the database
* Providing information that the word ID was not found

**Running tests in the local environment:**  
    To run the tests, download the files from the Postman_Tests folder and then import the collection file [Memento_application_integration_tests.postman_collection.json](/Postman_tests/Memento_application_integration_tests.postman_collection.json) and the environment file [Test_ENV.postman_environment.json](/Postman_tests/Test_ENV.postman_environment.json) to Postman.  
    The exact import process is described in the [Postman documentation](https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-data/#import-postman-data).  
> After importing the data, remember to select an environment and run the Memento application locally before running the tests.  

<p align="center">
    <img src="gif_files\postman.gif" alt="Gif shows the execution of tests in Postman" style="display: block; margin: auto; max-width: 800px;">
</p>

### GUI tests in Selenium

* TODO

## Contact

Created by [Przemysław Kozak](https://www.linkedin.com/in/przemyslaw-kozak/) - feel free to contact me!
