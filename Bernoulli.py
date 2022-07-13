import math
def calcule_rac_2eme_deg(suite_coeff) :
    d = (suite_coeff[1] * suite_coeff[1]) - (4 * suite_coeff[0] * suite_coeff[2]) #b2 -4*a*c
    print("delta vaut", d)

    if d > 0:
        x1 = (-suite_coeff[1] - math.sqrt(d)) / (2 * suite_coeff[0])
        x2 = (-suite_coeff[1] + math.sqrt(d)) / (2 * suite_coeff[0])
        y = []
        y.append(x1)
        y.append(x2)
        print("\nSOLUTION!!!")
        print("les racines de l'equation de 2eme degree sont ", y[0],y[1])
    elif d == 0:
        rd = -suite_coeff[1] / (2 * suite_coeff[0]) #-b/2*a
        print("racine double vaut ", rd)
    else:
        print("delta est negatif , les racines sont dans C,alors pour etre sur ,"
              "il faut soit ajouter des iterations ou la valeur d'epsilon est tres grand")

def horner(coef_poly,reste) :
    b=[]
    b.insert(0,coef_poly[0])
    print("b[", 0, "]=", b[0])
    for i in range(1,len(coef_poly)) :
        b.insert(i,(b[i-1]*reste)+coef_poly[i])
        print("b[",i,"]=",b[i-1],"*",reste,"+",coef_poly[i])
        print("= ",b[i],"\n\n")
        #la fonction horner() retourne une liste des coefficients obtenus par la methode d'horner
    return b
#image() ex : pour calculer x3 = x2*a+x1*b+x0*c , a,b,c ne changeant jamais , mais les xi changeant
def image(suite_coeff,x_initiaux) :
    result=0
    for i in range(3) :
        result=result+(suite_coeff[i]*x_initiaux[i])
    return result
#pour le nombre d'iterations maximals lors de la recherche d'une racine on le fixe sur 100000
def bern(suite_coeff,x_initiaux,epsilon,itex_max=100000) :
    x=x_initiaux
    x_de_i_par_image = image(suite_coeff, x)
    #on ajoute x3 a la liste des x initiaux qui a pour taille toujours 3 (contient x de n et c n+1 et x n+2)
    x.insert(0, x_de_i_par_image)
    #on enleve le x de i min de la liste des x initiaux (x3,x2,x1,x0) on enleve x0 ,
    #car lors de la calcule de x4 on aurra pas besoin de x0 , sauf x3 x2 x1
    x.pop()
    iterat=3
    #pour entrer dans la boucle while on prend epsilon =1
    error=1
    while(error>epsilon and error != math.inf  and error != -math.inf) :
         if(iterat>itex_max) :
             break
         if ( error== math.inf  or error== -math.inf ) : #math.inf est l'infini sous python
             break
         print("x",iterat,"= ",x_de_i_par_image)
         print("racine u=",x[0] / x[1])
         x_de_i_par_image = image(suite_coeff, x)
         x.insert(0, x_de_i_par_image)
         x.pop()
         #abs() c'est la fonction valeur absolue
         error = abs((x[0] / x[1]) - (x[1] / x[2]))
         print("avec une erreur = ",error)
         iterat=iterat+1
    print("x", iterat, "= ", x_de_i_par_image)
    print("racine u=", x[0] / x[1])
    print("avec une erreur = ", error)
    return x
def test_funtion() :
    suite_coeff=[]
    x_initiaux=[]
    a_plus_grand_coeff=float((input("Veuillez saisir le coefficient de x de plus grand puissance(x^3)")))

    if(a_plus_grand_coeff!=0) :
        for i in range(0,3) :
            a=float(input("Saisir les autres coefficients de p(x) a0(a) a1(b) a2(c) "))
            suite_coeff.append(a/a_plus_grand_coeff)

        print("Les coefficients du p(x) :\n")
        print(a_plus_grand_coeff,"\n")
        for i in range(0,3) :
            print("a",i," = ",suite_coeff[i])
        for i in range(0,3) :
            b=float(input("saisir les x initiaux x2 x1 x0 successivement"))
            x_initiaux.append(b)
        print("Les xi de depart sont : ")
        for i in range(0, 3):
            print(x_initiaux[i])
        #contidition dans la boucle while pour obliger la saisie d'une epsilon compris entre 0 et 1
        condition_epsilon=True
        while(condition_epsilon) :
            epsilon=float(input("veuillez saisir un epsilon compris entre 0 et 1"))
            condition_epsilon=False
            if (epsilon<0 or epsilon>1) :
                condition_epsilon=True

        #depart de l'algorithme de bernoulli
        #trois_xi_sup_apres_bernouil est une liste qui va contenir [x3;x2,x1] pour le depart de l'algorithme
        #à la fin de l'algorithme ,la liste va contenir xn+2 , xn+1,xn
        trois_xi_sup_apres_bernouil=bern(suite_coeff,x_initiaux,epsilon)
        racine_fin=trois_xi_sup_apres_bernouil[0]/trois_xi_sup_apres_bernouil[1]
        #la racine est la valeur retoutné par l'algorithme de range n+2/n+1
        # l indice 0 s'agit de x n+2  , l'indice 1 s'agit de x n+1 , l'indice 2 s'agit de x n
        print("la racine de p(x) exactement vaut",racine_fin)
        error_exacte = abs((trois_xi_sup_apres_bernouil[0] / trois_xi_sup_apres_bernouil[1]) - (trois_xi_sup_apres_bernouil[1] / trois_xi_sup_apres_bernouil[2]))
        print("pour une erreur de ",error_exacte)
        print("SCHEMA DE HORNER")
        coef_horner=horner(suite_coeff,racine_fin)
        print("les coefficients du polynome obtenues par la methode d'HORNER sont :")
        for i in range(0, 3):
            print("b[", i, "]= ", coef_horner[i])
        calcule_rac_2eme_deg(coef_horner)

    #a de x^3 egale zero , on est dans le cas d'une equation de 2eme degre
    else :
        print("puisque d=0 , on est dans le cas d'une equation de 2eme degre")
        for i in range(0,3) :
            a=float(input("saisir a,b,c de p(x) successivement"))
            suite_coeff.append(a)
        calcule_rac_2eme_deg(suite_coeff)


test_funtion()
