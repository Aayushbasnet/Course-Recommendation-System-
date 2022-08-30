# Load Exploratory Data Analysis(EDA) Packages
from operator import index
import pandas as pd
# removes unnecessary characters (filtering)
import neattext.functions as nfx       

# Load ML/RC Packages
# convert text into vectors
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer   
# our algorithm to check how similar out two documents are
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

def trainData():
    # Load out dataset
    df = pd.read_csv("data/udemy_courses.csv")  # df: data frame
    # print(df['course_title'])
    # print(dir(nfx))

    #Clean Text: stopwords,special characters
    df['clean_course_title'] = df['course_title'].apply(nfx.remove_stopwords)
    df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)
    # print(df[['course_title', 'clean_course_title']])

    #Vectorize our Text
    count_vect = CountVectorizer()
    cv_matrix = count_vect.fit_transform(df['clean_course_title']) # vectorized data
    # print(cv_matrix.todense())
    
    df_cv_words = pd.DataFrame(cv_matrix.todense(), columns=count_vect.get_feature_names_out())
    # print(df_cv_words.head())

    # Cosine Similarity Matrix
    cosine_sim_mat = cosine_similarity(cv_matrix)
    # print(cosine_sim_mat)
    # import seaborn as sns
    # sns.heatmap(cosine_sim_mat[0:10], annot=True)


    # print(df.head())

    # Get Course ID/Index and interchanging indices and course
    course_indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    return df, cosine_sim_mat, course_indices
    # print(course_indices['Beginner to Pro - Financial Analysis in Excel 2017'])

    # idx = course_indices['How To Maximize Your Profits Trading Options']
    # # print(idx)

    # scores = list(enumerate(cosine_sim_mat[idx]))
    # # print(cosine_sim_mat[idx])

    # # Sort our scores per cosine score
    # sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True) # revers - descending order
    # # ommiting itself/First value
    # sorted_scores = sorted_scores[1:]
    # # print(sorted_scores[0:10])

    # # Selected Courses Indices
    # selected_course_indices = [i[0] for i in sorted_scores] # short form for:
    #                                                             # selected_course_indices = []
    #                                                             # for i in sorted_scores:
    #                                                             #     selected_course_indices .append(i[0])
    #                                                             # print(selected_course_indices)
        
    # # Selected Courses Scores
    # selected_courses_scores = [i[1] for i in sorted_scores]

    # # Display course name (Recommend)
    # recommend_course_name = df['course_title'].iloc[selected_course_indices]
    # # print(recommend_course_name)
    # recv_df= pd.DataFrame(recommend_course_name)
    # # print(recv_df[0:15])

    # recv_df['similarity_scores'] = selected_courses_scores
    # # print(recv_df[0:15])


def recommend_course(title, number_of_recv):
    df, cosine_sim_mat, course_indices= trainData()
    # ID for title
    idx= course_indices[title]
    # print(idx)
    # Course Indices
    # Search inside cosine_sim_mat
    scores = list(enumerate(cosine_sim_mat[idx]))
    # Scores
    # Sort Scores
    sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)
    # sorted_scores = sorted_scores[1:]
    # sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)
    # Recommend
    selected_course_indices = [i[0] for i in sorted_scores]
    selected_course_scores = [i[1] for i in sorted_scores]
    recommend_course_name = df['course_title'].iloc[selected_course_indices]
    # print(df['course_id'].iloc[selected_course_indices])
    recv_df = pd.DataFrame(recommend_course_name)
    # print(recv_df)
    recv_df['similarity_scores'] = selected_course_scores
    recv_df['course_id'] = df['course_id']
    # Slecting top 10 course whose scores are greater than 0
    count = 0
    remove_course_index = 0
    for i in recv_df['course_title'].head(number_of_recv):
        if i == title :
            # print("found", i)
            remove_course_index = recv_df['course_title'].index.values[count]
        count += 1

    # # changing index to course_id if necessary
    # recv_df = recv_df.set_index('course_id') 
       
    # converting the result to json format for api
    sendJson = recv_df.drop(remove_course_index).head(number_of_recv).to_json(orient='index')
    print("remove_course_index:", remove_course_index)
    # print(sendJson)
    return sendJson

# result = recommend_course('Information Technology', 10)
# print(result)