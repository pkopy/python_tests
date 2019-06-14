import dictdiffer 

first = {
    "title": "hello",
    'enable': 'true',
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30"],
    "settings": {
        "assignees": [100, 101, 201],
    }
}

second = {
    "title": "hellooo",
    'enable': 'false',
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30", "/users/40"],
    "settings": {
        "assignees": [100, 101, 202],
    }
}

result = dictdiffer.diff(first, second)
print(dictdiffer)
for x in result:
    print(x[0])

# assert list(result) == [
#     ('change', ['settings', 'assignees', 2], (201, 202)),
#     ('add', 'stargazers', [(2, '/users/40')]),
#     ('change', 'title', ('hello', 'hellooo'))]