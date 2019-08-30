#!/bin/sh
python installSnmp.py

read -p "Do you want to install and run ireasoning sowfware?[Y/n]: "  userInput

if [ "$userInput" ==  "Y" ]; then
      python ireasoningInstall.py
else
       echo "Thank you for using this program :)"
fi
