from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

resources = [
    {
        "title": "B2 Conditionals gramar practice",
        "skill": "grammar",
        "level": "B2",
        "type": "grammar",
        "topic": "conditionals",
        "link": "https://englishwithchristian.com/b2-conditionals/"
    },

    {"title": "B2 reported speech grammar practice",
        "skill": "grammar",
        "level": "B2",
        "type": "grammar",
        "topic": "reported speech",
        "link": "https://englishwithchristian.com/b2-reported-speech/"
    },
        {

    "title": "B2 Vocabulary practice: holidays",
        "skill": "vocabulary",
        "level": "B2",
        "type": "vocabulary",
        "topic": "holidays",
        "link": "https://englishwithchristian.com/b2-vocabulary-holidays/"
    },

     {

    "title": "B2 Vocabulary practice: health and lifestyle",
        "skill": "vocabulary",
        "level": "B2",
        "type": "vocabulary",
        "topic": "health and lifestyle",
        "link": "https://englishwithchristian.com/b2-vocabulary-health-lifestyle/"
    },

    {

    "title": "B2 Vocabulary practice: health and lifestyle",
        "skill": "vocabulary",
        "level": "B2",
        "type": "vocabulary",
        "topic": "health and lifestyle",
        "link": "https://englishwithchristian.com/b2-vocabulary-health-lifestyle/"
    },

    {

    "title": "B2 Exam practice: use-of-english-part-1-quiz-1/",
        "skill": "vocabulary",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 1 Use of English B2",
        "link": "https://englishwithchristian.com/use-of-english-part-1-quiz-1/"
    },

    {

    "title": "B2 Exam practice: use-of-english-part-2-quiz-1/",
        "skill": "grammar",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 2 Use of English B2",
        "link": "https://englishwithchristian.com/b2-use-of-english-part-2-quiz-1/"
    },

      {

    "title": "B2 Exam practice: use-of-english-part-3-quiz-1/",
        "skill": "vocabulary/ grammar",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 3 Use of English B2",
        "link": "https://englishwithchristian.com/b2-use-of-english-part-3-quiz-1/"
    },

     {

    "title": "B2 Exam practice: use-of-english-part-4-quiz-1/",
        "skill": "vocabulary/ grammar",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 4 Use of English B2",
        "link": "https://englishwithchristian.com/b2-use-of-english-part-4-quiz-1/"
    },

  {

    "title": "B2 Exam practice: use-of-english-part-5-quiz-1/",
        "skill": "reading",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 5 Use of English B2",
        "link": "https://englishwithchristian.com/b2-reading-part-5-multiple-choice-reading-comprehension-quiz-1/"
    },
   
    {

    "title": "B2 Exam practice: use-of-english-part-6-quiz-1/",
        "skill": "reading",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 6 Use of English B2",
        "link": "https://englishwithchristian.com/b2-first-reading-part-6-gapped-text-missing-sentences-quiz-1/"
    },

 {

    "title": "B2 Exam practice: use-of-english-part-7-quiz-1/",
        "skill": "reading",
        "level": "B2",
        "type": "exam practice",
        "topic": "Part 7 Use of English B2",
        "link": "https://englishwithchristian.com/b2-first-reading-part-7-multiple-matching-short-texts-with-questions/"
    },

   {

    "title": "B1 Video Grammar Quiz",
        "skill": "Grammar",
        "level": "B1",
        "type": "video quiz",
        "topic": "B1 Video Quiz",
        "link": "https://www.youtube.com/watch?v=_9WbTMaRNg8"
    },
 
    
]


def chatbot(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return """
        Hi! I can help you find English practice activities.<br><br>
        Try asking for:<br>
        • B2 grammar<br>
        • vocabulary practice<br>
        • speaking exam practice
        """

    if "bye" in message:
        return "Goodbye!"

    if "help" in message:
        return """
        You can ask me things like:<br><br>
        • B2 grammar<br>
        • vocabulary practice<br>
        • speaking exam practice<br>
        • B1 video lesson
        """

    if "what should i practice" in message:
        return """
        For B2 English you should practise:<br><br>
        • grammar<br>
        • vocabulary<br>
        • reading<br>
        • exam tasks<br><br>
        Try asking for: <strong>B2 grammar</strong>
        """

    if "i don't know what to study" in message:
        return """
        You could start with:<br><br>
        • B2 grammar practice<br>
        • B2 vocabulary activities<br>
        • B2 exam practice<br><br>
        Try typing: <strong>B2 grammar</strong>
        """

    levels = ["a2", "b1", "b2", "c1"]

    skill_keywords = {
        "grammar": ["grammar", "grammatical"],
        "vocabulary": ["vocabulary", "words", "word"],
        "reading": ["reading", "read"],
        "speaking": ["speaking", "speak"],
        "listening": ["listening", "listen"],
        "writing": ["writing", "write"]
    }

    topic_keywords = {
        "conditionals": ["conditional", "conditionals"],
        "reported speech": ["reported speech", "reporting verbs"],
        "exam practice": ["exam", "exam practice", "fce", "b2 first", "use of english"],
        "holidays": ["holiday", "holidays", "travel"],
        "health and lifestyle": ["health", "lifestyle", "healthy living"]
    }

    found_level = None
    found_skill = None
    found_topic = None

    for level in levels:
        if level in message:
            found_level = level.upper()

    for skill, keywords in skill_keywords.items():
        for keyword in keywords:
            if keyword in message:
                found_skill = skill
                break
        if found_skill:
            break

    for topic, keywords in topic_keywords.items():
        for keyword in keywords:
            if keyword in message:
                found_topic = topic
                break
        if found_topic:
            break

    matches = []

    for r in resources:
        score = 0

        if found_level and r["level"].lower() == found_level.lower():
            score += 2

        if found_skill and found_skill in r["skill"].lower():
            score += 3

        if found_topic and found_topic in r["topic"].lower():
            score += 4

        if score > 0:
            matches.append((score, r))

    matches.sort(reverse=True, key=lambda x: x[0])

    if matches:
        top_matches = matches[:3]
        reply = "<strong>Here are some good matches:</strong><br><br>"

        for score, r in top_matches:
            reply += f"""
            <div style="margin-bottom: 12px;">
                <strong>{r['title']}</strong> ({r['level']} {r['skill']})<br>
                <a href="{r['link']}" target="_blank">Open activity</a>
            </div>
            """

        return reply

    return """
    I couldn't find a good match.<br><br>
    Try asking for:<br>
    • B2 grammar<br>
    • conditional activities<br>
    • reported speech<br>
    • exam practice
    """

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = chatbot(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5000)