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
print("""Odpowiedz na 3 pytania aby wyliczyć wartość swojego pozostałego
zadłużenia w każdym miesiącu przez 2 następne lata.""")
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
Luty2 = float((1 + (float(Luty2) + float(oprocentowanie)) / int(kwota)) * float(Styczeń2) - int(rata))
Marzec2 = float((1 + (float(Marzec2) + float(oprocentowanie)) / int(kwota)) * float(Luty2) - int(rata))
Kwiecień2 = float((1 + (float(Kwiecień2) + float(oprocentowanie)) / int(kwota)) * float(Marzec2) - int(rata))
Maj2 = float((1 + (float(Maj2) + float(oprocentowanie)) / int(kwota)) * float(Kwiecień2) - int(rata))
Czerwiec2 = float((1 + (float(Czerwiec2) + float(oprocentowanie)) / int(kwota)) * float(Maj2) - int(rata))
Lipiec2 = float((1 + (float(Lipiec2) + float(oprocentowanie)) / int(kwota)) * float(Czerwiec2) - int(rata))
Sierpień2 = float((1 + (float(Sierpień2) + float(oprocentowanie)) / int(kwota)) * float(Lipiec2) - int(rata))
Wrzesień2 = float((1 + (float(Wrzesień2) + float(oprocentowanie)) / int(kwota)) * float(Sierpień2) - int(rata))
Październik2 =  float((1 + (float(Październik2) + float(oprocentowanie)) / int(kwota)) * float(Wrzesień2) - int(rata))
Listopad2 = float((1 + (float(Listopad2) + float(oprocentowanie)) / int(kwota)) * float(Październik2) - int(rata))
Grudzień2 = float((1 + (float(Grudzień2) + float(oprocentowanie)) / int(kwota)) * float(Listopad2) - int(rata))
#Napisy koncowe
print("W styczniu Twoja pozostała kwota kredytu to {} zł.".format(round(Styczeń)))
print("W lutym Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Luty)), x=(round((Styczeń) - (Luty)))))
print("W marcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Marzec)), x=(round((Luty) - (Marzec)))))
print("W kwietniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Kwiecień)), x=(round((Marzec) - (Kwiecień)))))
print("W maju Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Maj)), x=(round((Kwiecień) - (Maj)))))
print("W czerwcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Czerwiec)), x=(round((Maj) - (Czerwiec)))))
print("W lipcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Lipiec)), x=(round((Czerwiec) - (Lipiec)))))
print("W sierpniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Sierpień)), x=(round((Lipiec) - (Sierpień)))))
print("We wrześniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Wrzesień)), x=(round((Sierpień) - (Wrzesień)))))
print("W październiku Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Październik)), x=(round((Wrzesień) - (Październik)))))
print("W listopadzie Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Listopad)), x=(round((Październik) - (Listopad)))))
print("W grudniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Grudzień)), x=(round((Listopad) - (Grudzień)))))
print("W styczniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Styczeń2)), x=(round((Grudzień) - (Styczeń2)))))
print("W lutym Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Luty2)), x=(round((Styczeń2) - (Luty2)))))
print("W marcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Marzec2)), x=(round((Luty2) - (Marzec2)))))
print("W kwietniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Kwiecień2)), x=(round((Marzec2) - (Kwiecień2)))))
print("W maju Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Maj2)), x=(round((Kwiecień2) - (Maj2)))))
print("W czerwcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Czerwiec2)), x=(round((Maj2) - (Czerwiec2)))))
print("W lipcu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Lipiec2)), x=(round((Czerwiec2) - (Lipiec2)))))
print("W sierpniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Sierpień2)), x=(round((Lipiec2) - (Sierpień2)))))
print("We wrześniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Wrzesień2)), x=(round((Sierpień2) - (Wrzesień2)))))
print("W październiku Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Październik2)), x=(round((Wrzesień2) - (Październik2)))))
print("W listopadzie Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Listopad2)), x=(round((Październik2) - (Listopad2)))))
print("W grudniu Twoja pozostała kwota kredytu to {piniondz} zł. To {x} zł mniej niż w poprzednim miesiącu."
      .format(piniondz=(round(Grudzień2)), x=(round((Listopad2) - (Grudzień2)))))

































