import random

def lotto():
    nums = random.sample(range(1, 50), 6)
    inputNums = []

    for i in range(6):
        while True:
            try:
                num = int(input(f"Podaj {i+1}. liczbę: "))
                if num < 1 or num > 49:
                    print("Liczba spoza zakresu. Wybierz liczbę od 1 do 49.")
                    continue                
                if num in inputNums:
                    print("Liczb już podana. Wybierz inną.")
                    continue                
                inputNums.append(num)
                break

            except ValueError:
                print("To nie jest liczba. Podaj ponownie.")

    hit = set(nums) & set(inputNums)
    print(f"Wylosowane liczby: {sorted(nums)}")
    print(f"Typowane liczby: {sorted(inputNums)}")
    print(f"Liczby trafione: {sorted(hit)}")

    with open("wyniki_lotto.txt", "a") as file:
        file.write(f"Wylosowane liczby: {sorted(nums)}\n")
        file.write(f"Typowane liczby: {sorted(inputNums)}\n")
        file.write(f"Liczby trafione: {sorted(hit)}\n")
        file.write("\n")
        
while True:
    lotto()
    option = input("Chcesz zagrać ponownie? (t/n): ")
    if option.lower() == "n":
        break