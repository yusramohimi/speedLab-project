import matplotlib.pyplot as plt
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.title('Salaryy for each age')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.plot(dev_x,dev_y)
# plt.show()



py_dev_x = [25,26,27,28,29,30,31,32,33,34,35]
py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(py_dev_x, py_dev_y)
plt.show()



import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11] 
y2 = [1, 4, 6, 8, 10]  

# Création du graphique
plt.plot(x, y1, color="r", linestyle="-", linewidth=2, marker="o", label="Données 1")
plt.plot(x, y2, color="b", linestyle="--", linewidth=2, marker="x", label="Données 2")

# Ajout de titres et étiquettes
plt.title("Comparaison de deux ensembles de données")
plt.xlabel("Titre pour l'axe X")
plt.ylabel("Titre pour l'axe Y")

# Ajout de la légende
plt.legend()

# Affichage du graphique
plt.show()
