������L: ��js������
���� ��ֵ
�ֲ�����
function js() {
    var a = "���Ǿֲ�����";
    return a;
}
console.log(a);

ȫ�ֱ���    �������ⶨ��ı���   ����ֱ�ӱ�����(������ǰ����var)=ֵ
var a;
function js() {
    a = "���Ǿֲ�����";
    return a;
}
console.log(a);

��ʹ��globe��ǰ���¿����ں����ж���ȫ�ֱ���

��ִ��--��js���ص�ʱ�������ܹ��Լ�ִ��;
!(function () {
    console.log(0000)
})()

(function () {
    console.log(0000)
})()

function() {
    console.log(0000)
}
��Ϊ����û�����������ڵ��ú���Ҫ�ں��������ʹ��()
����һ������Ҫ�Է��������������Ǽ���var ��������ʹ���������ǰ��������()����

�ڲ���������ڲ�����
var jm_
!(function () {
    function jm() {
        console.log("���ܳɹ�")
    }
    console.log(2)
    jm_=jm
})()

�����42�м���jm()��ô�����ڲ�����, ���������ֱ�������ô�Ͳ����ڲ����ö�������Ϊ�ⲿ����
jm_������������ʾ������, ����������һ��ִ�к���


�������͵�ת��:
���еı�����һ���ַ������յ���һ���ַ���


���������
�����������  ���ⲿ����ֱ�ӵ��õ�
window = {
    location: {
        href: "https://www.bilibili.com/video/BV15F411s7Qd?p=2&spm_id_from=pageDriver&vd_source=0fdac99acb455340431def8654ddd69a"
    }
   
}
window.location.href
���뻷��
����      ��һ��ȫ�ֱ��� ������ṩ
    (���������  ���滷��    ���뻷��)
location    �ṩ��һ���������ַ



html��Ⱦ����
document ȫ�ֱ���   js�����Դ�
��ͷ - ����ȱʧ�Ļ���
�¼�: ����¼�, �����¼�(����)
document.write()��ҳ���
document = {
    write: function () {

    }
}
document.write + "" == document.write.toString()
document.write.toString = function () { return "function write(){{native code}}" }
//hook�����滻ԭ�з���
document.getElementById("id")
< p id = "demo" > �ҵĵ�һ������</p >
document.getElementById("demo").innerHTML = "�������޸ġ�"
ʹ�� "id" ��������ʶ HTML Ԫ�أ��� innerHTML ����ȡ�����Ԫ�����ݣ�

var para = document.createElement('p')

����Object�������� ����һ������
{ firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" }
var person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};
person.lastName;
person["lastName"];

������Function�������� ����һ��������
function myFunction(a, b) { return a * b; }

ʹ�� window.alert() ���������
ʹ�� document.write() ����������д�� HTML �ĵ��С�
ʹ�� innerHTML д�뵽 HTML Ԫ�ء�
ʹ�� console.log() д�뵽������Ŀ���̨��

�������(����Ҫ����)

����ҳ��ʹ�ñ��Լ�js�������������������
�ڱ���ʹ��input �ύ��������Ƕϵ��޷����ÿ��ܾ����ڱ��е�����

������һ��������
var x = "Hello\
world";

��ʹ��return�Ĺ�����ֻ��ʹ�ú����ķ��� �����ں�����ʹ��return


������ʹ������������window.zhiyau = "1"
window.zhiyau
window["zhiyau"]

��������: �û�����   ���������Ϣ

get     post    httpЭ��
get ���������Ƴ���     ���ݸ���url����
post    ���ݲ����Ƴ���


js������˳��һ����js�ļ��ı�д˳��
�ӿ�ʼ��λ�ý���, ������һ�����Ա����е�����
1.�Ƿ���ִ��!function() { } ()
2.�����Ķ���var a,var xxx,
3.��ֵ��� a = 3;
4.�����ĵ���xxx()



12345   md5
md5(12345, 32) =
    e10adc3949
md5(12345, 16) = 49ba59a

����40λsha1
md5 32λ 16λ

�ڼ��Ԫ�ص�ʱ�����vue��js�ļ���ʹ��, ӦΪvue��һ��ǰ�˿��
axiosҲ��һ��ǰ�˿�Ҳ��ʹ����js�ļ�����
react jquery

����: Ѱ�ұ���password
password =
    password =
    password:
.password
password = {}

Ϊʲô�еı����Ѳ���, ����û�и��õķ���
��Ϊվ�ڽ����˻���
1.����    ��λ��λ�û�Ƚ�׼ȷ  ����λ�ý϶���Ҫɸѡ  ���ҿ����Ѳ���
2.dom�¼���λ     ��λ�¼��ȽϿ�ǰ(ԭ��: ������λ���û����������λ��)
�¼��ϵ�ͨ��ʹ��ɾ��dom�¼��е����ݶ�վ���Ӱ��, ȷ���Ƿ��Ǹ��¼�, ���Ҷ��¼�����js�Ĳ鿴
3.xhr�ϵ�: �ô���λ��λ���ڷ����������ǿ���ʵ�ָ�ջ       ����ֻ������xhr�����ݰ�
��һ�ַ�ʽͨ��xhr�Ķϵ� 1.ͨ����������ַ���й��� Ҳ��֧��������ʽ   �����ڿ���̨��Դ�����ѡ�������
2.network�ϵ����   jquery  js������������jqery���¶ϵ�   �ٽ�js�ļ��ڶ�ջ�е�jqueryjs����

�ϵ�ֻ�ܴ���var function ���е����ڱ����ĸ�ֵ�е�ð�ź��ܴ�ϵ�
    �ϵ�һ����ڷ�����ĵ�һ�е��ǲ��ܴ���functionһ����
Stringifyָ����һ������ת��json��ʽ


Promise�첽����
    ()ǰ��ľ��Ƿ���   ����֮��ľ��ǲ���

toUpperCase ����д()

jsencrypt.setPublicKey����һ��RSA������Ϊ����publickey��Կ���ǻ���һ��˽Կδ������

���Ե�ʱ����Ҫ��ĳ��ֵ ����Ҫ�ϵ��λ�ö�λ�����ֵ����һ��, ���ܿ�����ʵ������

�� ʹ�ñ���js�ļ����滻����Ҫ�����ݵ�������ַ��ʱ�������������ʽ��ƥ��\d+����˼�Ƕ����ݽ���ƥ��+����˼��ƥ��һ���ַ����Ƕ���ַ