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



class Cola:

    def __init__(self, cola_price=input('投入金額を入力して下さい：')):
        self.cola_price = cola_price


    def buy(self):
        if self.cola_price == 120:
            print('コーラを購入しました')

        elif self.cola_price > 120:
            print('コーラを購入しました')
            print('お釣りは¥' + str( self.cola_price - 120 ) + 'です')
        
        else:
            print('投入金額が不足しています')
            print(str( 120 - self.cola_price ) + '円足りません')

            
class Tea:

    def __init__(self, tea_price):
        self.tea_price = tea_price

    def buy(self):
        if self.tea_price == 80:
            print('お茶を購入しました')

        elif self.tea_price > 80:
            print('お茶を購入しました')
            print('お釣りは¥' + str( self.tea_price - 80 ) + 'です')
        
        else:
            print('投入金額が不足しています')
            print(str( 80 - self.tea_price ) + '円足りません')


class Cofe:

    def __init__(self, cofe_price):
        self.cofe_price = cofe_price

    def buy(self):
        if self.cofe_price == 100:
            print('コーヒーを購入しました')

        elif self.cofe_price > 100:
            print('コーヒーを購入しました')
            print('お釣りは¥' + str( self.cofe_price - 100 ) + 'です')
        
        else:
            print('投入金額が不足しています')
            print(str( 100 - self.cofe_price ) + '円足りません')



cola = Cola
tea = Tea
cofe = Cofe

print('コーラ', 'お茶', 'コーヒー')

type = input('購入する商品を選んで下さい：')



if type == 'コーラ':
    cola.buy()

elif type == 'お茶':
    tea.buy(int('投入金額を入力して下さい：'))

elif type == 'コーヒー':
    cofe.buy(int('投入金額を入力して下さい：'))

else:
    print('該当商品がありません')
