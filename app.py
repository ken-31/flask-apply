from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def get_info():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr

    print(f"IP: {ip_address}, User-Agent: {user_agent}")

    return render_template("camera.html")

@app.route("/upload", methods=["POST"])
def upload():
    image_data = request.form["image"]
    print(f"受信した画像データ（base64）：{image_data[:50]}...")
    return "画像受信しました！ありがとう！"

if __name__ == "__main__":
    app.run(debug=True)
