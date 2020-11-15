from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    


    #Used to create flow rules, no specific ports based on protocol and datalink
    def addFlowRule(self, nw_proto,dl_type):
        msg = of.ofp_flow_mod()
        match = of.ofp_match()
        # ICMP or ARP opcodes
        match.nw_proto = nw_proto 
        #  IP or ARP
        match.dl_type = dl_type 
        msg.match = match
        #L2 L3 Switchting output ports
        action = of.ofp_action_output(port = of.OFPP_NORMAL)#
        msg.actions.append(action)

        #sending rule to switch
        self.connection.send(msg)

    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    #add switch rules here
    #adding rules for allowing all arp packets
    addFlowRule(self,pkt.arp.REQUEST,pkt.ethernet.ARP_TYPE)
    addFlowRule(self,pkt.arp.REPLY,pkt.ethernet.ARP_TYPE)


    #adding rule for allowing all icmp packets
    addFlowRule(self,pkt.ipv4.ICMP_PROTOCOL,pkt.ethernet.IP_TYPE)


    #adding rule to drop all other packets
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    msg.match = match
    #lowest priority
    msg.priorty = 1
    #No action so everything else is dropped
    #sending rule to switch
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
   

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
