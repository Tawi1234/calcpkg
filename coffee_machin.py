

# 커피자판기 만들기
# 요구사항
# 프롬프트

# 어떤 커피를 원하세요? (아메리카노/라때/카푸치노)
# 입력을 받을 때 까지 반복

# 프롬프트에서 "off"할 경우 자판기가 종료
# 프롬프트에서 report 입력을 받을 경우
# 보고서를 출력

# 재료

# 커피가루 xxx ml
# 물 xxx ml
# 우유 xxxg
# 돈 : xxx원
# 만들 때 드는 재료가 충분한지 검사
# 재료가 부족할 경우 "재료가 부족합니다." 출력
# 재료가 충분할 때, 돈을 받음

# 10000원 5000원 1000원 500원 100원 10원
# 각각 지폐 또는 동전 몇개인지 입력
# 거스름돈 반환시 돈이 부족하면 메시지 출력
# 돈이 충분할 경우 거스름돈 반환

# 트랜젝션이 성공적인지 체크
# 자판기는 Money 부분 수익추가
# 커피에 해당하는 재료 감소
# 커피를 만듬
# 맛있는 커피(선택된 것) 나왔습니다. 좋은 시간 되세요


#========================================================================================================

# 커피 가격 : 아메리카노 1000원, 라떼 1500원, 

try_num = 0   #작동횟수
choice = "y"  #주문한 커피의 확인
price_num = 0 # 주문하는데 필요한 돈
#order_name  # 주문한 커피 이름
water_num = 300 # 물의 양                                       
coffee_num = 300 # 커피가루의 양                                                   
milk_num = 300  # 우유의 양                                                  
money_num = 5000 # 거스름돈의 양
 
print("찾아주셔서 감사합니다 고객님")
print(' ')                                



while True:                                                     
    order_name = str(input("주문하실 커피를 선택해주세요 (아메리카노/라떼/카푸치노)"))

    if str(order_name) == '아메리카노':
        print("아메리카노를 주문하시겠습니까?")
        print("가격은 1000원입니다.")
       

    if str(order_name) == '라떼':
        print("라떼를 주문하시겠습니까?")
        print("가격은 1500원입니다.")

    if str(order_name) == '카푸치노':
        print("아메리카노를 주문하시겠습니까?")
        print("가격은 2000원입니다.")

    else:
        print("주문을 제대로 입력해주세요")
    


while True:                                                     
  order_name = str(input("돈을 넣어주세요."))

  if str(order_name) == '아메리카노':
    print("아메리카노를 주문하시겠습니까?")
    print("가격은 1000원입니다.")

  if str(order_name) == '라떼':
    print("라떼를 주문하시겠습니까?")

  if str(order_name) == '카푸치노':
    print("아메리카노를 주문하시겠습니까?")

  else:
    print("주문을 제대로 입력해주세요")




print(f"고객님의 주문이 처리되고 있습니다.. {order_name}")
print(' ')

                                                     

# while(choice=="y"): 
                                                                  
#     print("숫자를 입력해주세요!")                                  
#     anser_num = int(input())                                     
#     try_num += 1  
#     score = (10 - try_num) * 10                                  
                                 

#     if anser_num < result_num:                                   
#         print("입력하신 숫자는 정답보다 작습니다...")               
#         print(' ')

#     if anser_num > result_num:
#         print("입력하신 숫자는 정답보다 큽니다...")
#         print(' ')

#     if try_num  ==  10:
#         print("아쉽게도 점수는 0 입니다..." )
#         print(' ')
#         result_num = str(result_num)
#         print("정답은 " + result_num + " 이었습니다.")
#         print(' ')
#         choice=input("다시하시겠습니까? (Y/N)")
#         print(' ')
#         try_num = 0
#         if(choice=="n"):
#             print('게임을 종료합니다.')
#             print(' ')
#             print(f'good bye {player_name}')
                                            
#     if anser_num == result_num:
#         print("입력하시는 숫자는 정답입니다! ")
#         print(' ')
#         try_num = str(try_num)
#         print("잘하셨습니다." + try_num +"번 만에 맞추셨습니다.")
#         print(f"{player_name}님의 점수는 {score}입니다.")
#         print(' ')
#         choice=input("다시하시겠습니까? (Y/N)")
#         print(' ')
#         try_num = 0
#         if(choice=="n"):
#             print('게임을 종료합니다.')
#             print(' ')
#             print(f'good bye {player_name}')
#             print(' ')
            
         

#    anser_num == result_num:
#    try_num = str(try_num)
#    print("잘하셨습니다." + try_num +"번 만에 맞추셨습니다.")
#    print(f"{player_name}님의 점수는 {score}입니다.")