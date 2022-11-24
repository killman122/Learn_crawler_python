作用域L: 改js的问题
定义 赋值
局部变量
function js() {
    var a = "我是局部变量";
    return a;
}
console.log(a);

全局变量    方法体外定义的变量   或者直接变量名(变量名前不加var)=值
var a;
function js() {
    a = "我是局部变量";
    return a;
}
console.log(a);

在使用globe的前提下可以在函数中定义全局变量

自执行--在js加载的时候函数就能够自己执行;
!(function () {
    console.log(0000)
})()

(function () {
    console.log(0000)
})()

function() {
    console.log(0000)
}
因为函数没有名字所以在调用后需要在函数的最后使用()
对于一个方法要对方法进行申明除非加上var 或者是在使用这个方法前将方法用()括起

内部函数如何内部调用
var jm_
!(function () {
    function jm() {
        console.log("加密成功")
    }
    console.log(2)
    jm_=jm
})()

如果在42行加入jm()那么就是内部调用, 但是如果是直接相等那么就不是内部调用而是申明为外部变量
jm_不加括号是显示出函数, 加入括号是一个执行函数


变量类型的转换:
所有的变量加一个字符串最终等于一个字符串


浏览器环境
脱离了浏览器  在外部不能直接调用的
window = {
    location: {
        href: "https://www.bilibili.com/video/BV15F411s7Qd?p=2&spm_id_from=pageDriver&vd_source=0fdac99acb455340431def8654ddd69a"
    }
   
}
window.location.href
补齐环境
对象      是一个全局变量 浏览器提供
    (浏览器环境  引擎环境    代码环境)
location    提供了一个浏览器地址



html渲染环境
document 全局变量   js引擎自带
补头 - 补齐缺失的环境
事件: 点击事件, 滑动事件(滑块)
document.write()网页输出
document = {
    write: function () {

    }
}
document.write + "" == document.write.toString()
document.write.toString = function () { return "function write(){{native code}}" }
//hook方法替换原有方法
document.getElementById("id")
< p id = "demo" > 我的第一个段落</p >
document.getElementById("demo").innerHTML = "段落已修改。"
使用 "id" 属性来标识 HTML 元素，并 innerHTML 来获取或插入元素内容：

var para = document.createElement('p')

对象（Object）字面量 定义一个对象：
{ firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" }
var person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};
person.lastName;
person["lastName"];

函数（Function）字面量 定义一个函数：
function myFunction(a, b) { return a * b; }

使用 window.alert() 弹出警告框。
使用 document.write() 方法将内容写到 HTML 文档中。
使用 innerHTML 写入到 HTML 元素。
使用 console.log() 写入到浏览器的控制台。

插件环境(不需要补齐)

在网页中使用表单以及js可以向服务器发送数据
在表单中使用input 提交其中如果是断点无法作用可能就是在表单中的作用

分行在一个变量中
var x = "Hello\
world";

在使用return的过程中只能使用函数的返回 就是在函数中使用return


数组中使用名字来索引window.zhiyau = "1"
window.zhiyau
window["zhiyau"]

加密数据: 用户密码   浏览器的信息

get     post    http协议
get 数据是限制长度     数据跟在url后面
post    数据不限制长度


js的运行顺序不一定是js文件的编写顺序
从开始的位置解析, 解析第一个可以被运行的条件
1.是否自执行!function() { } ()
2.变量的定义var a,var xxx,
3.赋值语句 a = 3;
4.方法的调用xxx()



12345   md5
md5(12345, 32) =
    e10adc3949
md5(12345, 16) = 49ba59a

长度40位sha1
md5 32位 16位

在检查元素的时候对于vue的js文件不使用, 应为vue是一个前端框架
axios也是一个前端库也不使用在js的计算中
react jquery

例子: 寻找变量password
password =
    password =
    password:
.password
password = {}

为什么有的变量搜不到, 还有没有更好的方法
因为站内进行了混淆
1.搜索    定位的位置会比较准确  但是位置较多需要筛选  并且可能搜不到
2.dom事件定位     定位事件比较靠前(原因: 多数定位在用户输入的明文位置)
事件断点通过使用删除dom事件中的内容对站点的影响, 确定是否是该事件, 并且对事件进行js的查看
3.xhr断点: 好处定位的位置在发包函数我们可以实现更栈       坏处只能用于xhr的数据包
第一种方式通过xhr的断点 1.通过特征码网址进行过滤 也是支持正则表达式   这里在控制台的源代码的选项中添加
2.network断点进入   jquery  js库用作发包在jqery中下断点   再将js文件在堆栈中的jqueryjs过滤

断点只能打在var function 等中但是在变量的赋值中的冒号后不能打断点
    断点一般打在方法体的第一行但是不能打在function一行上
Stringify指的是一个对象转到json格式


Promise异步请求
    ()前面的就是方法   括号之间的就是参数

toUpperCase 到大写()

jsencrypt.setPublicKey这是一个RSA加密因为存在publickey公钥但是还有一个私钥未被发现

调试的时候需要看某个值 必须要断点的位置定位在这个值的这一行, 才能看见真实的数据

在 使用本地js文件的替换中需要对数据的链接网址的时间戳进行正则表达式的匹配\d+的意思是对数据进行匹配+的意思是匹配一个字符或是多个字符