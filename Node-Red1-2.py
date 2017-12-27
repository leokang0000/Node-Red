[
    {
        "id": "173d6bbf.f63f34",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "94137501.1bed58",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "b18f3fbc.a0239",
        "type": "tab",
        "label": "Flow 4"
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
    },
    {
        "id": "30f3eb34.81ad24",
        "type": "inject",
        "z": "94137501.1bed58",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 190,
        "y": 340,
        "wires": [
            [
                "309ca12.756365e",
                "fd1728c3.bbdaa8"
            ]
        ]
    },
    {
        "id": "309ca12.756365e",
        "type": "function",
        "z": "94137501.1bed58",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"IhJObwSOKijxDXYU\"\n    };\n    \nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 400,
        "y": 340,
        "wires": [
            [
                "6a5e6fb6.c0aa2"
            ]
        ]
    },
    {
        "id": "75306ce4.7c2834",
        "type": "http response",
        "z": "94137501.1bed58",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 870,
        "y": 320,
        "wires": []
    },
    {
        "id": "9355143.49c6ce8",
        "type": "debug",
        "z": "94137501.1bed58",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 910,
        "y": 400,
        "wires": []
    },
    {
        "id": "6a5e6fb6.c0aa2",
        "type": "http request",
        "z": "94137501.1bed58",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DAqhMYX0/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 610,
        "y": 280,
        "wires": [
            [
                "75306ce4.7c2834",
                "9355143.49c6ce8"
            ]
        ]
    },
    {
        "id": "d7593daa.4c03",
        "type": "http request",
        "z": "94137501.1bed58",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DAqhMYX0/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 610,
        "y": 380,
        "wires": [
            [
                "75306ce4.7c2834",
                "9355143.49c6ce8"
            ]
        ]
    },
    {
        "id": "fd1728c3.bbdaa8",
        "type": "function",
        "z": "94137501.1bed58",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"IhJObwSOKijxDXYU\"\n    };\n    \nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 400,
        "y": 420,
        "wires": [
            [
                "d7593daa.4c03"
            ]
        ]
    }
]
