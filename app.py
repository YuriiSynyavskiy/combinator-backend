from flask import Flask
from flask import request
from flask import jsonify
from .utils import AnalyzeText
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)
cors = CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    uploaded_file = request.files['file']
    filters = dict(request.form)
    if not uploaded_file.filename.split(".")[1] == "docx":
        return jsonify({"message": "File type must be .docx"}), 400
    matched_data = AnalyzeText(uploaded_file, filters).analyze_file()
    return jsonify({"message": matched_data}), 200


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
