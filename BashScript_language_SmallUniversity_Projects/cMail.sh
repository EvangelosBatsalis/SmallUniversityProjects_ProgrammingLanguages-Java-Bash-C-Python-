DIR=$1
clear
#creates the requested log file adding date as append. I used touch because it cannot overwitte the log file
touch cMail.log
date >> cMail.log
#pwd
cd "$DIR"
#pwd
#check if argument has been given and if its not it will inform the user and the program will terminate
if [ $# == 0 ]
then
	echo "No arguments has been given the program now will terminate"
	exit

else
	if [ $# == 1  ]
	then
		pwd
	else
		#i used if to validate the existence of the txt file and it if does not then the program will teminate
		if [ -f "$1".txt  ]
		then
			#if it does not exist then it will terminate
			clear
			echo "File $1.txt not found. the program will now terminate"
			exit
		else
			#if the file exists
			echo "sending email to user: $1"
			mail -s 'Your logon history' "$1"@something.com <<< "$1".txt
			echo ""
			echo "Succesful script execution"
			echo "Thank you for using my program"
			echo ""
			exit
		fi
	fi
fi
