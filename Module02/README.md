# Module 2

## Network plan — the sketch, the subnet calculation, the SSID/channel, and the pod/group ID (pod<NN> / Gruppe ).
## Router baseline — model, OpenWrt version, LAN/WAN addresses, MACs, SSH access, extroot status, broker status, open ports. No passwords, no eduroam credentials.
## Study log — the running log: the theory you actually needed, the commands that surprised you, and the LLM answers you checked. This is not an essay and not a separate study phase.
## Discussion log — one line per discussion: who listened, what they asked, what you changed. This is personal; the shared study log is still one per pod.
## Vocabulary tracker — the Module 2 vocabulary table, copied with two extra columns: ✓ and Link / evidence. See the reference at the end for how to fill it.
## Captures — the pcap or the tshark/tcpdump -A text, and what each protocol proves.
## NAT and port forwarding — the rule, the two-sided capture, and the explanation.
## Take it home — the upstream switch and the evidence that the router still works.


## Disclaimer
For this module we made the whole setup on my laptop, so I will mostly supply the screenshots as evidence of our progress, while Jan will mostly provide the correspondings texts.

## Router Baseline
[a link]()


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

## Round 7
We tried to follow the insctructions but failed at the step to set wan active and read the wan ip adress. You con see in the round 7 pictures.

As a personal experience i already did port forwarding for a personal roleplaying/pen-and-paper session with friends, so they could connect with their computers to mine via FoundryVTT.

## Round 8
For evidence look at the following pictures:

## Round 9
I would run upstream OpenWrt on a router I depend on when it is explicitly supported, there is a reliable recovery method, and I can maintain regular updates and backups. I would avoid it for critical use if a required hardware feature is unsupported or no tested recovery procedure exists. The extra control is worthwhile for a lab or secondary router, while vendor firmware may be preferable for someone who needs integrated support and a guaranteed working telephone or Wi-Fi feature.

Extroot and installing packages through the CLI would be impossible or much harder with locked vendor firmware, as they require an accessible package manager and writable overlay configuration. I would miss vendor-specific features such as Cudy's travel-router mode, automatic firmware support, or the vendor mobile application.


## Learning Goals

## Learning Goal 1
Look at Router Baseline and Round 1, 4, 6

## Learning Goal 2
Look at Round 5

## Learning Goal 3
Round 1-4, 8

## Learning Goal 4
Look at Round 5


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
    