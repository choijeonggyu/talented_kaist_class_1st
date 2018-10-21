class Student:
    name = ''  # 속성 : 이름
    age = ''  # 속성 : 나이
    height = ""  # 속성 : 키

    def print_S(self):
        print("이름 : {0}, 나이 : {1}, 키 :{2}".format(self.name, self.age, self.height))


st1 = Student()
st1.name = "이하나"
st1.age = "16"
st1.height = "163"
st1.print_S()

st2 = Student()
st2.name = "김나라"
st2.age = "16"
st2.height = "171"
st2.print_S()

