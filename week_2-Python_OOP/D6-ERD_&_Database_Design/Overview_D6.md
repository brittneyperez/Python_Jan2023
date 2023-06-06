## **Week 2 - D6** | ２０２３年０１月１９日（木）

### Recap
- Python OOP
    - Classes
    - Instances
    - Attributes
    - Methods
    - Relationship between Databases and Web Development

## Topics to Cover
- ERD & Database Design
- ERD: Entity Relationship Diagram
    - The graphical representation of a schema.
- Create New Schema
    - Rename
    - Create Table
        - Naming Convention
        - id, primary key
        - **auto increment** (ALWAYS ENABLE for `id`)
        - `created_at` & `updated_at`
            - `NOW()` `ON UPDATE NOW()`
        - Passwords (ALWAYS set this up to `VARCHAR(255)`)
        - email is UNIQUE (`UQ`) since only one user can sign up per email
        - DataTypes
    - Relationships
        - One to One
        - One to Many
        - Many to Many
        - Create new table and Relationships.
            - foreign key
            - cascade on delete vs set null
    - Save your schemas with your assignments
    - Forward engineer
        - SAVE WORK BEFORE THIS STEP!
            - This will keep the ERD we were working on as well as serve as the basis of the schema we are trying to fix because how it presently is at the moment isn't functioning well in our project.
        - When forward engineering, under the '**Code Generation**' section, check the options '`DROP objects before each CREATE object`' and '`Generate DROP SCHEMA`'.
        - If we encounter an error in the forward engineering process, STOP the process and fix the error before trying again.
- ### **Take Aways**
    - Consistent naming convention everywhere
    - Consistent SDP (do everything methodically, no skipping steps)
    - Do as much with the DB as possible, rather than with queries
    - Check that you're doing what you think you're doing
    - Think twice about the best data type ex: `DATE` vs `DATETIME`