drop table amazon_table;
drop table nordstroms_table;
drop table mfa_table;
drop table corporate_analysis;


create table amazon_table (
"date" date,
"open" float8,
"high" float8,
"low" float8,
"close" float8,
"volume" float8
);

create table nordstroms_table (
"date" date,
"open" float8,
"high" float8,
"low" float8,
"close" float8,
"volume" float8
);

create table mfa_table (
"date" date,
"open" float8,
"high" float8,
"low" float8,
"close" float8,
"volume" float8
);

create table corporate_analysis (
"Company" text,
"Analysis" text
);
