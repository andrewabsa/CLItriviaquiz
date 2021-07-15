# T1A3 - Terminal app - General Knowledge Quiz

## Statement of purpose and scope of application
Trivia Quiz is designed as a fun application to test the user's general knowledge in a fun and methodical way. I decided to develop Trivia Quiz as it is a great way to test your skills whilst having some fun. Trivia Quiz is well suited for anyone no matter the age, as long as your here to have fun Trivia Quiz is for you. 

Trivia Quiz can be played in 3 game modes; Easy, Medium and Hard. Each with increasing difficult. Once a quiz has been completed, users get see their final score in a leaderboard, where they will be prompted to enter their name so the score can be allocated to said name. 

A bonus "time trial" quiz is available to play aswell. User's will see how fast they can solve math problems under a timer. Once again final score and name will be displayed in leaderboard.

## Main Features
### Quiz categories
**Multiple choice**
(MCQ) will prompt the user to respond to questions with four possible answers : (a,b,c,d)
Program will throw an error if it receives any other input that is not a,b,c,d.
E.g. "Sorry that was not one of the options. Please try again." 

**Game modes:** Choose from **Easy**, **Medium**, and **Hard**. 
Each game mode has unique questions and answers. 


**True or False**
True of False questions will prompt user to enter the answer as "T" for true or "F" for false.
Error handling will be implemented when user enters an answer that is not "T" or "F".

**Leaderboard**
 will store user's name and final score into a table where score data will be saved.

**Main Menu**
will contain instructions on how to play the quiz. And will include a prompt where the user will be able to input their desired name.

**Countdown Timer to prepare for quiz**
Players will be given a countdown timer to prepare for a quiz. Time will countdown in front of them.

## Intended User Interaction & Experience
The quiz application is intended to be used as program to test your knowledge.

The **leaderboard** feature can be accessed by users from the main menu and can also be seen on completion of a quiz. The leaderboard will store the user's data (name and score) and save it to the leaderboard.

The **short answer** option allows the user to have a choice between the type of quiz they want to play. There will be an option to choose between quizes in the main start up page.

There will be a bonus **time trial** quiz available upon successful completion of the short answer quiz and the MPC quiz. The time trial quiz will only be visible to the user once they answer all questions correctly in the two previous quizzes.


### Flow Chart

A flow chart representing the logic structured within my application.
![flowchart](termappflowchart.png)