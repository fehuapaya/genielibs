''' 
Arp Genie Ops Object Outputs for IOS.
'''


class ArpOutput(object):

	ShowIpArp = {
		'interfaces': {
			'FastEthernet0': {
				'ipv4': {
					'neighbors': {
						'10.1.8.1': {
							'age': '79',
							'ip': '10.1.8.1',
							'link_layer_address': '0012.7f57.ac80',
							'origin': 'dynamic',
							'protocol': 'Internet',
							'type': 'ARPA'},
						'10.1.8.146': {
							'age': '-',
							'ip': '10.1.8.146',
							'link_layer_address': '843d.c638.b9b7',
							'origin': 'static',
							'protocol': 'Internet',
							'type': 'ARPA'}}}},
			'Port-channel10': {
				'ipv4': {
					'neighbors': {
						'10.9.1.1': {
							'age': '-',
							'ip': '10.9.1.1',
							'link_layer_address': '843d.c638.b9c6',
							'origin': 'static',
							'protocol': 'Internet',
							'type': 'ARPA'}}}},
			'Vlan99': {
				'ipv4': {
					'neighbors': {
						'10.69.1.2': {
							'age': '-',
							'ip': '10.69.1.2',
							'link_layer_address': '843d.c638.b9c1',
							'origin': 'static',
							'protocol': 'Internet',
							'type': 'ARPA'}
					}
				}
			}
		}
	}
	ShowIpArpVrf = {
		'interfaces': {
			'GigabitEthernet2.390': {
				'ipv4': {
					'neighbors': {
						'10.12.90.1': {
							'age': '-',
							'ip': '10.12.90.1',
							'link_layer_address': 'fa16.3e24.787a',
							'origin': 'static',
							'protocol': 'Internet',
							'type': 'ARPA'},
						'10.12.90.2':
							{'age': '139',
							 'ip': '10.12.90.2',
							 'link_layer_address': 'fa16.3e8a.cfeb',
							 'origin': 'dynamic',
							 'protocol': 'Internet',
							 'type': 'ARPA'}
					}
				}
			},
			'GigabitEthernet2.410': {
				'ipv4': {
					'neighbors': {
						'10.12.110.1': {
							'age': '-',
							'ip': '10.12.110.1',
							'link_layer_address': 'fa16.3e24.787a',
							'origin': 'static',
							'protocol': 'Internet',
							'type': 'ARPA'}
					}
				}
			}
		}
	}
	ShowVrf = {
		'vrf': {
			'VRF1': {
				'route_distinguisher': '65000:1',
				'protocols': ['ipv4', 'ipv6'],
				'interfaces': ['GigabitEthernet2.390',
							   'GigabitEthernet2.410'],
			}
		}
	}
	ShowIpArpSummary = {
		'incomp_entries': 0,
		'total_entries': 8}

	ShowIpTraffic = {
		'arp_statistics': {
			'arp_drops_input_full': 0,
			'arp_in_other': 0,
			'arp_in_replies': 25520,
			'arp_in_requests': 26338,
			'arp_in_reverse': 42,
			'arp_out_proxy': 0,
			'arp_out_replies': 1399,
			'arp_out_requests': 123,
			'arp_out_reverse': 0},
		'bgp_statistics': {
			'bgp_received_keepalives': 0,
			'bgp_received_notifications': 0,
			'bgp_received_opens': 0,
			'bgp_received_route_refresh': 0,
			'bgp_received_total': 0,
			'bgp_received_unrecognized': 0,
			'bgp_received_updates': 0,
			'bgp_sent_keepalives': 0,
			'bgp_sent_notifications': 0,
			'bgp_sent_opens': 0,
			'bgp_sent_route_refresh': 0,
			'bgp_sent_total': 0,
			'bgp_sent_updates': 0},
		'eigrp_ipv4_statistics': {
			'eigrp_ipv4_received_total': 0,
			'eigrp_ipv4_sent_total': 0},
		'icmp_statistics': {
			'icmp_received_checksum_errors': 0,
			'icmp_received_echo': 43838,
			'icmp_received_echo_reply': 713,
			'icmp_received_format_errors': 0,
			'icmp_received_info_request': 0,
			'icmp_received_irdp_advertisements': 0,
			'icmp_received_irdp_solicitations': 0,
			'icmp_received_mask_replies': 0,
			'icmp_received_mask_requests': 0,
			'icmp_received_other': 0,
			'icmp_received_parameter': 0,
			'icmp_received_quench': 0,
			'icmp_received_redirects': 0,
			'icmp_received_timestamp': 0,
			'icmp_received_unreachable': 0,
			'icmp_sent_echo': 730,
			'icmp_sent_echo_reply': 43838,
			'icmp_sent_info_reply': 0,
			'icmp_sent_irdp_advertisements': 0,
			'icmp_sent_irdp_solicitations': 0,
			'icmp_sent_mask_replies': 0,
			'icmp_sent_mask_requests': 0,
			'icmp_sent_parameter_problem': 0,
			'icmp_sent_quench': 0,
			'icmp_sent_redirects': 0,
			'icmp_sent_time_exceeded': 0,
			'icmp_sent_timestamp': 0,
			'icmp_sent_unreachable': 4},
		'igmp_statistics': {
			'igmp_checksum_errors': '0/0',
			'igmp_dvmrp': '0/0',
			'igmp_format_errors': '0/0',
			'igmp_host_leaves': '0/0',
			'igmp_host_queries': '0/0',
			'igmp_host_reports': '0/0',
			'igmp_pim': '0/0',
			'igmp_total': '0/0'},
		'ip_statistics': {
			'ip_bcast_received': 653921,
			'ip_bcast_sent': 6,
			'ip_drop_encap_failed': 10,
			'ip_drop_forced_drop': 0,
			'ip_drop_no_adj': 0,
			'ip_drop_no_route': 0,
			'ip_drop_opts_denied': 0,
			'ip_drop_src_ip': 0,
			'ip_drop_unicast_rpf': 0,
			'ip_drop_unresolved': 0,
			'ip_frags_fragmented': 0,
			'ip_frags_no_fragmented': 0,
			'ip_frags_no_reassembled': 0,
			'ip_frags_reassembled': 0,
			'ip_frags_timeouts': 0,
			'ip_mcast_received': 0,
			'ip_mcast_sent': 0,
			'ip_opts_alert': 0,
			'ip_opts_basic_security': 0,
			'ip_opts_cipso': 0,
			'ip_opts_end': 0,
			'ip_opts_extended_security': 0,
			'ip_opts_loose_src_route': 0,
			'ip_opts_nop': 0,
			'ip_opts_other': 0,
			'ip_opts_record_route': 0,
			'ip_opts_strct_src_route': 0,
			'ip_opts_strm_id': 0,
			'ip_opts_timestamp': 0,
			'ip_opts_ump': 0,
			'ip_rcvd_bad_hop': 811,
			'ip_rcvd_bad_optns': 0,
			'ip_rcvd_checksum_errors': 0,
			'ip_rcvd_format_errors': 0,
			'ip_rcvd_local_destination': 843331,
			'ip_rcvd_not_gateway': 6,
			'ip_rcvd_sec_failures': 0,
			'ip_rcvd_total': 844148,
			'ip_rcvd_unknwn_protocol': 0,
			'ip_rcvd_with_optns': 0,
			'ip_sent_forwarded': 0,
			'ip_sent_generated': 212110},
		'ospf_statistics': {
			'ospf_received_checksum_errors': 0,
			'ospf_received_database_desc': 0,
			'ospf_received_hello': 0,
			'ospf_received_link_state_req': 0,
			'ospf_received_lnk_st_acks': 0,
			'ospf_received_lnk_st_updates': 0,
			'ospf_received_total': 0,
			'ospf_sent_database_desc': 0,
			'ospf_sent_hello': 0,
			'ospf_sent_lnk_st_acks': 0,
			'ospf_sent_lnk_st_updates': 0,
			'ospf_sent_total': 0},
		'pimv2_statistics': {
			'pimv2_asserts': '0/0',
			'pimv2_bootstraps': '0/0',
			'pimv2_candidate_rp_advs': '0/0',
			'pimv2_checksum_errors': 0,
			'pimv2_format_errors': 0,
			'pimv2_grafts': '0/0',
			'pimv2_hellos': '0/0',
			'pimv2_join_prunes': '0/0',
			'pimv2_non_rp': 0,
			'pimv2_non_sm_group': 0,
			'pimv2_registers': '0/0',
			'pimv2_registers_stops': '0/0',
			'pimv2_state_refresh': '0/0',
			'pimv2_total': '0/0'},
		'tcp_statistics': {
			'tcp_received_checksum_errors': 0,
			'tcp_received_no_port': 0,
			'tcp_received_total': 116563,
			'tcp_sent_total': 139252},
		'udp_statistics': {
			'udp_received_no_port': 289579,
			'udp_received_total': 682217,
			'udp_received_udp_checksum_errors': 0,
			'udp_sent_fwd_broadcasts': 0,
			'udp_sent_total': 28296}
		}

	ShowIpInterface = {
		"Vlan211": {
			"sevurity_level": "default",
			"ip_route_cache_flags": [
				"CEF",
				"Fast"
			],
			"enabled": True,
			"oper_status": "up",
			"address_determined_by": "configuration file",
			"router_discovery": False,
			"ip_multicast_fast_switching": False,
			"split_horizon": True,
			"bgp_policy_mapping": False,
			"ip_output_packet_accounting": False,
			"mtu": 1500,
			"policy_routing": False,
			"local_proxy_arp": False,
			"proxy_arp": True,
			"network_address_translation": False,
			"ip_cef_switching_turbo_vector": True,
			"icmp": {
				"redirects": "always sent",
				"mask_replies": "never sent",
				"unreachables": "always sent",
			},
			"ipv4": {
				"192.168.76.1/24": {
					"prefix_length": "24",
					"ip": "192.168.76.1",
					"secondary": False,
					"broadcase_address": "255.255.255.255"
				}
			},
			"ip_access_violation_accounting": False,
			"ip_cef_switching": True,
			"unicast_routing_topologies": {
				"topology": {
					"base": {
						"status": "up"
					}
				},
			},
			"ip_null_turbo_vector": True,
			"probe_proxy_name_replies": False,
			"ip_fast_switching": True,
			"ip_multicast_distributed_fast_switching": False,
			"tcp_ip_header_compression": False,
			"rtp_ip_header_compression": False,
			"input_features": ["MCI Check"],
			"directed_broadcast_forwarding": False,
			"ip_flow_switching": False
	   },
	   "GigabitEthernet0/0": {
			"sevurity_level": "default",
			'address_determined_by': 'setup command',
			"ip_route_cache_flags": [
				 "CEF",
				 "Fast"
			],
			"enabled": True,
			"oper_status": "up",
			"router_discovery": False,
			"ip_multicast_fast_switching": False,
			"split_horizon": True,
			"bgp_policy_mapping": False,
			"ip_output_packet_accounting": False,
			"mtu": 1500,
			"policy_routing": False,
			"local_proxy_arp": False,
			"vrf": "Mgmt-vrf",
			"proxy_arp": True,
			"network_address_translation": False,
			"ip_cef_switching_turbo_vector": True,
			"icmp": {
				"redirects": "always sent",
				"mask_replies": "never sent",
				"unreachables": "always sent",
			},
			"ipv4": {
				"10.1.8.134/24": {
					"prefix_length": "24",
					"ip": "10.1.8.134",
					"secondary": False,
					"broadcase_address": "255.255.255.255"
				}
			},
			"ip_access_violation_accounting": False,
			"ip_cef_switching": True,
			"unicast_routing_topologies": {
				"topology": {
					"base": {
						"status": "up"
					}
				},
			},
			"ip_null_turbo_vector": True,
			"probe_proxy_name_replies": False,
			"ip_fast_switching": True,
			"ip_multicast_distributed_fast_switching": False,
			"tcp_ip_header_compression": False,
			"rtp_ip_header_compression": False,
			"input_features": ["MCI Check"],
			"directed_broadcast_forwarding": False,
			"ip_flow_switching": False
	   },
	   "GigabitEthernet2": {
			"enabled": False,
			"oper_status": "down"
	   },
	   "GigabitEthernet1/0/1": {
			"sevurity_level": "default",
			'address_determined_by': 'setup command',
			"ip_route_cache_flags": [
				"CEF",
				"Fast"
			],
			"enabled": False,
			"oper_status": "down",
			"router_discovery": False,
			"ip_multicast_fast_switching": False,
			"split_horizon": True,
			"bgp_policy_mapping": False,
			"ip_output_packet_accounting": False,
			"mtu": 1500,
			"policy_routing": False,
			"local_proxy_arp": False,
			"proxy_arp": True,
			"network_address_translation": False,
			"ip_cef_switching_turbo_vector": True,
			"icmp": {
				"redirects": "always sent",
				"mask_replies": "never sent",
				"unreachables": "always sent",
			},
			"ipv4": {
				"10.1.1.1/24": {
					"prefix_length": "24",
					"ip": "10.1.1.1",
					"secondary": False,
					"broadcase_address": "255.255.255.255"
				},
				"10.2.2.2/24": {
					"prefix_length": "24",
					"ip": "10.2.2.2",
					"secondary": True
				},
			},
			"ip_access_violation_accounting": False,
			"ip_cef_switching": True,
			"unicast_routing_topologies": {
				"topology": {
					"base": {
						"status": "up"
					}
				},
			},
			'wccp': {
				'redirect_outbound': False,
				'redirect_inbound': False,
				'redirect_exclude': False,
			},
			"ip_null_turbo_vector": True,
			"probe_proxy_name_replies": False,
			"ip_fast_switching": True,
			"ip_multicast_distributed_fast_switching": False,
			"tcp_ip_header_compression": False,
			"rtp_ip_header_compression": False,
			"directed_broadcast_forwarding": False,
			"ip_flow_switching": False,
			"input_features": ["MCI Check", "QoS Classification", "QoS Marking"],
		}
	}

	Arp_info = {
		'interfaces': {
			'FastEthernet0': {
				'ipv4': {
					'neighbors': {
						'10.1.8.1': {
							'ip': '10.1.8.1',
                            'link_layer_address': '0012.7f57.ac80',
                            'origin': 'dynamic'},
                     	'10.1.8.146': {
                     		'ip': '10.1.8.146',
	                        'link_layer_address': '843d.c638.b9b7',
	                        'origin': 'static'}
	                }
	            }
	        },
            'GigabitEthernet0/0': {
            	'arp_dynamic_learning': {
            		'local_proxy_enable': False,
                    'proxy_enable': True}
            },
            'GigabitEthernet1/0/1': {
            	'arp_dynamic_learning': {
            		'local_proxy_enable': False,
                    'proxy_enable': True}
            },
            'Port-channel10': {
            	'ipv4': {
            		'neighbors': {
            			'10.9.1.1': {
            				'ip': '10.9.1.1',
                          	'link_layer_address': '843d.c638.b9c6',
                          	'origin': 'static'}
                    }
                }
            },
            'Vlan211': {
            	'arp_dynamic_learning': {
            		'local_proxy_enable': False,
                    'proxy_enable': True}
            },
            'Vlan99': {
            	'ipv4': {
            		'neighbors': {
            			'10.69.1.2': {
            				'ip': '10.69.1.2',
                           	'link_layer_address': '843d.c638.b9c1',
                           	'origin': 'static'}
                    }
                }
            },
			'GigabitEthernet2.390': {
				'ipv4': {
					'neighbors': {
						'10.12.90.1': {
							'ip': '10.12.90.1',
							'link_layer_address': 'fa16.3e24.787a',
							'origin': 'static',
						},
						'10.12.90.2':
							{
								'ip': '10.12.90.2',
								'link_layer_address': 'fa16.3e8a.cfeb',
								'origin': 'dynamic',
							}
					}
				}
			},
			'GigabitEthernet2.410': {
				'ipv4': {
					'neighbors': {
						'10.12.110.1': {
							'ip': '10.12.110.1',
							'link_layer_address': 'fa16.3e24.787a',
							'origin': 'static',
						}
					}
				}
			},
        },
 		'statistics': {'entries_total': 8,
                'in_drops': 0,
                'in_replies_pkts': 25520,
                'in_requests_pkts': 26338,
                'incomplete_total': 0,
                'out_replies_pkts': 1399,
                'out_requests_pkts': 123}
       	}