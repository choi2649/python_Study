class Contact:
    """
    __init__ 생성자 생성
    print(self) 함수 생성
    """

    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print(self):
        print("name : " + self.name)
        print("phone_number : " + self.phone_number)
        print("e_mail : " + self.e_mail)
        print("addr : " + self.addr)


def run():
    #입력받기
    name = input("name : ")
    phone_number = input("phone_number : ")
    e_mail = input("e_mail : ")
    addr = input("addr : ")
    #입력받은거 출력
    print(name, phone_number, e_mail, addr)
    #입력받은걸로 인스턴스 생성
    con = Contact(name, phone_number, e_mail, addr)
    con.print()

if __name__ == "__main__":
    run()