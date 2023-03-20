from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

# Main menu
def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "\033[31m1\033[0m. Show all contacts\n"
                       "\033[31m2\033[0m. Add a contacts\n"
                       "\033[31m3\033[0m. Search a contacts\n"
                       "\033[31m4\033[0m. Change contact\n"
                       "\033[31m5\033[0m. Delete contact\n"
                       "\033[31m6\033[0m. Export/Import data base\n"
                       "\033[31m7\033[0m. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                delete_contact()
            case "6":
                exp_imp()
            case "7":
                play = False
            case _:
                print("\033[31mTry again!\n\033[0m")

# Edit menu
def edit_menu():
    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}
    show_all()
    record_id = input("Enter the record id: ")
    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("\033[31m1\033[0m. surname\n"
                           "\033[31m2\033[0m. name\n"
                           "\033[31m3\033[0m. patronymic\n"
                           "\033[31m4\033[0m. phone number\n"
                           "\033[31m5\033[0m. exit\n")
            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("\033[31mThe data is not recognized, repeat the input.\033[0m")
    else:
        print("\033[31mThe data is not correct!\033[0m")

# 1. Show all contact
def show_all():
    if not all_data:
        print("Empty data")
    else:
        print("\033[33m")
        print(*all_data, sep="\n")
        print("\033[0m")

# 2. Add a record
def add_new_contact():
    global last_id
    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))
    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))
        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("\033[32mThe entry has been successfully added to the phone book!\n\033[0m")
    else:
        print("\033[31mThe data already exists!\033[0m")

# 3. Search contact
def search_contact():
    search_data = exist_contact(0, input("Enter the search data: "))
    if search_data:
        print("\033[33m")
        print(*search_data, sep="\n")
        print("\033[0m")
    else:
        print("\033[31mThe data is not correct!\033[0m")

# 4. Change contact
def change_contact(data_typle):
    global all_data
    symbol = "\n"
    record_id, num_data, data = data_typle
    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("\033[31mThe data already exist!\033[0m")
                return
            all_data[i] = " ".join(v)
            break
    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("\033[32mRecord changed!\n\033[0m")

# 5. Delete contact
def delete_contact():
    global all_data
    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")
    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]
        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("\033[32mRecord delete!\n\033[0m")
    else:
        print("\033[31mThe data is not correct!\033[0m")

# 6. Import & Export
def exp_imp():
    while True:
        print("\nExport/Import menu:")
        move = input("\033[31m1\033[0m. Import\n"
                     "\033[31m2\033[0m. Export\n"
                     "\033[31m3\033[0m. Exit\n")
        match move:
            case "1":
                imp_db(input("Enter the name of the file: "))
            case "2":
                exp_db(input("Enter the name of the file: "))
            case "3":
                return 0
            case _:
                print("\033[31mThe data is not recognized, repeat the input.\033[0m")

# Export
def exp_db(name):
    symbol = "\n"
    change_name = f"{name}.txt"
    if not path.exists(change_name):
        with open(change_name, "w", encoding="utf-8") as f:
            f.write(f"{symbol.join(all_data)}\n")

# Import
def imp_db(name):
    global file_base
    if path.exists(f"{name}.txt"):
        file_base = f"{name}.txt"
        read_records()

def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) > 6:
                break
        answer = input(f"\033[31mData is incorrect!\n"
                       f"User only use only the letters"
                       f" of the alphabet, the lenght"
                       f" of the number is more 6 digits\n\033[0m"
                       f"Enter a {num}: ")
    return answer

def read_records():
    global last_id, all_data
    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
    return all_data

main_menu()