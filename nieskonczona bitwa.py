#Przegrana bitwa
#Demonstruje przerazajace petle nieskonczone

print("Twoj samotny bohater jest otoczony przez ogromna armie troli.")
print("Wielka masa ich zgnilozielonych cial rozciaga sie az po horyzont.")
print("Bohater wyjmuje miecz z pochwy, gotow do stoczenia ostatniej swej walki.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    print("Bohater pokonuje złego trolla, " \
      "ale odnosi obrażenia i traci", damage, "punkty zdrowia.\n")


print("Twoj bohater walczyl dzielnie i pokonal", trolls, "trolle.")
print("Lecz niestety twoj bohater juz nie zyje")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
