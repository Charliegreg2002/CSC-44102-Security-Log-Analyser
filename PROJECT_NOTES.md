Security Log Analyser — Project Planning

Project Overview

For this project, I have decided to create a Security Log Analyser because I want it to link to my Master's degree in Cyber Security. The application will be developed using Python, and I will be using Visual Studio Code to write and test my code.

The main purpose of my application will be to analyse login records and identify potentially suspicious activity, such as repeated failed login attempts. I plan to design both a command-line version and a graphical user interface (GUI) using Tkinter. Both versions will have the same functionality, but the way the user interacts with them will be different.

How My Application Will Work

For my application, I have decided to use CSV files to import login records. These files will contain information such as the username, IP address, time and date of the login attempt, and whether the login was successful or unsuccessful.

Once the file has been imported, the application will analyse the records and look for any unusual login activity. The user will also be able to view the records and see which accounts have had failed login attempts.

Failed Login Detection

One of the main features I want to include is detecting repeated failed login attempts. My application will look at attempts coming from the same IP address and trying to access the same username.

I have decided to use a five-minute sliding window to identify suspicious activity. If there are three or four failed attempts within five minutes, the application will flag this as a warning. If there are five or more failed attempts, it will be flagged as urgent.

When an alert is triggered, I want the application to show the username, IP address, number of failed attempts and the warning level. This should make it easier for the user to understand what activity has been detected.

CSV Validation and Error Handling

Another feature I want to include is checking the CSV files for errors before the records are analysed. If any records contain missing or incorrect information, the application will skip those records but still allow the valid records to be analysed.

I also want the application to tell the user which rows contained errors and explain why they were rejected. If the file contains no valid records, the analysis should not continue.

If the application identifies duplicate records, I want them to be flagged for review rather than automatically deleted. These records will still be included in the calculations, although I understand this could affect the accuracy of the results if they are accidental duplicates.

The original CSV files will not be changed or deleted by the application.

Additional Features

Alongside detecting failed login attempts, I want to include a feature that allows the user to search for specific usernames or IP addresses. This will allow them to investigate particular accounts or sources of login activity.

I am also considering allowing the user to sort the login records and export the results into a separate file. These features will be looked at during development to make sure I have enough time to implement and test them properly.

Development and Testing

I plan to develop the command-line version first before moving on to the GUI version. I want both versions to use the same analysis functions so that I do not have to write the same code twice.

As I develop the application, I will test each feature to make sure it works correctly. This will include testing normal login records, incorrect information and situations where the number of failed attempts is close to the warning thresholds.

I also want to make sure I understand the functions I use and how they work, as I will need to explain the application during my demonstration.

GitHub and Version Control

I have created a public GitHub repository for this project and connected it to Visual Studio Code. I plan to commit my progress to GitHub on every day that I work on the application.

Each commit will explain what I have changed or added so that I can keep track of the development process. I also plan to use branches and pull requests when adding new features.

This will help me meet the requirements for Assessment 2 while keeping a record of how the application has developed.