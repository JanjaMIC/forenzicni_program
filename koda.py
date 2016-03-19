spremenljivka = open("dnk.txt").read()
#las
crn_las = "CCAGCAATCGC"
rjavi_las =  "GCCAGTGCCG"
korencek_las = "TTAGCTATCGC"

#obraz
kvadraten_obraz = "GCCACGG"
okrogel_obraz = "ACCACAA"
ovalen_obraz = "AGGCCTCA"

#oci
rjave_oci = "AAGTAGTGAC"
modre_oci = "TTGTGGTGGC"
zelene_oci = "GGGAGGTGGC"

#spol
moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"

#rasa
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

#ziga
ziga =  korencek_las or rjave_oci or okrogel_obraz
matej = crn_las or modre_oci or ovalen_obraz
miha =  rjavi_las or zelene_oci or kvadraten_obraz


if spremenljivka.find(ziga)>0:
    print "Ziga je lopov."

if spremenljivka.find(matej)>0:
    print "Matej je lopov."

if spremenljivka.find(miha)>0:
    print "Miha je lopov."

