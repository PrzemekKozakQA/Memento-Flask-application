#### 1. What is the Memento app?
Memento is a web application that helps the user learn and remember difficult concepts or words from foreign languages.

#### 2. What are the requirements to use the application?
To use the application, it is necessary to create an account. During registration, the user provides a unique username and a password consisting of at least 5 different characters. After creating an account, the user can add, edit and delete words/concepts. Only words/concepts added by the logged in user are available on each account.

#### 3. What features does the Memento app offer?
- The user can create an individual account. Once logged in, the user can add, edit and delete words/concepts in their individual account.
- In the 'Add new word' tab, the user adds a word/concept and its meaning.
- In the 'Search' tab, the user can search for words/concepts that he has already added, and then proceed to edit or delete them. It is also possible to display all words/concepts added to your account so far by entering the '%' sign in the search input.
- In the 'Memorize' tab, the user can practice his memory. After navigating to the tab, a word/concept is randomly selected. The user tries to recall its meaning, then reveals the text with the meaning and checks his memory. If the user decides that he already remembers a given word/concept well, he uses the checkbox to indicate that he no longer wants to select that word. This setting can be changed when editing a given word/concept.
- In the 'Quiz' tab, the user reads the definition and selects the word/concept that matches it. If he selects the correct word, it is highlighted in green, if the incorrect one is highlighted in red. After clicking the button, the next question is randomly selected.
- The 'My account' tab is used to change user data. It is possible to change the username if it is not occupied by another user. It is also possible to change the password and delete the account along with all information related to it.

#### 4. What is the technical stack of Memento?
The Memento application was written using the following technologies:
- Backend: Python language, Flask library and database SQLite
- Frontend: HTML, CSS using Bootstrap and Jinja. JavaScript with the JQuery library was used for dynamic elements on the pages.

#### 5. A detailed description of the application's source code:
The main project directory contains the following files:
- requirements.txt - the file contains a list of libraries that must be downloaded for the application to run

- README.md - application description file

- memento.db - SQLite database file that stores data entered by users. It contains two tables: users and words.

- app.py - The main application file, which contains information on what the program should do after sending requests to endpoints. It also contains the Flask application configuration along with user session settings.

- templates - folder containing the file from which the application's web pages are rendered.

- static - folder contains CSS files and JS scripts
     - style.css - the file contains custom styles added to the selected elements
     - js - folder with files containing JavaScript scripts

#### 6. CI using GitHub Actions:
The project used GitHub Actions to build a Docker image with the Memento application. If application files are changed in the repository, the trigger will start building and releasing a new version of the image to Docker Hub.
Details are available in the [Actions tab](https://github.com/PrzemekKozakQA/Memento_flask_app_CS50x_Final_project/actions).
