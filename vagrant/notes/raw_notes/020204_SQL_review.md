#### SQL Review

##### Manipulating Data
- [INSERT](http://www.postgresqltutorial.com/postgresql-insert/)
  - INSERT Syntax:

        INSERT INTO table(column1, column2, ...)
        VALUES (value1, value2,...);

  1. Specify the name of the table you want to insert a new row after the `INSERT INTO` clause, followed by a comma-seperated column list
  2. List a comma-seperated value list after the `VALUES` clause. The value list must be in the same order as the columns list specified after the table name.
  - INSERT Syntax with multiple rows:

        INSERT INTO table(column1, column2, ...)
        VALUES
          (value1, value2,...),
          (value1, value2,...), ...;

  - INSERT Syntax from another table:

        INSERT INTO table (column1, column2, ...)
        SELECT column1,column2,...
        FROM another_table
        WHERE condition;

- [UPDATE](http://www.postgresqltutorial.com/postgresql-update/)
  - UPDATE Syntax:

        UPDATE table
        SET column1 = value1
            column2 = value2 , ...
        WHERE condition

  1. Specify table name where you want to update data after `UPDATE` clause
  2. List the columns whose values you want to change in the `SET` clause.
    - If you update values in multiple columns, you use a comma (,) to separate each pair of column and value.
    - The columns that are not on the list retain their original values.
  3. Determine which rows you want to update in the condition of the `WHERE` clause.
    - if you omit the `WHERE` clause, all rows will be updated
- [DELETE](http://www.postgresqltutorial.com/postgresql-delete/)
  - DELETE Syntax:

        DELETE from table
        WHERE condition;

  1. Specify the table from which you want to delete data in the `DELETE FROM` clause
  2. Specify which rows you want to delete by using the condition in the `WHERE` clause.
    - The `WHERE` clause is optional; if omitted, all rows in the table will be deleted.

##### Querying Data
The [SELECT](http://www.postgresqltutorial.com/postgresql-select/) statement has the following clauses:

- General SELECT Syntax:

      SELECT
        column_1,
        column_2,
        ...
      FROM
        table_name;

  1. Specify the column of the table from which you want to query data in the `SELECT` clause
    - if you retrieve data from multiple columns, use a list of comma-seperated columns
    - in case you want to query data from all columns, you can use an asterisk (\*) as the shorthand
  2. Specify the name of the table from which you want to query data after the `FROM` keyword
- Using SELECT statement to query data from multiple columns:

      SELECT
        first_name,
        last_name,
        email
      FROM
        customer;

- Using SELECT statement to query data in all columns of a table:

      SELECT
        *
      FROM
        customer;

  - you should only use the asterisk (\*) shorthand for the ad-hoc queries to examine the data of a table
    - the asterisk (\*) retrieves all data from a table, which is usually unnecessary
    - the asterisk (\*) may retrieve unnecessary data from the database which increases the database and application layers, making your application slower and less scalable
- Using SELECT statement with only expressions example:

      SELECT 5 * 3 AS result;

  - Related Tutorial: [PostgreSQL LIMIT](http://www.postgresqltutorial.com/postgresql-limit/)

##### Structuring Data
- [CREATE TABLE](http://www.postgresqltutorial.com/postgresql-create-table/)
  - `CREATE TABLE` syntax:

        CREATE TABLE table_name (
          column_name TYPE column_constraint,
          table_constraint, table constraint
        ) INHERITS existing_table_name

    1. Specify the name of the new table after the `CREATE TABLE` clause
      - Use `TEMPORARY` to create a [temporary table](http://www.postgresqltutorial.com/postgresql-temporary-table/) ([temporary table tutorial](http://www.postgresqltutorial.com/postgresql-temporary-table/))
    2. List column name, data type, and column constraint (define rules for the column)
    2. Specify existing table from which the new table inherits; new table will contain all columns of the existing table and the columns defined in the `CREATE TABLE` statement
  - PostgreSQL column constraints:
    - [NOT NULL](http://www.postgresqltutorial.com/postgresql-not-null-constraint/): value of column cannot be `NULL`
    - [UNIQUE](http://www.postgresqltutorial.com/postgresql-unique-constraint/): value of column must be unique across whole table (except `NULL`)
    - [PRIMARY KEY](http://www.postgresqltutorial.com/postgresql-primary-key/): combination of `NOT NULL` and `UNIQUE`
    - [CHECK](http://www.postgresqltutorial.com/postgresql-check-constraint/):  
    - [REFERENCES](http://www.postgresqltutorial.com/postgresql-foreign-key/): constrains the value of the column that exists to a column in another table; can be used to define foreign key constraint
  - PostgreSQL table constraints
    - `UNIQUE (column_list)`: to force the value stored in the columns listed inside the parentheses to be unique
    - `PRIMARY KEY (column_list)`: to define the primary key that consists of multiple columns
    - `CHECK (condition)`: to check a condition when inserting or updating data
    - `REFERENCES`: to constrain the value stored in the column that must exist in a column in another table
- [ALTER TABLE](http://www.postgresqltutorial.com/postgresql-alter-table/)
  - `ALTER TABLE` syntax:

        ALTER TABLE table_name action;

  - Actions used with `ALTER TABLE`:
    - `ALTER TABLE table_name ADD COLUMN new_column_name TYPE;`: [add a column](http://www.postgresqltutorial.com/postgresql-add-column/)
    - `ALTER TABLE table_name DROP COLUMN column_name;`: [drop a column](http://www.postgresqltutorial.com/postgresql-drop-column/)
    - `ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;`: [rename a column](http://www.postgresqltutorial.com/postgresql-rename-column/)
    - [change a column’s data type](http://www.postgresqltutorial.com/postgresql-change-column-type/)
    - set a default value for the column
      - `ALTER TABLE table_name ALTER COLUMN column_name SET DEFAULT value`
      -  `ALTER TABLE table_name ALTER COLUMN column_name DROP DEFAULT`
    - `ALTER TABLE table_name ADD CHECK expression;`: add a [`CHECK` constraint](http://www.postgresqltutorial.com/postgresql-check-constraint/) to a column
    - `ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_definition;`: add a constraint
    - `ALTER TABLE table_name RENAME TO new_table_name;`: [rename a table](http://www.postgresqltutorial.com/postgresql-rename-table/)

- [DROP TABLE](http://www.postgresqltutorial.com/postgresql-drop-table/)
  - `DROP TABLE` syntax:

        DROP TABLE [IF EXISTS] table_name [CASCADE | RESTRICT];

    1. Specify name after `DROP TABLE` keyword to remove the table permanently from the database
      - add optional `IF EXISTS` parameter to avoid error resulting from dropping a nonexistent table
    -  `CASCADE` allows you to remove views, constraints, or additional dependent objects with the table automatically
    -  `RESTRICT` prevents `DROP TABLE` from completing successfully if there is any object that depends on it
    - You can use a comma-seperated list to remove multiple tables at once
    - Only superuser, schema owner, and table owner have privilege to remove a table

- [ADD TABLE](http://www.postgresqltutorial.com/postgresql-add-column/)
  -  `ADD TABLE` syntax:

          ALTER TABLE table_name
          ADD COLUMN new_column_name data_type;

    - to add multiple columns to an existing table, use multiple `ADD COLUMN` clauses in the `ALTER TABLE` statement
    - there is no option to specify the position of the new column in the table; it is automatically added to the end of the table

- [DROP COLUMN](http://www.postgresqltutorial.com/postgresql-drop-column/)
  - `DROP COLUMN` syntax:

            ALTER TABLE table_name
            DROP COLUMN column_name;

    - add optional `IF EXISTS` parameter to avoid error resulting from dropping a nonexistent column (results in a notice instead of an error)
    - `CASCADE` allows you to remove views, constraints, or additional dependent objects with the column automatically
  - `DROP COLUMN` syntax for removal of multiple columns:

            ALTER TABLE table_name
            DROP COLUMN column_name_1,
            DROP COLUMN column_name_2,
            ...;

    - notice that each `DROP COLUMN` clause is seperated by a comma

##### Joins and Groupings
- [INNER JOIN, OUTER JOINS](http://www.postgresqltutorial.com/postgresql-joins/)
  - [`INNER JOIN`](http://www.postgresqltutorial.com/postgresql-inner-join/): returns rows in A table that have the corresponding rows in B table
    - `INNER JOIN` syntax

          SELECT
            A.pka,
            A.c1,
            B.pkb,
            B.c2
          FROM
            A
          INNER JOIN B on A.pka = B.fka;

      1. Specify the column in both tables from which you want to select data in the `SELECT` clause
      2. Specify the main table (i.e. `A`) in the `FROM` clause
      3. Specify the table that the main table joins to (i.e. `B`) in the `INNER JOIN` clause. In addition, you put a join condition after the `ON` keyword (i.e. `A.pka = B.fka`)
  - [`LEFT JOIN`](http://www.postgresqltutorial.com/postgresql-left-join/): returns rows in the `A` (left) table that has corresponding rows in the `B` (right) table. a.k.a. `LEFT OUTER JOIN`
    - `LEFT JOIN` syntax

          SELECT
            A.pka,
            A.c1,
            A.pkb,
            B.c2
          FROM
            A
          LEFT JOIN B ON A .pka = B.

    - You can add a `WHERE` clause to select only films that are not in the inventory using a left join:

          SELECT
            film.film_id,
            film.title,
            inventory_id
          FROM
            film
          LEFT JOIN inventory ON inventory.film_id = film.film_id
          WHERE
            inventory.film_id IS NULL;       
  - [`FULL OUTER JOIN`](http://www.postgresqltutorial.com/postgresql-full-outer-join/) combines the results of both left join and right join. The result includes the matching rows from the both tables, and also the rows that do not match.
    - `FULL OUTER JOIN` syntax

          SELECT * FROM A
          FULL [OUTER] JOIN B on A.id = B.id

      - the `OUTER` keyword is optional
    - If the rows in the joined table do not match, the full outer join sets NULL values for every column of the table that lacks a matching row.
    - For the matching rows, a single row is included in the result set that contains columns populated from both joined tables.
- [GROUP BY, SUM, COUNT](http://www.postgresqltutorial.com/postgresql-group-by/)
  - Group rows into groups using [GROUP BY](http://www.postgresqltutorial.com/postgresql-group-by/) clause
      - divides the rows returned from the `SELECT` statement into groups
      - you can apply an aggregate function (ex. `SUM()` to calculate the sum of the items or `COUNT()` to get the number of items in groups)
      - must appear right after the `FROM` or `WHERE` clause
  - `GROUP BY` syntax:

          SELECT column_1, aggregate_function(column_2)
          FROM tbl_name
          GROUP BY column_1;
