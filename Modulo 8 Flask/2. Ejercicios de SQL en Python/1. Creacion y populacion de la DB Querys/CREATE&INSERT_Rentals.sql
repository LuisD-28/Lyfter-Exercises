CREATE TABLE lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES lyfter_car_rental.users(id),
    car_id INT NOT NULL REFERENCES lyfter_car_rental.cars(id),
    rental_date TIMESTAMP DEFAULT NOW(),
    rental_status VARCHAR(20) NOT NULL DEFAULT 'ongoing'
);

INSERT INTO lyfter_car_rental.rentals (user_id, car_id, rental_status)
VALUES
(1, 2, 'ongoing'),
(3, 1, 'completed'),
(4, 5, 'completed');