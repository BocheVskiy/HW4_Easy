# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    if len(ticket_number) == 6:
        one_number = ticket_number[:3]
        two_number = ticket_number[3:]

        one_sum = 0
        for i in one_number:
            one_sum = int(i) + one_sum

        two_sum = 0
        for i in two_number:
            two_sum = int(i) + two_sum

        if one_sum == two_sum:
            return True
        else:
            return False

print(lucky_ticket(123122))




