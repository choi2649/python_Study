import os

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
        if self.name == "연락처를 입력하세요":
            print("연락처를 입력하세요")
        else:
            print("name : " + self.name)
            print("phone_number : " + self.phone_number)
            print("e_mail : " + self.e_mail)
            print("addr : " + self.addr)


def addContact():
    name = input("name : ")
    phone_number = input("phone_number : ")
    e_mail = input("e_mail : ")
    addr = input("addr : ")
    #입력받은거 출력
    print(name, phone_number, e_mail, addr)
    #입력받은걸로 인스턴스 생성
    con = Contact(name, phone_number, e_mail, addr)
    con.print()
    return con




def contactListSelect():
    path = "./"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list if file.endswith(".txt")]
    print("123 : ", file_list_py.__len__())
    if(file_list_py.__len__() == 0):
        name = input("전화번호부명 생성 : ")
        name = name+".txt"
        f = open(name,"wt")
        f.close()
        return name
    print("file_list_py: {}".format(file_list_py))

    return selectList(file_list_py)

def selectList(file_list_py):
    num = 1;
    for index in file_list_py:
        print(num, " : " ,index)
        num +=1;

    idx = input("전화번호부 선택 : ")

    while int(idx) > num-1 or int(idx) <= 0:
        print("없는 숫자 입니다.")
        idx = input("전화번호부 선택 : ")

    return file_list_py[int(idx)-1];

def saveConList(conListName, contact_list):
    if(contact_list.__len__() > 0 ):
        f = open(conListName,"wt")
        for idx in contact_list:
            f.write(idx.name+"\n")
            f.write(idx.phone_number + "\n")
            f.write(idx.e_mail + "\n")
            f.write(idx.addr + "\n")
        f.close()
    else:
        print("연락처가 없습니다.")

def menuPrint():
    print("1. 연락처 추가")
    print("2. 추가연락처 출력")
    print("3. 추가연락처 저장")
    print("4. 추가연락처 삭제")
    print("5. 연락처모음 삭제")
    print("6. 연락처모음 출력")
    print("7. 종료")
    select = input("입력 : ")
    return int(select)

def run():
    con = Contact("연락처를 입력하세요","","","");
    contact_list = []
    while 1:
        menu = menuPrint()
        print(menu)
        if menu == 1:
            print(con.name)
            con = addContact()
            contact_list.append(con)
        if menu == 2:
            for idx in contact_list:
                idx.print()
                print("--------------------")
        if menu == 3:
            conListName = contactListSelect()
            saveConList(conListName, contact_list)
            print("12333: " ,conListName)
        elif menu == 7:
            break

    # #입력받기
    # name = input("name : ")
    # phone_number = input("phone_number : ")
    # e_mail = input("e_mail : ")
    # addr = input("addr : ")
    # #입력받은거 출력
    # print(name, phone_number, e_mail, addr)
    # #입력받은걸로 인스턴스 생성
    # con = Contact(name, phone_number, e_mail, addr)
    # con.print()

if __name__ == "__main__":
    run()