SELECT Person.email AS Email 
FROM Person
GROUP BY Email HAVING COUNT(*) > 1

-- OK,  32%,  100%