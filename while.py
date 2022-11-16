import random # 랜덤 모듈 임포트


choice="y" # 게임 상태 변수

guess_number=0 # 숫자 게임 입력값

index=0 # 10번의 기회에 관한 변수 초깃값


random_number=random.randint(1, 50) # 랜덤 함수에 따른 숫자 값


print("숫자 맞추기 게임\n") # 출력

print("─────") # 출력

print("1에서 50 이하의 숫자만 입력하세요. \n") # 출력

print("숫자를 맞출 수 있는 기회는 10번 입니다.\n") # 출력


while(choice=="y"): # 반복문 choice 값이 y일 경우 반복


    if(index==10): # index 값이 10일 경우

        print("10번의 기회가 끝났습니다.") # 출력

        print("프로그램을 종료합니다.") # 출력

        break # 반복문 빠져나옴


    elif(random_number==guess_number): # 게임이 다시 시작된 경우

        index=0 # index 값 초기화

        random_number=random.randint(1, 50) # 랜덤함수로 숫자 값 입력


    else:

        print("─────") # 출력

        guess_number=int(input("숫자 입력 : ")) # 숫자 입력

        print("") # 출력

        #숫자비교

        choice=number_compare(random_number, guess_number)

        index+=1 # 숫자 비교하는 횟수 증가