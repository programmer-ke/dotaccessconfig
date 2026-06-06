from dotconfig import Config

# A typical nested config from a real project
raw = {
    "app": {
        "name": "MyApp",
        "debug": True,
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "user": "admin",
                "password": "secret"
            }
        },
        "features": {
            "dark_mode": True,
            "notifications": ["email", "sms"]
        },
        "servers": [
            {"name": "web-01", "ip": "10.0.0.1"},
            {"name": "web-02", "ip": "10.0.0.2"}
        ],
        "some-key": "some value"
    }
}

config = Config(raw)

# Read deeply nested values with dot notation
print(config.app.name)              # "MyApp"
print(config.app.database.port)     # 5432
print(config.app.database.credentials.user)  # "admin"

# Access list items with index + dot notation
print(config.app.servers[0].name)   # "web-01"
print(config.app.servers[1].ip)     # "10.0.0.2"

# Access plain lists
print(config.app.features.notifications)  # ["email", "sms"]

# Keys that aren't valid Python identifiers still work
print(config.app["some-key"])    # "some value"


