


import cv2

# Charger l'image
image = cv2.imread("parcking.jpg")

if image is None:
    print("Erreur : image introuvable")

else:
    image = cv2.resize(image, (800, 600))

    # Définir les places de parking
    places = [
        (100, 100, 100, 100),
        (220, 100, 100, 100),
        (340, 100, 100, 100)
    ]

    for x, y, w, h in places:

        # Extraire la zone de parcking
        roi = image[y:y+h, x:x+w]

        # Calculer la luminosité moyenne
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        moyenne = gray.mean()

        # Déterminer l'état de la place
        if moyenne > 100:
            couleur = (0, 255, 0)
            etat = "LIBRE"
        else:
            couleur = (0, 0, 255)
            etat = "OCCUPEE"

        # Dessiner le rectangle
        cv2.rectangle(image, (x, y), (x+w, y+h), couleur, 3)

        # Afficher l'état
        cv2.putText(
            image,
            etat,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            couleur,
            2
        )

    cv2.imshow("SMART PARCKING", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
