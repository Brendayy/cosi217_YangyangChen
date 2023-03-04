from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Resource, Api
from ner import SpacyDocument

app = Flask(__name__)
api = Api(app)

class NER(Resource):

    def get(self):
        return {'info': 'api'}

    def post(self):
        input_text = request.get_data(True, True)
        ner = SpacyDocument(input_text)
        entities = ner.get_entities()
        result = []
        for entity in entities:
            [start_index, end_index, label, text] = entity
            # print(start_index, end_index, label, text)
            result.append({'start_index': start_index, 'end_index':end_index, 'label':label, 'text': text})
        return result

class markup(Resource):

    def post(self):
        input_text = request.get_data(True, True)
        ner = SpacyDocument(input_text)
        entities_markup = ner.get_entities_with_markup()
        return entities_markup

api.add_resource(NER, '/api')
api.add_resource(markup, '/api/markup')

markup = ""

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        input_text = request.form["input_text"]
        markup = get_markup(input_text)
        return render_template('report.html', markup = markup)

    return render_template('form.html', get_markup = get_markup)

def get_markup(text):
    ner = SpacyDocument(text)
    markup = ner.get_entities_with_markup()
    return markup
    # print(markup)
    # return redirect(url_for(".report", markup = markup))

# @app.get("/report")
# def report():
#     # markup = request.args["markup"]
#     return render_template(
#         'report.html',
#         # markup = markup
#         )


if __name__ == '__main__':
    app.run(port=5001, debug=True)


'''

curl http://127.0.0.1:5000/

curl http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"name": "sue"}'

curl http://127.0.0.1:5000/multiply/23

'''
