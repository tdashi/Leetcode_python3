1.转换为ASCII
ord()

2.取小写字母
string.lowercase

3.整除
mid = (end - start) // 2

4.取小数后k位
round(num,k)
然而,事实上,直接写1.00000/用float()更有用,参考346

5.随机取值
import random
random.randint(start, last)
random.sample(序列a，n):从序列a(str/list/set)中随机抽取n个元素，并将n个元素生以list形式返回
  
6.排序
6.1 sorted(iterable, cmp=None, key=None, reverse=False)
iterable -- 可迭代对象
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

6.2 list.sort(cmp=None, key=None, reverse=False)
只能用于list

7.绝对值
abs(num)

8.平方根
8.1 num_sqrt = num ** 0.5 num只能为正数
8.2 都可用
import cmath
num_sqrt = cmath.sqrt(num)

9.反转
list/str.reverse()
list/str[::-1]
sorted(reverse = True)

10.取值范围
range(start, stop[, step])
平时step是直接默认为1,而start为0时也可以不写
#当step!=1,需要被单独写出且start=0时,一定要记得把start写上,不然系统会将step当作stop用
eg: range(0, end, 2)

11.list化
list()
#string不能直接改变其中的内容,需要先list化,改变后再join

12.无穷大和无穷小
sys.maxsize或float('inf')
-sys.maxsize或-float('inf')
