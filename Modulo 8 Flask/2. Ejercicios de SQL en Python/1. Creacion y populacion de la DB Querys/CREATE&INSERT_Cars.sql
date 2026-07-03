CREATE TABLE lyfter_car_rental.cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    manufacture_year INT NOT NULL,
    car_status VARCHAR(20) NOT NULL DEFAULT 'available'
);

INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Toyota', 'Corolla', 2020, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Honda', 'Civic', 2019, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Ford', 'Focus', 2018, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Chevrolet', 'Cruze', 2017, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Nissan', 'Sentra', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Hyundai', 'Elantra', 2022, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Kia', 'Rio', 2019, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Volkswagen', 'Jetta', 2018, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Mazda', 'Mazda3', 2020, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Subaru', 'Impreza', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('BMW', '320i', 2017, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Mercedes-Benz', 'C200', 2019, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Audi', 'A4', 2020, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Lexus', 'IS300', 2022, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Tesla', 'Model 3', 2023, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Volvo', 'S60', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Peugeot', '208', 2018, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Renault', 'Clio', 2019, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Fiat', 'Tipo', 2017, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Skoda', 'Octavia', 2020, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Seat', 'Leon', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Mitsubishi', 'Lancer', 2016, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Suzuki', 'Swift', 2022, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Jeep', 'Compass', 2020, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Dodge', 'Charger', 2019, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Chrysler', '300', 2018, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('GMC', 'Terrain', 2021, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Cadillac', 'CT5', 2022, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Infiniti', 'Q50', 2020, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Acura', 'TLX', 2023, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Alfa Romeo', 'Giulia', 2021, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Mini', 'Cooper', 2019, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Jaguar', 'XE', 2018, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Land Rover', 'Discovery Sport', 2020, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Porsche', 'Macan', 2022, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Ferrari', 'Roma', 2023, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Lamborghini', 'Urus', 2024, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Aston Martin', 'Vantage', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Bentley', 'Continental GT', 2020, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Rolls-Royce', 'Ghost', 2022, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('BYD', 'Qin Plus', 2023, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Geely', 'Emgrand', 2021, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Chery', 'Arrizo 5', 2020, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Great Wall', 'Haval H6', 2022, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Tata', 'Altroz', 2019, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Mahindra', 'XUV300', 2021, 'rented');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Opel', 'Astra', 2018, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Citroen', 'C4', 2020, 'maintenance');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('DS', 'DS 4', 2022, 'available');
INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES ('Cupra', 'Formentor', 2023, 'rented');