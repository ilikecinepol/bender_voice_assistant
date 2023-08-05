import speech_recognition
import subprocess



sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

# data = 'Привет'
subprocess.run(f'echo {query} | RHVoice-client -s Aleksandr+CLB | aplanano gy', shell=True)