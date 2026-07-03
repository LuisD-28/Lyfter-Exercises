UPDATE lyfter_car_rental.rentals
SET rental_status = 'completed'
WHERE id = 4;


UPDATE lyfter_car_rental.cars
SET car_status = 'available'
WHERE id = (
    SELECT car_id 
    FROM lyfter_car_rental.rentals 
    WHERE id = 4
);
