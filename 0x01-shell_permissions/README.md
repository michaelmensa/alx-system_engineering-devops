#!/bin/bash
Shell permissions
Task 0; su -l [other_user]
Task 1; whoami displays the current working user.
Task 2; id -ng displays all the groups (names not id) the current user is in.
Task 3; sudo chown user some_file changes the owner of some_file to user.
Task 4; touch file_1 creates an empty file_1  
Task 5; chmod octal file_1
Task 6; chmod octal file_1 multiple permissions
Task 7; chmod a+x hello gives permissions to read and execute the file hello the owner, group and the world
Task 8; chmod 007 hello James Bond
Task 9; chmod 753 hello John Doe
Task 10; chmod reference=olleh hello mirror permissions
Task 11; chmod u+X * change all subdirectories of the working directory to executable. 
