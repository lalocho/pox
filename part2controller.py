from pox import *
#import pox.openflow.libopenflow_01 as of
#import pox.lib.packet as pkt

#log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    #add switch rules here
    addFlowRule(self,pkt.ipv4.ICMP_PROTOCOL,pkt.ethernet.IP_TYPE)
    addFLowRUle(self.pkt.arp.REQUEST,pkt.ethernet.ARP_TYPE)
    addFLowRUle(self.pkt.arp.REPLY,pkt.ethernet.ARP_TYPE)
    addFLowRUle(self.pkt.arp.REV_REQUEST,pkt.ethernet.ARP_TYPE)
    addFLowRUle(self.pkt.arp.REV_REPLY,pkt.ethernet.ARP_TYPE)
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priorty = 1
    self.connection.send(msg)

  def addFlowRule(self, nw_proto,dl_type):
        msg = of.ofp_flow_mod()
        match = of.ofp_match()
        match.nw_src = None
        match.nw_dst = None
        match.tp_src = None
        match.tp_dst = None
        match.nw_proto = nw_proto # 1 for ICMP or ARP opcode
        match.dl_type = dl_type # == 0x0800 for IP, 0x0806 for ARP
        msg.match = match
        msg.hard_timeout = 0
        msg.soft_timeout = 0
        msg.priority = 32768
        action = of.ofp_action_output(port = of.OFPP_NORMAL)
        msg.actions.append(action)
        self.connection.send(msg)
    
  def _handle_PacketIn (self, event):
    """
    Packets not handled by the router rules will be
    forwarded to this method to be handled by the controller
    """
   

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return
    """if packet.type == packet.ARP_TYPE:
    elif packet = packet.IP_TYPE:
        ippacket  = packet.payload
        if ippacket.protocol == packet.ICMP_PROTOCOL:
            icmpPacket = ippacket.payload
    packet_in = event.ofp # The actual ofp_packet_in message.
    print ("Unhandled packet :" + str(packet.dump()))"""

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
