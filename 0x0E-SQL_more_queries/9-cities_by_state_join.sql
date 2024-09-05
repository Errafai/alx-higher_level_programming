-- display the id of cities and cities with thier states
SELECT cities.id, cities.name, states.name
	FROM cities INNER JOIN states
	WHERE cities.state_id = states.id
