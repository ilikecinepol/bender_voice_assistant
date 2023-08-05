GNU
nano
4.8
gpt_answer.py
import speech_recognition
import subprocess
import openai
from ai_key import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
engine = "text-davinci-003"
sr = speech_recognition.Recognizer()


def question():
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query


# data = 'Привет'
# subprocess.run(f'echo {query} | RHVoice-client -s Aleksandr+CLB | aplanano gy', shell=True)


# Функция для ChatGPT
def ask(prompt):
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=1000)
    print('Вопрос:', prompt)
    print('\nОтвет:')
    query = completion.choices[0]['text']
    subprocess.run(f'echo "{query}" | RHVoice-client -s Aleksandr+CLB | aplay', shell=True)


speech = question()
ask(speech)
