#递归

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
Python 切片：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，不调用str的strip()方法。

在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成各种截取操作，非常方便。

要去除首尾的空格，只需要从头到尾、从尾到头各扫描一次，记录两端需要截取的位置，去除两端空格即可。

需要注意的是全是空格的情况。

def trim(s):
    length = len(s)

    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break;
        j = length-1;
        while s[j] == ' ' and j >= i:
            j -= 1
        s = s[i:j+1]

    return s
更加美观的是使用递归实现：

def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

附测试数据：

if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!') 

