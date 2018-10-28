# _*_ coding:UTF-8 _*_
from source import md5_moudle,b64_moudle,caesar,ascii_brute_moudle,rot13_moudle,factorization_moudle,num_to_QR_moudle
from source.morse_moudle import Morse
import urllib.request

def begin():
    print('''
    +---------------------------------------------------------------+

     1.MD5加密            8.Base85加密              15.字符串反转    
     2.Base64加密         9.Base85解密              16.URL编码       
     3.Base64解密         10.Morse加密              17.URL解码 
     4.Base32加密         11.Morse解密              18.rot13编解码 
     5.Base32解密         12.Caesar加密             19.01字符转二维码 
     6.Base16加密         13.Caesar解密             20.ASCII位移爆破
     7.Base16解密         14.Caesar爆破
     
    +---------------------------------------------------------------+
     ''')


    fun_choice = input('选择：')
    return int(fun_choice)

def URLDecode():
    a = input("URL:")
    b = urllib.request.quote(a,encoding='UTF-8')
    print(b)

def URLEncode():
    a = input("url:")
    b = urllib.request.unquote(a,encoding='UTF-8')
    print(b)


def reverse():
    a = input('需要反转的字符串:')
    b = a[::-1]
    print(b)

def md5():
    a = input('需要加密的字符串:')
    b = md5_moudle.md5_encode(a)
    print("MD5('%s'):%s" % (a, b))

def b64de():
    string = input('需解密的字符串：')
    a = b64_moudle.b64decode(string)
    print(a)

def b64en():
    string = input('需加密字符串：')
    a = b64_moudle.b64encode(string)
    print(a)

def b32en():
    string = input('需加密字符串：')
    a = b64_moudle.b32encode(string)
    print(a)

def b32de():
    string = input('需解密的字符串：')
    a = b64_moudle.b32decode(string)
    print(a)

def b16en():
    string = input('需加密字符串：')
    a = b64_moudle.b16encode(string)
    print(a)

def b16de():
    string = input('需解密的字符串：')
    a = b64_moudle.b16decode(string)
    print(a)

def b85en():
    string = input('需加密字符串：')
    a = b64_moudle.b85encode(string)
    print(a)

def b85de():
    string = input('需解密的字符串：')
    a = b64_moudle.b85decode(string)
    print(a)

def morse_en():
    a = Morse()
    b = a.morse_en()
    for i in b:
        print(i, end=' ')

def morse_de():
    a = Morse()
    b = a.morse_de()
    for i in b:
        print(i, end='')

def caesar_en():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_encode(a, key)
    print(b)

def caesar_de():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_decode(a, key)
    print(b)

def caesar_brute():
    a = input('String=')
    caesar.caesar_brute(a)

def ascii_brute():
    filename=input('(ASCII码一行一个)\nfilename=')
    ascii_brute_moudle.ascii_brute_main(filename)

def rot_encode():
    rot13_moudle.rot13_moudle_main()

def num_to_QRcode():
    filename=input('filename=')
    num_to_QR_moudle.num_to_QR_main(filename)

def main():
    try:
        while True:
            main_choice = begin()
            if main_choice == 1:
                md5()
            elif main_choice == 2:
                b64en()
            elif main_choice == 3:
                b64de()
            elif main_choice == 4:
                b32en()
            elif main_choice == 5:
                b32de()
            elif main_choice == 6:
                b16en()
            elif main_choice == 7:
                b16de()
            elif main_choice == 8:
                b85en()
            elif main_choice == 9:
                b85de()
            elif main_choice == 10:
                morse_en()
            elif main_choice == 11:
                morse_de()
            elif main_choice == 12:
                caesar_en()
            elif main_choice == 13:
                caesar_de()
            elif main_choice == 14:
                caesar_brute()
            elif main_choice == 15:
                reverse()
            elif main_choice == 16:
                URLEncode()
            elif main_choice == 17:
                URLDecode()
            elif main_choice == 18:
                rot_encode()
            elif main_choice == 19:
                num_to_QRcode()
            elif main_choice == 20:
                ascii_brute()
                exit(0)

            again = input('\n继续？(T/F)').upper()
            if again == 'F':
                break
    except Exception as e:
        print(e)
        print('异常中止')



if __name__ == '__main__':
    main()
