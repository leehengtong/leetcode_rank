import requests
import json
from tqdm import tqdm


def get_question_list():
    res = requests.get('https://leetcode.com/api/problems/all/').json()
    questions = {}
    for item in res["stat_status_pairs"]:
        stat = item['stat']
        questions[stat['question_id']] = {}

        questions[
            stat['question_id']]["question__title"] = stat["question__title"]
        questions[stat['question_id']]["question__title_slug"] = stat[
            "question__title_slug"]
        questions[
            stat['question_id']]["question__hide"] = stat["question__hide"]
        questions[stat['question_id']]["total_acs"] = stat["total_acs"]
        questions[
            stat['question_id']]["total_submitted"] = stat["total_submitted"]
        questions[stat['question_id']]["frontend_question_id"] = stat[
            "frontend_question_id"]
        questions[
            stat['question_id']]["is_new_question"] = stat["is_new_question"]
        questions[
            stat['question_id']]["difficulty"] = item['difficulty']["level"]
        questions[stat['question_id']]["paid_only"] = item["paid_only"]

    return questions


def get_question_info(titleSlug):
    query = {
        "operationName":
        "questionData",
        "variables": {
            "titleSlug": titleSlug
        },
        "query":
        """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    boundTopicId
    title
    titleSlug
    content
    translatedTitle
    translatedContent
    isPaidOnly
    difficulty
    likes
    dislikes
    isLiked
    similarQuestions
    contributors {
      username
      profileUrl
      avatarUrl
      __typename
    }
    langToValidPlayground
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    companyTagStats
    codeSnippets {
      lang
      langSlug
      code
      __typename
    }
    stats
    hints
    solution {
      id
      canSeeDetail
      __typename
    }
    status
    sampleTestCase
    metaData
    judgerAvailable
    judgeType
    mysqlSchemas
    enableRunCode
    enableTestMode
    envInfo
    libraryUrl
    __typename
  }
}
"""
    }
    res = requests.post('https://leetcode.com/graphql',
                        json=query).json()['data']['question']
    info = {}
    info["questionId"] = res["questionId"]
    info["questionFrontendId"] = res["questionFrontendId"]
    info["boundTopicId"] = res["boundTopicId"]
    info["title"] = res["title"]
    info["titleSlug"] = res["titleSlug"]
    info["translatedTitle"] = res["translatedTitle"]
    info["translatedContent"] = res["translatedContent"]
    info["isPaidOnly"] = res["isPaidOnly"]
    info["difficulty"] = res["difficulty"]
    info["likes"] = res["likes"]
    info["dislikes"] = res["dislikes"]
    info["isLiked"] = res["isLiked"]
    info["similarQuestions"] = res["similarQuestions"]
    info["contributors"] = res["contributors"]
    info["topicTags"] = res["topicTags"]
    info["link"] = "https://leetcode.com/problems/" + titleSlug

    return info


def Difficulty(value):
    if value == 1:
        return 'Easy'
    elif value == 2:
        return 'Medium'
    elif value == 3:
        return 'Hard'
    else:
        return 'Unknown'


if __name__ == "__main__":
    questions = get_question_list()
    data = {}

    question_ids = list(questions.keys())
    for i in tqdm(range(len(question_ids))):
        question_id = question_ids[i]
        question = questions[question_id]
        if question['question__hide']:
            continue

        info = get_question_info(question['question__title_slug'])
        topics = [topic['name'] for topic in info['topicTags']]
        difficulty = Difficulty(question['difficulty'])
        similars = []
        for item in json.loads(info['similarQuestions']):
            similars.append({
                'title': item['title'],
                'titleSlug': item['titleSlug']
            })

        data[question_id] = {
            "questionId":
            int(info["questionId"]),
            "questionFrontendId":
            int(info["questionFrontendId"]),
            "boundTopicId":
            info["boundTopicId"],
            "title":
            info["title"],
            "titleSlug":
            info["titleSlug"],
            "isPaidOnly":
            info["isPaidOnly"],
            "difficulty":
            difficulty,
            "likes":
            info["likes"],
            "dislikes":
            info["dislikes"],
            "isLiked":
            info["isLiked"],
            "similarQuestions":
            similars,
            "topicTags":
            topics,
            "link":
            "https://leetcode.com/problems/" +
            question['question__title_slug'],
            "question__hide":
            question["question__hide"],
            "total_acs":
            question["total_acs"],
            "total_submitted":
            question["total_submitted"],
            "is_new_question":
            question["is_new_question"],
            "paid_only":
            question["paid_only"]
        }

    with open("data.js", 'w') as f:
        json.dump(list(data.values()), f)
