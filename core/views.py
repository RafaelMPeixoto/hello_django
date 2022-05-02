from curses.ascii import HT
import re
from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def calculadora(request, valor1, valor2):
    resultado1 = float(valor1 + valor2)
    resultado2 = float(valor1 * valor2)
    resultado3 = float(valor1 / valor2)
    resultado4 = float(valor1 - valor2)
    return HttpResponse(f'<h1>Valor da soma de {valor1} + {valor2} é {resultado1} <p> A multiplicação de {valor1} x {valor2} é {resultado2}</p> <p>A divisão de {valor1} / {valor2} é {resultado3}</p> <p>A subtração de {valor1} - {valor2} é {resultado4}</p> </h1>')
    



 