import json, pyaudio
from vosk import Model, KaldiRecognizer
import openai
from ai_key import OPENAI_API_KEY
import subprocess

openai.api_key = OPENAI_API_KEY
engine = "text-davinci-003"
model = Model('vosk-model-small-ru-0.22')
rate = 44100
rec = KaldiRecognizer(model, rate)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=rate)
stream.start_stream()


# Функция для ChatGPT
def ask(prompt):
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=1000)
    print('Вопрос:', prompt)
    print('\nОтвет:')
    print(completion.choices[0]['text'])

# Функция прослушивания микрофона
def listen():
    while True:
        data = stream.read(400, exception_on_overflow=False)
        if rec.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer['text']:
                yield
                answer['text']


for text in listen():
    if 'привет' in text:
        subprocess.run(f'echo "Я люблю вас, мешки с мясом!" | RHVoice-client -s Aleksandr+CLB | aplay', shell=True)
    print(text)
