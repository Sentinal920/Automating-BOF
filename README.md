# Automating-BOF-OSCP
This was made just for the OSCP BOF, and this helped me to complete OSCP BOF exam machine under 15mins.
 
For practice you can use tryhackme bof room which is similar to oscp
https://tryhackme.com/room/bufferoverflowprep

## Step-1
Edit CONFIG.py

Start by editing config.py file with correct values.

## Step-2
Run ./1.py 

Keep restarting immunity when asked and note down offset value once found

![Automating BOF](https://github.com/Sentinal920/Automating-BOF/raw/main/images/automatebof.png)

## Step-3
change offset value in 2.py and run with any arguments to find badchars

./2.py badchars

## Step-4
Run ./2.py and enter found badchars along with first found address

## Step-5
Generate msfvenom payload, replace the payload in 3.py

Edi the value of offset  and retn variable

Run ./3.py to get the shell back
