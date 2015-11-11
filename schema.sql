drop table if exists users;
create table users (
  id integer primary key autoincrement,
  user_name text not null
);

drop table if exists progression;
create table progression(
    id integer primary key autoincrement,
    user_name text,
    story_name text,
    point_number integer,
    FOREIGN KEY (user_name) REFERENCES users(user_name)
);