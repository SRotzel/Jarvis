import ollama
import speech_recognition as sr
import pyttsx3 as tts

class Jarvis:
    def __init__(self) -> None:
        print("Booting up!\n...")

        self.abortCommands = ["abort", "exit", "terminate"]
        self.vengine = tts.init()
        voices = self.vengine.getProperty('voices')
        self.vengine.setProperty('voice', voices[1].id)

        print("Done!")
    
    ##--- In and output per voice---##
    def listen(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            print("Listening...")
            #recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source) # check if audio is valid, could cause errors!!!
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
    def speak(self, text):     
        self.vengine.say(text)
        self.vengine.runAndWait()
    ##--- In and output per voice---##

    def communicate(self, m):
        return ollama.chat(model='Jarvis', messages=[
            {
                'role': 'user',
                'content': m,
            },
        ])
    
    def process(self, commands):
        response = self.communicate(commands)
        print(response['message']['content'])
        self.speak(response['message']['content'])

        if any(c in commands for c in self.abortCommands):
            return False
        return True

# make this its own file main.py 
def main():
    j = Jarvis()
    keepRunning=True

    while keepRunning:
        i = j.listen()
        print("Processing: "+i)
        keepRunning = j.process(i)

if __name__ == "__main__":
    main()