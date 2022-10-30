per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
deposit = []
for values in per_cent.values():
    deposit.append(int(money * values / 100))
max_income = max(deposit)
print(f"Cумма, которую вы можете заработать - {deposit}")
print(f"Максимальная сумма, которую вы можете заработать - {max_income}")
