from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os
import random

# 自身の名称を app という名前でインスタンス化する
# app = Flask(__name__)
app = Flask(__name__, static_folder="img")
# index にアクセスされた場合の処理
@app.route('/')
def index():
    title = "ようこそ"
    message = "君の名前を教えてくれ"
    # messageとtitleをindex.htmlに変数展開
    return render_template('index.html',
                           message=message, title=title)

contents = [
                    '学生時代に頑張った事はなんですか', 
                    '自己PRを教えて下さい', 
                    '就活の軸を教えて下さい', 
                    'あなたはどうしてこの会社を選んだのか教えて下さい', 
                    '将来やりたいことを教えて下さい'
                    ]
    
bangou = [0,1,2,3,4]

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "いらっしゃい"

    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))

    # POSTメソッドの場合
    else:
        # リクエストフォームから「名前」を取得
        # name = request.form['name']
        # nameとtitleをindex.htmlに変数展開
        suuzi = random.choice(bangou)
        content = contents[suuzi]

        return render_template('questions.html',content=content,suuzi=suuzi)

@app.route('/post', methods=['GET', 'POST'])
def rechallenge():
    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))

    # POSTメソッドの場合
    else:
        # リクエストフォームから「名前」を取得
        name = request.form['suuzi']
        # nameとtitleをindex.htmlに変数展開
        del contents[suuzi]
        del bangou[suuzi]
        suuzi = random.choice(bangou)
        content = contents[suuzi]
        return render_template('questions.html',content=content,suuzi=suuzi)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)