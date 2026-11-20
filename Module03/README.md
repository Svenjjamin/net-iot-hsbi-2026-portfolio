# Module 03


## Overlay plan — the underlay/overlay sketch, the overlay addresses, the lighthouse, the Node-RED host, the MQTT path, and the note to Mara.

## Study log — what you actually needed, what surprised you, the LLM answers you checked. One pod member keeps it; the others link to it and add one sentence.

## Bundle notes — what the bundle contains and where it went. No keys, no certificates, no credentials.

## Discussion log — one line per discussion: who listened, what they asked.

## Remote proof — the ping/ssh output from another network, and the Node-RED URL.

## MQTT through the overlay — broker address, topics, the flow, the command that changed an output.

## Round 01

Nebula-IP-Adresse: 10.100.0.20

## Round 2
link to Jan, Jan screenshot

## Round 4
link Round4-network_plan.png

1. Underlay connections
Museum: The sculpture and broker leave the museum network through the campus router/firewall or NAT. There is no public inbound port forward.
Campus: The Node-RED cluster uses the HSBI underlay network.
Home/mobile: Mara's laptop may connect through home Wi-Fi or mobile/DSL NAT.
Hotel: Her laptop appears behind hotel NAT and may receive no public inbound address.
These underlay networks remain independent. The Nebula tunnel is carried through ordinary Internet traffic.

2. Overlay connections
Nebula provides private virtual addresses and an encrypted L3 tunnel. The lighthouse stores peer information and assists with NAT traversal. It is not the MQTT broker, does not receive application MQTT data in normal direct operation, and is not required to be installed on every device.

3. OSI-layer overview
Tunnel start – pod router: L1 Physical/L2 Ethernet or Wi-Fi, L3 IP routing and NAT, and L4 UDP for the Nebula underlay transport. Nebula encrypts and encapsulates overlay IP packets.
Underlay network: L1/L2 carry the physical link, while L3 routes private and public IP packets. NAT changes source addresses but normally does not need to open an inbound port.
Nebula overlay: L3 provides virtual addresses and routing, while encryption protects the encapsulated packets.
MQTT connection: L4 TCP port 1883, with MQTT at L7 carrying the topic and command.
Tunnel end – Node-RED host: Nebula terminates the tunnel at L3, decrypts the packet, and forwards it to the MQTT/Node-RED application on L7.
Application path: Sculpture → pod LAN MQTT broker → router Nebula interface → Node-RED Nebula peer → Node-RED flow, and in reverse for commands.

4. Overlay, lighthouse and instructor explanation
An overlay network is a virtual private network built on top of existing physical networks. It gives devices private addresses and encrypted tunnels without changing their underlay network or requiring public inbound firewall ports.

The lighthouse introduces peers and helps them determine public and NAT addresses. If UDP hole punching establishes a direct connection, traffic does not pass through the lighthouse. If peers cannot establish a direct path, the lighthouse may relay traffic instead.

The instructor prepared the Nebula CA, signed node certificates, private keys, lighthouse configuration, DNS, and firewall rules. To repeat this at another site, create a new host certificate and key signed by the same CA, deploy the Nebula bundle and config, configure routing/firewall rules, and permit the required peer groups.

5. Answer to Mara Voss
Mara, you can update and monitor the sculpture without asking the museum IT team to open an inbound firewall port. The sculpture uses the local MQTT broker, and the pod router creates a secure private network connection to the Node-RED dashboard. The router and the Node-RED host appear to each other as private Nebula addresses, even when both networks use NAT. We did not change or expose the museum firewall, public IP configuration, or inbound router rules. You can now read status and send one MQTT command while Mara or another authorized person is elsewhere. Mara does not need a museum server account; a Nebula certificate and key belong to the machine. The limitation is that both ends must run a Nebula client, and a connection relayed through the lighthouse can be slower than a direct or local LAN connection.

6. Study log
Nebula-manager provides a unified CLI for managing multiple Nebula servers and certificates, while Tailscale adds a managed identity-based control plane, device administration, ACLs, and easy sharing. NetBird provides identity-based, WireGuard-based zero-trust access with self-hosting options, SSO, MFA, and granular network policies. This class runs an independent Nebula CA so students learn certificate issuance and mesh security directly and do not depend on an external account or control service.

Bundle notes
The bundle contains the CA certificate, the pod's host certificate, the host private key, and config.yml. The certificates and key belong in /etc/nebula/ on the router, while the private key must have mode 600. The bundle is a credential and should never be added to Git or shared in screenshots or chat.

## Round 5

connecting to the router directly is way faster than connecting via nebula

## Round 6
see pictures
+ node red picture at jans to see the recieved messages (seconds since when it runs)

## Learning Goals

## Reflection 1

[Reflection 1](../Reflections/ref01.md)
