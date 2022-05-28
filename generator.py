import random
from js import document
from pyodide import create_proxy

def generate(event):
        s = "Your random number is " + str(random.randint(1,100))

        document.getElementById("output").innerHTML = s

document.getElementById("generate").addEventListener("click", create_proxy(generate))