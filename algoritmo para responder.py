# Importar
import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init()
voice_id = 'spanish-latin-am'
engine.setProperty('voice',voice_id)
rate = engine.getProperty('rate')

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline


the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)

"""import csv

with open('C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Respuestas de texto/textos.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)"""



# Ejemplo tokenización
contexto = "miguel"
pregunta = '¿cómo me llamo?'

encode = tokenizer.encode_plus(pregunta, contexto, return_tensors='pt')
input_ids = encode['input_ids'].tolist()
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
for id, token in zip(input_ids[0], tokens):
  print('{:<12} {:>6}'.format(token, id))
  print('')

# Ejemplo de inferencia (pregunta-respuesta)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
salida = nlp({'question':pregunta, 'context':contexto})
print(salida)


import speech_recognition as sr

from textwrap import wrap

def pregunta_respuesta(model, contexto, nlp):
  
  # Imprimir contexto
  print('Contexto:')
  print('-----------------')
  print('\n'.join(wrap(contexto)))

  # Loop preguntas-respuestas:

#######################
  continuar = True
  while continuar:
    r = sr.Recognizer()
  
    with sr.Microphone() as source:
      print("Say Something...")
      audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        print("What did you say: {}".format(text))
    except:
        print("I am sorry! I can not understand!")
        text="no hay pregunta"
    print('\nPregunta:')
    print('-----------------')
    pregunta = str("¿"+"{}".format(text)+"?")

    continuar = pregunta!=''

    if continuar:
      salida = nlp({'question':pregunta, 'context':contexto})
      print('\nRespuesta:')
      print('-----------------')
      print(salida['answer'])
      engine.say(salida['answer'])
      engine.runAndWait()
      engine.stop()

    if (text=="no hay pregunta"):
      salida = nlp({'question':pregunta, 'context':contexto})
      respuesta="Podrias decirlo mas despacio"
      print(respuesta)
      engine.say(respuesta)
      engine.runAndWait()
      engine.stop()


contexto="Decir Coca-Cola es sinónimo de fiesta, celebración o quedada con amigos. Esta bebida universal, creada en Atlanta un 8 de mayo de 1886, se sirve de la misma manera en cumpleaños infantiles o barras de discotecas. Su historia arranca hace 132 años en el pequeño laboratorio del farmacéutico John S. Pemberton quien quería crear un jarabe contra los problemas de digestión que además aportase energía, incluso se llegó a decir que en la fórmula inicial había un porcentaje de cocaína algo que la compañía siempre ha negado. La farmacia Jacobs fue la primera en comercializar el preparado a un precio de 5 centavos el vaso, vendiendo unos nueve cada día. Era solo el inicio de una historia que ha convertido a la Coca-Cola en la bebida más famosa del mundo."

pregunta_respuesta(model, contexto, nlp)
