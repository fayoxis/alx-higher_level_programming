-- this script creates the database hbtn_0d_usa and it's  table cities
--  on a MySQL server.


    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
