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
    category,
    priority,
    COUNT(ticket_id) AS total_tickets,
    AVG(resolution_time_hours) AS avg_resolution_time,
    assigned_group,
    COUNT(CASE WHEN status = 'Closed' THEN 1 END) * 100.0 / COUNT(ticket_id) AS closure_rate
FROM tickets
GROUP BY category, priority, assigned_group;
