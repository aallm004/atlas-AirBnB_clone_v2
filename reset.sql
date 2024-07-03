select DATABASE() as 'Database', count(*) as 'Tables Before' from information_schema.tables where table_schema = DATABASE();
drop table if exists reviews;
drop table if exists place_amenity;
drop table if exists places;
drop table if exists cities;
drop table if exists states;
drop table if exists users;
drop table if exists amenities;
select ' ' as '', ' ' as '', count(*) as 'Tables After' from information_schema.tables where table_schema = DATABASE();
