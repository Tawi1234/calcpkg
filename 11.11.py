# ## 텍스트 게임 만들기
#  - 클래스 사용을 배제한 제한적인 환경에서 프로그램을 만들어 기본 자료구조 흐름제어 능력을 기른다.

#  - 게임주제
#   - text 게임
#    - 1~100 까지 임의의  수를 플레이어가 최소로 시도해서 맞추는 게임

# ## step

# ## step 1 
#  - 게임이 시작하면 "Enjoy, custom game world" 문구 출력

#  입력을 받습니다. 게임 이름을 입력하세요 단 29자 내로
#  - 플레이어가 입력할 때 까지 무제한 대기, 반복
#  - 29자 이상 입력할 경우 "초과 되었습니다."
#  - 20 이내로 정상 입력시
#   game_titel 변수에 제목을 담는다

#   - 닉네임을 입력 받음
#   - 입력에 대한 검사는 위와 동일
#   - player_name 변수에 저장

#   - 프럼프트를 출력
#   - '''
#    ============================
#    =  game_title              =
#    =   welcome Player_name    =
#    ============================
#    '''

#    - 컴퓨터가 1~100까지 임의의 점수 렌덤생성
#    - 입력프롬프트 "1~ 100까지 입력하세요>"
#    - 사용자가 입력하면
#      - 입력 안하고 엔터칠 경우 예외 상황들을 처리
   

#    - 컴퓨터 값과 플에이어 값을 비교해
#    - 작으면 작다 크면 크다를 출력하고 다시 입력대기
#     - 점수 : (10 - 시도횟수) / 10
#     - n회 시도해서 m점 

#     - 다시 하시겠습니까? yes시 다시 게임시작
#     - no면 게임종료
#     - 게임 종료시 메시지 출력 "good bye

#---------------------------------------------------------------------------------------------------

import random                                                    # 모듈(random) 사용을 위한 호출  : 숫자에 랜덤 부여
 
try_num = 0                                                      # 변수(try_num)값 0으로 설정

print("Enjoy, custom game world")                                # 게임 환영인사 출력 
print(' ')                                                       # 가독성을 위한 공백추가

while True:                                                      # 반복문 무한반복 설정 : 이름 설정을 위한 반복문
    player_name = str(input("이름을 입력하세요.  ※29자 내※"))    # 변수(play_name)은 input에 입력되는 값과 같음(str으로 설정)

    if len(player_name) > 29:                                    # 만약(if) 입력된 플레이어 이름(play_name)의 길이가 29를 초과 할 경우 
        print("입력 가능한 글자수를 초과하였습니다.")               # " 입력 가능한 글자수를 초과하였습니다." 출력
        print(' ')                                               
    else:                                                        # 그밖에(else) 상황이라면 : 29자 이내의 이름이라면
        print("이름이 등록되셨습니다.")                            # "이름이 등록되셨습니다." 출력
        print(' ')                                                    
        break                                                    # 반복을 끝냄 
    
print(f"반갑습니다. {player_name}")                               # 인삿말과 이름(Player_name) 출력
print(' ')

choice = "y"                                                     # 변수(choice)는 y와 같음 : 게임 다시 시작을 위한 값
result_num = random.randint(1, 10)                               # 변수(result_num)에 1~ 10 사이의 변수 입력
anser_num = 0                                                    # 변수(anser_num) : 입력횟수를 알기 위한 변수
score = 0                                                        # 변수(score) : 점수를 알기 위한 변수
                       
while(choice=="y"):                                              # 반복문 실행 : 변수(choice)가 y와 값이 같을 때 반복문 다시 실행
                                                                  
    print("숫자를 입력해주세요!")                                  # 숫자를 입력하라는 안내 출력      
    anser_num = int(input())                                      # 변수(anser_num) : 인풋에 입력되는 값과 같으며 숫자형으로 입력 
    try_num += 1                                                  # 변수(try_num) : 실행횟수 카운트를 위한 수식 : 반복문이 돌때 마다 1씩 증가 
    score = (10 - try_num) * 10                                   # 변수(score) : 최대 100점으로 설정 횟수 한번당 10점씩 감점   
                                 

    if anser_num < result_num:                                    # 만약(if) 입력 된 값(anser_num)이 생성된 랜덤값(result_num) 보다 크기가 작다면
        print("입력하신 숫자는 정답보다 작습니다...")                # "입력하신 숫자는 정답보다 작습니다..." 출력
        print(' ')

    if anser_num > result_num:                                    # 만약(if) 입력 된 값(anser_num)이 생성된 랜덤값(result_num) 보다 크기가 크다면
        print("입력하신 숫자는 정답보다 큽니다...")                  # "입력하신 숫자는 정답보다 큽니다.." 출력
        print(' ')

    if try_num  ==  10:                                           # 만약(if) 실행횟수(try_num)가 10에 도달한다면 : 도전횟수를 10회로 제한
        print("아쉽게도 점수는 0 입니다..." )                       # "아쉽게도 점수는 0 입니다..." 출력
        print(' ')
        result_num = str(result_num)                              # 변수(result_num) 의 값은 문자형 변수(result_num)의 값과 같다.
        print("정답은 " + result_num + " 이었습니다.")              # 정답(result_num) 출력
        print(' ')
        choice=input("다시하시겠습니까? (Y/N)")                     # 변수(choice)는 input의 값과 같다 : 다시하기 동작을 위한 부분 Y 입력 시 다시 시작 n 입력시 종료
        print(' ')
        try_num = 0                                                # 실행횟수(try_num)을 0으로 리셋 : 하지 않을 경우 이전 횟수가 누적되어 오류
        if(choice=="n"):                                           # 만약(if) 변수(choice)가 "n" 과 같아질 때 : n 입력 시 게임 종료
            print('게임을 종료합니다.')                              # 게임종료 출력
            print(' ')
            print(f'good bye {player_name}')                       # 마지막으로 good bye 와 플레이어 네임 출력
                                            
    if anser_num == result_num:                                    # 만약(if) 변수(anser_num) == 변수(result_num)이 같을 때 : 입력한 값이 정답 일 경우
        print("입력하시는 숫자는 정답입니다! ")                      # 정답안내 문자 출력
        print(' ')                          
        try_num = str(try_num)                                     # 변수(try_num)은 str(try_num)과 같다 : 변수(try_num) 문자형으로 변환하기 위한 것
        print("잘하셨습니다." + try_num +"번 만에 맞추셨습니다.")     # 축하와 실행횟수(try_num)출력
        print(f"{player_name}님의 점수는 {score}입니다.")            # 플레이어 이름(player_name)과 점수(score) 출력
        print(' ')
        choice=input("다시하시겠습니까? (Y/N)")                      #  만약(if) 변수(choice)가 "n" 과 같아질 때 : n 입력 시 게임 종료
        print(' ')
        try_num = 0                                                 # 실행횟수(try_num)을 0으로 리셋 : 하지 않을 경우 이전 횟수가 누적되어 오류
        if(choice=="n"):                                            # 만약(if) 변수(choice)가 "n" 과 같아질 때 : n 입력 시 게임 종료 
            print('게임을 종료합니다.')                               # 게임종료 출력
            print(' ')
            print(f'good bye {player_name}')                        # 마지막으로 good bye 와 플레이어 네임 출력
            print(' ')
            
         

#    anser_num == result_num:
#    try_num = str(try_num)
#    print("잘하셨습니다." + try_num +"번 만에 맞추셨습니다.")
#    print(f"{player_name}님의 점수는 {score}입니다.")
   