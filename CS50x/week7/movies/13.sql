SELECT people.name FROM people JOIN stars, movies
ON people.id = stars.person_id AND movies.id = stars.movie_id AND people.name != "Kevin Bacon"
WHERE movies.id IN (SELECT movies.id FROM movies JOIN stars, people ON people.id = stars.person_id AND movies.id = stars.movie_id AND people.name = "Kevin Bacon");