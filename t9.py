import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                return False
                break
        else:
            return True
            break
    N = int(input("Digite um valor: "))
    cont = 0
    num = 2
    primos = ""
    while cont <= N:
        if ehprimo(num) is True:
            primos = primos + str(num)+","
            cont += 1
        num = num + 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

