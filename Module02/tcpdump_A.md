root@OpenWrt:~# mosquitto_pub -h 192.168.14.1 -t "totaltollestopic" -m "megamessage"
root@OpenWrt:~# tcpdump -r /tmp/pod.pcap -A
reading from file /tmp/pod.pcap, link-type EN10MB (Ethernet), snapshot length 262144
13:12:16.441075 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 8451+ A? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-W.!............accounts.google.com.....
13:12:16.441077 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.59999 > OpenWrt.lan.53: 49634+ AAAA? accounts.google.com. (37)
`.>..-.@.)g......x..8.r..)g.............._.5.-.Q.............accounts.google.com.....
13:12:16.457498 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 8451 1/0/0 A 142.251.127.84 (53)
`....=.@.)g..............)g......x..8.r..5...=AW!............accounts.google.com..............H.....T
13:12:16.458289 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.59999: 49634 1/0/0 AAAA 2a00:1450:4001:c21::54 (65)
`..1.I.@.)g..............)g......x..8.r..5._.IAc.............accounts.google.com..............H..*..P@..!.......T
13:12:16.460333 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 22298+ A? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-!.W............accounts.google.com.....
13:12:16.460945 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 22298 1/0/0 A 142.251.127.84 (53)
`....=.@.)g..............)g......x..8.r..5...=AWW............accounts.google.com..............H.....T
13:12:16.462378 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.59999 > OpenWrt.lan.53: 34976+ AAAA? accounts.google.com. (37)
`.>..-.@.)g......x..8.r..)g.............._.5.-...............accounts.google.com.....
13:12:16.462970 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.59999: 34976 1/0/0 AAAA 2a00:1450:4001:c21::54 (65)
`..1.I.@.)g..............)g......x..8.r..5._.IAc.............accounts.google.com..............H..*..P@..!.......T
13:12:41.701711 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:12:41.702738 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:12:51.497704 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 50931+ A? cc-api-data.adobe.io. (38)
`.\....@.)g......x..8.r..)g................5...7.............cc-api-data.adobe.io.....
13:12:51.497995 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.59999 > OpenWrt.lan.53: 2707+ AAAA? cc-api-data.adobe.io. (38)
`......@.)g......x..8.r..)g.............._.5..x.
............cc-api-data.adobe.io.....
13:12:51.514109 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 50931 6/0/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com., A 52.31.167.175, A 52.48.202.212, A 52.212.178.60 (263)
`......@.)g..............)g......x..8.r..5....B).............cc-api-data.adobe.io..............#...cc-api-data-ew1...2.......&.2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb eu-west-1        amazonaws.com..........&..4............&..40...........&..4..<
13:12:51.515576 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.59999: 2707 3/1/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com. (299)
`..1.3.@.)g..............)g......x..8.r..5._.3BM
............cc-api-data.adobe.io..............#...cc-api-data-ew1...2.......&.2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb   eu-west-1       amazonaws.com..........-.H.ns-1566      awsdns-03.co.uk..awsdns-hostmaster.amazon......... ......u....<
13:13:07.541766 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:13:07.543170 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:13:18.838192 IP 192.168.14.146.57997 > OpenWrt.lan.53: 36739+ HTTPS? main.vscode-cdn.net. (37)
E..Av.....&............5.-...............main
vscode-cdn.net..A..
13:13:18.838571 IP 192.168.14.146.63868 > OpenWrt.lan.53: 23426+ A? main.vscode-cdn.net. (37)
E..Av.....&..........|.5.-..[............main
vscode-cdn.net.....
13:13:18.854591 IP OpenWrt.lan.53 > 192.168.14.146.57997: 36739 2/1/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net. (173)
E.....@.@..A.........5...................main
vscode-cdn.net..A...........9..
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...].........7.tm1.dns-tm.com..msnhst microsoft..xa'..........$.....<
13:13:18.856772 IP OpenWrt.lan.53 > 192.168.14.146.63868: 23426 3/0/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net., A 150.171.109.99 (122)
E.....@.@..s.........5.|...w[............main
vscode-cdn.net..............9..
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...V............mc
13:13:34.945716 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 55538+ A? hbrt.adobe.com. (32)
`.\..(.@.)g......x..8.r..)g................5.(3..............hbrt.adobe.com.....
13:13:34.946007 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.59999 > OpenWrt.lan.53: 5549+ AAAA? hbrt.adobe.com. (32)
`....(.@.)g......x..8.r..)g.............._.5.(...............hbrt.adobe.com.....
13:13:34.962175 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 55538 2/0/0 CNAME hbrt-or1-ext-vip.adobe.com., A 192.147.130.245 (79)
`....W.@.)g..............)g......x..8.r..5...WAq.............hbrt.adobe.com..................hbrt-or1-ext-vip...,..............
13:13:34.963539 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.59999: 5549 1/1/0 CNAME hbrt-or1-ext-vip.adobe.com. (128)
`..1...@.)g..............)g......x..8.r..5._..A..............hbrt.adobe.com..................hbrt-or1-ext-vip...........g.5.exfer-vip-01.corp..
hostmaster....8........X.$.....,
13:14:00.258722 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 34024+ A? wpad.lan. (26)
`.\..".@.)g......x..8.r..)g................5."...............wpad.lan.....
13:14:00.259041 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55122 > OpenWrt.lan.53: 3595+ A? wpad.lan. (26)
`..?.".@.)g......x..8.r..)g..............R.5."$..............wpad.lan.....
13:14:00.259044 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.59999 > OpenWrt.lan.53: 19509+ AAAA? wpad.lan. (26)
`....".@.)g......x..8.r..)g.............._.5.".{L5...........wpad.lan.....
13:14:00.259044 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55837 > OpenWrt.lan.53: 22715+ AAAA? wpad.lan. (26)
`.%..".@.)g......x..8.r..)g................5.".7X............wpad.lan.....
13:14:00.259837 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 34024 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:14:00.260740 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55122: 3595 NXDomain 0/0/0 (26)
`
@..".@.)g..............)g......x..8.r..5.R."A<.............wpad.lan.....
13:14:00.261446 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.59999: 19509 NXDomain 0/0/0 (26)
`..1.".@.)g..............)g......x..8.r..5._."A<L5...........wpad.lan.....
13:14:00.262402 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55837: 22715 NXDomain 0/0/0 (26)
`.ds.".@.)g..............)g......x..8.r..5..."A<X............wpad.lan.....
13:14:28.301735 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 57922+ A? push.services.mozilla.com. (43)
`.\..3.@.)g......x..8.r..)g................5.3.L.B...........push.services.mozilla.com.....
13:14:28.302320 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 60277+ AAAA? push.services.mozilla.com. (43)
`....3.@.)g......x..8.r..)g................5.3p..u...........push.services.mozilla.com.....
13:14:28.306228 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 60277 0/1/0 (124)
`......@.)g..............)g......x..8.r..5....A..u...........push.services.mozilla.com................E.ns-679  awsdns-20.net..awsdns-hostmaster.amazon."....... ......u...Q.
13:14:28.317950 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 57922 1/0/0 A 34.107.243.93 (59)
`....C.@.)g..............)g......x..8.r..5...CA].B...........push.services.mozilla.com................."k.]
13:14:28.321087 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 64276+ A? push.services.mozilla.com. (43)
`....3.@.)g......x..8.r..)g................5.3{..............push.services.mozilla.com.....
13:14:28.321739 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 64276 1/0/0 A 34.107.243.93 (59)
`....C.@.)g..............)g......x..8.r..5...CA].............push.services.mozilla.com................."k.]
13:14:28.323524 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 27608+ AAAA? push.services.mozilla.com. (43)
`.\..3.@.)g......x..8.r..)g................5.3..k............push.services.mozilla.com.....
13:14:28.324143 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 27608 0/1/0 (147)
`......@.)g..............)g......x..8.r..5....A.k............push.services.mozilla.com......services.mozilla.com..........H.ns-679      awsdns-20.net..awsdns-hostmaster.amazon.com........ ......u...Q.
13:14:29.487055 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 54895+ A? polka.typekit.com. (35)
`....+.@.)g......x..8.r..)g................5.+S..o...........polka.typekit.com.....
13:14:29.487347 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 26711+ AAAA? polka.typekit.com. (35)
`.\..+.@.)g......x..8.r..)g................5.+..hW...........polka.typekit.com.....
13:14:29.503251 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 54895 4/0/0 A 3.231.72.45, A 44.209.32.89, A 34.232.214.120, A 54.204.24.43 (99)
`....k.@.)g..............)g......x..8.r..5...kA..o...........polka.typekit.com...................H-............,. Y............"..x............6..+
13:14:29.504618 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 26711 0/1/0 (117)
`....}.@.)g..............)g......x..8.r..5...}A.hW...........polka.typekit.com................F.ns-1260 awsdns-29.org..awsdns-hostmaster.amazon......... ......u...Q.
13:15:01.302700 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.62215 > OpenWrt.lan.53: 21757+ HTTPS? www.bing.com. (30)
`..6.&.@.)g......x..8.r..)g................5.&T.T............www.bing.com..A..
13:15:01.303060 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.50060 > OpenWrt.lan.53: 13049+ A? www.bing.com. (30)
`....&.@.)g......x..8.r..)g................5.&..2............www.bing.com.....
13:15:01.310617 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 36048+ A? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5.".@.............wpad.lan.....
13:15:01.311243 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 36048 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:15:01.319396 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.62215: 21757 3/1/0 CNAME www-www.bing.com.trafficmanager.net., CNAME www.bing.com.edgekey.net., CNAME e86303.dscx.akamaiedge.net. (212)
`......@.)g..............)g......x..8.r..5....A.T............www.bing.com..A..........?..%.www-www.bing.com.trafficmanager.net..*.......0...www.bing.com.edgekey.J.[......?....e86303.dscx
akamaiedge.J.........{.1.n0dscx..
hostmaster.akamai..j...................
13:15:01.320868 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.50060: 13049 12/0/0 CNAME www-www.bing.com.trafficmanager.net., CNAME www.bing.com.edgekey.net., CNAME e86303.dscx.akamaiedge.net., A 2.16.204.155, A 2.16.204.147, A 2.16.204.148, A 2.16.204.149, A 2.16.204.150, A 2.16.204.143, A 2.16.204.145, A 2.16.204.144, A 2.16.204.146 (295)
`.UU./.@.)g..............)g......x..8.r..5.../BI2............www.bing.com.............?..%.www-www.bing.com.trafficmanager.net..*.......0...www.bing.com.edgekey.J.[......?....e86303.dscx
akamaiedge.J.~.......   .......~....... .......~....... .......~....... .......~....... .......~....... .......~..............~.......  .......~....... ......
13:15:01.668309 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 38076+ A? login.microsoftonline.com. (43)
`.\..3.@.)g......x..8.r..)g................5.3...............login.microsoftonline.com.....
13:15:01.668601 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 52849+ AAAA? login.microsoftonline.com. (43)
`....3.@.)g......x..8.r..)g................5.3.I.q...........login.microsoftonline.com.....
13:15:01.685249 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 38076 11/0/0 CNAME login.mso.msidentity.com., CNAME ak.privatelink.msidentity.com., CNAME www.tm.a.prd.aadg.akadns.net., A 20.190.160.131, A 20.190.160.22, A 20.190.160.128, A 20.190.160.3, A 40.126.32.134, A 20.190.160.5, A 40.126.32.74, A 20.190.160.65 (277)
`......@.)g..............)g......x..8.r..5....B7.............login.microsoftonline.com.............     4...login.mso
msidentity.".7...........ak.privatelink.A.Z...........www.tm.a.prd.aadg.akadns.net..w...............w...............w...............w...............w..........(~ ..w...............w..........(~ J.w.............A
13:15:01.686738 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 52849 11/0/0 CNAME login.mso.msidentity.com., CNAME ak.privatelink.msidentity.com., CNAME www.tm.a.prd.aadg.akadns.net., AAAA 2603:1026:3000:d8::1, AAAA 2603:1027:1:c8::2, AAAA 2603:1026:3000:d0::d, AAAA 2603:1027:1:c8::, AAAA 2603:1027:1:d0::6, AAAA 2603:1026:3000:c8::6, AAAA 2603:1027:1:d0::3, AAAA 2603:1027:1:d8::4 (373)
`....}.@.)g..............)g......x..8.r..5...}B..q...........login.microsoftonline.com.............     4...login.mso
msidentity.".7...........ak.privatelink.A.Z...........www.tm.a.prd.aadg.akadns.net..w..........&..&0............w..........&..'.............w..........&..&0............w..........&..'.............w..........&..'.............w..........&..&0............w..........&..'.............w..........&..'............
13:15:06.436193 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 5488+ A? login.live.com. (32)
`.\..(.@.)g......x..8.r..)g................5.(V..p...........login.live.com.....
13:15:06.436574 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 59471+ AAAA? login.live.com. (32)
`....(.@.)g......x..8.r..)g................5.(e@.O...........login.live.com.....
13:15:06.453138 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 5488 12/0/0 CNAME login.msa.msidentity.com., CNAME www.tm.lg.prod.aadmsa.akadns.net., CNAME prdv4a.aadg.msidentity.com., CNAME www.tm.v4.a.prd.aadg.trafficmanager.net., A 20.190.160.65, A 20.190.160.66, A 20.190.160.132, A 40.126.32.68, A 40.126.32.74, A 40.126.32.134, A 20.190.160.17, A 20.190.160.64 (317)
`....E.@.)g..............)g......x..8.r..5...EB_.p...........login.live.com..................login.msa
msidentity...,.........".www.tm.lg.prod.aadmsa.akadns.net..O...........prdv4a.aadg.6.}.........&.www.tm.v4.a.prd.aadg.trafficmanager.l...............A...............B............................(~ D............(~ J............(~ ................................@
13:15:06.454159 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 59471 4/1/0 CNAME login.msa.msidentity.com., CNAME www.tm.lg.prod.aadmsa.akadns.net., CNAME prdv4a.aadg.msidentity.com., CNAME www.tm.v4.a.prd.aadg.trafficmanager.net. (247)
`......@.)g..............)g......x..8.r..5....B..O...........login.live.com..................login.msa
msidentity...,.........".www.tm.lg.prod.aadmsa.akadns.net..O...........prdv4a.aadg.6.}.........&.www.tm.v4.a.prd.aadg.trafficmanager.l.............tm1.dns-tm..
hostmaster..wd.`.......,.$......
13:15:07.781768 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:15:07.782528 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:15:09.500386 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.51494 > OpenWrt.lan.53: 31851+ HTTPS? community-sites.emqx.com. (42)
`.c..2.@.)g......x..8.r..)g..............&.5.2..|k...........community-sites.emqx.com..A..
13:15:09.500749 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.51740 > OpenWrt.lan.53: 54321+ A? community-sites.emqx.com. (42)
`.h..2.@.)g......x..8.r..)g................5.2.-.1...........community-sites.emqx.com.....
13:15:09.729027 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.51740: 54321 1/0/0 A 54.215.63.195 (58)
`..$.B.@.)g..............)g......x..8.r..5...BA\.1...........community-sites.emqx.com..............X..6.?.
13:15:09.737616 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.51494: 31851 0/1/0 (115)
`....{.@.)g..............)g......x..8.r..5.&.{A.|k...........community-sites.emqx.com..A.............=.ns3.dnsv4.!.enterprise2dnsadmin.dnspod.!j.s...........u.....
13:15:12.446696 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 2306+ A? wpad.lan. (26)
`.\..".@.)g......x..8.r..)g................5."1.        ............wpad.lan.....
13:15:12.447330 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 2306 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<        ............wpad.lan.....
13:15:14.001137 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 43261+ A? gfe.nvidia.com. (32)
`....(.@.)g......x..8.r..)g................5.(...............gfe.nvidia.com.....
13:15:14.001429 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 2051+ AAAA? gfe.nvidia.com. (32)
`.\..(.@.)g......x..8.r..)g................5.(i).............gfe.nvidia.com.....
13:15:14.017978 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 43261 2/0/0 A 72.25.64.8, A 72.25.64.38 (64)
`....H.@.)g..............)g......x..8.r..5...HAb.............gfe.nvidia.com.................H.@.............H.@&
13:15:14.019109 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 2051 0/1/0 (97)
`....i.@.)g..............)g......x..8.r..5...iA..............gfe.nvidia.com..............N.5.dns1.p07.nsone.net.
hostmaster.5b.Vp.........       :....,
13:15:17.448903 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 3463+ A? cc-api-data.adobe.io. (38)
`......@.)g......x..8.r..)g................5..r..............cc-api-data.adobe.io.....
13:15:17.450014 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 1159+ AAAA? cc-api-data.adobe.io. (38)
`.\....@.)g......x..8.r..)g................5.................cc-api-data.adobe.io.....
13:15:17.465131 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 3463 6/0/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos508-prod-va6.ethos.adobe.net., CNAME dunamis-ethos508-prod-va6-856defacfb833db1.elb.us-east-1.amazonaws.com., A 52.73.45.44, A 52.6.228.48, A 34.233.49.149 (261)
`......@.)g..............)g......x..8.r..5....B'.............cc-api-data.adobe.io..............9...cc-api-data-ew1...2.......<.1.ethos.dunamis.ethos508-prod-va6.ethos.adobe.net..P.......<.H*dunamis-ethos508-prod-va6-856defacfb833db1.elb   us-east-1        amazonaws.com..........<..4I-,.........<..4..0.........<..".1.
13:15:17.466626 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 1159 3/1/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos508-prod-va6.ethos.adobe.net., CNAME dunamis-ethos508-prod-va6-856defacfb833db1.elb.us-east-1.amazonaws.com. (297)
`....1.@.)g..............)g......x..8.r..5...1BK.............cc-api-data.adobe.io..............9...cc-api-data-ew1...2.......<.1.ethos.dunamis.ethos508-prod-va6.ethos.adobe.net..P.......<.H*dunamis-ethos508-prod-va6-856defacfb833db1.elb   us-east-1        amazonaws.com..........<.H.ns-1826      awsdns-36.co.uk..awsdns-hostmaster.amazon......... ......u....<
13:15:22.742591 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 29968+ A? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.)..u............www.youtube.com.....
13:15:22.743809 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 38076+ AAAA? www.youtube.com. (33)
`.\..).@.)g......x..8.r..)g................5.)...............www.youtube.com.....
13:15:22.758808 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 29968 8/0/0 A 142.251.151.4, A 142.251.152.4, A 142.251.157.4, A 142.251.153.4, A 142.251.154.4, A 142.251.156.4, A 142.251.150.4, A 142.251.155.4 (161)
`......@.)g..............)g......x..8.r..5....A.u............www.youtube.com.....................................................................................................................................
13:15:22.760555 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 38076 8/0/0 AAAA 2001:4860:4827:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:482d:400::, AAAA 2001:4860:482c:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:4829:400::, AAAA 2001:4860:482a:400::, AAAA 2001:4860:482b:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#.............www.youtube.com................. .H`H'...................... .H`H(...................... .H`H-...................... .H`H,...................... .H`H&...................... .H`H)...................... .H`H*...................... .H`H+..........
13:15:22.762140 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 38545+ A? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.).(.............www.youtube.com.....
13:15:22.762796 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 38545 8/0/0 A 142.251.151.4, A 142.251.152.4, A 142.251.157.4, A 142.251.153.4, A 142.251.154.4, A 142.251.156.4, A 142.251.150.4, A 142.251.155.4 (161)
`......@.)g..............)g......x..8.r..5....A..............www.youtube.com.....................................................................................................................................
13:15:22.764327 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 27652+ AAAA? www.youtube.com. (33)
`.\..).@.)g......x..8.r..)g................5.));l............www.youtube.com.....
13:15:22.765758 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 27652 8/0/0 AAAA 2001:4860:4827:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:482d:400::, AAAA 2001:4860:482c:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:4829:400::, AAAA 2001:4860:482a:400::, AAAA 2001:4860:482b:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#l............www.youtube.com................. .H`H'...................... .H`H(...................... .H`H-...................... .H`H,...................... .H`H&...................... .H`H)...................... .H`H*...................... .H`H+..........
13:15:28.881370 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 58013+ A? ss-prod-ew1-ns.aws.adobess.com. (48)
`....8.@.)g......x..8.r..)g................5.8...............ss-prod-ew1-ns.aws.adobess.com.....
13:15:28.881653 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 45899+ AAAA? ss-prod-ew1-ns.aws.adobess.com. (48)
`.\..8.@.)g......x..8.r..)g................5.8E..K...........ss-prod-ew1-ns.aws.adobess.com.....
13:15:28.897416 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 58013 3/0/0 A 52.211.47.154, A 52.209.121.172, A 54.247.146.61 (96)
`....h.@.)g..............)g......x..8.r..5...hA..............ss-prod-ew1-ns.aws.adobess.com.................4./.............4.y.............6..=
13:15:28.899008 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 45899 0/1/0 (132)
`......@.)g..............)g......x..8.r..5....A..K...........ss-prod-ew1-ns.aws.adobess.com..............=.H.ns-1676   awsdns-17.co.uk..awsdns-hostmaster.amazon.'....... ......u...Q.
13:15:33.621718 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:15:33.622958 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:15:57.140870 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 45599+ A? events.gfe.nvidia.com. (39)
`..../.@.)g......x..8.r..)g................5./<[.............events.gfe.nvidia.com.....
13:15:57.141251 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 57427+ AAAA? events.gfe.nvidia.com. (39)
`.\../.@.)g......x..8.r..)g................5./...S...........events.gfe.nvidia.com.....
13:15:57.156941 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 45599 1/0/0 A 18.198.233.49 (55)
`....?.@.)g..............)g......x..8.r..5...?AY.............events.gfe.nvidia.com..............>.....1
13:15:57.158378 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 57427 0/1/0 (104)
`....p.@.)g..............)g......x..8.r..5...pA..S...........events.gfe.nvidia.com..............z.5.dns1.p07.nsone.net.
hostmaster.<b.Vp.........       :....,
13:15:58.990997 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 40007+ A? lightstep.kaizen.nvidia.com. (45)
`....5.@.)g......x..8.r..)g................5.5xi.G..........    lightstep.kaizen.nvidia.com.....
13:15:58.991289 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 5694+ AAAA? lightstep.kaizen.nvidia.com. (45)
`.\..5.@.)g......x..8.r..)g................5.5...>..........    lightstep.kaizen.nvidia.com.....
13:15:59.007543 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 40007 4/0/0 CNAME proxies-prod-ew3.otel.kaizen.nvidia.com., A 15.224.121.252, A 13.36.189.128, A 51.45.53.30 (129)
`......@.)g..............)g......x..8.r..5....A..G..........    lightstep.kaizen.nvidia.com..................proxies-prod-ew3.otel...9............y..9...........$...9..........3-5.
13:15:59.008550 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 5694 4/0/0 CNAME proxies-prod-ew3.otel.kaizen.nvidia.com., AAAA 2a05:d012:fc8:411d:a903:cefc:9acf:6f04, AAAA 2a05:d012:fc8:412c:5f3f:57c2:b77b:be97, AAAA 2a05:d012:fc8:410c:207c:8c09:aa65:7a88 (165)
`......@.)g..............)g......x..8.r..5....A..>..........    lightstep.kaizen.nvidia.com..................proxies-prod-ew3.otel...9..........*.....A.......o..9..........*.....A,_?W..{...9..........*.....A. |.     .ez.
13:15:59.461776 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:15:59.464302 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:16:25.221723 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:16:25.222884 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:16:51.061787 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:16:51.063107 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:17:41.621716 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:17:41.623090 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:17:53.335109 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [S], seq 2753325516, win 65535, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
E..4v.@....G...........[..i..........   ..............
13:17:53.335520 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [S.], seq 3241142512, ack 2753325517, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 4], length 0
E..4..@.@............[.../....i......
..............
13:17:53.336294 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 1, win 255, length 0
E..(v.@....R...........[..i../..P...s...
13:17:53.341346 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 1:35, ack 1, win 255, length 34
E..Jv.@..../...........[..i../..P........ ..MQTT...<........mqttx_a8bbbd1e
13:17:53.341634 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [.], ack 35, win 4013, length 0
E..($n@.@.x~.........[.../....i.P.......
13:17:53.342690 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 1:12, ack 35, win 4013, length 11
E..3$o@.@.xr.........[.../....i.P....   ..      ...".
!..
13:17:53.386097 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 12, win 255, length 0
E..(v.@....P...........[..i../..P...s...
13:17:53.388912 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 35:61, ack 12, win 255, length 26
E..Bv.@....5...........[..i../..P...'..........iotiscooltrustme/1.
13:17:53.389448 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 12:18, ack 61, win 4012, length 6
E...$p@.@.xv.........[.../....j P.............
13:17:53.431826 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 18, win 255, length 0
E..(v.@....N...........[..j     ./..P...s_..
13:18:19.029630 IP 192.168.14.146.56771 > OpenWrt.lan.53: 45208+ HTTPS? main.vscode-cdn.net. (37)
E..Av.....&*...........5.-.@.............main
vscode-cdn.net..A..
13:18:19.030002 IP 192.168.14.146.62319 > OpenWrt.lan.53: 20034+ A? main.vscode-cdn.net. (37)
E..Av.....&).........o.5.-..NB...........main
vscode-cdn.net.....
13:18:19.046076 IP OpenWrt.lan.53 > 192.168.14.146.56771: 45208 2/1/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net. (173)
E...2;@.@.j..........5...................main
vscode-cdn.net..A..............
vscode-cdn.z01.azurefd...1.......2...mr-z01
tm-azurefd...].........7.tm1.dns-tm.com..msnhst microsoft..xa'..........$.....<
13:18:19.047451 IP OpenWrt.lan.53 > 192.168.14.146.62319: 20034 3/0/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net., A 150.171.109.98 (122)
E...2<@.@.j7.........5.o...wNB...........main
vscode-cdn.net.................
vscode-cdn.z01.azurefd...1.......2...mr-z01
tm-azurefd...V.......   ....mb
13:18:19.781770 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:18:19.782963 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:18:45.621712 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:18:45.623154 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:18:53.389124 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 61:63, ack 18, win 255, length 2
E..*v.@....I...........[..j     ./..P....T....
13:18:53.389633 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 18:20, ack 63, win 4012, length 2
E..*$q@.@.xy.........[.../....j.P.........
13:18:53.435190 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 20, win 255, length 0
E..(v.@....J...........[..j../..P...s[..
13:19:19.381754 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:19:19.382790 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:19:23.302517 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 65060+ A? self.events.data.microsoft.com. (48)
`....8.@.)g......x..8.r..)g................5.8...$...........self.events.data   microsoft.com.....
13:19:23.302916 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 5793+ AAAA? self.events.data.microsoft.com. (48)
`....8.@.)g......x..8.r..)g................5.8...............self.events.data   microsoft.com.....
13:19:23.319246 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 65060 3/0/0 CNAME self-events-data.trafficmanager.net., CNAME onedscolprdeus55.eastus.cloudapp.azure.com., A 74.151.238.136 (166)
`......@.)g..............)g......x..8.r..5....A..$...........self.events.data   microsoft.com..............I.%.self-events-data.trafficmanager.net..<.........).onedscolprdeus55.eastus.cloudapp.azure.'.m..........J...
13:19:23.320482 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 5793 2/1/0 CNAME self-events-data.trafficmanager.net., CNAME onedscolprdeus55.eastus.cloudapp.azure.com. (211)
`......@.)g..............)g......x..8.r..5....A..............self.events.data   microsoft.com..............I.%.self-events-data.trafficmanager.net..<.........).onedscolprdeus55.eastus.cloudapp.azure.'.~.........1.ns1-201    azure-dns.'.msnhst....'........,.       :....<
13:19:31.429887 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 61460+ A? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."+..............wpad.lan.....
13:19:31.430215 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55122 > OpenWrt.lan.53: 4315+ A? wpad.lan. (26)
`
oI.".@.)g......x..8.r..)g..............R.5."!..............wpad.lan.....
13:19:31.430217 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.53141 > OpenWrt.lan.53: 8622+ AAAA? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."..!............wpad.lan.....
13:19:31.430217 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.50638 > OpenWrt.lan.53: 36666+ AAAA? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."...:...........wpad.lan.....
13:19:31.431016 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 61460 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:19:31.432008 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55122: 4315 NXDomain 0/0/0 (26)
`
@..".@.)g..............)g......x..8.r..5.R."A<.............wpad.lan.....
13:19:31.432701 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.53141: 8622 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<!............wpad.lan.....
13:19:31.433464 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.50638: 36666 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.:...........wpad.lan.....
13:19:45.438933 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 63692+ A? v10.events.data.microsoft.com. (47)
`....7.@.)g......x..8.r..)g................5.76..............v10.events.data    microsoft.com.....
13:19:45.440033 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.56862 > OpenWrt.lan.53: 51213+ AAAA? v10.events.data.microsoft.com. (47)
`..E.7.@.)g......x..8.r..)g................5.7\t.............v10.events.data    microsoft.com.....
13:19:45.454968 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 63692 3/0/0 CNAME win-global-asimov-leafs-events-data.trafficmanager.net., CNAME onedscolprdeus62.eastus.cloudapp.azure.com., A 74.151.238.102 (184)
`......@.)g..............)g......x..8.r..5....A..............v10.events.data    microsoft.com..............0.8#win-global-asimov-leafs-events-data.trafficmanager.net..;.......,.).onedscolprdeus62.eastus.cloudapp.azure.&............J..f
13:19:45.456935 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.56862: 51213 2/1/0 CNAME win-global-asimov-leafs-events-data.trafficmanager.net., CNAME onedscolprdeus62.eastus.cloudapp.azure.com. (229)
`..@...@.)g..............)g......x..8.r..5....B..............v10.events.data    microsoft.com..............0.8#win-global-asimov-leafs-events-data.trafficmanager.net..;.......,.).onedscolprdeus62.eastus.cloudapp.azure.&.........,.1.ns1-201azure-dns.&.msnhst....'........,.        :....<
13:19:46.444894 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 2836+ A? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."...............wpad.lan.....
13:19:46.444897 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55122 > OpenWrt.lan.53: 42026+ A? wpad.lan. (26)
`
oI.".@.)g......x..8.r..)g..............R.5."...*...........wpad.lan.....
13:19:46.445279 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.56862 > OpenWrt.lan.53: 26551+ AAAA? wpad.lan. (26)
`..E.".@.)g......x..8.r..)g................5.".:g............wpad.lan.....
13:19:46.445281 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.58834 > OpenWrt.lan.53: 60273+ AAAA? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."8..q...........wpad.lan.....
13:19:46.445964 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 2836 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:19:46.446652 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55122: 42026 NXDomain 0/0/0 (26)
`
@..".@.)g..............)g......x..8.r..5.R."A<.*...........wpad.lan.....
13:19:46.447334 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.56862: 26551 NXDomain 0/0/0 (26)
`..@.".@.)g..............)g......x..8.r..5..."A<g............wpad.lan.....
13:19:46.448097 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.58834: 60273 NXDomain 0/0/0 (26)
`.ZG.".@.)g..............)g......x..8.r..5..."A<.q...........wpad.lan.....
13:19:53.685621 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 63:65, ack 20, win 255, length 2
E..*w.@................[..j../..P....P....
13:19:53.686123 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 20:22, ack 65, win 4012, length 2
E..*$r@.@.xx.........[.../....j.P.........
13:19:53.731049 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 22, win 255, length 0
E..(w.@................[..j../..P...sW..
13:20:46.457934 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 57524+ A? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5.";\.............wpad.lan.....
13:20:46.457936 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55122 > OpenWrt.lan.53: 27301+ A? wpad.lan. (26)
`
oI.".@.)g......x..8.r..)g..............R.5.".3j............wpad.lan.....
13:20:46.458317 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.58080 > OpenWrt.lan.53: 58943+ AAAA? wpad.lan. (26)
`.9..".@.)g......x..8.r..)g................5."@..?...........wpad.lan.....
13:20:46.458319 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.51930 > OpenWrt.lan.53: 49661+ AAAA? wpad.lan. (26)
`....".@.)g......x..8.r..)g................5."}8.............wpad.lan.....
13:20:46.459045 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 57524 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:20:46.459757 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55122: 27301 NXDomain 0/0/0 (26)
`
@..".@.)g..............)g......x..8.r..5.R."A<j............wpad.lan.....
13:20:46.460521 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.58080: 58943 NXDomain 0/0/0 (26)
`....".@.)g..............)g......x..8.r..5..."A<.?...........wpad.lan.....
13:20:46.461196 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.51930: 49661 NXDomain 0/0/0 (26)
`.,..".@.)g..............)g......x..8.r..5..."A<.............wpad.lan.....
13:20:52.532814 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 14862+ A? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.)W.:............www.youtube.com.....
13:20:52.533910 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 10467+ AAAA? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.)[E(............www.youtube.com.....
13:20:52.549022 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 14862 8/0/0 A 142.251.155.4, A 142.251.150.4, A 142.251.153.4, A 142.251.157.4, A 142.251.152.4, A 142.251.154.4, A 142.251.151.4, A 142.251.156.4 (161)
`......@.)g..............)g......x..8.r..5....A.:............www.youtube.com.....................................................................................................................................
13:20:52.551121 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 10467 8/0/0 AAAA 2001:4860:4829:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:482b:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:482a:400::, AAAA 2001:4860:482c:400::, AAAA 2001:4860:4827:400::, AAAA 2001:4860:482d:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#(............www.youtube.com................. .H`H)...................... .H`H&...................... .H`H+...................... .H`H(...................... .H`H*...................... .H`H,...................... .H`H'...................... .H`H-..........
13:20:52.552725 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 30093+ A? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.).-u............www.youtube.com.....
13:20:52.553365 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 30093 8/0/0 A 142.251.155.4, A 142.251.150.4, A 142.251.153.4, A 142.251.157.4, A 142.251.152.4, A 142.251.154.4, A 142.251.151.4, A 142.251.156.4 (161)
`......@.)g..............)g......x..8.r..5....A.u............www.youtube.com.....................................................................................................................................
13:20:52.554520 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 63258+ AAAA? www.youtube.com. (33)
`....).@.)g......x..8.r..)g................5.)...............www.youtube.com.....
13:20:52.555177 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 63258 8/0/0 AAAA 2001:4860:4829:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:482b:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:482a:400::, AAAA 2001:4860:482c:400::, AAAA 2001:4860:4827:400::, AAAA 2001:4860:482d:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#.............www.youtube.com................. .H`H)...................... .H`H&...................... .H`H+...................... .H`H(...................... .H`H*...................... .H`H,...................... .H`H'...................... .H`H-..........
13:20:54.681471 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 65:67, ack 22, win 255, length 2
E..*w.@....[...........[..j../..P....L....
13:20:54.682183 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 22:24, ack 67, win 4012, length 2
E..*$s@.@.xw.........[.../....j.P.........
13:20:54.726493 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 24, win 255, length 0
E..(w.@....\...........[..j../..P...sS..
13:21:24.101784 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:21:24.102937 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:21:24.524884 IP 192.168.14.146.55168 > OpenWrt.lan.53: 55427+ HTTPS? mobile.events.data.microsoft.com. (50)
E..Nw.....%+...........5.:qt.............mobile.events.data     microsoft.com..A..
13:21:24.525244 IP 192.168.14.146.51466 > OpenWrt.lan.53: 4536+ A? mobile.events.data.microsoft.com. (50)
E..Nw.....%*.........
.5.:F..............mobile.events.data   microsoft.com.....
13:21:24.541569 IP OpenWrt.lan.53 > 192.168.14.146.55168: 55427 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com. (215)
E...T.@.@.Gm.........5...................mobile.events.data     microsoft.com..A...........=.'.mobile.events.data.trafficmanager.net..>.......;.).onedscolprdeus66.eastus.cloudapp.azure.).........;.1.ns1-201  azure-dns.).msnhst....'........,.       :....<
13:21:24.543090 IP OpenWrt.lan.53 > 192.168.14.146.51466: 4536 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com., A 74.151.238.98 (170)
E...T.@.@.G..........5.
.................mobile.events.data     microsoft.com..............=.'.mobile.events.data.trafficmanager.net..>.......;.).onedscolprdeus66.eastus.cloudapp.azure.).q.......     ..J..b
13:21:45.914644 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 54194+ A? telemetry.individual.githubcopilot.com. (56)
`....@.@.)g......x..8.r..)g................5.@L.............    telemetry
individual.githubcopilot.com.....
13:21:45.914647 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 9650+ AAAA? telemetry.individual.githubcopilot.com. (56)
`....@.@.)g......x..8.r..)g................5.@.q%...........    telemetry
individual.githubcopilot.com.....
13:21:45.918568 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 9650 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.%...........    telemetry
individual.githubcopilot.com..............>...copilot-telemetry-service.githubusercontent./.D.......`...glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:21:45.931045 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 54194 3/0/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com., A 140.82.112.22 (170)
`......@.)g..............)g......x..8.r..5....A.............    telemetry
individual.githubcopilot.com..............?...copilot-telemetry-service.githubusercontent./.D.......a...glb-db52c2cf8be544.github./.~.......'...Rp.
13:21:47.323787 IP 192.168.14.146.54062 > OpenWrt.lan.53: 14188+ HTTPS? api.github.com. (32)
E..<w.....%;...........5.(..7l...........api.github.com..A..
13:21:47.324143 IP 192.168.14.146.60483 > OpenWrt.lan.53: 13588+ A? api.github.com. (32)
E..<w.....%:.........C.5.(..5............api.github.com.....
13:21:47.340014 IP OpenWrt.lan.53 > 192.168.14.146.54062: 14188 0/1/0 (116)
E...X.@.@.C..........5...|.q7l...........api.github.com..A.............H.ns-1707        awsdns-21.co.uk..awsdns-hostmaster.amazon......... ......u...Q.
13:21:47.341127 IP OpenWrt.lan.53 > 192.168.14.146.60483: 13588 1/0/0 A 20.250.119.72 (48)
E..LX.@.@.D
.........5.C.8.-5............api.github.com...................wH
13:21:47.388874 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 14739+ A? api.github.com. (32)
`....(.@.)g......x..8.r..)g................5.($.9............api.github.com.....
13:21:47.389161 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 49028+ AAAA? api.github.com. (32)
`....(.@.)g......x..8.r..)g................5.(...............api.github.com.....
13:21:47.389707 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 14739 1/0/0 A 20.250.119.72 (48)
`....8.@.)g..............)g......x..8.r..5...8AR9............api.github.com...................wH
13:21:47.390416 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 49028 0/0/0 (32)
`....(.@.)g..............)g......x..8.r..5...(AB.............api.github.com.....
13:21:47.925955 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 27906+ A? mobile.events.data.microsoft.com. (50)
`....:.@.)g......x..8.r..)g................5.:0.m............mobile.events.data microsoft.com.....
13:21:47.925957 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 28079+ AAAA? mobile.events.data.microsoft.com. (50)
`....:.@.)g......x..8.r..)g................5.:".m............mobile.events.data microsoft.com.....
13:21:47.942335 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 27906 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com., A 74.151.238.98 (170)
`......@.)g..............)g......x..8.r..5....A.m............mobile.events.data microsoft.com..............&.'.mobile.events.data.trafficmanager.net..>.......$.).onedscolprdeus66.eastus.cloudapp.azure.).q..........J..b
13:21:47.944343 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 28079 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com. (215)
`......@.)g..............)g......x..8.r..5....A.m............mobile.events.data microsoft.com..............&.'.mobile.events.data.trafficmanager.net..>.......$.).onedscolprdeus66.eastus.cloudapp.azure.).........$.1.ns1-201  azure-dns.).msnhst....'........,.       :....<
13:21:48.439802 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.56938 > OpenWrt.lan.53: 7056+ HTTPS? production-copilot-host-westus3.webpubsub.azure.com. (69)
`..K.M.@.)g......x..8.r..)g..............j.5.M(..............production-copilot-host-westus3    webpubsub.azure.com..A..
13:21:48.440420 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60227 > OpenWrt.lan.53: 8077+ A? production-copilot-host-westus3.webpubsub.azure.com. (69)
`..+.M.@.)g......x..8.r..)g..............C.5.MW..............production-copilot-host-westus3    webpubsub.azure.com.....
13:21:48.456863 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60227: 8077 2/0/0 CNAME production-copilot-host-westus3.privatelink.webpubsub.azure.com., A 20.150.244.245 (143)
`..<...@.)g..............)g......x..8.r..5.C..A..............production-copilot-host-westus3    webpubsub.azure.com..................production-copilot-host-westus3.privatelink.,.Q..............
13:21:48.466083 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.56938: 7056 1/1/0 CNAME production-copilot-host-westus3.privatelink.webpubsub.azure.com. (210)
`./O...@.)g..............)g......x..8.r..5.j..A..............production-copilot-host-westus3    webpubsub.azure.com..A...............production-copilot-host-westus3.privatelink.,.,.......,.G.ns1-06   azure-dns.<.azuredns-hostmaster microsoft.<...........,.$.....,
13:21:49.180161 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.52758 > OpenWrt.lan.53: 19130+ HTTPS? api.githubcopilot.com. (39)
`       .../.@.)g......x..8.r..)g................5./..J............api.githubcopilot.com..A..
13:21:49.180516 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60858 > OpenWrt.lan.53: 24489+ A? api.githubcopilot.com. (39)
`..../.@.)g......x..8.r..)g................5./.L_............api.githubcopilot.com.....
13:21:49.183564 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.52758: 19130 1/1/0 CNAME glb-db52c2cf8be544.github.com. (144)
`.x....@.)g..............)g......x..8.r..5....A.J............api.githubcopilot.com..A.......... ....glb-db52c2cf8be544.github...F.........5.dns1.p08.nsone.net.
hostmaster.db..7....... ..u.....
13:21:49.197432 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60858: 24489 2/0/0 CNAME glb-db52c2cf8be544.github.com., A 140.82.112.22 (95)
`....g.@.)g..............)g......x..8.r..5...gA._............api.githubcopilot.com............. ....glb-db52c2cf8be544.github...3.......#...Rp.
13:21:49.220560 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 6674+ A? api.individual.githubcopilot.com. (50)
`....:.@.)g......x..8.r..)g................5.:K..............api
individual.githubcopilot.com.....
13:21:49.220562 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 19945+ AAAA? api.individual.githubcopilot.com. (50)
`....:.@.)g......x..8.r..)g................5.:
IM............api
individual.githubcopilot.com.....
13:21:49.224132 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 19945 2/1/0 CNAME api.githubcopilot.com., CNAME glb-db52c2cf8be544.github.com. (192)
`......@.)g..............)g......x..8.r..5....A.M............api
individual.githubcopilot.com..............M...api...>......     ....glb-db52c2cf8be544.github.).c.........H.ns-1707    awsdns-21.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:21:49.227316 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 60055+ AAAA? api.individual.githubcopilot.com. (50)
`....:.@.)g......x..8.r..)g................5.:m..............api
individual.githubcopilot.com.....
13:21:49.229874 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 60055 2/1/0 CNAME api.githubcopilot.com., CNAME glb-db52c2cf8be544.github.com. (192)
`......@.)g..............)g......x..8.r..5....A..............api
individual.githubcopilot.com..............M...api...>......     ....glb-db52c2cf8be544.github.).c.........H.ns-1707    awsdns-21.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:21:49.236166 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 6674 3/0/0 CNAME api.githubcopilot.com., CNAME glb-db52c2cf8be544.github.com., A 140.82.112.22 (124)
`......@.)g..............)g......x..8.r..5....A..............api
individual.githubcopilot.com..............L...api...>......     ....glb-db52c2cf8be544.github.).P.......#...Rp.
13:21:53.621795 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:21:53.622763 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:21:55.681329 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 67:69, ack 24, win 255, length 2
E..*w.@....U...........[..j../..P....H....
13:21:55.681919 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 24:26, ack 69, win 4012, length 2
E..*$t@.@.xv.........[.../....j.P.........
13:21:55.727879 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 26, win 255, length 0
E..(w.@....V...........[..j../.
P...sO..
13:21:59.235190 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 48667+ AAAA? telemetry.individual.githubcopilot.com. (56)
`....@.@.)g......x..8.r..)g................5.@a.............    telemetry
individual.githubcopilot.com.....
13:21:59.238010 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 48667 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.............    telemetry
individual.githubcopilot.com..............1...copilot-telemetry-service.githubusercontent./.D.......S...glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:22:00.073691 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 15614+ A? mobile.events.data.microsoft.com. (50)
`....:.@.)g......x..8.r..)g................5.:`.<............mobile.events.data microsoft.com.....
13:22:00.073983 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 20828+ AAAA? mobile.events.data.microsoft.com. (50)
`....:.@.)g......x..8.r..)g................5.:?.Q\...........mobile.events.data microsoft.com.....
13:22:00.075673 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 20828 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com. (259)
`......@.)g..............)g......x..8.r..5....B%Q\...........mobile.events.data microsoft.com................'.mobile.events.data.trafficmanager.net..>.........,.onedscolprdeus66.eastus.cloudapp.azure.com..eastus.cloudapp.azure.com..........A.ns1-201      azure-dns.com..msnhst   microsoft.com...'........,.     :....<
13:22:00.089993 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 15614 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus66.eastus.cloudapp.azure.com., A 74.151.238.98 (170)
`......@.)g..............)g......x..8.r..5....A.<............mobile.events.data microsoft.com................'.mobile.events.data.trafficmanager.net..>.........).onedscolprdeus66.eastus.cloudapp.azure.).q.......     ..J..b
13:22:08.695674 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 56059+ AAAA? telemetry.individual.githubcopilot.com. (56)
`....@.@.)g......x..8.r..)g................5.@D.............    telemetry
individual.githubcopilot.com.....
13:22:08.698740 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 56059 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.............    telemetry
individual.githubcopilot.com..............'...copilot-telemetry-service.githubusercontent./.D.......I...glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:22:17.605414 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 17877+ A? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-".E............accounts.google.com.....
13:22:17.605905 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 23857+ AAAA? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-.G]1...........accounts.google.com.....
13:22:17.622005 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 17877 1/0/0 A 142.251.127.84 (53)
`....=.@.)g..............)g......x..8.r..5...=AWE............accounts.google.com..............!.....T
13:22:17.623489 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 23857 1/0/0 AAAA 2a00:1450:4001:c21::54 (65)
`....I.@.)g..............)g......x..8.r..5...IAc]1...........accounts.google.com..............!..*..P@..!.......T
13:22:17.626542 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 43107+ A? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-...c...........accounts.google.com.....
13:22:17.627134 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 43107 1/0/0 A 142.251.127.84 (53)
`....=.@.)g..............)g......x..8.r..5...=AW.c...........accounts.google.com..............!.....T
13:22:17.629384 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 44839+ AAAA? accounts.google.com. (37)
`....-.@.)g......x..8.r..)g................5.-.Q.'...........accounts.google.com.....
13:22:17.630029 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 44839 1/0/0 AAAA 2a00:1450:4001:c21::54 (65)
`....I.@.)g..............)g......x..8.r..5...IAc.'...........accounts.google.com..............!..*..P@..!.......T
13:22:56.689493 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 69:71, ack 26, win 255, length 2
E..*w.@................[..j../.
P....D....
13:22:56.690013 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 26:28, ack 71, win 4012, length 2
E..*$u@.@.xu.........[.../.
..j.P.........
13:22:56.734039 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 28, win 255, length 0
E..(w.@..../...........[..j../..P...sK..
13:23:19.197704 IP 192.168.14.146.52780 > OpenWrt.lan.53: 26809+ HTTPS? main.vscode-cdn.net. (37)
E..Ax1....$..........,.5.-..h............main
vscode-cdn.net..A..
13:23:19.199053 IP 192.168.14.146.55626 > OpenWrt.lan.53: 27995+ A? main.vscode-cdn.net. (37)
E..Ax2....$..........J.5.-
.m[...........main
vscode-cdn.net.....
13:23:19.214006 IP OpenWrt.lan.53 > 192.168.14.146.52780: 26809 2/1/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net. (173)
E...{.@.@. ..........5.,....h............main
vscode-cdn.net..A..........     ...
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...].......+.7.tm1.dns-tm.com..msnhst microsoft..xa'..........$.....<
13:23:19.215384 IP OpenWrt.lan.53 > 192.168.14.146.55626: 27995 3/0/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net., A 150.171.109.105 (122)
E...{.@.@. ..........5.J...wm[...........main
vscode-cdn.net.............     ...
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...V............mi
13:23:57.690567 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 71:73, ack 28, win 255, length 2
E..*x.@....U...........[..j../..P....@....
13:23:57.691067 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 28:30, ack 73, win 4012, length 2
E..*$v@.@.xt.........[.../....j.P.........
13:23:57.735980 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 30, win 255, length 0
E..(x.@....V...........[..j../..P...sG..
13:24:27.301752 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:24:27.302783 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:24:31.315118 IP 192.168.14.146.60263 > OpenWrt.lan.53: 57807+ HTTPS? mobile.events.data.microsoft.com. (50)
E..Nx.....$%.........g.5.:TA.............mobile.events.data     microsoft.com..A..
13:24:31.315495 IP 192.168.14.146.58731 > OpenWrt.lan.53: 46869+ A? mobile.events.data.microsoft.com. (50)
E..Nx.....$$.........k.5.:.7.............mobile.events.data     microsoft.com.....
13:24:31.331645 IP OpenWrt.lan.53 > 192.168.14.146.60263: 57807 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdaue52.australiaeast.cloudapp.azure.com. (221)
E.....@.@..W.........5.g.................mobile.events.data     microsoft.com..A...........b.'.mobile.events.data.trafficmanager.net..>.......(.0.onedscolprdaue52.australiaeast.cloudapp.azure.).........(.0.ns1-06    azure-dns.).msnhst....'........,.       :....<
13:24:31.333141 IP OpenWrt.lan.53 > 192.168.14.146.58731: 46869 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdaue52.australiaeast.cloudapp.azure.com., A 40.79.163.154 (177)
E.....@.@............5.k.................mobile.events.data     microsoft.com..............b.'.mobile.events.data.trafficmanager.net..>.......(.0.onedscolprdaue52.australiaeast.cloudapp.azure.).q..........(O..
13:24:42.309861 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 32506+ A? ecs.office.com. (32)
`.=$.(.@.)g......x..8.r..)g................5.(.1~............ecs.office.com.....
13:24:42.310156 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 992+ AAAA? ecs.office.com. (32)
`.o..(.@.)g......x..8.r..)g................5.(X..............ecs.office.com.....
13:24:42.326340 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 32506 6/0/0 CNAME ecs.office.trafficmanager.net., CNAME dual-s-0005-office.config.skype.com., CNAME ecs-office.s-0005.dual-s-msedge.net., CNAME s-0005.dual-s-msedge.net., A 52.123.129.14, A 52.123.128.14 (213)
`......@.)g..............)g......x..8.r..5....A.~............ecs.office.com..............8...ecs.office.trafficmanager.net..,.........".dual-s-0005-office.config.skype...W........."
ecs-office.s-0005.dual-s-msedge.F.......................e..4{...........e..4{..
13:24:42.327853 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 992 6/0/0 CNAME ecs.office.trafficmanager.net., CNAME dual-s-0005-office.config.skype.com., CNAME ecs-office.s-0005.dual-s-msedge.net., CNAME s-0005.dual-s-msedge.net., AAAA 2603:1063:27:1::14, AAAA 2603:1063:27:2::14 (237)
`......@.)g..............)g......x..8.r..5....B..............ecs.office.com..............8...ecs.office.trafficmanager.net..,.........".dual-s-0005-office.config.skype...W........."
ecs-office.s-0005.dual-s-msedge.F.......................,..&..c.'...................,..&..c.'..........
13:24:53.313485 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 1698+ A? assets.msn.com. (32)
`.=$.(.@.)g......x..8.r..)g................5.(...............assets.msn.com.....
13:24:53.313776 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 42259+ AAAA? assets.msn.com. (32)
`.o..(.@.)g......x..8.r..)g................5.(+..............assets.msn.com.....
13:24:53.329865 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 1698 5/0/0 CNAME assets-msn-com-world-atm-default.trafficmanager.net., CNAME assets.msn.com-ion.edgesuite.net., CNAME a1666.dscr.akamai.net., A 92.226.3.26, A 92.226.3.33 (204)
`......@.)g..............)g......x..8.r..5....A..............assets.msn.com.............=p.5 assets-msn-com-world-atm-default.trafficmanager.net..,.......5...assets.msn.com-ion        edgesuite.\.m...........a1666.dscr.akamai.\.........
..\............
..\..!
13:24:53.331307 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 42259 5/0/0 CNAME assets-msn-com-world-atm-default.trafficmanager.net., CNAME assets.msn.com-ion.edgesuite.net., CNAME a1666.dscr.akamai.net., AAAA 2a02:3040:0:6::5ce2:321, AAAA 2a02:3040:0:6::5ce2:31a (228)
`......@.)g..............)g......x..8.r..5....B..............assets.msn.com.............=p.5 assets-msn-com-world-atm-default.trafficmanager.net..,.......5...assets.msn.com-ion        edgesuite.\.m...........a1666.dscr.akamai.\............*.0@........\..!............*.0@........\...
13:24:53.548205 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 26070+ A? login.live.com. (32)
`.=$.(.@.)g......x..8.r..)g................5.(.Be............login.live.com.....
13:24:53.548593 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 37543+ AAAA? login.live.com. (32)
`.o..(.@.)g......x..8.r..)g................5.(...............login.live.com.....
13:24:53.565296 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 26070 12/0/0 CNAME login.msa.msidentity.com., CNAME www.tm.lg.prod.aadmsa.trafficmanager.net., CNAME prdv4a.aadg.msidentity.com., CNAME www.tm.v4.a.prd.aadg.akadns.net., A 20.190.160.67, A 20.190.160.20, A 20.190.160.3, A 20.190.160.64, A 40.126.32.134, A 20.190.160.66, A 20.190.160.22, A 20.190.160.128 (317)
`....E.@.)g..............)g......x..8.r..5...EB_e............login.live.com..................login.msa
msidentity...,.........*.www.tm.lg.prod.aadmsa.trafficmanager.net..O...........prdv4a.aadg.6.............www.tm.v4.a.prd.aadg.akadns.t...............C...............................................@............(~ ................B................................
13:24:53.566302 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 37543 4/1/0 CNAME login.msa.msidentity.com., CNAME www.tm.lg.prod.aadmsa.trafficmanager.net., CNAME prdv4a.aadg.msidentity.com., CNAME www.tm.v4.a.prd.aadg.akadns.net. (252)
`......@.)g..............)g......x..8.r..5....B..............login.live.com..................login.msa
msidentity...,.........*.www.tm.lg.prod.aadmsa.trafficmanager.net..O...........prdv4a.aadg.6.............www.tm.v4.a.prd.aadg.akadns.t...........3.internal..
hostmaster.akamai..g....._..._..._.....
13:24:55.753448 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 47252+ A? aepxlg.adobe.com. (34)
`.=$.*.@.)g......x..8.r..)g................5.*...............aepxlg.adobe.com.....
13:24:55.753742 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 55107+ AAAA? aepxlg.adobe.com. (34)
`.o..*.@.)g......x..8.r..)g................5.*.b.C...........aepxlg.adobe.com.....
13:24:55.770130 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 47252 10/0/0 CNAME dsb4h3ustf.data.adobedc.net., A 63.140.62.172, A 63.140.62.128, A 63.140.62.166, A 63.140.62.34, A 63.140.62.236, A 63.140.62.200, A 63.140.62.139, A 63.140.62.210, A 63.140.62.120 (219)
`......@.)g..............)g......x..8.r..5....A........
.....aepxlg.adobe.com.............$?..
dsb4h3ustf.data.adobedc.net..........$..?.>..........$..?.>..........$..?.>..........$..?.>".........$..?.>..........$..?.>..........$..?.>..........$..?.>..........$..?.>x
13:24:55.771564 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 55107 1/1/0 CNAME dsb4h3ustf.data.adobedc.net. (134)
`......@.)g..............)g......x..8.r..5....A..C...........aepxlg.adobe.com.............$?..
dsb4h3ustf.data.adobedc.net..9........./.ns201.adobe.F
hostmaster..xi. ..Q...Q...Q....<
13:24:57.541722 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:24:57.542686 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:24:58.686541 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [P.], seq 73:75, ack 30, win 255, length 2
E..*x.@....Q...........[..j../..P....<....
13:24:58.687052 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [P.], seq 30:32, ack 75, win 4012, length 2
E..*$w@.@.xs.........[.../....j.P.........
13:24:58.733910 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 32, win 255, length 0
E..(x.@....R...........[..j../..P...sC..
13:25:03.259900 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 21501+ A? browser.events.data.msn.com. (45)
`.=$.5.@.)g......x..8.r..)g................5.5.2S............browser.events.data.msn.com.....
13:25:03.260994 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 57765+ AAAA? browser.events.data.msn.com. (45)
`.o..5.@.)g......x..8.r..)g................5.5Y..............browser.events.data.msn.com.....
13:25:03.276186 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 21501 3/0/0 CNAME global.asimov.events.data.trafficmanager.net., CNAME onedscolprdcus57.centralus.cloudapp.azure.com., A 4.150.223.100 (175)
`......@.)g..............)g......x..8.r..5....A.S............browser.events.data.msn.com.............>....global.asimov.events.data.trafficmanager.net..9.......#.,.onedscolprdcus57    centralus.cloudapp.azure.$.s.............d
13:25:03.277600 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 57765 2/1/0 CNAME global.asimov.events.data.trafficmanager.net., CNAME onedscolprdcus57.centralus.cloudapp.azure.com. (230)
`......@.)g..............)g......x..8.r..5....B..............browser.events.data.msn.com.............>....global.asimov.events.data.trafficmanager.net..9.......#.,.onedscolprdcus57    centralus.cloudapp.azure.$.........#.;.ns1-201  azure-dns.$.msnhst      microsoft.$..'........,.        :....<
13:25:09.154797 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 18914+ A? telemetry.individual.githubcopilot.com. (56)
`.=$.@.@.)g......x..8.r..)g................5.@.[I...........    telemetry
individual.githubcopilot.com.....
13:25:09.155091 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 2576+ AAAA? telemetry.individual.githubcopilot.com. (56)
`.o..@.@.)g......x..8.r..)g................5.@..
...........     telemetry
individual.githubcopilot.com.....
13:25:09.161264 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 2576 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.
...........     telemetry
individual.githubcopilot.com..............s...copilot-telemetry-service.githubusercontent./.D...........glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:25:09.173695 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 18914 3/0/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com., A 140.82.113.21 (170)
`......@.)g..............)g......x..8.r..5....A.I...........    telemetry
individual.githubcopilot.com..............s...copilot-telemetry-service.githubusercontent./.D...........glb-db52c2cf8be544.github./.~.......;...Rq.
13:25:09.377771 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 35816+ A? api.individual.githubcopilot.com. (50)
`.o..:.@.)g......x..8.r..)g................5.:.d.............api
individual.githubcopilot.com.....
13:25:09.378072 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 61853+ AAAA? api.individual.githubcopilot.com. (50)
`.=$.:.@.)g......x..8.r..)g................5.:t..............api
individual.githubcopilot.com.....
13:25:09.382195 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 61853 2/1/0 CNAME api.githubcopilot.com., CNAME glb-db52c2cf8be544.github.com. (192)
`......@.)g..............)g......x..8.r..5....A..............api
individual.githubcopilot.com..................api...>......     ....glb-db52c2cf8be544.github.).c.........H.ns-1707    awsdns-21.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:25:09.394118 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 35816 3/0/0 CNAME api.githubcopilot.com., CNAME glb-db52c2cf8be544.github.com., A 140.82.113.21 (124)
`......@.)g..............)g......x..8.r..5....A..............api
individual.githubcopilot.com..................api...>......     ....glb-db52c2cf8be544.github.).P.......;...Rq.
13:25:10.389829 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 54056+ A? api.github.com. (32)
`.=$.(.@.)g......x..8.r..)g................5.(...(...........api.github.com.....
13:25:10.390206 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 61159+ AAAA? api.github.com. (32)
`.o..(.@.)g......x..8.r..)g................5.(a..............api.github.com.....
13:25:10.391817 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 61159 0/0/0 (32)
`....(.@.)g..............)g......x..8.r..5...(AB.............api.github.com.....
13:25:10.406433 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 54056 1/0/0 A 140.82.121.5 (48)
`....8.@.)g..............)g......x..8.r..5...8AR.(...........api.github.com..............&...Ry.
13:25:11.165745 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 6626+ A? mobile.events.data.microsoft.com. (50)
`.o..:.@.)g......x..8.r..)g................5.:v..............mobile.events.data microsoft.com.....
13:25:11.166122 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 30747+ AAAA? mobile.events.data.microsoft.com. (50)
`.=$.:.@.)g......x..8.r..)g................5.:%.x............mobile.events.data microsoft.com.....
13:25:11.183164 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 6626 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus59.centralus.cloudapp.azure.com., A 4.150.223.102 (173)
`......@.)g..............)g......x..8.r..5....A..............mobile.events.data microsoft.com..............:.'.mobile.events.data.trafficmanager.net..>.......8.,.onedscolprdcus59      centralus.cloudapp.azure.).q.............f
13:25:11.184091 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 30747 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus59.centralus.cloudapp.azure.com. (218)
`......@.)g..............)g......x..8.r..5....A.x............mobile.events.data microsoft.com..............:.'.mobile.events.data.trafficmanager.net..>.......8.,.onedscolprdcus59      centralus.cloudapp.azure.).........8.1.ns1-201  azure-dns.).msnhst....'........,.       :....<
13:25:23.088637 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 17192+ AAAA? telemetry.individual.githubcopilot.com. (56)
`.o..@.@.)g......x..8.r..)g................5.@..C(..........    telemetry
individual.githubcopilot.com.....
13:25:23.091466 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 17192 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.C(..........    telemetry
individual.githubcopilot.com..............e...copilot-telemetry-service.githubusercontent./.D...........glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:25:23.331931 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 23974+ A? mobile.events.data.microsoft.com. (50)
`.=$.:.@.)g......x..8.r..)g................5.:@A]............mobile.events.data microsoft.com.....
13:25:23.333211 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 5952+ AAAA? mobile.events.data.microsoft.com. (50)
`.o..:.@.)g......x..8.r..)g................5.:y..@...........mobile.events.data microsoft.com.....
13:25:23.335592 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 5952 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus59.centralus.cloudapp.azure.com. (265)
`......@.)g..............)g......x..8.r..5....B+.@...........mobile.events.data microsoft.com................'.mobile.events.data.trafficmanager.net..>.......,./.onedscolprdcus59      centralus.cloudapp.azure.com.   centralus.cloudapp.azure.com........,.A.ns1-201 azure-dns.com..msnhst   microsoft.com...'........,.     :....<
13:25:23.347797 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 23974 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus59.centralus.cloudapp.azure.com., A 4.150.223.102 (173)
`......@.)g..............)g......x..8.r..5....A.]............mobile.events.data microsoft.com................'.mobile.events.data.trafficmanager.net..>.......,.,.onedscolprdcus59      centralus.cloudapp.azure.).q.............f
13:25:24.422800 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 46070+ A? cc-api-data.adobe.io. (38)
`.o....@.)g......x..8.r..)g................5.................cc-api-data.adobe.io.....
13:25:24.423092 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 44490+ AAAA? cc-api-data.adobe.io. (38)
`.=$...@.)g......x..8.r..)g................5.................cc-api-data.adobe.io.....
13:25:24.439933 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 46070 6/0/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com., A 52.31.167.175, A 52.48.202.212, A 52.212.178.60 (263)
`......@.)g..............)g......x..8.r..5....B).............cc-api-data.adobe.io..............
...cc-api-data-ew1...2.........2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb  eu-west-1       amazonaws.com.............4...............40..............4..<
13:25:24.440943 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 44490 3/1/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com. (299)
`....3.@.)g..............)g......x..8.r..5...3BM.............cc-api-data.adobe.io..............
...cc-api-data-ew1...2.........2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb  eu-west-1       amazonaws.com............H.ns-1566      awsdns-03.co.uk..awsdns-hostmaster.amazon......... ......u....<
13:25:27.621719 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:25:27.622728 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:25:38.686119 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 22731+ AAAA? telemetry.individual.githubcopilot.com. (56)
`.o..@.@.)g......x..8.r..)g................5.@..X...........    telemetry
individual.githubcopilot.com.....
13:25:38.688942 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 22731 2/1/0 CNAME copilot-telemetry-service.githubusercontent.com., CNAME glb-db52c2cf8be544.github.com. (238)
`......@.)g..............)g......x..8.r..5....B.X...........    telemetry
individual.githubcopilot.com..............U...copilot-telemetry-service.githubusercontent./.D.......w...glb-db52c2cf8be544.github./...........H.ns-1707 awsdns-21.co.uk..awsdns-hostmaster.amazon./....... ......u...Q.
13:26:07.240230 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 44261+ A? alive.github.com. (34)
`.=$.*.@.)g......x..8.r..)g................5.*<..............alive.github.com.....
13:26:07.241349 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 60033+ AAAA? alive.github.com. (34)
`.o..*.@.)g......x..8.r..)g................5.*...............alive.github.com.....
13:26:07.242714 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 60033 1/0/0 CNAME live.github.com. (63)
`....G.@.)g..............)g......x..8.r..5...GAa.............alive.github.com..................live.github.com.
13:26:07.256521 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 44261 2/0/0 CNAME live.github.com., A 140.82.114.26 (69)
`....M.@.)g..............)g......x..8.r..5...MAg.............alive.github.com..................live...........7...Rr.
13:26:07.259869 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 37037+ AAAA? alive.github.com. (34)
`.o..*.@.)g......x..8.r..)g................5.*K..............alive.github.com.....
13:26:07.260466 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 37037 1/0/0 CNAME live.github.com. (63)
`....G.@.)g..............)g......x..8.r..5...GAa.............alive.github.com..................live.github.com.
13:26:07.262206 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 46074+ A? live.github.com. (33)
`.=$.).@.)g......x..8.r..)g................5.)...............live.github.com.....
13:26:07.262865 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 46074 1/0/0 A 140.82.114.26 (49)
`....9.@.)g..............)g......x..8.r..5...9AS.............live.github.com..............7...Rr.
13:26:07.264095 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 50587+ AAAA? live.github.com. (33)
`.o..).@.)g......x..8.r..)g................5.)U..............live.github.com.....
13:26:07.264675 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 50587 0/0/0 (33)
`....).@.)g..............)g......x..8.r..5...)AC.............live.github.com.....
13:26:07.265595 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 49171+ AAAA? alive.github.com. (34)
`.=$.*.@.)g......x..8.r..)g................5.*)..............alive.github.com.....
13:26:07.266185 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 49171 1/0/0 CNAME live.github.com. (63)
`....G.@.)g..............)g......x..8.r..5...GAa.............alive.github.com..................live.github.com.
13:26:07.267576 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 18290+ AAAA? alive.github.com. (34)
`.o..*.@.)g......x..8.r..)g................5.*..Gr...........alive.github.com.....
13:26:07.268766 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 18290 1/0/0 CNAME live.github.com. (63)
`....G.@.)g..............)g......x..8.r..5...GAaGr...........alive.github.com..................live.github.com.
13:26:10.058460 IP 192.168.14.146.63459 > OpenWrt.lan.53: 41247+ HTTPS? mobile.events.data.microsoft.com. (50)
E..Nx.....$!...........5.:.u.............mobile.events.data     microsoft.com..A..
13:26:10.058833 IP 192.168.14.146.56453 > OpenWrt.lan.53: 58915+ A? mobile.events.data.microsoft.com. (50)
E..Nx.....$ ...........5.:_..#...........mobile.events.data     microsoft.com.....
13:26:10.077738 IP OpenWrt.lan.53 > 192.168.14.146.63459: 41247 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus73.eastus.cloudapp.azure.com. (215)
E....N@.@............5...................mobile.events.data     microsoft.com..A...........o.'.mobile.events.data.trafficmanager.net..>.......5.).onedscolprdeus73.eastus.cloudapp.azure.).........5.1.ns1-201  azure-dns.).msnhst....'........,.       :....<
13:26:10.078865 IP OpenWrt.lan.53 > 192.168.14.146.56453: 58915 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdeus73.eastus.cloudapp.azure.com., A 74.151.238.97 (170)
E....O@.@............5.......#...........mobile.events.data     microsoft.com..............o.'.mobile.events.data.trafficmanager.net..>.......5.).onedscolprdeus73.eastus.cloudapp.azure.).q..........J..a
13:26:12.101738 ARP, Request who-has 192.168.14.146 tell OpenWrt.lan, length 28
...........R.h..............
13:26:12.103083 ARP, Reply 192.168.14.146 is-at 58:96:1d:17:81:fd (oui Unknown), length 28
........X............R.h....
13:26:12.402366 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 63598+ A? www.youtube.com. (33)
`.=$.).@.)g......x..8.r..)g................5.)...n...........www.youtube.com.....
13:26:12.402650 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 2121+ AAAA? www.youtube.com. (33)
`.o..).@.)g......x..8.r..)g................5.)nq.I...........www.youtube.com.....
13:26:12.420551 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 63598 8/0/0 A 142.251.155.4, A 142.251.151.4, A 142.251.152.4, A 142.251.156.4, A 142.251.157.4, A 142.251.150.4, A 142.251.154.4, A 142.251.153.4 (161)
`......@.)g..............)g......x..8.r..5....A..n...........www.youtube.com..............|...............|...............|...............|...............|...............|...............|...............|......
13:26:12.421875 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 2121 8/0/0 AAAA 2001:4860:482c:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:4829:400::, AAAA 2001:4860:482d:400::, AAAA 2001:4860:482b:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:4827:400::, AAAA 2001:4860:482a:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#.I...........www.youtube.com..............{.. .H`H,...................{.. .H`H&...................{.. .H`H)...................{.. .H`H-...................{.. .H`H+...................{.. .H`H(...................{.. .H`H'...................{.. .H`H*..........
13:26:12.423250 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 40827+ A? www.youtube.com. (33)
`.=$.).@.)g......x..8.r..)g................5.)...{...........www.youtube.com.....
13:26:12.423888 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 40827 8/0/0 A 142.251.155.4, A 142.251.151.4, A 142.251.152.4, A 142.251.156.4, A 142.251.157.4, A 142.251.150.4, A 142.251.154.4, A 142.251.153.4 (161)
`......@.)g..............)g......x..8.r..5....A..{...........www.youtube.com..............|...............|...............|...............|...............|...............|...............|...............|......
13:26:12.427727 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 8523+ AAAA? www.youtube.com. (33)
`.o..).@.)g......x..8.r..)g................5.)Uo!K...........www.youtube.com.....
13:26:12.428399 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 8523 8/0/0 AAAA 2001:4860:482c:400::, AAAA 2001:4860:4826:400::, AAAA 2001:4860:4829:400::, AAAA 2001:4860:482d:400::, AAAA 2001:4860:482b:400::, AAAA 2001:4860:4828:400::, AAAA 2001:4860:4827:400::, AAAA 2001:4860:482a:400:: (257)
`....   .@.)g..............)g......x..8.r..5... B#!K...........www.youtube.com..............{.. .H`H,...................{.. .H`H&...................{.. .H`H)...................{.. .H`H-...................{.. .H`H+...................{.. .H`H(...................{.. .H`H'...................{.. .H`H*..........
13:26:29.041515 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [F.], seq 32, ack 75, win 4012, length 0
E..($x@.@.xt.........[.../....j.P.......
13:26:29.042609 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [.], ack 33, win 255, length 0
E..(x.@....O...........[..j../..P...sB..
13:26:29.044309 IP 192.168.14.146.56798 > OpenWrt.lan.1883: Flags [F.], seq 75, ack 33, win 255, length 0
E..(x.@....N...........[..j../..P...sA..
13:26:29.044570 IP OpenWrt.lan.1883 > 192.168.14.146.56798: Flags [.], ack 76, win 4012, length 0
E..(..@.@............[.../....j.P...d...
13:26:33.685335 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [S], seq 676411696, win 65535, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
E..4x.@....A...........[(Q90.........W..............
13:26:33.685755 IP OpenWrt.lan.1883 > 192.168.14.146.52984: Flags [S.], seq 3794354574, ack 676411697, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 4], length 0
E..4..@.@............[...)A.(Q91.....
..............
13:26:33.686809 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [.], ack 1, win 255, length 0
E..(x.@....L...........[(Q91.)A.P....b..
13:26:33.687251 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [P.], seq 1:35, ack 1, win 255, length 34
E..Jx.@....)...........[(Q91.)A.P...Gh... ..MQTT...<........mqttx_a8bbbd1e
13:26:33.687476 IP OpenWrt.lan.1883 > 192.168.14.146.52984: Flags [.], ack 35, win 4013, length 0
E..(.'@.@............[...)A.(Q9SP.......
13:26:33.688346 IP OpenWrt.lan.1883 > 192.168.14.146.52984: Flags [P.], seq 1:12, ack 35, win 4013, length 11
E..3.(@.@............[...)A.(Q9SP....   ..      ...".
!..
13:26:33.692899 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [P.], seq 35:61, ack 12, win 255, length 26
E..Bx.@....0...........[(Q9S.)A.P...ic.........iotiscooltrustme/1.
13:26:33.693490 IP OpenWrt.lan.1883 > 192.168.14.146.52984: Flags [P.], seq 12:18, ack 61, win 4012, length 6
E....)@.@............[...)A.(Q9mP.............
13:26:33.739193 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [.], ack 18, win 255, length 0
E..(x.@....I...........[(Q9m.)A.P.......
13:27:00.644374 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 52169+ A? safebrowsing.googleapis.com. (45)
`.=$.5.@.)g......x..8.r..)g................5.5.G.............safebrowsing
googleapis.com.....
13:27:00.644685 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 26086+ AAAA? safebrowsing.googleapis.com. (45)
`.o..5.@.)g......x..8.r..)g................5.5=.e............safebrowsing
googleapis.com.....
13:27:00.660437 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 52169 1/0/0 A 142.251.110.95 (61)
`....E.@.)g..............)g......x..8.r..5...EA_.............safebrowsing
googleapis.com...................n_
13:27:00.661639 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 26086 1/0/0 AAAA 2a00:1450:4001:c1f::5f (73)
`....Q.@.)g..............)g......x..8.r..5...QAke............safebrowsing
googleapis.com.................*..P@.........._
13:27:00.665976 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 37041+ A? safebrowsing.googleapis.com. (45)
`.=$.5.@.)g......x..8.r..)g................5.5;_.............safebrowsing
googleapis.com.....
13:27:00.666728 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 37041 1/0/0 A 142.251.110.95 (61)
`....E.@.)g..............)g......x..8.r..5...EA_.............safebrowsing
googleapis.com...................n_
13:27:00.669209 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 56786+ AAAA? safebrowsing.googleapis.com. (45)
`.o..5.@.)g......x..8.r..)g................5.5...............safebrowsing
googleapis.com.....
13:27:00.669808 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 56786 1/0/0 AAAA 2a00:1450:4001:c1f::5f (73)
`....Q.@.)g..............)g......x..8.r..5...QAk.............safebrowsing
googleapis.com.................*..P@.........._
13:27:34.677027 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [P.], seq 61:63, ack 18, win 255, length 2
E..*x.@....E...........[(Q9m.)A.P....
....
13:27:34.677530 IP OpenWrt.lan.1883 > 192.168.14.146.52984: Flags [P.], seq 18:20, ack 63, win 4012, length 2
E..*.*@.@............[...)A.(Q9oP.........
13:27:34.723784 IP 192.168.14.146.52984 > OpenWrt.lan.1883: Flags [.], ack 20, win 255, length 0
E..(x.@....F...........[(Q9o.)A.P.......
13:27:41.088462 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 38297+ A? ublockorigin.pages.dev. (40)
`.=$.0.@.)g......x..8.r..)g................5.0.J.............ublockorigin.pages.dev.....
13:27:41.088771 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 45417+ AAAA? ublockorigin.pages.dev. (40)
`.o..0.@.)g......x..8.r..)g................5.0f..i...........ublockorigin.pages.dev.....
13:27:41.104764 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 38297 2/0/0 A 188.114.97.4, A 188.114.96.4 (72)
`....P.@.)g..............)g......x..8.r..5...PAj.............ublockorigin.pages.dev..................ra..............r`.
13:27:41.106117 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 45417 2/0/0 AAAA 2a06:98c1:3120::4, AAAA 2a06:98c1:3121::4 (96)
`....h.@.)g..............)g......x..8.r..5...hA..i...........ublockorigin.pages.dev.................*...1 ......................*...1!..........
13:27:41.108230 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 33131+ A? ublockorigin.pages.dev. (40)
`.=$.0.@.)g......x..8.r..)g................5.0.x.k...........ublockorigin.pages.dev.....
13:27:41.108821 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 33131 2/0/0 A 188.114.97.4, A 188.114.96.4 (72)
`....P.@.)g..............)g......x..8.r..5...PAj.k...........ublockorigin.pages.dev..................ra..............r`.
13:27:41.110040 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 28311+ AAAA? ublockorigin.pages.dev. (40)
`.o..0.@.)g......x..8.r..)g................5.0..n............ublockorigin.pages.dev.....
13:27:41.110670 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 28311 2/0/0 AAAA 2a06:98c1:3120::4, AAAA 2a06:98c1:3121::4 (96)
`....h.@.)g..............)g......x..8.r..5...hA.n............ublockorigin.pages.dev.................*...1 ......................*...1!..........
13:27:55.981645 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 29113+ A? cc-api-data.adobe.io. (38)
`.=$...@.)g......x..8.r..)g................5...[q............cc-api-data.adobe.io.....
13:27:55.981991 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 64174+ AAAA? cc-api-data.adobe.io. (38)
`.o....@.)g......x..8.r..)g................5.................cc-api-data.adobe.io.....
13:27:55.998618 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 29113 6/0/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com., A 52.212.178.60, A 52.48.202.212, A 52.31.167.175 (263)
`......@.)g..............)g......x..8.r..5....B)q............cc-api-data.adobe.io..................cc-api-data-ew1...2.........2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb eu-west-1        amazonaws.com.............4..<............40..............4...
13:27:55.999596 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 64174 3/1/0 CNAME cc-api-data-ew1.adobe.io., CNAME ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net., CNAME dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb.eu-west-1.amazonaws.com. (299)
`....3.@.)g..............)g......x..8.r..5...3BM.............cc-api-data.adobe.io..................cc-api-data-ew1...2.........2.ethos.dunamis.ethos502-prod-irl1.ethos.adobe.net..P.........I+dunamis-ethos502-prod-irl1-1c6eda20abd94916.elb eu-west-1        amazonaws.com............H.ns-1566      awsdns-03.co.uk..awsdns-hostmaster.amazon......... ......u....<
13:28:09.453129 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.54950 > OpenWrt.lan.53: 40577+ HTTPS? update.code.visualstudio.com. (46)
`..v.6.@.)g......x..8.r..)g................5.6...............update.code.visualstudio.com..A..
13:28:09.453508 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.63511 > OpenWrt.lan.53: 17212+ A? update.code.visualstudio.com. (46)
`....6.@.)g......x..8.r..)g................5.6..C<...........update.code.visualstudio.com.....
13:28:09.469630 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.54950: 40577 2/1/0 CNAME vscode-update-g6gcb6ggdthkctd9.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net. (202)
`.!....@.)g..............)g......x..8.r..5....A..............update.code.visualstudio.com..A.............0.vscode-update-g6gcb6ggdthkctd9.z01.azurefd.net..:.......$...mr-z01
tm-azurefd.e.}.......!.4.tm1.dns-tm.%.msnhst    microsoft.%xa'..........$.....<
13:28:09.470983 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.63511: 17212 3/0/0 CNAME vscode-update-g6gcb6ggdthkctd9.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net., A 150.171.109.99 (154)
`......@.)g..............)g......x..8.r..5....A.C<...........update.code.visualstudio.com................0.vscode-update-g6gcb6ggdthkctd9.z01.azurefd.net..:.......$...mr-z01
tm-azurefd.e.v............mc
13:28:13.202829 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.65389 > OpenWrt.lan.53: 64116+ HTTPS? main.vscode-cdn.net. (37)
`.%..-.@.)g......x..8.r..)g..............m.5.-t..t...........main
vscode-cdn.net..A..
13:28:13.205719 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.65002 > OpenWrt.lan.53: 18342+ A? main.vscode-cdn.net. (37)
`.U}.-.@.)g......x..8.r..)g................5.-h.G............main
vscode-cdn.net.....
13:28:13.219466 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.65389: 64116 2/1/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net. (173)
`......@.)g..............)g......x..8.r..5.m..A..t...........main
vscode-cdn.net..A..............
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...].........7.tm1.dns-tm.com..msnhst microsoft..xa'..........$.....<
13:28:13.221474 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.65002: 18342 3/0/0 CNAME vscode-cdn.z01.azurefd.net., CNAME mr-z01.tm-azurefd.net., A 150.171.109.98 (122)
`......@.)g..............)g......x..8.r..5....A.G............main
vscode-cdn.net.................
vscode-cdn.z01.azurefd...1...........mr-z01
tm-azurefd...V.......   ....mb
13:28:15.284056 IP 192.168.14.146.55904 > OpenWrt.lan.53: 30394+ HTTPS? default.exp-tas.com. (37)
E..Ax.....#..........`.5.-..v............default.exp-tas.com..A..
13:28:15.284421 IP 192.168.14.146.51786 > OpenWrt.lan.53: 11896+ A? default.exp-tas.com. (37)
E..Ax.....#..........J.5.-.u.x...........default.exp-tas.com.....
13:28:15.284693 IP 192.168.14.146.62541 > OpenWrt.lan.53: 57042+ HTTPS? exp.individual.githubcopilot.com. (50)
E..Nx.....#..........M.5.:.!.............exp
individual.githubcopilot.com..A..
13:28:15.284695 IP 192.168.14.146.61206 > OpenWrt.lan.53: 15052+ A? exp.individual.githubcopilot.com. (50)
E..Nx.....#............5.:..:............exp
individual.githubcopilot.com.....
13:28:15.290179 IP OpenWrt.lan.53 > 192.168.14.146.62541: 57042 1/1/0 CNAME exp-tas.githubcopilot.com. (156)
E....>@.@............5.M.................exp
individual.githubcopilot.com..A...........j.
.exp-tas.............H.ns-1727  awsdns-23.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:28:15.302217 IP OpenWrt.lan.53 > 192.168.14.146.55904: 30394 1/1/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net. (146)
E....@@.@............5.`....v............default.exp-tas.com..A.............(.deault-exp-tas-com.e-0014.e-msedge.net..K.........-.ns1.K.msnhst  microsoft..x*0Q.........$......
13:28:15.303351 IP OpenWrt.lan.53 > 192.168.14.146.61206: 15052 2/0/0 CNAME exp-tas.githubcopilot.com., A 4.225.11.192 (88)
E..t.A@.@..S.........5...`.U:............exp
individual.githubcopilot.com..............i.
.exp-tas...>......./......
13:28:15.309957 IP 192.168.14.146.52395 > OpenWrt.lan.53: 32192+ A? default.exp-tas.com. (37)
E..Ax.....#............5.-W.}............default.exp-tas.com.....
13:28:15.316903 IP OpenWrt.lan.53 > 192.168.14.146.51786: 11896 3/0/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-msedge.net., A 13.107.5.93 (119)
E....B@.@..3.........5.J...t.x...........default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........D.D...........k.]
13:28:15.317446 IP OpenWrt.lan.53 > 192.168.14.146.52395: 32192 3/0/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-msedge.net., A 13.107.5.93 (119)
E....C@.@..2.........5.....t}............default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........D.D...........k.]
13:28:16.728002 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 44418+ A? default.exp-tas.com. (37)
`.=$.-.@.)g......x..8.r..)g................5.-p..............default.exp-tas.com.....
13:28:16.728661 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 44418 3/0/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-msedge.net., A 13.107.5.93 (138)
`......@.)g..............)g......x..8.r..5....A..............default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........e-0014.e-msedge.net..e...........k.]
13:28:16.729191 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60954 > OpenWrt.lan.53: 17632+ AAAA? default.exp-tas.com. (37)
`.o..-.@.)g......x..8.r..)g................5.-..D............default.exp-tas.com.....
13:28:16.735527 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 3449+ A? exp.individual.githubcopilot.com. (50)
`.=$.:.@.)g......x..8.r..)g................5.:P7.y...........exp
individual.githubcopilot.com.....
13:28:16.735819 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.62489 > OpenWrt.lan.53: 27391+ AAAA? exp.individual.githubcopilot.com. (50)
`....:.@.)g......x..8.r..)g................5.:.(j............exp
individual.githubcopilot.com.....
13:28:16.736443 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 3449 2/0/0 CNAME exp-tas.githubcopilot.com., A 4.225.11.192 (105)
`....q.@.)g..............)g......x..8.r..5...qA..y...........exp
individual.githubcopilot.com..............h...exp-tas.githubcopilot.com..>..............
13:28:16.739463 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.62489: 27391 1/1/0 CNAME exp-tas.githubcopilot.com. (156)
`.5o...@.)g..............)g......x..8.r..5....A.j............exp
individual.githubcopilot.com..............h.
.exp-tas.............H.ns-1727  awsdns-23.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:28:16.754997 IP 192.168.14.146.60954 > OpenWrt.lan.53: 17632+ AAAA? default.exp-tas.com. (37)
E..Ax.....#............5.-T=D............default.exp-tas.com.....
13:28:16.763683 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60954: 17632 2/1/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-dc-msedge.net. (179)
`......@.)g..............)g......x..8.r..5....A.D............default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........e-0014.e-dc-msedge.T.l.........-.ns1.l.msnhst     microsoft..x+.Y.........$......
13:28:16.764207 IP OpenWrt.lan.53 > 192.168.14.146.60954: 17632 2/1/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-dc-msedge.net. (179)
E.....@.@..q.........5......D............default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........e-0014.e-dc-msedge.T.l.........-.ns1.l.msnhst microsoft..x+.Y.........$......
13:28:17.025222 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57594 > OpenWrt.lan.53: 61097+ HTTPS? default.exp-tas.com. (37)
`..~.-.@.)g......x..8.r..)g................5.-.n.............default.exp-tas.com..A..
13:28:17.025599 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.55388 > OpenWrt.lan.53: 25879+ A? default.exp-tas.com. (37)
`....-.@.)g......x..8.r..)g..............\.5.-..e............default.exp-tas.com.....
13:28:17.025872 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.60996 > OpenWrt.lan.53: 4479+ HTTPS? exp.individual.githubcopilot.com. (50)
`..?.:.@.)g......x..8.r..)g..............D.5.:>Y.............exp
individual.githubcopilot.com..A..
13:28:17.026129 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.61797 > OpenWrt.lan.53: 59480+ A? exp.individual.githubcopilot.com. (50)
`
_..:.@.)g......x..8.r..)g..............e.5.:d..X...........exp
individual.githubcopilot.com.....
13:28:17.029304 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57594: 61097 1/1/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net. (146)
`.G....@.)g..............)g......x..8.r..5....A..............default.exp-tas.com..A.............(.deault-exp-tas-com.e-0014.e-msedge.net..K.........-.ns1.K.msnhst      microsoft..x*0Q.........$......
13:28:17.030624 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.55388: 25879 3/0/0 CNAME deault-exp-tas-com.e-0014.e-msedge.net., CNAME e-0014.e-msedge.net., A 13.107.5.93 (119)
`..t...@.)g..............)g......x..8.r..5.\..A.e............default.exp-tas.com................(.deault-exp-tas-com.e-0014.e-msedge.net..1...........D.D...........k.]
13:28:17.034538 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.60996: 4479 1/1/0 CNAME exp-tas.githubcopilot.com. (156)
`..z...@.)g..............)g......x..8.r..5.D..A..............exp
individual.githubcopilot.com..A...........h.
.exp-tas.............H.ns-1727  awsdns-23.co.uk..awsdns-hostmaster.amazon.)....... ......u...Q.
13:28:17.035675 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.61797: 59480 2/0/0 CNAME exp-tas.githubcopilot.com., A 4.225.11.192 (88)
`..d.`.@.)g..............)g......x..8.r..5.e.`Az.X...........exp
individual.githubcopilot.com..............g.
.exp-tas...>.......-......
13:28:17.489088 IP 192.168.14.146.60269 > OpenWrt.lan.53: 9476+ HTTPS? mobile.events.data.microsoft.com. (50)
E..Nx.....#..........m.5.:..%............mobile.events.data     microsoft.com..A..
13:28:17.489473 IP 192.168.14.146.59754 > OpenWrt.lan.53: 61451+ A? mobile.events.data.microsoft.com. (50)
E..Nx.....#..........j.5.:HB.............mobile.events.data     microsoft.com.....
13:28:17.508886 IP OpenWrt.lan.53 > 192.168.14.146.60269: 9476 2/1/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus71.centralus.cloudapp.azure.com. (218)
E.....@.@..:.........5.m....%............mobile.events.data     microsoft.com..A...........`.'.mobile.events.data.trafficmanager.net..>.......&.,.onedscolprdcus71      centralus.cloudapp.azure.).........&.1.ns1-201  azure-dns.).msnhst....'........,.       :....<
13:28:17.510244 IP OpenWrt.lan.53 > 192.168.14.146.59754: 61451 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus71.centralus.cloudapp.azure.com., A 4.150.223.97 (173)
E.....@.@..f.........5.j.................mobile.events.data     microsoft.com..............`.'.mobile.events.data.trafficmanager.net..>.......&.,.onedscolprdcus71      centralus.cloudapp.azure.).q.............a
13:28:18.926472 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.57516 > OpenWrt.lan.53: 49232+ A? mobile.events.data.microsoft.com. (50)
`.=$.:.@.)g......x..8.r..)g................5.:...P...........mobile.events.data microsoft.com.....
13:28:18.926775 IP6 fd29:67cc:bbf:0:9978:1afa:3891:7299.62489 > OpenWrt.lan.53: 24399+ AAAA? mobile.events.data.microsoft.com. (50)
`....:.@.)g......x..8.r..)g................5.:+._O...........mobile.events.data microsoft.com.....
13:28:18.927471 IP6 OpenWrt.lan.53 > fd29:67cc:bbf:0:9978:1afa:3891:7299.57516: 49232 3/0/0 CNAME mobile.events.data.trafficmanager.net., CNAME onedscolprdcus71.centralus.cloudapp.azure.com., A 4.150.223.97 (176)
`......@.)g..............)g......x..8.r..5....A..P...........mobile.events.data microsoft.com.............._.'.mobile.events.data.trafficmanager.net..>.......%./.onedscolprdcus71      centralus.cloudapp.azure.com..q.............a
13:28:18.943761 63:6f:75:6e:74:73 (oui Unknown) > 00:00:00:08:61:63 (oui Ethernet), ethertype Unknown (0x0667), length 280:
        0x0000:  6f6f 676c 6503 636f 6d00 001c 0001 f9e9  oogle.com.......
        0x0010:  fe6a b57d 0900 7300 0000 7300 0000 5896  .j.}..s...s...X.
        0x0020:  1d17 81fd d40d ab52 a568 86dd 6006 0489  .......R.h..`...
        0x0030:  003d 1140 fd29 67cc 0bbf 0000 0000 0000  .=.@.)g.........
        0x0040:  0000 0001 fd29 67cc 0bbf 0000 9978 1afa  .....)g......x..
        0x0050:  3891 7299 0035 e0ac 003d 4157 45d5 8180  8.r..5...=AWE...
        0x0060:  0001 0001 0000 0000 0861 6363 6f75 6e74  .........account
        0x0070:  7306 676f 6f67 6c65 0363 6f6d 0000 0100  s.google.com....
        0x0080:  01c0 0c00 0100 0100 0000 2100 048e fb7f  ..........!.....
        0x0090:  54f9 e9fe 6a81 8309 007f 0000 007f 0000  T...j...........
        0x00a0:  0058 961d 1781 fdd4 0dab 52a5 6886 dd60  .X........R.h..`
        0x00b0:  0c9c 8d00 4911 40fd 2967 cc0b bf00 0000  ....I.@.)g......
        0x00c0:  0000 0000 0000 01fd 2967 cc0b bf00 0099  ........)g......
        0x00d0:  781a fa38 9172 9900 35ee 1a00 4941 635d  x..8.r..5...IAc]
        0x00e0:  3181 8000 0100 0100 0000 0008 6163 636f  1...........acco
        0x00f0:  756e 7473 0667 6f6f 676c 6503 636f 6d00  unts.google.com.
        0x0100:  001c 0001 c00c 001c 0001                 ..........
oogle.com........j.}    .s...s...X........R.h..`....=.@.)g..............)g......x..8.r..5...=AWE............accounts.google.com..............!.....T...j..      .........X........R.h..`....I.@.)g..............)g......x..8.r..5...IAc]1...........accounts.google.com...........
tcpdump: pcap_loop: invalid packet capture length 20992020, bigger than snaplen of 262144
root@OpenWrt:~#