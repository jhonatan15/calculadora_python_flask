from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html', valor3 = valor3, resultado = resultado)

#Variables globales
valor1 = ""
valor2 = ""
expr = ""
valor3 = ""
resultado = ""
igual = ""

@app.route('/calculator', methods=['POST'])
def calculadora():
    if request.method == 'POST':
        #recuperar datos de los button del index
        button = request.form['button']
        print(button)

        #Declarar variables globales
        global valor1, valor2, valor3, expr, resultado, igual
        expressions = ["+","-","x","/","%","c"]
        numbers = ["1","2","3","4","5","6","7","8","9","0"]

        for i in numbers:
            if i == button:
                if resultado != "":
                    valor1 = ""
                    valor2 = ""
                    valor3 = ""
                    expr = ""
                    resultado = ""
                    igual = ""
                if expr == "":
                    valor1 = valor1 + button
                else:
                    valor2 = valor2 + button


        for i in expressions:
            if i == button:
                if valor1 != "":
                    expr = button

        if button == "d":
            if resultado != "":
                valor1 = ""
                valor2 = ""
                valor3 = ""
                expr = ""
                resultado = ""
                igual = ""
            if expr == "":
                valor1 = ""
            else:
                valor2 = ""

        valor3 = valor1 + " " + expr + " " + valor2

        if expr == "c":
            valor1 = ""
            valor2 = ""
            valor3 = ""
            expr = ""
            resultado = ""
            igual = ""

        if button == "=":
            igual = "="

        if igual == "=":
            porcentaje = "%"
            if expr == "+":
                resultado = int(valor1) + int(valor2)
            elif expr == "-":
                resultado = int(valor1) - int(valor2)
            elif expr == "x":
                resultado = int(valor1) * int(valor2)
            elif expr == "/":
                resultado = int(valor1) / int(valor2)
            elif expr == "%":
                resultado = int((int(valor1) * int(valor2)) / 100)

        print(button)
        print(valor1)
        print(valor2)
        print(valor3)
        print(igual)
        print(expr)
        print(resultado)
        return render_template('index.html', valor3 = valor3, resultado = resultado)




if __name__ == '__main__':
    app.run(port = 3000, debug = True)
