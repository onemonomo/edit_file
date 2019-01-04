# coding=utf8
import sys

def main():
    print sys.getdefaultencoding() # 系统默认代码中出现的字符对应的二进制码用编码方式进行encode = ascii
    tmp1 = '中文'  # 这是一个str，也就是说使用二进制存的，在系统默认编码的方式下存。 错！！！这是当前文件的内容，应该是以coding声明进行encode
    print type(tmp1), tmp1  # 这个tmp1是str类型，print时，自动用前面声明的coding方式进行decode成unicode
    print tmp1.decode('utf8') # 这里decode成功，说明前面tmp1定义的时候确实使用utf8进行encode，而不是系统默认的ascii

    tmp2 = (u'中文').encode('gbk')
    print type(tmp2), tmp2  # 这个tmp2也是str类型，但是是gbk编码后的，print时默认用coding方式进行decode成unicode，所以乱码了

    tmp = u'中文' # 这个前缀u类似于强转(decode)str为unicode，所以如果不添加coding=utf8注释，那么以ascii进行编码的话，是支持不了这个中文的
    print type(tmp), tmp

    utf8_file = open('utf8', 'w') # open文件，在不指定encoding方式的条件下，返回的都是str二进制串，这个二进制串就是实际存在文件中的。
    
    # 如果已经申明了coding=utf8，这里可以不进行encode，因为这里会默认用utf8进行encode后存入文件，不会用unicode的码流存到文件
    # 错！！！不是用utf8去encode，而是ascii。也就是系统默认的encode方式，说明codng=utf8只在代码中的字符串，和整个代码本身的字符起作用
    # 这个编码声明是coding而不是encode
    utf8_file.write(tmp.encode('utf8'))
    utf8_file.close()

    # wb和w的区别是，如果在win平台，那么如果不以二进制写，会将\n符号，写为\r\n(回车+换行)
    # rb则是文件结束符的区别，以r读文件，会进行二进制转换为字符，其中如果读到了0x1A这个字节(对应字符为EOF)，则结束了，后面的内容就遗漏了。
    utf8_file = open('utf8_b', 'wb') 
    utf8_file.write(tmp.encode('utf8'))
    utf8_file.close()

    gbk_file = open('gbk', 'w')
    gbk_file.write(tmp.encode('gbk'))
    gbk_file.close()

    read_utf8 = open('utf8', 'r')
    for line in read_utf8.readlines():
        print type(line), line
        print type(line.decode('utf8')), line.decode('utf8')

    read_gbk = open('gbk', 'r')
    for line in read_gbk.readlines():
        print type(line), line
        print type(line.decode('gbk')), line.decode('gbk')

if __name__ == '__main__':
    main()