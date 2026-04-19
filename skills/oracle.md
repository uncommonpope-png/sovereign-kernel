# Oracle Skill

Query Oracle databases and manage Oracle DB connections.

## Use When
- Running SQL queries against Oracle databases
- Managing Oracle DB schemas and objects
- Database administration tasks

## sqlplus (Oracle CLI)
```bash
# Connect to database
sqlplus user/password@hostname:1521/service_name

# Run query
sqlplus -S user/password@host:1521/svc << 'EOF'
SELECT table_name FROM user_tables;
EXIT;
EOF

# Execute SQL file
sqlplus user/password@host:1521/svc @script.sql

# Non-interactive query
echo "SELECT COUNT(*) FROM orders;" | sqlplus -S user/pass@host:1521/svc
```

## Python (cx_Oracle / oracledb)
```python
import oracledb
conn = oracledb.connect(user="user", password="pass", dsn="host:1521/svc")
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees WHERE department_id = :dept", dept=10)
for row in cursor.fetchall():
    print(row)
conn.close()
```

## Common SQL Patterns
```sql
-- List tables
SELECT table_name FROM user_tables ORDER BY table_name;

-- Table structure
SELECT column_name, data_type, nullable FROM user_tab_columns WHERE table_name = 'MY_TABLE';

-- Running queries
SELECT sql_text, elapsed_time FROM v$sql WHERE elapsed_time > 1000000 ORDER BY elapsed_time DESC;
```

## Notes
- DSN format: host:port/service_name
- Thin mode (oracledb): no Oracle client install needed
- Thick mode: requires Oracle Instant Client
