'''
주제:클래스 배우기
이름: 홍주아
학번:201732039
'''
class fraction :#클래스정의
    def __init__(self, c , d):#함수정의
        self.n1=c#변수선언
        self.n2=d#변수선언

    def __str__(self):#함수정의
        return str(self.n1) + "/" + str(self.n2)#리턴으로 보내기

    def __add__(self,x):#함수정의
        n=self.n2*x.n1+self.n1*x.n2#변수선언
        d=self.n2*x.n2#변수선언
        a=fraction(n,d)#변수선언
        return a#리턴으로 보내기

    def __sub__(self,x):#함수정의
        n=self.n2*x.n1-self.n1*x.n2#변수선언
        d=self.n2*x.n1#변수선언
        b=fraction(n,d)#변수선언
        return b#리턴으로 보내기


    def __eq__(self,a):#함수정의
        return (self.n1+a.n2)==(a.n1*self.n2)#리턴으로 보내기

    def __lt__(self,a):#함수정의
        return (self.n1+a.n2)<(a.n1*self.n2)#리턴으로 보내기

    def __gt__(self,a):#함수정의
        return (self.n1+a.n2)>(a.n1*self.n2)#리턴으로 보내기

    def __ne__(self,a):#함수정의
        return (self.n1+a.n2)!=(a.n1*self.n2)#리턴으로 보내기



fn=fraction(2,4)#변수선언
sn=fraction(4,7)#변수선언
print(fn+sn)#출력
print(fn-sn)#출력
print(fn==sn)#출력
print(fn<sn)#출력
print(fn>sn)#출력
print(fn!=sn)#출력



