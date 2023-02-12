def send_sms():
    number = input("Zadejte cislo, kam chcete poslat SMS: ")
    if not check_number(number):
        print("Neplatne cislo.")
        return
    message = input("Zadejte text zpravy: ")
    cost = calculate_cost(message)
    print("Cena zpravy bude", cost, "Kc.")

def check_number(number):
    if len(number) == 9 or (len(number) == 13 and number[:4] == "+420"):
        return True
    return False

def calculate_cost(message):
    return (len(message) // 180 + 1) * 3

send_sms()
