#!/usr/local/opt/python@3.10/bin/python3
status_code = 418
NOT_FOUND = 404
match status_code:
    case 200:
        print("OK!")
    case NOT_FOUND:
        print("HTTP Not Found")