
# Flask Dependencies
from flask import Flask, jsonify, request, redirect, Blueprint, render_template
from flask_restplus import Api, Resource, fields
import cosine
import data
import re

# Custom Imports
import database

# Initialize Flask Application
app = Flask(__name__)


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


# Load Abstract Texts from DB
query = """ SELECT ar.AcademicRecordID, ar.Title, ar.PublicationId, ara.AbstractText
                FROM    CompSciPublications.AcademicRecord AS ar,
                        CompSciPublications.AcademicRecordAbstract AS ara
                WHERE   ar.AcademicRecordID=ara.AcademicRecordID
        """
abstracts = []
academic_record_list = database.execute_query(query)
for academic_record in academic_record_list:
    abstract_text = academic_record['AbstractText']
    title_text = academic_record['Title']
    abstracts.append((title_text, cleanhtml(abstract_text)))


@app.route("/",  methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        print("get")
        return render_template('index.html', sorted_data=[])
    else:
        user_given_abstract = request.form['abstract']
        # threshold = request.form['threshold']
        threshold = .20

        # Calculate Cosine Similarities
        cos_sim = cosine.cosine_helper(user_given_abstract, abstracts)
        filtered_data = data.filter_data(cos_sim, threshold)
        sorted_data = data.sort_data(filtered_data)
        data.print_data(user_given_abstract, sorted_data)

        no_result = (len(sorted_data) == 0)
        return render_template('index.html', sorted_data=sorted_data, no_result=no_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_debugger=False,
            use_reloader=False, passthrough_errors=True)
