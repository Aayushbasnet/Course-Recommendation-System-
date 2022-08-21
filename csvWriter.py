# Load csv package
import csv
# Load json request
import json
def csvWiter(course_id, course_title):
    with open('data/udemy_courses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # jd = json.loads(jsonData)
        # print(jd)
        # course_id = jd.get("course_id")
        # course_title = jd.get("course_title")
        writer.writerows([[course_id, course_title]])
# csvWiter(json.dumps({"course_title":"Trading Options Basics","similarity_scores":0.5773502692,"course_id":889066}))