# tabela wartosci inflacji:
Styczeń = 1.592824484
Luty = -0.453509101
Marzec = 2.324671717
Kwiecień = 1.261254407
Maj = 1.782526286
Czerwiec = 2.329384541
Lipiec = 1.502229842
Sierpień = 1.782526286
Wrzesień = 2.328848994
Październik = 0.616921348
Listopad = 2.352295886
Grudzień = 0.337779545
Styczeń2 = 1.577035247
Luty2 = -0.292781443
Marzec2 = 2.48619659
Kwiecień2 = 0.267110318
Maj2 = 1.417952672
Czerwiec2 = 1.054243267
Lipiec2 = 1.480520104
Sierpień2 = 1.577035247
Wrzesień2 = -0.07742069
Październik2 = 1.165733399
Listopad2 = -0.404186718
Grudzień2 = 1.499708521
#Pytania, zebranie wartosci dla kwota, oprocentowanie i rata
print("""odpowiedz na 3 pytania aby wyliczyć wartość swojego pozostałego
zadłużenia w każdym miesiącu przez 2 nasępne lata.""")
print("1/3: Jaka jest kwota pożyczki w zł?")
kwota = int(input())
print("2/3: Ile wynosi wartość oprocentowania w procentach?")
oprocentowanie = float(input())
print("3/3: Ile wynosi kwota raty?")
rata = int(input())
#Podsumowanie
print("""Pożyczona kwota to {} zł. Oprocentowanie wynosi {} %.
Obecnie płacisz {} zł raty.""".format(kwota, oprocentowanie, rata))
#Wyliczenia dla kolejnych 24m
Styczeń = float((1 + (float(Styczeń) + float(oprocentowanie)) / int(kwota)) * int(kwota) - int(rata))
Luty = float((1 + (float(Luty) + float(oprocentowanie)) / int(kwota)) * float(Styczeń) - int(rata))
Marzec = float((1 + (float(Marzec) + float(oprocentowanie)) / int(kwota)) * float(Luty) - int(rata))
Kwiecień = float((1 + (float(Kwiecień) + float(oprocentowanie)) / int(kwota)) * float(Marzec) - int(rata))
Maj = float((1 + (float(Maj) + float(oprocentowanie)) / int(kwota)) * float(Kwiecień) - int(rata))
Czerwiec = float((1 + (float(Czerwiec) + float(oprocentowanie)) / int(kwota)) * float(Maj) - int(rata))
Lipiec = float((1 + (float(Lipiec) + float(oprocentowanie)) / int(kwota)) * float(Czerwiec) - int(rata))
Sierpień = float((1 + (float(Sierpień) + float(oprocentowanie)) / int(kwota)) * float(Lipiec) - int(rata))
Wrzesień = float((1 + (float(Wrzesień) + float(oprocentowanie)) / int(kwota)) * float(Sierpień) - int(rata))
Październik = float((1 + (float(Październik) + float(oprocentowanie)) / int(kwota)) * float(Wrzesień) - int(rata))
Listopad = float((1 + (float(Listopad) + float(oprocentowanie)) / int(kwota)) * float(Październik) - int(rata))
Grudzień = float((1 + (float(Grudzień) + float(oprocentowanie)) / int(kwota)) * float(Listopad) - int(rata))
Styczeń2 = float((1 + (float(Styczeń2) + float(oprocentowanie)) / int(kwota)) * int(Grudzień) - int(rata))
Luty2 = float((1 + (float(Luty) + float(oprocentowanie)) / int(kwota)) * float(Styczeń2) - int(rata))
Marzec2 = float((1 + (float(Marzec) + float(oprocentowanie)) / int(kwota)) * float(Luty2) - int(rata))
Kwiecień2 = float((1 + (float(Kwiecień) + float(oprocentowanie)) / int(kwota)) * float(Marzec2) - int(rata))
Maj2 = float((1 + (float(Maj) + float(oprocentowanie)) / int(kwota)) * float(Kwiecień2) - int(rata))
Czerwiec2 = float((1 + (float(Czerwiec) + float(oprocentowanie)) / int(kwota)) * float(Maj2) - int(rata))
Lipiec2 = float((1 + (float(Lipiec) + float(oprocentowanie)) / int(kwota)) * float(Czerwiec2) - int(rata))
Sierpień2 = float((1 + (float(Sierpień) + float(oprocentowanie)) / int(kwota)) * float(Lipiec2) - int(rata))
Wrzesień2 = float((1 + (float(Wrzesień) + float(oprocentowanie)) / int(kwota)) * float(Sierpień2) - int(rata))
Październik2 =  float((1 + (float(Październik) + float(oprocentowanie)) / int(kwota)) * float(Wrzesień2) - int(rata))
Listopad2 = float((1 + (float(Listopad) + float(oprocentowanie)) / int(kwota)) * float(Październik2) - int(rata))
Grudzień2 = float((1 + (float(Grudzień) + float(oprocentowanie)) / int(kwota)) * float(Listopad2) - int(rata))




























