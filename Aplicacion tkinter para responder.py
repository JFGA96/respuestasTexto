from typing import Literal
import pyttsx3
from pyttsx3 import engine
import tkinter as tk
from tkinter import ttk
from textwrap import wrap
import speech_recognition as sr
from textwrap import wrap
from tkinter import *
from tkinter import messagebox

##Seleccion de voz y rate################################
engine = pyttsx3.init()
voice_id = 'spanish-latin-am'
engine.setProperty('voice',voice_id)
rate = engine.getProperty('rate')
##########################################################

##############Seleccion de modelo ###########################################
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)
############################################################################

pregunta="coca cola"
archivo = open('C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Respuestas de texto/nuevo.txt',mode='r',encoding='utf-8')
contexto = str(archivo.read().splitlines())
archivo.close()
#contexto="La Universidad La Gran Colombia es una entidad de derecho privado, sin ánimo de lucro, constituida como una corporación y consagrada a la promoción de la cultura profesional de los pueblos iberoamericanos y al afianzamiento de los vínculos históricos entre éstos.Conforme a la voluntad del fundador Julio César García, la Universidad La Gran Colombia inicia sus labores en febrero de 1951, año en que se firma la primera carta fundacional. En el año de 1953 recibió la personería jurídica mediante la resolución número 47 expedida por el Ministerio de Justicia, en la cual se configura el carácter de la Institución que, interpretado a través de sus principios, ha permitido la armonización entre el pensamiento y la realización de su misión transformadora. Universal por definición, atenderá a todos los frentes de la cultura y la formación humana, preferentemente el fomento de la investigación científica y tecnológica y la enseñanza a los hombres de trabajo en las técnicas profesionales, las tecnologías de punta o las profesiones o disciplinas que racionalizan sus procesos productivos mediante los programas de pregrado y seminarios de formación continuada que garanticen la formación permanente y la promoción de estudios de profundización e investigación y de alta cultura para postgraduados en programas académicos de especializaciones, maestrías y doctorados. Los valores de la universidad son bolivariana,Cristiana,Hispanica y solidaria. Es solidaria Porque está comprometida con la educación de las gentes de menores recursos económicos y con la promoción permanente de la cultura de la solidaridad. Es hispanica Porque se constituye en una defensa permanente de los valores culturales heredados de la Madre Patria. Es Bolivariana Porque fiel a los ideales del Libertador, contribuye a la integración de los pueblos hispanoamericanos en general y grancolombianos en particular, para gestar una nueva civilización. Es cristiana Porque está dedicada a la afirmación de la dignidad humana y a la búsqueda comunitaria de la verdad. El rector de la universidad La gran colombia es Marco Tulio Calderón Peñaloza. El vicerrector de innovacion y empresarismo de la universidad La gran colombia es Victor Manuel Perez Argüelles"
# Ejemplo tokenización

encode = tokenizer.encode_plus(pregunta, contexto, return_tensors='pt')
input_ids = encode['input_ids'].tolist()
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
for id, token in zip(input_ids[0], tokens):
  #print('{:<12} {:>6}'.format(token, id))
  print('')

# Ejemplo de inferencia (pregunta-respuesta)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
salida = nlp({'question':pregunta, 'context':contexto})


def pregunta_respuesta_escrito(model, contexto, nlp,pregunta):
  
  # Imprimir contexto
  print('Contexto:')
  print('-----------------')
  #print('\n'.join(wrap(contexto)))
  # Loop preguntas-respuestas:
#######################
  print('\nPregunta:')
  print('-----------------')
  print(pregunta)
    #pregunta = str(input())
    
    #pregunta = str("¿"+"{}".format()+"?")

  continuar = pregunta!=''

  if continuar:
    salida = nlp({'question':pregunta, 'context':contexto})
    print('\nRespuesta:')
    print('-----------------')
    print(salida['answer'])
    entrada.set(salida['answer'])
    engine.say(salida['answer'])
    engine.runAndWait()
    engine.stop()
    #messagebox.showinfo('Respuesta', ''+salida['answer'])
    #mesajeTxt2['text']=(salida['answer'])

      
