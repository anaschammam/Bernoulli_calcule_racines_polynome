import math
def calcule_rac_2eme_deg(suite_coeff) :
    d = (suite_coeff[1] * suite_coeff[1]) - (4 * suite_coeff[0] * suite_coeff[2]) #b2 -4*a*c
    racine=[]
    if d > 0:
        x1 = (-suite_coeff[1] - math.sqrt(d)) / (2 * suite_coeff[0])
        x2 = (-suite_coeff[1] + math.sqrt(d)) / (2 * suite_coeff[0])
        racine.append(x1)
        racine.append(x2)
    elif d == 0:
        rd = -suite_coeff[1] / (2 * suite_coeff[0]) #-b/2*a
        racine.append(rd)
    else:
        pass
    return racine,d

def horner(coef_poly,x_etoile) :
    print("P(X)=",coef_poly)
    b=[]
    b.insert(0,coef_poly[0])
    for i in range(1,len(coef_poly)) :
        b.insert(i,(b[i-1]*x_etoile)+coef_poly[i])
        #la fonction horner() retourne une liste des coefficients obtenus par la methode d'horner
    if(len(b)>2) :
        b.pop() #eliminer le reste de la division de p(x) par x-x_etoile
    return b
#image() ex : pour calculer x3 = x2*a+x1*b+x0*c , a,b,c ne changeant jamais , mais les xi changeant
def image(suite_coeff,x_initiaux) :
    result=0
    for i in range(len(suite_coeff)) :
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
    e1=1
    e2=1
    #pour entrer dans la boucle while on prend epsilon =1
    error=1
    while(error>epsilon) :
        if (math.isfinite(x[0] / x[1]) == False or math.isfinite(x[1] / x[2]) == False or x[1]==0 or x[2]==0):
            x[0]=x[1]
            x[1]=x[2]
            break
        else :
            x_de_i_par_image = image(suite_coeff, x)
            x.insert(0, x_de_i_par_image)
            x.pop()
            if(x[1]!=0 and x[2]!=0 and math.isfinite(x[0] / x[1]) and math.isfinite(x[1] / x[2])) :
                e1 = x[0] / x[1]
                e2 = x[1] / x[2]
                print("u=", x[0] / x[1])
            error = abs(e1 - e2)
            print("avec une erreur = ", error)
            if (x[1] == 0 or x[2] == 0 or math.isfinite(x[0] / x[1]) == False or math.isfinite(x[1] / x[2]) == False ):
                x[0] = x[1]
                x[1] = x[2]
                break
            iterat = iterat + 1

    return x
def deviser_par_a0(suite_coeff) :
    for i in range(1,len(suite_coeff)) :
        suite_coeff[i]=-suite_coeff[i]/suite_coeff[0]
    return suite_coeff
def test_funtion() :
    suite_coeff=[]
    x_initiaux=[]

    degre_n=int(input("saisir le degre du polynome"))
    racine=[]
    erreurs=[]
    if (degre_n>2) :
        for i in range(0, degre_n + 1):
            a = float(input("Saisir les coefficients de p(x) de plus grand au plus petit "))
            suite_coeff.append(a)

        print("Les coefficients du p(x) :\n")
        for i in range(0, len(suite_coeff)):
            print("a", i, " = ", suite_coeff[i])
        for i in range(0, degre_n):
            b = float(input("saisir les x initiaux successivement"))
            x_initiaux.append(b)
        print("Les xi de depart sont : ")
        for i in range(0, degre_n):
            print(x_initiaux[i])
        # contidition dans la boucle while pour obliger la saisie d'une epsilon compris entre 0 et 1
        condition_epsilon = True
        while (condition_epsilon):
            epsilon = float(input("veuillez saisir un epsilon compris entre 0 et 1"))
            condition_epsilon = False
            if (epsilon < 0 or epsilon > 1):
                condition_epsilon = True
        while(degre_n>2) :

            #depart de l'algorithme de bernoulli
            #trois_xi_sup_apres_bernouil est une liste qui va contenir [x3;x2,x1] pour le depart de l'algorithme
            #à la fin de l'algorithme ,la liste va contenir xn+2 , xn+1,xn
            if(suite_coeff[0]!=0) :
                suite_to_horner=suite_coeff.copy()
                suite_coeff=deviser_par_a0(suite_coeff)
                suite_coeff.pop(0)
                xi_bernouil=bern(suite_coeff,x_initiaux,epsilon)
                racine_fin=xi_bernouil[0]/xi_bernouil[1]
                #la racine est la valeur retoutné par l'algorithme de range n+2/n+1
                # l indice 0 s'agit de x n+2  , l'indice 1 s'agit de x n+1 , l'indice 2 s'agit de x n
                print("la racine de p(x) exactement vaut",racine_fin)
                racine.append(racine_fin)
                error_exacte = abs((xi_bernouil[0] / xi_bernouil[1]) - (xi_bernouil[1] / xi_bernouil[2]))
                print("pour une erreur de ",error_exacte)
                erreurs.append(error_exacte)
                print("SCHEMA DE HORNER")
                coef_horner=horner(suite_to_horner,racine_fin)
                print("les coefficients du Q(X) obtenues par la methode d'HORNER sont :")
                for i in range(0, degre_n):
                    print("b[", i, "]= ", coef_horner[i])
                degre_n=degre_n-1
                suite_coeff=coef_horner
                x_initiaux=xi_bernouil
            else :
                degre_n=degre_n-1
                continue
            r_2eme,delta=calcule_rac_2eme_deg(coef_horner)
            racine.append(r_2eme)
        print("delta vaut",delta,"\nles racines réelles sont :",racine)
        # a de x^3 egale zero , on est dans le cas d'une equation de 2eme degre
    elif (degre_n == 2):
            print("puisque n=2 , on est dans le cas d'une equation de 2eme degre")
            for i in range(0, 3):
                a = float(input("saisir a,b,c de p(x) successivement"))
                suite_coeff.append(a)
            racine,delta=calcule_rac_2eme_deg(suite_coeff)
            print("delta vaut", delta, "\nles racines réelles sont :", racine)

    elif(degre_n==1) :
            a = float(input("saisir a"))
            b = float(input("saisir b"))
            print("x etoile vaut",-b/a)
    else :
        print("tout x est solution dans R")





test_funtion()
