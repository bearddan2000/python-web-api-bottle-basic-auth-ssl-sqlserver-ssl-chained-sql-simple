# python-web-api-bottle-basic-auth-ssl-sqlserver-ssl-chained-sql-simple

## Description
Creates an api of `dog` by using chained sql functions for a bottle project.
Has the ability to query by parameters.

Remotely tested with *testify*, the ssl is not verified.

Requires basic authentication for endpoints.

| username | password |
| -------- | -------- |
| *user* | *pass* |

Sql server uses self-signed ssl.

## Tech stack
- python
  - bottle
  - sqlalchemy
  - testify
  - requests
- mssql

## Docker stack
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- Get all dogs: https://localhost/dog
  - Schema id, breed, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/dog/<id> -u 'user:pass'
  - Read: https://localhost/dog/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/dog/<id>/<breed>/<color> -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/dog/<id> -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
