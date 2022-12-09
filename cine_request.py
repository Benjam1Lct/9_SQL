mycursor.execute("SELECT titre FROM film WHERE genre = 'Drame'")
mycursor.execute("SELECT DISTINCT titre FROM film JOIN projection AS p ON p.num_film = film.num_film WHERE p.num_cine = 3")
