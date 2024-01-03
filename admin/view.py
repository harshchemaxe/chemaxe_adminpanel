from flask import render_template


def adminbp():
	return render_template('dashboard.html')

def userpage():
	return render_template('user.html')

def userlistbp():
	return render_template('userlist.html')

def brockerlistbp():
	return render_template('brockerlist.html')

def commbp():
	return render_template('communication.html')

def detailspage():
	return render_template('companydetail.html')

def parapage():
	return render_template('parameters.html')

def productpage():
	return render_template('addproduct.html')

def productbp():
	return render_template('product.html')

def tradebp():
	return render_template('trade.html')

def tdashboardbp():
	return render_template('trade_dashboard.html')

def historicalpricebp():
	return render_template('historicalprice.html')

def tradedatabp():
	return render_template('tradedata.html')

def ltphistoricalbp():
	return render_template('ltphistorical.html')

def marketdepthbp():
	return render_template('marketdepth.html')

def financebp():
	return render_template('finance.html')

def usrdetailsbp():
	return render_template('user_details.html')

def editproductbp():
	return render_template('edit_product.html')

def portsbp():
	return render_template('ports.html')

def editportbp():
	return render_template('edit_port.html')

def helpandsupportbp():
	return render_template('help_and_support.html')

