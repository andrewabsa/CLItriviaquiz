# Implementation Plan

My implementation thought process was to tackle the more difficult and time consuming parts with the most priority and then work from there.

The table has steps that are prioritised 1-3, 1 being top priority and 3 being not so prioritised.

Steps with 1 priority level, have the deadline of being completed in the next 3 days. Priority levels 2 must be completed before Friday. Priority level 3 will only be added if there is enough time. 


| General | Leaderboard Feature | Countdown Timer Feature | Main Menu Feature |
| --- | --- | --- | -- |
| Startup screen [1]  |  Receive score and name data from user [1]   | Use a while loop to create a count down timer which diplays at the start of each quiz   [1]  |  Create 4 game mode options for users to choose from [1] (easy, medium, hard, "time trial") |
| How to play/instructions  [2] | Present the leaderboard with score and name data to the user [2] | Print final time next to score in the leaderboard [3] |  Print game modes on startup screen [3]
| Show game mode options to the user [1] | Save user data so it is still accessible after finishing a quiz [2]| Store timer in a function [2]|  Receive user input to choose game mode [3]
| Create a function to display questions to the user [1] |  Assign a function to display the leaderboard [2]|Print a message to prepare user|Account for errors when user input does not match any game modes [1]
| Create function to receive user input for answers [1] |Assign a function to add to the leader board |Assign a function for the timer |Link game options to the startup screen with the use of variables
| Return feedback at the end of the quiz [2] | |
| Give user input to enter their nickname to be placed on the leaderboard [2]
| Return a total score upon completion of a quiz to go next to their name on the leaderboard [2]
| Hide final quiz untill user successfully completes all others [3]
| Receive user answer input either as multiple choice option (a,b,c) or literal answer/word. [2]