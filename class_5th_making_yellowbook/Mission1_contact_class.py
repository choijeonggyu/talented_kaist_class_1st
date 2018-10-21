class contact:
    name = ""
    number = ""

book=[]

def add():
    con = contact()
    print("추가할 연락처를 입력하세요.")
    print("name: " , end ="")
    con.name = input()
    print("number: " , end ="")
    con.number = input()
    book.append(con)

def delete():
    print("삭제할 이름을 입력하세요.")
    print("name: ", end='')
    name = input()

    length = len(book)
    for i in range(0, length):
        if book[i].name == name:
            del book[i]
    print(" 연락처가 삭제 되엇습니다.")

def printbook():
    length = len(book)
    for i in range (0,length):
        print("name : ", book[i].name)
        print("number : ", book[i].number)

add()
add()
add()

delete()
printbook()

