liste_finale = []
wordlist = ["WELCOME", "BONUS", "VIP", "MAX", "CODE", "TEST", "PREPROD"]
for i in wordlist:

    for j in range(0,130,5):
        if j%10 == 5 and j>30:
            continue
        if j==0:
            liste_finale.append(i)
        else:
            liste_finale.append(f'{i}{j}')

    for j in ["2019", "2020", "2021", "2022", "2023"]:
        liste_finale.append(f'{i}{j}')
    
    for k in wordlist:
        if i!=k:
            for j in range(0,130,5):
                if j%10 == 5 and j>30:
                    continue
                if j==0:
                    liste_finale.append(f'{i}{k}')
                else:
                    liste_finale.append(f'{i}{k}{j}')

            for j in ["2019", "2020", "2021", "2022", "2023"]:
                liste_finale.append(f'{i}{k}{j}')

with open("generated_wordlist", "a") as f:
    for _ in liste_finale:
        f.write(f"{_}\n")
