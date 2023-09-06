for p in range(3):                    # przykład pętli zagnieżdżonej (1)
    for q in range(4):
        if q==2:
            print(f"Pomijamy q={q}")
            continue                     # pomiń (instrukcja continue) jeśli wartość q=2
        print (f"(p={p} q={q})", end =" ")

print()
print()



for p in range(3):                    # przykład pętli zagnieżdżonej (2)
    for q in range(4):
        if q==2:
            print(f"Wykryto q={q}")
            break                     # wyjdź z iteracji (instrukcja break) jesli wartość q=2
        print (f"(p={p} q={q})", end =" ")

print("* Kilka przykładów użycia pętli while")
