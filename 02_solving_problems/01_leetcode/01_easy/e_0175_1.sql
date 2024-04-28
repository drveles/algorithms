SELECT firstname AS firstName, lastname AS lastName, city, state
FROM Address
RIGHT JOIN Person ON Person.PersonId = Address.PersonId 
-- OK, 72%, 100%