[
    {
        "id": "94137501.1bed58",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
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
