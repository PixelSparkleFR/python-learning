if __name__ == '__main__':
    prix_tv = 1300
    porte_monaie = int(input("Veuillez renseigner votre argent : "))
    print("Votre porte monaie est de "+ str(porte_monaie)+"€. La télévision que vous voulez acheter est de "+str(prix_tv)+"€.")

    if prix_tv > porte_monaie:
        print("Vous n'avez pas assez d'argent pour l'acheter. Revenez plus tard.")
    else:
        reponse = input("Voulez vous acheter cette télévision ? (O/N) : ")
        if reponse == "O":
            solde_final = porte_monaie - prix_tv
            print("Merci pour votre achat. Votre porte monaie est de maintenant "+str(solde_final)+"€.")
