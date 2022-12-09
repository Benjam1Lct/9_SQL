mycursor.execute("SELECT titre FROM film WHERE genre = 'Drame'")
mycursor.execute("SELECT DISTINCT titre FROM film JOIN projection AS p ON p.num_film = film.num_film WHERE p.num_cine = 3")
mycursor.execute("SELECT DISTINCT nom, prenom FROM individu ")
mycursor.execute("SELECT DISTINCT nom, prenom FROM individu JOIN film AS f ON f.num_ind = individu.num_ind")
