# Course Recommendation System using Udemy Dataset
### Algorithm
+ Cosine Similarity
+ Linear Similarity
### Workflow
+ Read Dataset
+ Vectorized our dataset using CountVectorizer
+ Use Algorithm: Cosine Similarity Matrix
+ Get ID, Score
+ Recommend the course

### API
> Get JSON format data in http://127.0.0.1:5000/
+ Hit http://127.0.0.1:5000/?course_title={course name}
   + eg: http://127.0.0.1:5000/?course_title=Computer

> POST course_id and course_title in http://127.0.0.1:5000/course-data/ 
* Note: The data must be in json format.
+ Hit http://127.0.0.1:5000/course-data/
   + eg: {"course_id": 15,"course_title": "The Information Technology"}