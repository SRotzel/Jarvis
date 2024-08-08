#**What is this project about **

This is just a fun little experiment I am currently "conducting" with the goal of having an AI that can communicate with me,
Use a camera to understand whats going on in the real world, and perhaps even using a beamer to make some sort of 
augmented reality workbench.

#**How to run this project**

In order to run this program, you will have to install Ollama and python, as well as some other libraries listed below
But first, install python and ollama

##*Linux (Change depending on distro)*

'''batch
sudo dnf install python
sudo dnf install ollama

pip install speech_recognition, pyttsx3, ollama
'''

##*Windows*

For windows, you will have to install Ollama from the official website: https://ollama.com
If you already have Python installed, these are the last steps you'll have to complete:
'''batch
pip install speech_recognition, pyttsx3, ollama
'''

#**How to customize the AI**

In this project, there is a "Modelfile" included.
In this file, you can change the prompt you would like to give the AI and 
the AI model it uses. Currently I use gemma2, but there are many others you can choose from,
again also showcased on the Ollama website https://ollama.com

After you have changed the Modelfile to your likings, you have to run these commands
in order to create your own "model"
'''batch
ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>'
'''
and to verify it has worked, you can run
'''batch
ollama run choose-a-model-name
'''

Further instructions on this can be found here: https://github.com/ollama/ollama/tree/main/docs
