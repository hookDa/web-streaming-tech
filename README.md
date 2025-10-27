local-cdn-lab/
│
├── 📁 my-origin/          <-- 📦 オリジンサーバー関連
│   ├── app.py             (Python Flask サーバー)
│   ├── test.json          (配信するJSONファイル)
│   └── requirements.txt   (Flaskインストール用)
│
├── 📁 my-cdn/              <-- 🚀 CDNサーバー関連
│   └── nginx.conf         (Nginx設定ファイル)
│
└── README.md              (手順をメモしておくと便利)

# オリジンサーバーを起動
## プロジェクトルートに移動
```
cd /path/to/local-cdn-lab
```
## 1. オリジンフォルダに移動
```
cd my-origin
```

## 2. 必要なライブラリをインストール
```
pip install -r requirements.txt
```

## 3. オリジンサーバーを起動
```
python app.py
```

## プロジェクトルートに移動
```
cd /path/to/local-cdn-lab
```

# CDNサーバーを起動
## 1. CDNフォルダに移動
```
cd my-cdn
```

## 2. DockerでNginxを起動
### (カレントディレクトリの nginx.conf をマウントする)
```
docker run --rm -p 8080:8080 --name my-cdn \
-v "`pwd`/nginx.conf":/etc/nginx/nginx.conf:ro \
-v "`pwd`/cache_data":/tmp/nginx_cache \
nginx
```


## 3.アクセス
```
http://localhost:8080/test.json
```