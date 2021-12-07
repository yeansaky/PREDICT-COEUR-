from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)


model = pickle.load(open('model_pickle', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post_predict', methods=['post', 'get'])
def predict():
    for x in request.form.values():
        if not x:
            erreur = "Rensigner tout les champs"
            return render_template('index.html', erreur=erreur)
    input_valeur = [float(x) for x in request.form.values()]
    tab_np = np.array(input_valeur)
    tab_np = np.reshape(tab_np, (1, -1))

    pred = model.predict(tab_np)
    return render_template('index.html', pred=pred)


if __name__ == "__main__":
    app.run(debug=True)
