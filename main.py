import random

class Domanda:
    def __init__(self, testo, livello, corretta, risposte = []):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.risposte = risposte

    def __str__(self):
        return f" {self.testo}"


infile = open("domande.txt", "r")
line = infile.readline()
domande = []

while line != "":
    while line != "\n":
        testo = line
        livello = infile.readline()
        corretta = infile.readline()
        errata1 = infile.readline()
        errata2 = infile.readline()
        errata3 = infile.readline()
        risposte = [corretta, errata1, errata2, errata3]
        line = infile.readline()
        d = Domanda(testo, livello, corretta, risposte)
        domande.append(d)
    line = infile.readline()
infile.close()


class Punteggio:
    def __init__(self, nickname, punti):
        self.nickname = nickname
        self.punti = punti

    def __str__(self):
        return (f"{self.nickname} {self.punti} \n")

liv = 0
punteggio = 0
for d in domande:
    domanda = random.choice(domande)
    risposte = domanda.risposte[:] #in modo da non puntare alla stessa lista in memoria
    random.shuffle(risposte)

    print(f"Livello {liv}: {domanda.testo}")
    for i, risposta in enumerate(risposte, 1):
        print(f"{i}. {risposta}")

    scelta = int(input("Inserisci la risposta corretta:"))
    if risposte[scelta - 1] == domanda.corretta:
        print("La risposta è corretta")
        punteggio += 1
        liv += 1
    else:
        print(f"La risposta è errata! La risposta corretta era {domanda.corretta}")
        break


nickname = str(input("Inserisci il tuo nickname:"))
file_punti = open("punti.txt", "r")
p = Punteggio(nickname, punteggio)
punteggi = []
punteggi.append(p)

riga = file_punti.readline()
while riga != "":
    info = riga.strip().split(" ")
    punteggi.append(Punteggio(info[0], int(info[1])))
    riga = file_punti.readline()
file_punti.close()


outfile = open("punti.txt", "a")
outfile.write(f"\n{nickname} {punteggio}")
outfile.close()

punteggi.sort(key=lambda x: x.punti, reverse=True)
with open("punti.txt", "w") as file_finale:
    for p in punteggi:
        file_finale.write(p.__str__())
