/*******************************************************************************
 * @author  Mario Minardi
 * @Email mariominardi96@gmail.com
 * @file  POST_request_sender.m
 * @Type  Matlab
 * @brief TBC
 * @date  08/25/2022 (dd/mm/yy)
 *******************************************************************************/


%MATLAB
function [] = POST_request_sender(topology_from_RYU, link_mapping, lifetime, switches, number_of_VN) 

import matlab.net.http.RequestMessage
topology = topology_from_RYU;

%%% IMPORTANT: the topology only tells the switches connection. Since the traffic starts from host, the last link between 
%source_host-switch and switch-dest_host should be taken into account too.

%We define a vector which counts the number of the available port connected to an host for each switch.
hosts_switch = zeros(switches, 2);

%define POST request parameters
options = weboptions('RequestMethod','post', 'MediaType','application/json');
url = 'http://localhost:8080/stats/flowentry/add';

for j = 1 : switches
   
    %here we define the next available port in the switch, connected to the switch j
    hosts_switch(j,2) = 1;
    
end


number_of_links = length(topology);
      
%here for each traffic requests, the POST requests will be originated

   i = number_of_VN; 
   path = link_mapping;
   expiration = lifetime;
   length_path = length(path);
   %the requests identifier start from 101, so we add the number to 100
   Vlan_id = 100 + i;
   
   %here the first cycle for with the POST request starting from the second
   %switch in the path until the switch before the last one. 
   %the first and last switches are particular cases and are treated
   %separately. 
   
   for j = 2: (length_path - 1)
            switch_before = path(j-1);
            switch_id = path(j);
            switch_after = path(j+1);

            %now the ports has to be found in the topology. 
            for k = 1: number_of_links 
                     
                     if hex2dec(topology(k).src.dpid) == switch_id && hex2dec(topology(k).dst.dpid) == switch_after
                         output_port = hex2dec(topology(k).src.port_no);
                         break
                     end 
                     
            end
            
            for k = 1 : number_of_links 
                
                     if hex2dec(topology(k).src.dpid) == switch_id && hex2dec(topology(k).dst.dpid) == switch_before
                         input_port = hex2dec(topology(k).src.port_no);
                         break
                     end   
                     
            end
            
            %the body of the POST request is created
            body1 = strcat('{"dpid": ', int2str(switch_id),',"hard_timeout": ', int2str(expiration), ',"match":{"in_port": ', int2str(input_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(output_port), ',"type": "OUTPUT"}]}' );
            body2 = strcat('{"dpid": ', int2str(switch_id),',"hard_timeout": ', int2str(expiration), ',"match":{"in_port": ', int2str(output_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(input_port), ',"type": "OUTPUT"}]}' );

            %the POST request is sent
            webwrite(url, body1, options);
            webwrite(url, body2, options);
    
   end
   
   %now the special cases described above are treated
   %here the link between the first and second switch is instantiated
      switch_initial = path(1);
      switch_after = path(2);  

      for k = 1: number_of_links 
                     
            if hex2dec(topology(k).src.dpid) == switch_initial && hex2dec(topology(k).dst.dpid) == switch_after
                        
                 output_port = hex2dec(topology(k).src.port_no);
                 break
                 
            end
      end 
      
    %now the input port, for the moment we can assume that it is defined automatically depending on the number of hosts present
    %find the available port which connect the host source to the first switch 
      available_port = hosts_switch(switch_initial,2);
      hosts_switch(switch_initial,2) = hosts_switch(switch_initial,2) + 1;
      input_port = available_port;   
    
    %create and send the POST request to forward the traffic from the first switch to the second one.    
      body1 = strcat('{"dpid": ', int2str(switch_initial),',"hard_timeout": ', int2str(expiration),',"match":{"in_port": ', int2str(input_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(output_port), ',"type": "OUTPUT"}]}' );
      body2 = strcat('{"dpid": ', int2str(switch_initial),',"hard_timeout": ', int2str(expiration), ',"match":{"in_port": ', int2str(output_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(input_port), ',"type": "OUTPUT"}]}' );

      webwrite(url, body1, options);
      webwrite(url, body2, options);
   
   
   %this is the second special case, the one at the end of the path, which
   %works similar to the case just explained. 
      switch_initial = path(length_path -1);
      switch_after = path(length_path);  

      for k = 1 : number_of_links 
                     
            if hex2dec(topology(k).src.dpid) == switch_after && hex2dec(topology(k).dst.dpid) == switch_initial
                        
                 input_port = hex2dec(topology(k).src.port_no);
                 break
            end
      end

      available_port = hosts_switch(switch_after,2);
      hosts_switch(switch_after,2) = hosts_switch(switch_after,2) + 1;

      output_port = available_port;
   
      body1 = strcat('{"dpid": ', int2str(switch_after),',"hard_timeout": ', int2str(expiration), ',"match":{"in_port": ', int2str(input_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(output_port), ',"type": "OUTPUT"}]}' );
      body2 = strcat('{"dpid": ', int2str(switch_after),',"hard_timeout": ', int2str(expiration), ',"match":{"in_port": ', int2str(output_port), ',"dl_vlan":', int2str(Vlan_id), '},"actions":[{"port":', int2str(input_port), ',"type": "OUTPUT"}]}' );
      
      webwrite(url, body1, options);
      webwrite(url, body2, options);
      

end
