# PythonMMP
Opto Memory-Mapped Protocol module for Python
-----
... function list and instructions coming "soon" / eventually

<details><summary>Functions</summary>

* **O22MMP(host)** - Initialize an Opto22 Memory Mapped object residing at 'host' address.

* **SetHDDigitalPointState(module, channel, state)** - The HD digital output at <channel> on <module> will be toggled to <state>, which should be either 1 or 0. Returns status code.

* **WriteBlock(address, value)** - Write <value> into memory location <address>. Returns int status.

* **BuildWriteBlockRequest(dest,value)** - Build the write block request bytearray. Returns bytearray block.

* **BuildReadBlockRequest(dest** - Build the read block request bytearray. Returns bytearray block.

* **UnpackWriteResponse(data)** - Unpacks the integer status code from bytes 4-8 of a write response. Returns int status.

* **close()** - Closes the socket connection to the device. Call this before the end of the script.
