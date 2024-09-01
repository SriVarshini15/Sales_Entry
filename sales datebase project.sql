create database inventory;
use inventory;
create table category(
    category_id int primary key,
    category_name varchar(100)
);
insert into category (
    category_id,
    category_name
)
values(
    1,
    'Groceries'
);
insert into category (
    category_id,
    category_name
)
values(
    2,
    'Beverages'
);
insert into category (
    category_id,
    category_name
)
values(
    3,
    'Ice-Creams'
);
create table product(
    product_id int primary key,
    product_name varchar(100) not null,
    category_id int not null,
    quantity_in_stock float not null,
    rate float not null,
    foreign key (category_id) references category (category_id)
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    1,
    'Rice 25kg Ponni',
    1,
    25,
    1500
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate
)
values (
    2,
    'Rice 10kg Ponni',
    1,
    25,
    600
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    3,
    'Toor Dhal Udayam 1kg',
    1,
    50,
    100
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    4,
    'Uradh Dhal Udayam 1kg',
    1,
    50,
    90
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate
)
values (
    5,
    'Thumbs up 100ml',
    2,
    30,
    20
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    6,
    'Coco-Cola 100ml',
    2,
    30,
    20
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    7,
    'Sprite 100ml',
    2,
    30,
    20
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    8,
    'Fanta 100ml',
    2,
    30,
    20
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    9,
    'Arun ice cup – Chocolate',
    3,
    10,
    25
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    10,
    'Arun ice cup – Strawberry',
    3,
    10,
    25
);
insert into product (
    product_id,
    product_name,
    category_id,
    Quantity_in_stock,
    Rate 
)
values (
    11,
    'Arun ice cup – Almonds-nut',
    3,
    10,
    25
);
create table `order`(
    order_number int primary key,
    Customer_name varchar(100),
    Date_purchased date not null
); 
create table order_item(
    order_number int not null,
    Item_number int not null,
    Product_id int not null,
    Quantity_purchased int not null,
    Rate float not null,
    value float not null
);
create table order_item(
    order_number int not null,
    Item_number int not null,
    product_id int not null,
    Quantity_purchased int not null,
    Rate float not null,
    value float not null,
    foreign key (order_number) references `order` (order_number),
    foreign key (product_id) references product (product_id)
);