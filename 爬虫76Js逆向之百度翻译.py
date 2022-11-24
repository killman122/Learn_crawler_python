#由抓包可以得到,因为token不变,然而sign在改变所以需要对sign进行解密
#所以由于网站中的js进行计算
#观察可得token值随着请求接口返回并且为固定值不随着改变
#请求token的接口     https://fanyi.baidu.com/