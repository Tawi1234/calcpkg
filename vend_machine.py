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

#======================================================


order_count_num = 0     # 주문횟수
order_name = ""         # 주문음료
ame_order = "아메리카노" # 아메리카노 주문
la_order = "라떼"        # 라떼 주문
ch_order = "카푸치노" # 카푸치노 주문
ame_price = 1000        # 아메리카노 가격
la_price = 1500         # 라떼가격
ch_price = 2000         # 카푸치노 가격
input_money = 0         # 입금된 돈
in_money = 50000        # 자판기 내부 돈
out_money = 0           # 거스름돈
add_num = 0             # 추가금 


print("저희 자판기를 찾아와주셔서 감사합니다.")   # 인삿말 출력부분                 
print(' ')                                       # 가독성을 위한 공백


while True:                                                                                 #반복문(무한반복)
    order_name = str(input("주문하실 음료를 선택해주세요 : (아메리카노 / 라떼/ 카푸치노)"))  #변수(order_name) 과 input에 대한 입력값 비교

    if order_name == ame_order:
        print(f"주문하신 음료 {order_name}의 가격은 {ame_price}입니다.")
        break
    if order_name == la_order:
        print(f"주문하신 음료 {order_name}의 가격은 {la_price}입니다.") 
        break
    if order_name == ch_order:
        print(f"주문하신 음료 {order_name}의 가격은 {ch_price}입니다.")
        break
    else:
      print(' ')   
      print("잘못된 주문입니다. 다시 주문해주세요.")
      print(' ')  

                                                                              
while True:                                            
    input_money = int(input("돈을 투입해주세요. ", "(거스름돈은 반환됩니다.")) 

    if  order_name == ame_order and input_money == ame_price:
        print(f"{input_money}원이 들어왔습니다. {order_name}을 준비중이니 잠시만 기다려주세요.")     
        break

    if  order_name == la_order and input_money == la_price:
        print(f"{input_money}원이 들어왔습니다. {order_name}을 준비중이니 잠시만 기다려주세요.") 
        break

    if  order_name == ch_order and input_money == ch_price:
        print(f"{input_money}원이 들어왔습니다. {order_name}을 준비중이니 잠시만 기다려주세요.") 
        break

    if  order_name == ame_order and input_money < ame_price:
        add_num = ame_price - input_money
        print(f"{input_money}원이 들어왔습니다. {add_num}원 만큼 추가로 투입해주세요")
    
    if  order_name == ame_order and input_money < la_price:
        add_num = la_price - input_money
        print(f"{input_money}원이 들어왔습니다. {add_num}원 만큼 추가로 투입해주세요")   

    if  order_name == ame_order and input_money < ch_price:
        add_num = ch_price - input_money
        print(f"{input_money}원이 들어왔습니다. {add_num}원 만큼 추가로 투입해주세요")   


