INSERT INTO lyfter_car_rental.rentals 
(user_id, car_id, rental_status)
VALUES 
(50, 4, 'ongoing');

UPDATE lyfter_car_rental.cars
SET car_status = 'rented'
WHERE id = 4;
