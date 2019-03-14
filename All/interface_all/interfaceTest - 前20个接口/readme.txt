1、测试前的工作
（1）【第3个接口需要一个入参code】换取应用授权令牌之前，请先调用获取code：
https://openauth.alipay.com/oauth2/appToAppAuth.htm?app_id=2018112762317943&redirect_uri=http://naka.jvzj.cn/alipay_call_back
用户名  xurannan@vdongchina.com
密码 vdongchina123
（2）【第5个接口需要一个入参code】换取授权访问令牌前，请先调用获取code：
https://openauth.alipay.com/oauth2/publicAppAuthorize.htm?app_id=2018112762317943&scope=auth_user&redirect_uri=http://naka.jvzj.cn/alipay_call_back
用户名  xurannan@vdongchina.com
密码 vdongchina123


2、测试流程简介
（1）第1个接口agentCreate返回batchNo，给第2个接口mniCreate使用作为入参
（2）第3个接口getAuthToken返回app_auth_token，给后面接口使用（用到该参数的接口：）
（3）第5个接口oauth返回的accessToken，给第7个接口使用


3、测试注意事项
（1）第2个接口mniCreate：小程序的中文名和英文名可能重名，目前做了随机组合（中文18位，英文18位），但无法连接支付宝数据库，没法保证不重名
（2）第10个接口deleteMembers：user_id不一定在数据库中存在，删除时可能会报错不存在
（3）第11个接口往后，小程序的template_version、template_id、app_version暂时用开发给的（这个需要用代码创建小程序）


