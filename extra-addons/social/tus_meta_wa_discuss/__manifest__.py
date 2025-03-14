{
    'name': 'Odoo Meta WhatsApp Discuss | Odoo Whatsapp Bidirectional Integration',
    'version': '1.3.',
    'author': 'TechUltra Solutions Private Limited',
    'category': 'Discuss',
    'live_test_url': 'https://www.techultrasolutions.com/blog/news-2/odoo-whatsapp-integration-a-boon-for-business-communication-25',
    'company': 'TechUltra Solutions Private Limited',
    'website': "https://www.techultrasolutions.com/",
    'price': 89,
    'currency': 'USD',
    'summary': 'whatsapp discuss , Whatsapp bi-directional chat is the whatsapp chat room where user can interact to the customer and bi-directional chat can be done via this module',
    'description': """
        whatsapp chatroom is the functionality where user can use the discuss features of the odoo base to extend that to use the whatsapp communication between the user and customer
    """,
    'depends': ['web', 'tus_meta_whatsapp_base'],
    'data': [
        "data/cron.xml",
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'mail.assets_discuss_public': [
            'tus_meta_wa_discuss/static/src/js/components/*/*.js',
            'tus_meta_wa_discuss/static/src/js/models/*/*.js',
            'tus_meta_wa_discuss/static/src/scss/thread_view_nav.scss',
            'https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js',
            'https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css',
        ],
        'web.assets_backend': [
            ('replace', 'web/static/src/legacy/js/owl_compatibility.js','tus_meta_wa_discuss/static/src/js/owl_compatibility.js'),
            # 'tus_meta_wa_discuss/static/src/js/owl_compatibility.js',
            'tus_meta_wa_discuss/static/src/js/components/*/*.js',
            'tus_meta_wa_discuss/static/src/js/models/*/*.js',
            'tus_meta_wa_discuss/static/src/js/AgentsList.js',
            'tus_meta_wa_discuss/static/src/js/MessagesList.js',
            'tus_meta_wa_discuss/static/src/js/wa_thread_view.js',
            'tus_meta_wa_discuss/static/src/js/action_dialog.js',
            'tus_meta_wa_discuss/static/src/scss/*.scss',
            'https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js',
            'https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css',
            'tus_meta_wa_discuss/static/src/xml/*.xml',
        ],
        # 'web.assets_qweb': [
        # ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/main_screen.gif'],
    # 'post_init_hook': '_set_image_in_company',
}
