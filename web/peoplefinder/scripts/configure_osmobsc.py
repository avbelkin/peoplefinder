import sys
import socket
import telnetlib


def main(argv=sys.argv):
    try:
        tn = telnetlib.Telnet("localhost", "4242", 5)
        print "Connect to VTY SUCCESS!"
    except socket.error:
        sys.exit("Create VTY connection failed!")

    try:
        tn.read_until("OpenBSC>", 5)
        print "Read VTY welcome message SUCSESS!"
    except socket.error:
        sys.exit("Read VTY wellcome message failed!")

    try:
        tn.write("enable\n")
        tn.read_until("OpenBSC#", 5)
        tn.write("configure terminal\n")
        tn.read_until("OpenBSC(config)#", 5)

        tn.write("mncc-int\n")
        tn.read_until("OpenBSC(config-mncc-int)#", 5)
        tn.write("meas-feed destination 127.0.0.1 8888\n")
        tn.read_until("OpenBSC(config-mncc-int)#", 5)

        tn.write("exit\n")
        tn.read_until("OpenBSC(config)#", 5)

        tn.write("smpp\n")
        tn.read_until("OpenBSC(config-smpp)#", 5)
        # tn.write("no smpp-first\n")
        # tn.read_until("OpenBSC(config-smpp)#", 5)
        tn.write("system-id OSMO-SMPP\n")
        tn.read_until("OpenBSC(config-smpp)#", 5)

        tn.write("esme OSMPP\n")
        tn.read_until("OpenBSC(config-smpp-esme)#", 5)

        tn.write("password antani\n")
        tn.read_until("OpenBSC(config-smpp-esme)#", 5)

        tn.write("default-route\n")
        tn.read_until("OpenBSC(config-smpp-esme)#", 5)
        
        tn.write("exit\n")
        tn.read_until("OpenBSC(config)#",5)
        
        tn.write("network\n")
        tn.read_until("OpenBSC(config-net)#",5)
        
        tn.write("network country code 250\n")
        tn.read_until("OpenBSC(config-net)#",5)
        tn.write("mobile network code 66\n")
        tn.read_until("OpenBSC(config-net)#",5)
        
        tn.write("bts 0\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        
        tn.write("cell reselection hysteresis 14\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        tn.write("cell reselection offset 126\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        tn.write("cell_identity 0\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        tn.write("location_area_code 1\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        tn.write("base_station_id_code 63\n")
        tn.read_until("OpenBSC(config-net-bts)#",5)
        
        tn.write("write file\n")
        tn.read_until("OpenBSC(config-net-bts)#", 5)

        print "Configuration smpp SUCCSESS!"

    except socket.error:
        sys.exit("Configuration OpenBSC FAILED!")


if __name__ == "__main__":
    main()
