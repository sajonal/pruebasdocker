from flask import Flask, request, render_template_string

app = Flask(__name__)

datos = []

html = """
<h2>Registro simple</h2>

<form method="POST">
Nombre: <input type="text" name="nombre">
<input type="submit" value="Guardar">
</form>

<h3>Datos registrados</h3>
<ul>
{% for d in datos %}
<li>{{d}}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET","POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"]
        datos.append(nombre)
    return render_template_string(html, datos=datos)

app.run(host="0.0.0.0", port=5000)