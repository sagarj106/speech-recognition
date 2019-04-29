import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source,timeout=3,phrase_time_limit=3)

try:
	text=r.recognize_google(audio)
	print("You said " + r.recognize_google(audio))

except sr.UnknownValueError:
	print("Could not understand audio")

except sr.RequestError as e:
	print("Could not request results; {0}".format(e))