def pregunta_respuesta_escuchar(model, contexto, nlp):
  
  # Imprimir contexto
  print('Contexto:')
  print('-----------------')
  #print('\n'.join(wrap(contexto)))

  # Loop preguntas-respuestas:
#######################
  
  
  r = sr.Recognizer()
    
  with sr.Microphone() as source:
    #labelestado['text']="Escuchando"
    print("Say Something...")
    audio = r.listen(source)

  try:
    text = r.recognize_google(audio, language='es-ES')
    print("What did you say: {}".format(text))
  except:
    print("I am sorry! I can not understand!")
    text="no hay pregunta"
    labelestado['text']=text
      
  

  print('\nPregunta:')
  print('-----------------')
  pregunta="¿"+text+"?"
  mesajeTxt.delete(1.0,"end")
  mesajeTxt.insert(1.0,pregunta)
  print(pregunta)
    #pregunta = str(input())
    
    #pregunta = str("¿"+"{}".format()+"?")

  continuar = pregunta!=''

  if continuar:
      salida = nlp({'question':pregunta, 'context':contexto})
      print('\nRespuesta:')
      print('-----------------')
      entrada.set(salida['answer'])
      print(salida['answer'])
      engine.say(salida['answer'])
      engine.runAndWait()
      engine.stop()
      
      
      



def guardardatos():
    mensaje=mesajeTxt.get(1.0, "end-1c")
    newmensaje=StringVar()
    newmensaje=mensaje
    if botonguardar:
        pregunta_respuesta_escrito(model, contexto, nlp,newmensaje)

def escuchardatos():
    escuchar=int()
    escuchar=1
    if botonEscuchar:
        pregunta_respuesta_escuchar(model, contexto, nlp)
    return(escuchar)
    


ventana= Tk()
ventana.title("Aplicacion pregunta-respuesta")
ventana.geometry("400x500")
ventana.maxsize(400, 500)

miframe=Frame(ventana)
miframe.grid()

labelTitle = tk.Label(miframe, text="Preguntame acerca de \n La universidad La Gran Colombia", font=('Microsoft Sans Serif',14, 'bold'))
labelTitle.grid(row=0, column=0,padx=20,pady=0)


labelpregunta= tk.Label(miframe,text="Pregunta",font=("Poppins",12))
labelpregunta.grid(row=1, column=0,padx=0,pady=5)

labelestado= tk.Label(miframe,text="",font=("Poppins",12),fg='red')
labelestado.grid(row=5, column=0,padx=5,pady=5)

labelrespuesta= tk.Label(miframe,text="Respuesta",font=("Poppins",12),fg='red')
labelrespuesta.grid(row=7, column=0,padx=5,pady=5)

mesajeTxt= Text(miframe,width=45,height=5)
mesajeTxt.grid(row=3, column=0,padx=10,pady=1)

#labelrespuesta= Label(miframe,font=("Poppins",12),fg='red')
#labelrespuesta.grid(row=7, column=0,padx=0,pady=5)
entrada=StringVar()
#mesajeTxt2= Text(miframe,width=45,height=5)
#mesajeTxt2.grid(row=7, column=0,padx=10,pady=1)
campo=Entry(miframe,textvariable=entrada,width=50,fg='red')
campo.grid(row=8, column=0,padx=10,pady=1)

mensajeNombre = StringVar()

etiquetacombo=Label(fg="red",font=("Popinns",12))
#etiquetacombo.grid(row=8, column=0,padx=20,pady=1)

botonguardar= Button(miframe,text="guardar",fg="black",font=("Poppins",12), command=guardardatos)
botonguardar.grid(row=4, column=0,padx=0,pady=5)

botonEscuchar= Button(miframe,text="escuchar",fg="black",font=("Poppins",12), command=escuchardatos)
botonEscuchar.grid(row=6, column=0,padx=0,pady=50)

ventana.mainloop()
