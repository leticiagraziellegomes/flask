from flask import Flask

app = Flask(__name__)

@app.route("/medianotas/<x>/<y>/<z>")
def medianotas(x,y,z):
    soma = float(x) + float(y) + float(z)
    media = soma/3
    if(media>=60):
        return "Você foi aprovado"
    elif(media<60):
        return "Você foi reprovado"

    