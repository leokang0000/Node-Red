[
    {
        "id": "173d6bbf.f63f34",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "11cf3b53.5e7bc5",
        "type": "debug",
        "z": "173d6bbf.f63f34",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 1220,
        "y": 380,
        "wires": []
    },
    {
        "id": "40a56da0.3a89d4",
        "type": "switch",
        "z": "173d6bbf.f63f34",
        "name": "if == 0",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 820,
        "y": 460,
        "wires": [
            [
                "536cc644.4dc128"
            ],
            [
                "5a3bc179.99946"
            ]
        ]
    },
    {
        "id": "f1cc816c.2a16e",
        "type": "rpi-gpio out",
        "z": "173d6bbf.f63f34",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 1260,
        "y": 480,
        "wires": []
    },
    {
        "id": "2e2b7d25.eaa132",
        "type": "rpi-gpio in",
        "z": "173d6bbf.f63f34",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 520,
        "y": 460,
        "wires": [
            [
                "40a56da0.3a89d4",
                "11cf3b53.5e7bc5"
            ]
        ]
    },
    {
        "id": "536cc644.4dc128",
        "type": "change",
        "z": "173d6bbf.f63f34",
        "name": "123",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 980,
        "y": 460,
        "wires": [
            [
                "f1cc816c.2a16e"
            ]
        ]
    },
    {
        "id": "5a3bc179.99946",
        "type": "change",
        "z": "173d6bbf.f63f34",
        "name": "123",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 990,
        "y": 520,
        "wires": [
            [
                "f1cc816c.2a16e"
            ]
        ]
    }
]
