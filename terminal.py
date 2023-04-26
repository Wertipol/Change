productMoney = int(input('Сколько стоит сумма всех товаров: '))
userMoney = int(input('Сколько вы даете денег продавцу: '))
coins = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]
changeCoins = []

change = userMoney - productMoney
value = change

while value > 0:
    for i in range(len(coins)):
        while value >= coins[i]:
            value -= coins[i]
            changeCoins.append(coins[i])

print(f'Ваша сдача должна составлять: {change} \nПо начилным это:')
print(*changeCoins, sep=', ')
