
x = open("dnk.txt").read()
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


if x.find(korencek_las) > 0 and x.find(rjave_oci) > 0 and x.find(okrogel_obraz) > 0:
    print "Ziga je lopov."

if x.find(crn_las) > 0 and x.find(modre_oci) > 0 and x.find(ovalen_obraz) > 0:
    print "Matej je lopov."

if x.find(rjavi_las) > 0 and x.find(zelene_oci) > 0 and x.find(kvadraten_obraz) > 0:
    print "Miha je lopov."

