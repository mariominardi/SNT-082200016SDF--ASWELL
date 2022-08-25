
%/*******************************************************************************
% * @author  Mario Minardi
% * @Email	mariominardi96@gmail.com
% * @file    GET_request_sender.m
% * @Type	Matlab
% * @brief   TBC
% * @date    08/25/2022 (dd/mm/yy)
% *******************************************************************************/


function [adjacent_matrix, topology_from_RYU] = GET_request_sender() 

import matlab.net.http.RequestMessage
%%%%HTTP GET request to get all the links and the number of SDN-enabled
%%%%switches
r = RequestMessage;
response = send(r, 'http://localhost:8080/v1.0/topology/links');
response1 = send(r, 'http://localhost:8080/v1.0/topology/switches');

switches = response1.Body.Data;
topology = response.Body.Data;

number_of_links = length(topology);

%initialize the adjacency matrix as a squared zero matrix
matrix_sub = zeros(length(switches), length(switches));

for i = 1 : number_of_links
    
  %for each link, obtain the number of switch source and switch destination
  %conversion from hexadecimal is needeed. 
  
       first_switch = hex2dec(topology(i).src.dpid);
       second_switch = hex2dec(topology(i).dst.dpid);
       matrix_sub(first_switch, second_switch) = 1;
    
end

adjacent_matrix = matrix_sub; 
topology_from_RYU = topology;

end