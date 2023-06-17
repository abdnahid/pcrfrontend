from flask import Flask, send_file
from flask_cors import CORS
from openpyxl import Workbook
import os
from test_report import InspectionExcel

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
    return "Hey there! Its working!"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
