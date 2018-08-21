# PythonMMP
Opto Memory-Mapped Protocol module for Python
-----
... function list and instructions coming "soon" / eventually

<details><summary>Functions</summary>

* **O22MMP(host)** - Initialize an Opto22 Memory Mapped object residing at 'host' address.

	* **O22MMP()** - Default to `localhost` / `127.0.0.1`

* **ReadRawOffset(offset, size, data_type)** - Rads the raw address at `offset` collecting `size` bytes and using `data_type` formatting to unpack it.

* **LastError()** - Returns the last error to cause a not acknowledged (NAK) response code.

* **IPAddressE0()** - Returns the IP address associated with Ethernet 0 on the controller.

* **MACAddressE0()** - Returns the MAC address associated with Ethernet 0 on the controller.

* **IPAddressE1()** - Returns the IP address associated with Ethernet 1 on the controller.

* **MACAddressE1()** - Returns the MAC address associated with Ethernet 1 on the controller.

* **UnitDescription()** - Returns the device unit description. For example, `GRV-EPIC-PR1`

* **FirmwareVersion()** - Returns the device firmware version. For example, 'R1.1a'


* **SetHDDigitalPointState(module, channel, state)** - The HD digital output at `channel` on `module` will be toggled to `state`, which should be either 1 or 0. Returns status code.

* **GetHDDigitalPointState(module, channel)** - The state of the HD digital output at `channel` on `module` will be fetched. Returns state either 1 or 0.


* **GetAnalogPointMin(module, channel)** - Return the minimum float value of the analog I/O installed at `channel` on `module`.

* **GetAnalogPointMax(module, channel)** - Return the maximum float value of the analog I/O installed at `channel` on `module`.

* **GetAnalogPointValue(module, channel)** - Return the current float value of the analog I/O installed at `channel` on `module`.

* **SetAnalogPointValue(module, channel, value)** - Set the analog I/O installed at `channel` on `module` to be `value`. `value` should be a float.


* **WriteBlock(address, value)** - Write `value` into memory location `address`. Relies on `BuildWriteBlockRequest()`, wraps up `.send()` and `.recv()` methods. Returns int status.

* **ReadBlock(address)** - Read value at memory location `address`. Relies on `BuidReadBlockRequest()`, wraps up `.send()` and `.recv()` methods. Returns unpacked string data.


* **BuildWriteBlockRequest(dest, value)** - Build the write block request bytearray. Returns bytearray block.<br>
	This is an internally used utility method to build a read request. Client code isn't likely to need it.

* **BuildReadBlockRequest(dest, size)** - Build the read block request bytearray. Returns bytearray block.<br>
	This is an internally used utility method to build a read request. Client code isn't likely to need it.


* **UnpackReadResponse(data, data_type)** - Unpacks the string data from bytes 16-20 of a read response. Returns formatted data.<br>
	`data_type` --> struct format characters 'c', 'i', 'd', 'f', etc., or specifically 'FIRMWARE', 'IP', or 'MAC' for custom formatting, or 'NONE' for raw binary data.

* **UnpackWriteResponse(data)** - Unpacks the integer status code from bytes 4-8 of a write response. Returns int status.<br>

* **close()** - Closes the socket connection to the device. Call this before the end of the script.

</details>