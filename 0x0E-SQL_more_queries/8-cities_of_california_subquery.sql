-- display a table has only the cities that are in the california state
SELECT cities.id, cities.name
	FROM cities, states
	WHERE cities.state_id = states.id AND states.name = "California"
