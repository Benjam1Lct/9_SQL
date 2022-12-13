"""
1.
SELECT DISTINCT titre 
FROM film 
WHERE genre = 'drame'

2.
SELECT Distinct titre, f.num_film  
FROM  film AS f 
JOIN projection AS p 
ON p.num_film = f.num_film 
JOIN cinema AS c 
ON c.num_cine = p.num_cine 
WHERE p.num_cine = 3 ;

3.
SELECT Distinct i.nom, i.prenom  
FROM  individu AS i 
JOIN film AS f 
ON i.num_ind = f.num_ind 

4.
SELECT Distinct i.nom, i.prenom  
FROM  individu AS i 
JOIN jouer AS j 
ON i.num_ind = j.num_ind 
JOIN film AS f 
ON f.num_film = j.num_film                                 

5.
SELECT DISTINCT i.nom, i.prenom 
FROM  individu AS i 
JOIN film AS f 
ON f.num_ind = i.num_ind 
JOIN jouer AS j 
ON j.num_ind = f.num_ind ;

6.
SELECT DISTINCT titre 
FROM film AS f 
JOIN projection AS p 
ON f.num_film = p.num_film 
WHERE p.dates <= '2002-12-31' AND p.dates >= '2002-01-01' ;

7.
SELECT DISTINCT titre 
FROM film 
WHERE film.num_ind = 3
                    
8.
SELECT DISTINCT i.nom, i.prenom 
FROM individu AS i 
JOIN (SELECT f.num_ind, f.genre 
    FROM film AS f ) AS film_dr
ON film_dr.num_ind = i.num_ind
JOIN (SELECT f.num_ind, f.genre 
    FROM film AS f ) AS film_ep
ON film_ep.num_ind = i.num_ind
WHERE film_dr.genre = 'drame' AND film_ep.genre = 'epouvante' ;

9.                                
SELECT DISTINCT titre 
FROM  film AS f 
JOIN projection AS p 
ON p.num_film = f.num_film 
JOIN jouer AS j 
ON j.num_film = f.num_film 
JOIN individu AS i 
ON i.num_ind = j.num_ind 
WHERE p.num_cine = 3 AND i.nom = 'kidman' AND i.prenom = 'nicole' ;

10.
SELECT DISTINCT i.nom, i.prenom 
FROM individu AS i 
JOIN jouer AS j 
ON j.num_ind = i.num_ind
JOIN film AS f 
ON f.num_film = j.num_film
WHERE f.genre != 'drame' ;

11.
SELECT DISTINCT i.nom, i.prenom 
FROM individu AS i
JOIN (SELECT Distinct i.nom, i.prenom  
    FROM  individu AS i 
    JOIN film AS f 
    ON i.num_ind = f.num_ind) AS rea 
ON i.prenom = rea.prenom
JOIN (SELECT Distinct i.nom, i.prenom  
    FROM  individu AS i
    JOIN jouer AS j 
    ON i.num_ind = j.num_ind 
    JOIN film AS f 
    ON f.num_film = j.num_film ) AS acteur
ON i.prenom = acteur.prenom
WHERE acteur.prenom LIKE rea.prenom AND acteur.nom != rea.nom

12.
SELECT DISTINCT i.nom, i.prenom 
FROM  individu AS i 
JOIN jouer AS j 
ON j.num_ind = i.num_ind
JOIN projection AS p
ON p.num_film = j.num_film 
JOIN cinema AS c 
ON c.num_cine = p.num_cine
WHERE p.num_cine = 3 AND p.dates LIKE '2%' ;

13.
SELECT DISTINCT titre 
FROM film AS f 
JOIN projection AS p 
ON p.num_film = f.num_film
WHERE YEAR(f.annee)+5 <= YEAR(p.dates)
"""