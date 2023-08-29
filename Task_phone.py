def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('I:\GB_practice\pyton_for_st\HW_08\phonebook.txt')

    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('lastname')
            new_number=input('new number')
            print(change_number(phone_book, last_name, new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_lastname=input('lastname')
            user_name=input('name')
            user_phone=input('phone')
            user_comment=input('comment')
            user_data=[user_lastname, user_name, user_phone, user_comment]
            add_user(phone_book, user_data)
            #write_txt('phonebook.txt', phone_book)
        elif choice==7:
            filename="I:\GB_practice\pyton_for_st\HW_08\phonebook.txt"
            write_txt(filename, phone_book)
        choice=show_menu()

def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Записать изменения\n'
          '8. Закончить работу\n')
    choice=int(input())
    return choice

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия','Имя','Телефон','Описание']
    with open('phonebook.txt','r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def print_result(filename):
    for i in range(len(filename)):
        print(filename[i])
    print()

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия']==last_name:
            print(phone_book[i]['Телефон'])

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия']==last_name:
            phone_book[i]['Телефон']=new_number
            print(phone_book[i])
def delete_by_lastname(phone_book, lastname):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия']==lastname:
            phone_book[i].clear()
            print(phone_book)

def find_by_number(phone_book,number):
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон']==number:
            print(phone_book[i])

def add_user(phone_book, user_data):
    fields=['Фамилия','Имя','Телефон','Описание']
    record=dict(zip(fields, user_data))
    print(phone_book)
    phone_book.append(record)

    print(phone_book) 
    return(phone_book)

work_with_phonebook()
