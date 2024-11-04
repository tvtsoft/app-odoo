# -*- coding: utf-8 -*-

# Copyright (C) 2008-2008 凯源吕鑫 lvxin@gmail.com   <basic chart data>
#                         维智众源 oldrev@gmail.com  <states data>
# Copyright (C) 2012-2012 南京盈通 ccdos@intoerp.com <small business chart>
# Copyright (C) 2008-now  开阖软件 jeff@osbzr.com    < PM and LTS >
# Copyright (C) 2017-now  jeffery9@gmail.com
# Copyright (C) 2018-now  欧度智能 https://www.odooai.cn

{
    'name': '2025最新中国会计科目表.企业标准会计.Latest Chinese Accounting for odoo18',
    'version': '24.11.04',
    'author': 'odooai.cn',
    'category': 'Accounting/Localizations/Account Charts',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': """    
    Multi level account chart. Chinese enhance. Focus on account chart.
    Add account chart group data. Account group, Chinese tax.
    Set chinese account report. 
    """,
    'description': """
    最新中国化财务，主要针对标准会计科目表作了优化。
    1. 2025最新会计科目表，处理营改增后会计科目调整。odoo 18专用。
    2. 超级管理员自动开启全部会计功能，可管理会计科目表等。
    3. 增强对生产企业会计科目的支持，增加数据资产入表支持。
    4. 将菜单中设置为"财务"。
    5. 补充分类及标签信息。
    6. 更多的税项处理，处理营改增，更新至最新税率。
    7. 会计科目表增加上下级支持，增加树状结构，支持多级科目，配合 "app_web_superbar" 使用可轻易实现树状导航。
    8. 使用金蝶的会计科目命名法对多级科目进行初始化。可自行调整为用友科目命名法
    9. 增加中文数字和阿拉伯数字的转换(可安装cn2an库，pip3 install cn2an)
    10. 注意，建议在没有业务数据，没有会计科目的初始环境。可以使用 "app_odoo_customize" 模块清除财务数据，重置会计科目。

    中国财务，中国会计，中国城市
    欧度智能，odooai.cn
    The Latest Chinese Account
    Including the following data in the Accounting Standards for Business Enterprises
    包含企业会计准则以下数据
    * Chart of Accounts
    * 中国会计科目表模板
    * Tax templates
    * 税金模板
    """,
    'depends': [
        'account',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'security/res_groups.xml',
        'views/account_account_views.xml',
        'views/account_views.xml',
        'data/account_account_tag_data.xml',
        'report/account_report.xml',
        'report/report_voucher.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'external_dependencies': {
    #     'python': ['cn2an']
    # },
}
