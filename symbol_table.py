def f():  # f는 객체..
    l_a = 2
    l_b = '마이콜'
    print(locals())

class MyClass:  #이거는 클래스 객체이다.
    x = 10
    y = 20

o = MyClass()   # 클래스 정보를 담고있는 객체가 있는 것이다.
# 파이썬은 클래스로 하려고 하지않고 자바로 하려고하신다- 강사님.. / 틀을 기반으로 객체를 만들면, 그놈도 심볼테이블을 가지고 있다.

g_a = 1
g_b = '둘리'

print(globals())  # 테이블: 딕셔너리이다  # 글로벌: 모듈의 심볼들 다 모아놓음..

f()

#심볼테이블을 가지고 있는 것들
# 모듈 ,
# 클래스 객체
# 인스턴스 객체
# 정의된 함수.

# 1. 정의된 함수
f.k = 'hello'
print(f.__dict__)  #내장되있는 변수이람,, 태아불 낭ㄴㄷ다.  #레퍼런스 아이디 주소, 찾아가면 그 값이 있을것인데, 그걸 보여준다.
#모ㅓ듈에있는거 함수에있는거 하나,, 클래스에 있는거 하나.



# 다음시간,, 오늘한거 정리,, 문제 좀 풀어보기. # 2번문제, 쉬운문제 섞어서 풀게끔..

