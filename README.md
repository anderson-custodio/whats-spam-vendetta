# WhatsApp Spam Vendetta

After getting tired of receiving spam calls all the time, I decided to create a script to discourage spammers from continuing to call me.  
If you want to send a lot of messages to a target whatsapp number, follow the procedures below.

## Pre-requisites

First you have to install the dependencies running: `pip install -r requirements.txt`.  
Then you need to access your whatsapp web and get the x,y coordinates of the field where you write the message and also of the send the message button.  
You can get coordinates using `xdtool` on Ubuntu running the commands: `sudo apt-get install xdtool` and then `while sleep 1; do xdotool getmouselocation; done`  
Get the coordinates of a maximized whatsapp window and use the script on a maximized window too.  
With the coordinates, follow the next step to send the messages.

## How to use

Run `python main.py <phone number> <message input x, y coordinates> <send button x, y coordinates>`, for example: `python main.py +5511999999999 1570 1620 1030 /tmp/whats-spam-vendetta/matrix_small.txt`.  
You can create a file with your custom messages and the script will send it line by line.

## Caution

Start by using a very small message file to see how the script works. As the mouse is busy while running the script you will not be able to use the computer while it is running.  
Remember that you are solely responsible for your actions. Be careful not to break the laws of your territory.
