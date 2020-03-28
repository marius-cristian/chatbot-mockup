# chatbot-mockup


## Project Structure:
	in the ```chatbot``` folder the simple client service can be found

	int the ```DataService``` folder the rest api can be found


## How to run on Ubuntu (alternatively just read the Makefiles):
	
	1. for the data service: ```cd DataService && make start-rest```

	2. for the chatbotservice: ```cd chatbot && make start-chatbot```


## How to add messages in the database:

	navigate to http://localhost:8000/chatmessages/


## To get a random message:

	navigate to http://localhost:8000/random/

## The structure of the Makefiles

	The make files contain shortcuts for different tasks; the naming is explanatory.

## Test Coverage:
	
	Unfortunately the project does not contain any tests due to time constraints.

## Operational Plan

	Please Consult ```Operational Plan.txt```

## Deviation Report:
	
	Please constul ```Report.txt```