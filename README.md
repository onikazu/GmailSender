# GmailSender
## 概要
gmailからメールをパイソンを用いて送信するプログラム。

## 使い方
- info_temp.iniのmail1に送信元アドレス、mail2に送信先アドレス、pass1に送信元のgmailパスワードを入力する。
- 以下のコードをターミナルにディレクトリを移動してから打ち込む
~~~
$ mv info_temp.ini info.ini
~~~

- 以下のURLから自分のGoogleアカウントの「安全性の低いアプリがアカウントにアクセスするのを許可する」の項目を有効に
してやる。この操作はchromeから行うとうまくいかない時があるので別のブラウザを使うと良い  
https://support.google.com/accounts/answer/6010255?pli=1&authuser=3  

- 以下のコードをターミナルにディレクトリを移動してから打ち込む
~~~
$ python gmail.py
~~~

## 参考資料
https://qiita.com/bgg0u/items/630a87ce1a44778bbeb1  
https://productforums.google.com/forum/#!topic/gmail-ja/h51cPXyRzI0  
http://www.python.ambitious-engineer.com/archives/648  
