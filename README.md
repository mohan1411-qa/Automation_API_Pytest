## API Automation Framework
 Developoed API Automation Framework using python, pytest and request library to automate REST APIs.

 ## Project
Automated rest api's using request library.

# Framework structure 
1. Logs :- Contains the automation logs to debug the scripts.
2. TestSuite :- Contains different folder of app modules. Under app modules will have test methods.
3. Utilities :- All the utils methods declared under utilities
     1. Config Utils :- Methods related to tests config declared under config utils
     2. Env Utils :- All environment related should come under env utils.
     3. Http utils :- GET, POST, UPDATE, PATCH, PUT methods related methods declared under http_utils.
     4. Json utils :- All the json related methods would be declared under this folder.
     5. Log utils :- Logs related method would be under this folder.
4. Assertion :- All assertions method should declare under assertion folder. So that we can reuse it for other test cases as well.
5. Environment :- All the enviroment config have kept under this folder. Based on user input test will pick the config.
                 1. All the endpoints of api also kept here.

6. Payloads :- Requests payload have kept in payload folder.

## How to run the tests
You can the tests in two ways : 
  1.Using IDE 
  2.Using Command Line py.test -s -v <script_path>

## Requirements
  1. Python
  2. Request library
  3. Pytest

## DB Connection
Yet to implement
  
 
