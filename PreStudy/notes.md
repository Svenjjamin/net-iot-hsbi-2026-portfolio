# Was möchtest du machen?
    - Sensordaten auslesen, analysieren und interpretieren


# Vorteile von TCP/IP gegenüber ISO/OSI-Modell?
    - OSI ist ein generelles theoretisches Modell 
    - TCP/IP ist ein für die konkrete Praxis entwickeltes Modell
    - TCP/IP ist mit 4 Layern simpler in der Aufmachung

1. The Core Story: Based on the IoTempower inspiration video, describe one IoT scenario you findcompelling. Who uses it, and what devices need to communicate?
    - Sensordaten auslesen, zb von Seismographen, um Erdbeben frühzeitig vorherzusagen

2. Addressing & Subnetting: Explain in your own words what an IP address and a subnet mask are.Why can't two devices on the same local subnet have the same IP?
    - eine IP Adresse ist quasi die Adresse des Computers unter der er zu erreichen ist. Sie besteht aus 2 Teilen, dem Netzwerkteil und dem Geräteteil
    - die Subnetzmaske gibt an, welcher Teil der IP-Adresse zum Netzwerk gehört und welcher Teil das Gerät definiert
    - wenn 2 Geräte innerhalb eines lokalen Netzwerkes die selbe Adresse hätten, wären die Daten nicht eindeutig zustellbar, die Zustellung würde fehlschlagen

3. OSI vs. TCP/IP Reality: The ISO/OSI model specifi es 7 layers, while TCP/IP uses 4. In real-worldIoT systems, why do rigid layer boundaries often break down or cause unnecessary overhead?(Hint: consider tiny sensor packets vs. large headers).
    - jeder Layer benötigt Metadaten, die bei der Übertragung zum einwandfreien Ablauf mitgeschickt werden müssen, bei IoT-System, die oft viele kleine Datenübertragungen versenden, bläht das Datenstrom oft zu sehr auf, bzw. sprengt die vorhandenen Speicher- und Datenübertragungskapazitäten

4. Decoupling with Pub/Sub: In a smart home with 10 temperature sensors and 3 displays, why isan MQTT broker more maintainable than each sensor opening direct HTTP connections to everydisplay?
    - statt einzelnen Verbindungen, von jedem Sensor zu jedem Display, gibt es mit dem Broker ein zentrales Hub, welches den Datenstrom vom jeweiligen Publisher zum jeweiligen Subscriber leitet
    - des reduziert die Anzahl an Verbindungen von 30 auf 13
    - außerdem ist leichter neue Geräte hinzuzufügen, da keine neuen Querverbindungen zu allen bestehenden Geräten aufgemacht werden müssen, sondern die neuen Geräte nur als Publisher/Subscriber zum Broker verbunden werden müssen
    
5. Network Boundary Refl ection: When you work from home, can your laptop directly ping a deviceon a classmate's home Wi-Fi? Why or why not? What does a mesh overlay network like Nebula orYggdrasil change about this?
    - dadurch dass die lokalen IP-Adressen privat sind, können Geräte von außerhalb diese nicht direkt anpingen
    - ein Mesh Overlay Network gibt allen Geräten innerhalb eine neue global eineindeutige IP-Adresse, über die diese dann kommunizieren können