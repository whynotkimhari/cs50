SELECT movies.title FROM movies JOIN stars, people
ON movies.id = stars.movie_id AND people.id = stars.person_id AND people.name = "Johnny Depp"
WHERE movies.id IN (SELECT movies.id FROM movies JOIN stars, people ON movies.id = stars.movie_id AND people.id = stars.person_id AND people.name =  "Helena Bonham Carter");