from flask import Flask,request
import time
app=Flask(__name__)
@app.route('/')
def hello():
    time1=time.time()
    time2=time.strftime("%Y%m%d%H%M%S",time.localtime())
    # return "hello word!!!!!!!3"
    # print(time1)
    return "当前时间是："+str(time1)+"转换成分钟后是："+time2
@app.route('/aoo/')
def orr():
    t=request.args.get('info')
    if t == None:
        return "没有输入info"
    return t
@app.route('/ao')
def ott():
    t=request.args.get('info','info的默认值')
    return t
if __name__ == '__main__':
    # app.run(debug=True,port=5000)
    app.run(port=5000)