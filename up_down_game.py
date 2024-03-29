import random

my_account = 100

def up_down_manager(my_num, com_num, life):
    if my_num == com_num:
        print('\n정답입니다!\n축하드립니다. 배팅한 금액의 2배를 돌려받습니다.')
        return True
    elif my_num > com_num:
        if life > 1:
            print('\n컴퓨터 : 제시한 숫자보다 <<다운>> 하세요.')

        return False
    elif my_num < com_num:
        if life > 1:
            print('\n컴퓨터 : 제시한 숫자보다 <<업>> 하세요.')

        return False

while my_account > 0:
    print('--------------------------------------------------------------------')
    print('\n게임을 진행하시겠습니까?\n\n0 을 입력할시 게임 완전 종료, 1 을 입력할시 <<업다운 게임>> 참가')
    my_answer = int(input('>> '))

    if my_answer == 0:
        print('\n<게임을 완전히 종료합니다>')
        break
    elif my_answer != 1:
        print('\n0 또는 1 을 입력하세요')
        continue
    else:
        print('\n<게임에 입장합니다>')
        print(f'\n현재 잔액 : {my_account}')

        while True:
            print('\n얼마를 배팅하시겠습니까?')
            my_bet = int(input('>> '))

            if my_bet > my_account:
                print('\n현재 잔액보다 큰 금액을 배팅할 수 없습니다.')
                continue

            my_account -= my_bet
            print(f'\n<현재 잔액 중 {my_bet} 이 배팅되었습니다>\n당신의 남은 잔액은 {my_account} 입니다.')
            break
        
        computer_number = random.randrange(1, 101)
        life = 5

        while life > 0:
            print('--------------------------------------------------------------------')
            print(f'\n남은 생명 : {life}\n\n1 ~ 100 의 숫자 중 당신의 숫자를 입력하세요.')
            my_number = int(input('>> '))

            if up_down_manager(my_number, computer_number, life):
                my_account += my_bet * 2
                break
            else:
                life -= 1

                if life == 0:
                    print('--------------------------------------------------------------------')
                    print(f'\n정답은 {computer_number} 이였습니다.\n\n<생명을 모두 사용하셨으므로 <<업다운 게임>>을 종료합니다>')
                    break

                continue

        if my_account == 0:
            print('--------------------------------------------------------------------')
            print('\n<금액을 모두 사용하셨으므로 게임을 완전히 종료합니다>')