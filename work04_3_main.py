#!__*__coding:utf-8__*__
#이 파일을 계속 확장해 나갈 것입니다.

import cmd, sys
import work04_1_day3final as f
import work03_3_moviejson as m
import work04_4 as naver

class MyShell(cmd.Cmd):
    intro = """
    ======================================
    파이썬 데이터 분석 실무 프로그램입니다.
    Help 나 ?를 눌러서 도움말을 보십시오
    ======================================"""
    prompt = '(명령어를 입력해주세요)>>'

    # doc_header = "도움말은"

    # -----basic turtle commands ----
    def do_file(self,arg):
        'movie the turtle forward by the specified distance : FORWARd 10'
        f.work03_2_csv_file_open3()
    def do_movie(self, arg):
        'Turn turtle right by given number of degrees : RIGHT 20'
        m.x()
    def do_home(self, arg):
        'Return turtle to the home position : HOME'

    def do_quit(self, arg):
        'Stop recording, close the turtle window, and exit : BYE'
        print('이용해 주셔서 감사합니다.')
        return True

    def do_naver(self, arg):
        '네이버에서 값을 가지고 옵니다'
        naver.run_naver_search_from_blog(arg)
        print('검색 이용해 주셔서 감사합니다.')
        return True

    def precmd(self, line):
        line=line.lower()
        print("precmd" + line)
        return line

    def postcmd(self, stop, line):
        print(stop)
        print("postcmd:" + line)
        return stop

if __name__=='__main__':
    MyShell().cmdloop()