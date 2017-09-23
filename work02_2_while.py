#!__*__coding:utf-8__*__        #무조건 이거 쓰고 시작해라,""이 --으로 보임.

prompt="""
1. Add
2. Del
3. List
4. Quit

please input number
"""

input_number=1
while input_number in [1, 2, 3, 4]:
    input_number=int(input(prompt))
    break