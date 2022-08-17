import app


test_event = {"mode": "all", "test": False}


result = app.handler(test_event, None)

print(result)
