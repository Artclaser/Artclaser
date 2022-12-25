# Demande de l'investissement initial
investment = float(input("Entrez le montant de l'investissement initial (en €) : "))

# Demande du taux de rendement
rate = float(input("Entrez le taux de rendement (en %) : "))

# Demande de la durée de l'investissement
years = int(input("Entrez la durée de l'investissement (en années) : "))

# Calcul de la rentabilité

earnings = investment * (1 + rate / 100) ** years

rentabilité = investment * (1 + rate / 100) ** years

# Affichage du résultat
print(f"Le montant total après {years} ans est de {earnings:.2f}.")


