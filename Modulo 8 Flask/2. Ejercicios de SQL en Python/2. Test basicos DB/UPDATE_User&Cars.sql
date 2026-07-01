UPDATE lyfter_car_rental.users
SET account_status = 'inactive'
WHERE id = 51;


UPDATE lyfter_car_rental.cars
SET car_status = 'maintenance'
WHERE id = 51;


UPDATE lyfter_car_rental.cars
SET car_status = 'out_of_service'
WHERE id = 4;