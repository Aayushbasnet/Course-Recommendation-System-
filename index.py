from pickle import GET
from flask import Flask, jsonify,request
from csvWriter import csvWiter
from main import recommend_course
# Import Module
# import json
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def sendData():
    # eg: hit http://127.0.0.1:5000/?course_title=Computer 
    if request.method == 'GET':
        course_title = request.args.get('course_title')
        rc = recommend_course(course_title, 10)
        return rc
    # return json.dumps(rc)
    
@app.route('/course-data/', methods = ['POST'])
def courseData():
    print("I am course data")
    if request.method == 'POST':
        data = request.json
        course_id = data['course_id']
        course_title = data['course_title']
        # print(request.json)
        csvWiter(course_id, course_title)
        recommend_course(course_title, 10)
        return jsonify({"response":"Ok"})
    
if __name__ == '__main__':
    app.run(debug=True)