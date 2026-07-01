CREATE TABLE lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    account_status VARCHAR(20) NOT NULL DEFAULT 'active'
);

Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Marilyn Marvin', 'Irving.Renner@hotmail.com', 'Joelle76', 'hgHCmLAjl2HUaII', '2024-12-24', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Joyce Ledner', 'Allen_Goyette@hotmail.com', 'Laron.Effertz', 'lzDG585OjxmDOxv', '2025-03-21', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Frances Schinner-Sporer', 'Jeannette.Collins@gmail.com', 'Zachery_Durgan', 'hPf4PrgJQUQaGmz', '2024-09-11', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Ismael Wilderman', 'Gregg_Kihn35@gmail.com', 'Bernard.Klein', '_KMM5XGvOMgSyFw', '2024-08-06', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Meredith Klocko', 'Ricardo_Simonis69@gmail.com', 'Delpha_Hackett18', 'kXcKT_sNAGg3SCN', '2024-11-04', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Sarah Kulas', 'Scott.Durgan@yahoo.com', 'Devan_Marks71', '719uEMQXDXMx7RV', '2024-12-17', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Myra White', 'Kent.Kunze81@gmail.com', 'Julianne72', 'tjI1v_LcGv5ldIN', '2024-08-03', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Sidney Streich PhD', 'Alonzo.Hudson23@yahoo.com', 'Nels.Lowe12', 'PK36z_fIJXuWKLJ', '2024-12-23', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Ricky Buckridge', 'Brandon_Gusikowski@hotmail.com', 'Guillermo_Marquardt59', 'kmn1MYrjDH1U8fP', '2025-06-15', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Flora Rosenbaum', 'Sammy_Abbott79@gmail.com', 'Don_Borer34', 'vrnOkziexDEk1R_', '2024-08-14', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Marcella Braun', 'Marsha_Harvey0@hotmail.com', 'Earnestine.Mraz73', '5r2iqcwX5eHzhB2', '2024-07-14', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Rex Stokes', 'Dianna.Pollich@yahoo.com', 'Reid.Cassin55', 'UoRBAQZqLX0IwRh', '2024-12-19', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Eddie Jakubowski', 'Willie.Franecki@yahoo.com', 'Ryder.Collins', '8NkOskZ3yF3ZtEa', '2024-09-24', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Melba Farrell', 'Gwendolyn.Gulgowski@gmail.com', 'Jacky.Franecki', 'LOsICBX8veQ15Sv', '2024-12-19', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Colin Schinner', 'Matthew_Fahey@gmail.com', 'Juston_Abbott85', '99dl3X_ixI2eXJI', '2025-06-24', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Kirk Schaefer DDS', 'Angelo.Lowe@hotmail.com', 'Collin76', 'n0jreAT6ILtmD98', '2025-03-18', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Roberta Wiza', 'Mario_Lang-Jakubowski76@yahoo.com', 'Cristian.Zemlak', 'jx3xDs1f5trdcrv', '2024-11-03', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Rudy Medhurst', 'Victor_Dach61@gmail.com', 'Cielo.Tremblay79', 'ruI0dEXahWc7ThP', '2024-11-25', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Ruby Weber', 'Katie_Ritchie66@gmail.com', 'Clemens_Schumm', '54hs2rYF6YRri_E', '2025-04-20', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Marilyn Borer', 'Natasha.Hudson@yahoo.com', 'Marcel71', '9CcGxHJjGOgAX7E', '2025-05-28', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Angel Kovacek', 'Kathy_Sporer8@yahoo.com', 'Michele_Tremblay21', '108RfLvZRjwfdYE', '2024-07-07', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Tom Schuster', 'Ruby.Dooley26@gmail.com', 'Berenice_Lockman', '2J94cgxW8n_IqkG', '2025-04-25', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Darryl Brown', 'Judy.Kris72@hotmail.com', 'Libby69', '5t7aFaw0u_wmsm8', '2024-11-04', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Corey Waters Sr.', 'Miriam.McLaughlin19@hotmail.com', 'Maryjane_Stokes', '8rjidtqn1owW1D2', '2025-05-23', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Mamie Ward', 'Kristine_Koepp29@yahoo.com', 'Karianne52', 'vVTuFiZOjuxtpuH', '2024-11-12', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Lola Dare', 'Tamara_Lakin@hotmail.com', 'Caleb_Greenfelder77', 'CWoklVBjPESKJH9', '2025-01-08', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Linda Orn', 'Mack_Schamberger91@yahoo.com', 'Janelle.Leffler89', 'heFlpkmNpdTjx36', '2025-03-14', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Ed Stamm', 'Sonia_Hand43@gmail.com', 'Elbert31', 'cSpOVwpn6mjcacy', '2025-01-22', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Frederick Jaskolski', 'Douglas_Walsh@hotmail.com', 'Ruben_Kling', 'aoyDM7Y9u8X3Tww', '2024-09-16', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Dr. Kathy Quigley', 'Daniel.Hegmann@yahoo.com', 'Nikki_Mertz', '06dBWjIb9HpPq6K', '2024-10-10', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Jennifer Tromp', 'Sergio_Bosco@hotmail.com', 'Wade_Hegmann5', 'SsDZq6CX0G4Wakv', '2025-02-23', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Phillip Gibson', 'Gertrude.Fay@gmail.com', 'Gerhard90', 'kNDNHsWqKcfWbB8', '2025-06-06', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Rebecca Boyle', 'Israel_Rosenbaum29@gmail.com', 'Clovis.Effertz42', 'pGRRCApy1Mu1fcx', '2024-11-25', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Gertrude Schneider', 'Fredrick_Daniel@gmail.com', 'Lucienne_Boyle68', 'aEgVcVD_w52LheW', '2025-02-11', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Jay Pollich I', 'Samantha_Schulist@hotmail.com', 'Ephraim59', 'AYFkco0ULsUJ0sg', '2024-08-10', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Howard Kuhic', 'Mamie_Pouros@hotmail.com', 'Julius_Hilll90', 'WLtJn7LcFXZbnQ3', '2025-06-21', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Meredith Herzog', 'Jennifer_Lueilwitz@yahoo.com', 'Trycia.Predovic', 'NipfiCdowjBm1UF', '2024-07-05', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Jon Gutkowski', 'Don.Larson@hotmail.com', 'Dandre41', 'EDuSKYHG9NzNWau', '2024-12-08', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Florence Schowalter', 'Laverne_Prohaska@hotmail.com', 'Trey_Feil22', 'DwkhMoYJxORdMPT', '2025-02-24', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Kristopher Herman V', 'Ruth_Lebsack@gmail.com', 'Ericka72', 'cPpDRa2yT96gZ7p', '2024-10-05', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Vincent Jones', 'Mindy.Collier78@yahoo.com', 'Rashawn12', 'CLX8XFXqNRS6via', '2024-07-27', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Felix Hettinger DDS', 'Dave.Leffler56@hotmail.com', 'Nick_Parker53', 'R_O2M4I7Vvt4T1b', '2025-06-09', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Pat Daugherty', 'Victoria.Parisian@hotmail.com', 'Logan44', 'pi1U15o01jA9ryx', '2024-07-14', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Dianne White', 'Doris_Kohler@yahoo.com', 'Twila.Torp36', 'D9Te9vdI6lbyjob', '2025-04-10', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Victor Steuber', 'Jack.Hodkiewicz@hotmail.com', 'Addison_Parker87', 'pD3tHjYQUCyWbia', '2024-11-03', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Shelly Mertz', 'Melba.Nikolaus68@yahoo.com', 'Barbara.Russel18', 'pO30Lmr05Xucglo', '2024-08-01', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Noel Strosin', 'Allan.Wiegand-Rempel@yahoo.com', 'Erica.Denesik84', 'PYIXR1gmYnC3e8p', '2024-08-05', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Janice Padberg', 'Ernesto_Reichert@yahoo.com', 'Dawson24', 'KoB4wv95bpYIlrs', '2024-08-11', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Marvin Runolfsson', 'Grace_Wuckert@gmail.com', 'Ahmed16', 'avt4O6XkxwLl6J3', '2025-03-28', 'active');
Insert Into lyfter_car_rental.users (full_name, email, username, password, birth_date, account_status) VALUES ('Velma Zemlak', 'Roger_Bechtelar@hotmail.com', 'Zechariah55', 'uKfZrwvbROsgBPH', '2025-04-27', 'active');

