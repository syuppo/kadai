# 自動販売機プログラムを作成して下さい。
# 最初にコンソールに購入できる飲み物を出力させて下さい。
# その後
# キーボードから入力を行わせ、
# 入力された文言に対して判定をかけて
# 該当商品が存在すれば投入金額を入力させ、
# 該当商品ががない場合は、
# 「該当商品がありません」とメッセージを出力させ、
# 購入を続けるか問いて下さい。
# 投入金額を入力後
# 足りない場合は
# 「投入金額が不足しています」
# 「○○○○○円足りません」
# と出力させる。
# 足りた場合且つ、お釣りが出る場合、
# 「○○○○を購入しました。」
# 「お釣りは￥○○○です」
# と出力させる
# 購入を続けるか、購入を終了するかを選ばせ
# 続ける場合は、画面をクリアして
# 自動販売機の商品を再度表示させ
# 終了する場合はそのままプログラムを終了させる



import sys
import os


drink_dic = {'コーラ':120, 'お茶':80, 'コーヒー':100}

while True:
    print('コーラ', 'お茶', 'コーヒー')
    drink_type = input('購入する商品を選んで下さい：')

    if drink_type == 'コーラ':
        print(drink_dic['コーラ'],'円です')
        try:
            price = int(input('投入金額を入力して下さい：'))

            if  price == drink_dic['コーラ']:
                print('商品を購入しました')
                print('お釣りはありません')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break

            elif price > drink_dic['コーラ']:
                print('商品を購入しました')
                print('お釣りは',price - drink_dic['コーラ'],'円です')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break
            
            else:
                shortage = drink_dic['コーラ'] - price
                print('投入金額が不足しています')
                print(shortage,'円足りません')

                while shortage > 0:
                    shortage2 = shortage - int(input('投入金額を入力して下さい：'))         
                    if shortage2 == 0:
                        print('商品を購入しました')
                        print('お釣りはありません')
                        break

                    elif shortage2 > 0:
                        print('投入金額が不足しています')
                        print(shortage2,'円足りません')
                        shortage = shortage2
                        continue

                    elif shortage2 < 0:
                        print('商品を購入しました')
                        print('お釣りは',shortage2*-1,'円です')
                        break
        except ValueError:
            print('※数値を入力して下さい')
            

        while True:
            x = input('購入を続けますか？ y/n:')
            if x == 'y':
                os.system('clear')
                break

            elif x == 'n':
                sys.exit()

            else:
                continue


    elif drink_type == 'お茶':
        print(drink_dic['お茶'],'円です')

        try:
            price = int(input('投入金額を入力して下さい：'))

            if  price == drink_dic['お茶']:
                print('商品を購入しました')
                print('お釣りはありません')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break

            elif price > drink_dic['お茶']:
                print('商品を購入しました')
                print('お釣りは',price - drink_dic['お茶'],'円です')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break
            
            else:
                shortage = drink_dic['お茶'] - price
                print('投入金額が不足しています')
                print(shortage,'円足りません')

                while shortage > 0:
                    shortage2 = shortage - int(input('投入金額を入力して下さい：'))         
                    if shortage2 == 0:
                        print('商品を購入しました')
                        print('お釣りはありません')
                        break

                    elif shortage2 > 0:
                        print('投入金額が不足しています')
                        print(shortage2,'円足りません')
                        shortage = shortage2
                        continue

                    elif shortage2 < 0:
                        print('商品を購入しました')
                        print('お釣りは',shortage2*-1,'円です')
                        break
            
        except ValueError:
            print('※数値を入力して下さい')


        while True:
            x = input('購入を続けますか？ y/n:')
            if x == 'y':
                os.system('clear')
                break

            elif x == 'n':
                sys.exit()

            else:
                continue
  

                
    elif drink_type == 'コーヒー':
        print(drink_dic['コーヒー'],'円です')

        try:
            price = int(input('投入金額を入力して下さい：'))

            if  price == drink_dic['コーヒー']:
                print('商品を購入しました')
                print('お釣りはありません')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break

            elif price > drink_dic['コーヒー']:
                print('商品を購入しました')
                print('お釣りは',price - drink_dic['コーヒー'],'円です')
                x = input('購入を続けますか？ y/n:')
                if x == 'y':
                    os.system('clear')
                    continue
                elif x == 'n':
                    break
            
            else:
                shortage = drink_dic['コーヒー'] - price
                print('投入金額が不足しています')
                print(shortage,'円足りません')

                while shortage > 0:
                    shortage2 = shortage - int(input('投入金額を入力して下さい：'))         
                    if shortage2 == 0:
                        print('商品を購入しました')
                        print('お釣りはありません')
                        break

                    elif shortage2 > 0:
                        print('投入金額が不足しています')
                        print(shortage2,'円足りません')
                        shortage = shortage2
                        continue

                    elif shortage2 < 0:
                        print('商品を購入しました')
                        print('お釣りは',shortage2*-1,'円です')
                        break

        except ValueError:
            print('※数値を入力して下さい')

        while True:
            x = input('購入を続けますか？ y/n:')
            if x == 'y':
                os.system('clear')
                break

            elif x == 'n':
                sys.exit()

            else:
                continue
   
            

    else:
        print('該当商品がありません')
        while True:
            x = input('購入を続けますか？ y/n:')
            if x == 'y':
                os.system('clear')
                break

            elif x == 'n':
                sys.exit()

            else:
                continue
