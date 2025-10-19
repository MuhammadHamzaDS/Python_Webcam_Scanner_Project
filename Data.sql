CREATE DATABASE barcode_system;

USE barcode_system;

CREATE TABLE scanned_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    barcode_data VARCHAR(255),
    scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM barcode_system;
