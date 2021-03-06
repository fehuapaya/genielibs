'''NXOS implementation for Switchover triggers'''

# import python
import logging

# import pyats
from pyats import aetest
from pyats.utils.objects import R

# Genie Libs
from genie.libs.sdk.libs.utils.mapping import Mapping
from genie.libs.sdk.triggers.ha.ha import \
                       TriggerSwitchover as CommonSwitchover

log = logging.getLogger(__name__)

# Trigger required data settings
# Which key to exclude for Platform Ops comparison
platform_exclude = ['maker', 'disk_used_space','disk_total_space',
                    'rp_uptime', 'sn', 'disk_free_space',
                    'image', 'kickstart_image', 'issu']


class TriggerSwitchover(CommonSwitchover):
    """Do switchover on device."""
    
    __description__ = """Do switchover on device.

    trigger_datafile:
        Mandatory:
            timeout: 
                max_time (`int`): Maximum wait time for the trigger,
                                in second. Default: 180
                interval (`int`): Wait time between iteration when looping is needed,
                                in second. Default: 15
        Optional:
            tgn_timeout (`int`): Maximum wait time for all traffic threads to be
                                 restored to the reference rate,
                                 in second. Default: 60
            tgn_delay (`int`): Wait time between each poll to verify if traffic is resumed,
                               in second. Default: 10
            static:
                The keys below are dynamically learnt by default.
                However, they can also be set to a custom value when provided in the trigger datafile.

                active_rp: `str`
                standby_rp: `str`
                lc: `str`

                (e.g) interface: '(?P<interface>Ethernet1*)' (Regex supported)
                    OR
                    interface: 'Ethernet1/1/1' (Specific value)
    steps:
        1. Learn Platform Ops object and store the "active" RP and "standby" RP
           if has any, otherwise, SKIP the trigger
        2. Do switchover by command "system switchover"
        3. Learn Platform Ops again and verify the roles of 
           "active" RP and "standby" RP are swapped,
           and verify left attributes from the ops are the same as the Ops in step 1
        4. Update platform PTS if feature pts is enabled,
           Update global/local veirifications if enabled

    """

    # Mapping of Information between Ops and Conf
    # Also permit to dictates which key to verify
    mapping = Mapping(requirements={'ops.platform.platform.Platform':{
                                        'requirements': [\
                                            ['slot', 'rp', '(?P<active_rp>.*)',
                                              'redundancy_state', 'active'],
                                            ['slot', 'rp', '(?P<active_rp>.*)',
                                              'state', 'active'],
                                            ['slot', 'rp', '(?P<standby_rp>.*)',
                                              'redundancy_state', 'ha-standby'],
                                            ['slot', 'rp', '(?P<standby_rp>.*)',
                                              'state', 'ha-standby'],
                                            ['slot', 'lc', '(?P<lc>.*)',
                                             'state', '(?P<lc_status>ok|active|standby)']
                                          ],
                                        'all_keys': True,
                                        'exclude': platform_exclude}},
                      verify_ops={'ops.platform.platform.Platform':{
                                      'requirements': [\
                                          ['slot', 'rp', '(?P<active_rp>.*)',
                                           'redundancy_state', 'ha-standby'],
                                          ['slot', 'rp', '(?P<active_rp>.*)',
                                           'state', 'ha-standby'],
                                          ['slot', 'rp', '(?P<standby_rp>.*)',
                                           'redundancy_state', 'active'],
                                          ['slot', 'rp', '(?P<standby_rp>.*)',
                                           'state', 'active'],
                                          ['slot', 'lc', '(?P<lc>.*)',
                                           'state', '(ok|active|standby)']],
                                    'exclude': platform_exclude}},
                      num_values={'active_rp':1, 'standby_rp':1})
