from flask import request, current_app
from flask.ext.paginate import Pagination

def get_css_framework():
    return current_app.config.get('CSS_FRAMEWORK', 'bootstrap3')

def show_single_page_or_not():
	return current_app.config.get('SHOW_SINGLE_PAGE', False)

def get_link_size():
    return current_app.config.get('LINK_SIZE', 'sm')	

def get_page_items():
	page = int(request.args.get('page', 1))
	per_page = request.args.get('per_page')
	if not per_page:
		per_page = current_app.config.get('PER_PAGE', 10)
	else:
		per_page = int(per_page)

	offset = (page - 1) * per_page
	return page, per_page, offset

def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(css_framework=get_css_framework(),
    				  link_size=get_link_size(),
                      show_single_page=show_single_page_or_not(),
                      **kwargs
                      )