from flask import Flask, Blueprint, render_template
from admin.view import *


admin_bp = Blueprint('admin', __name__, url_prefix='/csr/', template_folder='templates', static_folder='static', static_url_path='/static')


admin_bp.add_url_rule('/', 'admin', adminbp)
admin_bp.add_url_rule('/users', 'users', userpage)
admin_bp.add_url_rule('/userlist', 'userlist', userlistbp)
admin_bp.add_url_rule('/brockerlist', 'brockerlist', brockerlistbp)
admin_bp.add_url_rule('/communication', 'communication', commbp)
admin_bp.add_url_rule('/details', 'details', detailspage)
admin_bp.add_url_rule('/parameters', 'parameters', parapage)
admin_bp.add_url_rule('/addproduct', 'addproduct', productpage)
admin_bp.add_url_rule('/product', 'product', productbp)
admin_bp.add_url_rule('/trade', 'trade', tradebp)
admin_bp.add_url_rule('/trade_dashboard', 'trade_dashboard', tdashboardbp)
admin_bp.add_url_rule('/historicalprice', 'historicalprice', historicalpricebp)
admin_bp.add_url_rule('/tradedata', 'tradedata', tradedatabp)
admin_bp.add_url_rule('/ltphistorical', 'ltphistorical', ltphistoricalbp)
admin_bp.add_url_rule('/marketdepth', 'marketdepth', marketdepthbp)
admin_bp.add_url_rule('/finance', 'finance', financebp)
admin_bp.add_url_rule('/userdetails', 'userdetails', usrdetailsbp)
admin_bp.add_url_rule('/editproduct', 'editproduct', editproductbp)
admin_bp.add_url_rule('/ports', 'ports', portsbp)
admin_bp.add_url_rule('/editport', 'editport', editportbp)
admin_bp.add_url_rule('/help&support', 'helpandsupport', helpandsupportbp)