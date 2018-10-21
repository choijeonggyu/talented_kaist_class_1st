class contact:
    name = ""
    number = ""

book=[]

def add():
    con = contact()
    print("추가할 연락처를 입력하세요.")
    print("name: " )
    con.name = input()
    print("number: ")
    con.number = input()
    book.append(con)


def delete():
    print("삭제할 이름을 입력하세요.")
    print("name: ")

    print(" 연락처가 삭제 되엇습니다.")
def printbook():


add()
add()
add()
delete()
printbook()