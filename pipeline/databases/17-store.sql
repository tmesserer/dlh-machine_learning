-- this comment is a description of the script below
DELIMITER $$
CREATE TRIGGER dec_stock
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE NEW.item_name = name;
END$$
DELIMITER ;
