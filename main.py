import speech_recognition

sr = speech_recognition.Recognizer()
# cmd start in the end voice action
sr.pause_threshold = 0.6
with speech_recognition.Microphone(device_index=0) as mic:
    # filter noises
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()

print(query)


def welcome():
    print("Hello Creator !")


if "amadeus" in query:
    if "amadeus начни программу" in query:
        welcome()
    else:
        print("suck")

