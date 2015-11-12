drop table if exists users;
create table users (
  id integer primary key autoincrement,
  user_name text unique not null
);

drop table if exists progression;
create table progression(
    id integer primary key autoincrement,
    user_name text not null,
    story_name text not null,
    point_number integer default 0,
    FOREIGN KEY (user_name) REFERENCES users(user_name)
);