katok = []

# 데이터 추가
def add_data(friend):
    katok.append(friend)

# 데이터 삽입
def insert_data(position, friend):
    katok.insert(position, friend)

# 데이터 삭제
def delete_data(friend):
    if friend in katok:
        katok.remove(friend)
    else:
        print(f"{friend}은(는) 리스트에 없습니다.")

# 전체 출력
def print_data():
    print("현재 친구 리스트:", katok)


# ----------- 메인 코드 -----------
while True:
    print("\n--- 카카오톡 친구 리스트 메뉴 ---")
    print("1. 친구 추가")
    print("2. 친구 삽입")
    print("3. 친구 삭제")
    print("4. 리스트 출력")
    print("5. 종료")

    choice = input("메뉴 선택 (1~5): ")

    if choice == "1":
        name = input("추가할 친구 이름 입력: ")
        add_data(name)
        print_data()

    elif choice == "2":
        pos = int(input("삽입할 위치(0부터 시작): "))
        name = input("삽입할 친구 이름 입력: ")
        insert_data(pos, name)
        print_data()

    elif choice == "3":
        name = input("삭제할 친구 이름 입력: ")
        delete_data(name)
        print_data()

    elif choice == "4":
        print_data()

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("1~5 사이의 숫자를 입력해주세요.")
