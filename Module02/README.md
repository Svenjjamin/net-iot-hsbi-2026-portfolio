# Module 2

## Router Baseline
Jan has documented our progress of setting up the router:
[a link]()
I will mostly supply the the screenshots, because we worked on my laptop.

## Round 1: Flash OpenWrt — from factory to your router

1. Verify the hardware. The label must say TR1200 v1. Do not cross-flash a different revision or model.
Checked. Version is correct.

2. Get the two images. The Cudy-signed intermediate image (the stock UI only accepts that), and the current stable OpenWrt sysupgrade image for cudy_tr1200-v1 that the instructor names. Do not use a snapshot. Verify the SHA-256 of the OpenWrt image. Your instructors may have provided additional resources in the LMS; check there as well and compare them with this manual. The two should complement each other — if they contradict, that is a curiosity worth recording, not a reason to guess.


3. Connect by Ethernet. Laptop to the router's LAN port, open http://192.168.10.1, and flash the intermediate image. Wait until the router has rebooted; do not interrupt power. If the laptop keeps its old 192.168.10.x lease, renew DHCP or set a temporary static address such as 192.168.1.2.
4. Replace the intermediate build. Reconnect to http://192.168.1.1, flash the OpenWrt sysupgrade image, and do not keep settings. Set a strong root password.
5. Verify the result. ubus call system board, uname -a, df -h /overlay, and ssh root@192.168.1.1 — the router keeps the OpenWrt default until Round 4 moves it to 192.168.14.1.
6. If it fails, stop. Ask the instructor; do not force a TFTP/UART recovery unless the instructor walks you through it. A working spare is better than a bricked router.


## Round 4 / Schritt 3

## Round 5
link zu tcpdumb md

## Round 6
link zu module 02 readme jan


## Round 8
For evidence look at the following pictures:



## Learning Goals

> **How to use the learning goals.** Copy the module's learning goals from the course workbook into the block below. Keep the `LG1`, `LG2`, … IDs and a one-word keyword. In each task, write `Proves: LG2` (or link to `[LG2](#lg2)`) so you can find the evidence quickly at checkpoint time. In the **Evidence** line under each goal, link to the task that proves it.

<a id="lg1"></a>
### LG1 — `<keyword>`

<copy the goal here>

**Evidence:** [Task 1](#task-1)

<a id="lg2"></a>
### LG2 — `<keyword>`

<copy the goal here>

**Evidence:** [Task 2](#task-2)

<a id="lg3"></a>
### LG3 — `<keyword>`

<copy the goal here>

**Evidence:** [Task 3](#task-3)

<a id="task-1"></a>
## Task 1 — `<short title>`

**Proves:** [LG1](#lg1)

This task was executed by myself.

<a id="task-2"></a>
## Task 2 — `<short title>`

**Proves:** [LG2](#lg2)

This task was executed by my partner. The implementation was about ...
It is [here](https://github.com/partner/iot-portfolio/Module02/README.md#task-2).

<a id="task-3"></a>
## Task 3 — `<short title>`

**Proves:** [LG3](#lg3)

...

## Reflection 2

[Reflection 2](../Reflections/ref02.md)

If the module is longer than 1 week, you might have several reflections within it. If not, delete this and the following.

## Reflection 3
[Reflection 3](../Reflections/ref03.md)


## Discussion Log
Gewonnene Erkenntnis: Der Lan-Port muss über DHCP laufen
Nach dem Flash des Routers ändert sich die IP-Adresse umgehend, daher muss man sich beim nächsten mal verbinden mit der neuen IP-Adresse verbinden

Round 01:
    Wir haben den Router komplett zurückgesetzt, um dann mit der gelieferten Datei die gewünschten Einstellungen vorzunehmen.
    Und wir haben dazu eine physiche Ethernet Verbindung genutzt, da diese zuverlässiger und schneller ist, als eine wireless-Verbindnung.

Eduroam zu Radio1 hinzufügen:
    Es ist wichtig, dass nur 1 Netzwerk angezeigt wird. Mehrere parallel erstellte Netzwerke können zu Problemen führen.
    