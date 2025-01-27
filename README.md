# ingresarAHaxballElo

## Description

This is a web scrapping project in python that uses selenium to enter into a haxball automaticaly, iterating until the room has some free space or it doesnt exist.

It uses the following libraries:

+ Selenium
+ dotenv

## Instalattion

Before running the application you must run the following bash' commands if you didn't have installed some of the libraries used in the program:

+ `pip install selenium`
+ `pip install python-dotenv`

And after that, you should be able to run the code correctly without any errors

Then, for running the program correctly you should:

+ Set the .env enviorement to have your own auth, name, geo location and password
    + To have your own auth and geo, you can:
    
        1. Press f12,
        1. Go to storage
        1. Click in Local Storage
        1. Open the https://www.haxball.com
        1. Search the key tgat says: 'player_auth_key'
        1. Copy that key and paste it into the .env
        1. For the geo, do the same, but instead of search for 'player_auth_key', look for 'geo' 

## Features
The program allows you to:
+ Set your name custom
+ Set the custom extrapolation
+ Store your password and avoid to log in every time you enter into the room
+ Enter automaticaly into the room without the need to click every time to verify that the room is not complete

Future features:
+ Custom the web browser to be able to be in dark mode
+ Custom the web to have a default value in case none player name is set, and the same with the password and extrapolation
