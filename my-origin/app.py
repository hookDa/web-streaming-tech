from flask import Flask, send_file, make_response
import datetime
app = Flask(__name__)

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def chrome_devtools_json():
    # 204 No Content (空のレスポンス) を返す
    return "", 204
@app.route('/test.json')
def get_json():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ★★★ オリジン /test.json が呼ばれました ★★★")
    response = make_response(send_file('test.json', mimetype='application/json'))
    response.headers['Cache-Control'] = 'public, max-age=60'
    # response.headers['Cache-Control'] = 'no-store, max-age=0'
    
    response.headers['Vary'] = 'Accept-Language'
    return response
if __name__ == '__main__':
    app.run(port=8000, debug=False)