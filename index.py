import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook3():
    req = request.get_json(force=True)
    action =  req.get("queryResult").get("action")
    if (action == "dramaC"):
        rate =  req.get("queryResult").get("parameters").get("rate")
        info = "您選擇的戲劇分類是：" + rate + "，相關戲劇：\n"
        collection_ref = db.collection("最新劇集_全部")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if rate in dict["rate"]:
                result += "片名：" + dict["text"] + "\n"
                result += "分類：" + dict["rate"] + "\n\n"
                result += "介紹網址：" + dict["link"] + "\n\n\n"
        info += result
    if (action == "dramaC"):
        rate =  req.get("queryResult").get("parameters").get("rate")
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
        rate =  req.get("queryResult").get("parameters").get("rate")
        info = "您選擇的電影分類是：" + rate + "，相關電影：\n"
        collection_ref = db.collection("最新電影_全部")
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
        rate =  req.get("queryResult").get("parameters").get("rate")
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
        rate =  req.get("queryResult").get("parameters").get("rate")
        info = "您選擇的動漫分類是：" + rate + "，相關動漫：\n"
        collection_ref = db.collection("最新動漫_全部")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if rate in dict["rate"]:
                result += "片名：" + dict["text"] + "\n"
                result += "分類：" + dict["rate"] + "\n\n"
        info += result

    elif (action == "CityWeather"):
        city =  req.get("queryResult").get("parameters").get("city")
        token = "rdec-key-123-45678-011121314"
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=" + token + "&format=JSON&locationName=" + str(city)
        Data = requests.get(url)
        Weather = json.loads(Data.text)["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"]
        Rain = json.loads(Data.text)["records"]["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"]
        MinT = json.loads(Data.text)["records"]["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"]
        MaxT = json.loads(Data.text)["records"]["location"][0]["weatherElement"][4]["time"][0]["parameter"]["parameterName"]
        info = city + "的天氣是" + Weather + "，降雨機率：" + Rain + "%"
        info += "，溫度：" + MinT + "-" + MaxT + "度"

    return make_response(jsonify({"fulfillmentText": info}))

#if __name__ == "__main__":
#    app.run()