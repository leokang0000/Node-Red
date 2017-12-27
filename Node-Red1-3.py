[
    {
        "id": "b18f3fbc.a0239",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "db8f868d.2eac58",
        "type": "inject",
        "z": "b18f3fbc.a0239",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 170,
        "y": 320,
        "wires": [
            [
                "ec3255c0.bd4a18",
                "c1d60290.88bea"
            ]
        ]
    },
    {
        "id": "ec3255c0.bd4a18",
        "type": "function",
        "z": "b18f3fbc.a0239",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"IhJObwSOKijxDXYU\"\n    };\n\nmsg.payload= \"Temperature,,25.3\";\nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 380,
        "y": 320,
        "wires": [
            [
                "9e6b6573.e96518"
            ]
        ]
    },
    {
        "id": "48a8ec2e.8824c4",
        "type": "http response",
        "z": "b18f3fbc.a0239",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 850,
        "y": 300,
        "wires": []
    },
    {
        "id": "50667d24.1f1cb4",
        "type": "debug",
        "z": "b18f3fbc.a0239",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 890,
        "y": 380,
        "wires": []
    },
    {
        "id": "9e6b6573.e96518",
        "type": "http request",
        "z": "b18f3fbc.a0239",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DAqhMYX0/datapoints.csv",
        "tls": "",
        "x": 590,
        "y": 360,
        "wires": [
            [
                "48a8ec2e.8824c4",
                "50667d24.1f1cb4"
            ]
        ]
    },
    {
        "id": "c1d60290.88bea",
        "type": "function",
        "z": "b18f3fbc.a0239",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"IhJObwSOKijxDXYU\"\n    };\n\nmsg.payload= \"Humidity,,35\";\nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 380,
        "y": 400,
        "wires": [
            [
                "9e6b6573.e96518"
            ]
        ]
    }
]
