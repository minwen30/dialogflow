import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    rate = request.get_json()['queryResult']['parameters']['movie']
    db = firestore.client()
    response_text = "您選擇的電影分類是：" + rate + "，相關電影："
    if rate == "全部電影":
        movies_collection = db.collection("最新電影_全部")
        query = movies_collection.stream()
    elif rate in ["動作片", "喜劇片", "愛情片", "科幻片", "恐怖片", "劇情片", "戰爭片", "紀錄片"]:
        movies_collection = db.collection("最新電影_分類")
        query = movies_collection.where("rate", "==", rate).stream()
    movies = list(query)
    for movie in movies:
        response_text += "\n片名：" + movie.get("text") + "\n介紹：" + movie.get("link")
    return make_response(jsonify({
        "fulfillmentText": response_text
    }))

    """if (action == "dramaC"):
        rate =  req.get("queryResult").get("parameters").get("drama")
        info = "您選擇的戲劇分類是：" + rate + "，相關戲劇：\n"
        collection_ref = db.collection("最新劇集_分類")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if rate in dict["rate"]:
                result += "片名：" + dict["text"] + "\n"
                result += "分類：" + dict["rate"] + "\n\n"
                result += "介紹網址：" + dict["link"] + "\n\n\n"
        info += result
    if (action == "movieC"):
        rate =  req.get("queryResult").get("parameters").get("movie")
        info = "您選擇的電影分類是：" + rate + "，相關電影：\n"
        collection_ref = db.collection("最新電影_分類")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if rate in dict["rate"]:
                result += "片名：" + dict["text"] + "\n"
                result += "分類：" + dict["rate"] + "\n\n"
                result += "介紹網址：" + dict["link"] + "\n\n\n"
        info += result
    if (action == "cartoonC"):
        rate =  req.get("queryResult").get("parameters").get("cartoon")
        info = "您選擇的動漫分類是：" + rate + "，相關動漫：\n"
        collection_ref = db.collection("最新動漫_全部")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if rate in dict["rate"]:
                result += "片名：" + dict["text"] + "\n"
                result += "分類：" + dict["rate"] + "\n\n"
        info += result"""

#if __name__ == "__main__":
#    app.run()