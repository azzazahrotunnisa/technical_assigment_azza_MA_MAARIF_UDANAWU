from flask import Flask, request

app = Flask(__name__)

@app.route('/sic')
def sic():
    return 'kelas sic 2024'

@app.route('/',methods=['POST'])
def post():
    user_post = request.get_json()
    suhu = user_post['suhu']
    kelembapan = user_post['kelembapan']
    nama = user_post['nama']
    return f"holaa!! nama ku {nama} dari MAALMA, suhu = {suhu}, kelembapan = {kelembapan}"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

