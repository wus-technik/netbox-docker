# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }

PLUGINS = [
    'netbox_qrcode',
    'netbox_dns',
    'netbox_documents',
    'netbox_inventory',
    'netbox_topology_views',
    'netbox_floorplan'
]

#'nextbox_ui_plugin',
# 

PLUGINS_CONFIG = {
    'netbox_qrcode': {
        'with_text': True,
        'text_fields': ['name', 'serial'],
        'font': 'ArialMT',
        'font_size': 12, # If the value is 0 or the line does not exist, then the text is automatically adjusted
        'custom_text': 'Property of SomeCompany\ntel.8.800333554-CALL',
        'text_location': 'up',
        'qr_version': 1,
        'qr_error_correction': 0,
        'qr_box_size': 4,
        'qr_border': 4,
        # per object options
        'cable': None,  # disable QR code for Cable object
        'rack': {
            'text_fields': [
                'site',
                'name',
                'facility_id',
                'tenant',
                'cf.cf_name'
            ]
        },
        'device': {
            'qr_box_size': 6,
            'custom_text': None,
        }
    }
}
