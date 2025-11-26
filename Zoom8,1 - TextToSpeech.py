import tkinter
from gtts import gTTS  # uses this manner for only importing the sub-module
# Google's Text to Seech (gtts)


screen = tkinter.Tk()
screen.geometry("400x400")


def speak():
    text1 = user_input.get()
    speech = gTTS(text=text1, lang="en", slow=False)
    speech.save("TtSSpeech.wav")


title = tkinter.Label(screen, text="Text to Speech")
user_input = tkinter.Entry(screen)
submit_btn = tkinter.Button(screen, text="Submit", command=speak)

title.pack()
user_input.pack()
submit_btn.pack()

screen.mainloop()
