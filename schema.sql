DROP TABLE IF EXISTS zadania;

CREATE TABLE zadania (
    id integer primary key autoincrement,  --identyfikator
    zadanie text not null,   --opis zadania do wykonania
    zrobione boolean not null,   --informacja czy zadanie wykonano
    data_dodania datetime not null --data dodania zadania
);

INSERT INTO zadania (id, zadanie, zrobione, data_dodania)
VALUES (null, 'Posprzątać pokój', 0, datetime(current_timestamp));
INSERT INTO zadania (id, zadanie, zrobione, data_dodania)
VALUES (null, 'Podlać kwiaty', 0, datetime(current_timestamp));