import openai
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())
client = openai.Client()
modelo = "gpt-4o"

def geracao_texto(mensangens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model = modelo,
        temperature=0,
        max_tokens=1000,
        stream=True    
    )
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    mensagens.append({'role': 'assitant', 'content': texto_completo})
    return mensagens
if __name__ == '__main__':
    os.system("cls")
    print('Meu Primeiro ChatBot! Ola Mundo da AI')
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role': 'user', 'content': input_usuario})
        mensagens = geracao_texto(mensagens)     