# i am using clear to clear the console
clear

#welcome message
echo "Welcome to Elina's program!!"

#validate the existence of cMail.sh file. If not exists because then the program will be terminat
if [ ! -f "cMail.sh" ]
then
	echo "Error!! file cMail.sh not found the program will teminate"
	exit
fi

#loop wilhe fot user validation with defence programming
while [ true ]
do
	# used if to exit the program during user validation
	read -p "Please ENTER User Name or type exit to terminate the program:  " userName

	if [ "$userName" = "exit" ]
	then	
			clear
        	echo "The program will now terminate....."
        	echo "Thank you for using my program"
        	exit
	fi

#i used getent to read from user passwd Operating System database the existence of the userName andi used this one also to validate if the user exists 
  if getent passwd "$userName";
	then
		#asks from user to create a directory
		clear
		read -p "Please enter a directory name to be created: " userInputDir

	#checks if the directory exists if not the file will be replaces
    if [ -d "$userInputDir" ]
    then
    		#check if the file exsts if it does the a message will inform the user
			if [ -d "$userInputDir" ]
			then
				echo ""
				echo "File exists do you want to replace the file?"
				read -p "please enter y or n: " replaceUserChoice
				if [ "$replaceUserChoice" = "y" ]
				then
					mkdir -p "$userInputDir"
				else
					clear
					continue
				fi
			fi
    else
    		#if the file does not exist then the file will be created and inside that file i have create a txt file with all requirements from step 9 of coursework
			mkdir "$userInputDir"
			cd "$userInputDir"
			# i created with > command to overwitten the file because of coursework step 9 requierements
			echo "" > "$userName".txt
			echo "Login information about user: $userName" >> "$userName".txt
			#i used last and head to filter as pipe the first 10 lines
			last "$userName" | head >> "$userName".txt

			#i used who with an if to check if the username is online and if it does then it will append a message to the .txt file. I used grep -q to filter the existance of the user name and quite mode because it doesnt reply anything to the console
		    if who -u | grep -q "$userName"
			  then
				  echo "User: $userName is Online" >> "$userName".txt
			  else
				  echo "User: $userName is Offline" >> "$userName".txt
			  fi
			# last i added date as apeend to .txt file
			date >> "$userName".txt
    fi

    	#i used wile to loop again to the 3 categories menu and choose if you want to exit or send the txt file to the user using cMail
		while [ true  ]
		do
			  clear
			  echo "1 for User logon history"
			  echo "2 to Send user message"
			  echo "3 to exit"

#input the choice from the menu i created
			  read -p "please ENTER your coice: " userChoice

			#i use if to clarify to the user if any incorrect input
			  if [ "$userChoice" != 1 ] && [ "$userChoice" != 2 ] && [ "$userChoice" != 3 ]
			  then
			    clear
			    echo "Input is not VALID please make a VALID input"
			  fi


				if [ "$userChoice" = 1 ]
				then
					clear
					cd "$userInputDir"
					clear
				  	cat "$userName".txt
					echo ""
					#because of while i used read command to pause to selection 1
					read -p "Press ENTER to continue"
	  			fi

	  			if [ "$userChoice" = 2 ]
		  		then
		  			#i used cd .. to move back one file and find the cMail
		  			cd ".."
		  			
		  			#i have run the cMail with two arguments read from a variable userName and userInputDir 
			  		./cMail.sh "$userName" "$userInputDir"
			  		exit
			  	fi

	          	if [ "$userChoice" = 3 ]
				then
				    clear
				    echo "Thank you for using my program"
				    					#because of while i used read command to pause to selection 1

				    read -p "Press ENTER to continue"
				    exit
				fi		
		done
  else
    clear
    echo "user name does not exist in the system please enter a valid user name"
  fi
done