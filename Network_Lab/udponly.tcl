#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows (for NAM)
$ns color 1 Blue
$ns color 2 Red

#Open the NAM trace file
set nf [open shagunhbd.nam w]
$ns namtrace-all $nf

set np [open shagunhbd.tr w]
$ns trace-all $np

#Define a 'finish' procedure
proc finish {} {
        global ns nf np
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file        
	exec nam shagunhbd.nam &
        exit 0
}

#Create four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.7Mb 20ms DropTail
$ns duplex-link $n3 $n4 1.7Mb 20ms DropTail
#Set Queue Size of link (n2-n3) to 10
$ns queue-limit $n2 $n3 10
$ns queue-limit $n3 $n4 10

#Give node position (for NAM)
$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right

#Monitor the queue for link (n2-n3). (for NAM)
$ns duplex-link-op $n2 $n3 queuePos 0.5
$ns duplex-link-op $n3 $n4 queuePos 0.5


set udp1 [new Agent/UDP]
$ns attach-agent $n1 $udp1

set udp2 [new Agent/UDP]
$ns attach-agent $n0 $udp2

set null [new Agent/Null]
$ns attach-agent $n4 $null

$ns connect $udp1 $null
$ns connect $udp2 $null

$udp1 set fid_ 1
$udp2 set fid_ 2

#Setup a CBR over UDP connection
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1

set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp2


# setting packet size 
$cbr1 set packet_size_ 1000
$cbr2 set packet_size_ 1000

#setting bit rate
$cbr1 set rate_ 1mb
$cbr2 set rate_ 1mb

# setting random false means no noise
$cbr1 set random_ false
$cbr2 set random_ false


#Schedule events for the CBR agents
$ns at 0.1 "$cbr1 start"
$ns at 1.0 "$cbr2 start"
$ns at 6.0 "$cbr1 stop"
$ns at 6.5 "$cbr2 stop"



#Call the finish procedure after 5 seconds of simulation time
$ns at 7.0 "finish"

#Print CBR packet size and interval
puts "CBR packet size = [$cbr1 set packet_size_]"
puts "CBR interval = [$cbr1 set interval_]"
puts "CBR packet size = [$cbr2 set packet_size_]"
puts "CBR interval = [$cbr2 set interval_]"

#Run the simulation
$ns run



#save this file as filename.tcl
#then open terminal and go to directory where code is saved
#type ns filename.tcl
