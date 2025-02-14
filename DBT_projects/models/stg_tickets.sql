CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    category TEXT,
    sub_category TEXT,
    priority TEXT,
    created_date TIMESTAMP,
    resolved_date TIMESTAMP,
    status TEXT,
    assigned_group TEXT,
    technician TEXT,
    resolution_time_hours FLOAT,
    customer_impact TEXT
);

SELECT
    ticket_id,
    category,
    sub_category,
    priority,
    created_date,
    resolved_date,
    status,
    assigned_group,
    technician,
    resolution_time_hours,
    customer_impact,
    DATE_PART('year', created_date) AS year,
    DATE_PART('month', created_date) AS month,
    DATE_PART('day', created_date) AS day
FROM tickets;
