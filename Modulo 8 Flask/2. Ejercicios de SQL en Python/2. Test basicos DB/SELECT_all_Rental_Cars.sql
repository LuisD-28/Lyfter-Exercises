SELECT c.*
FROM lyfter_car_rental.cars c
JOIN lyfter_car_rental.rentals r
ON c.id = r.car_id
WHERE r.rental_status = 'ongoing';


SELECT *
FROM lyfter_car_rental.cars
WHERE car_status = 'available';