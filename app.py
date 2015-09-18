#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import sqlite3
from flask import Flask, render_template, g, request
import sql_queries
from functions import get_css_framework, show_single_page_or_not, get_page_items, get_pagination, get_link_size

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

# Specify location of Spiceworks Database
DATABASE = 'PATH TO DATABASE HERE'

@app.before_request
def before_request():
	g.conn = sqlite3.connect(DATABASE)
	g.conn.row_factory = sqlite3.Row
	g.cur = g.conn.cursor()

@app.teardown_request
def teardown(error):
	if hasattr(g, 'conn'):
		g.conn.close()

@app.route('/')
def home():

	repairs_sql = g.cur.execute(sql_queries.get_top10_repairs)
	repairs = g.cur.fetchall()

	loans_sql = g.cur.execute(sql_queries.get_top10_loans)
	loans = g.cur.fetchall()

	misc_sql = g.cur.execute(sql_queries.get_top10_misc)
	misc = g.cur.fetchall()


	return render_template('dashboard.html',
	 repairs=repairs,
	 loans=loans,
	 misc_tickets=misc,
	)

@app.route('/all_tickets')
def all_tickets():
	g.cur.execute(sql_queries.all_tickets_count)
	total = g.cur.fetchone()[0]
	page, per_page, offset = get_page_items()

	sql = sql_queries.get_all_tickets.format(offset, per_page)
	g.cur.execute(sql)

	tickets = g.cur.fetchall()

	pagination = get_pagination(page=page,
								per_page=per_page,
								total=total,
								record_name='tickets',
								format_total=True,
								format_number=True,
								)
	return render_template('tickets_list.html', tickets=tickets,
							page=page,
							per_page=per_page,
							pagination=pagination,
							page_title='All Tickets',
							)

@app.route('/repairs')
def repairs():
	g.cur.execute(sql_queries.all_repairs_count)
	total = g.cur.fetchone()[0]
	page, per_page, offset = get_page_items()

	sql = sql_queries.get_repairs_tickets.format(offset, per_page)
	g.cur.execute(sql)

	tickets = g.cur.fetchall()

	pagination = get_pagination(page=page,
								per_page=per_page,
								total=total,
								record_name='tickets',
								format_total=True,
								format_number=True,
								)
	return render_template('tickets_list.html', tickets=tickets,
							page=page,
							per_page=per_page,
							pagination=pagination,
							page_title='Repairs',
							)

@app.route('/loans')
def loans():
	sql = sql_queries.all_loans_count
	g.cur.execute(sql)
	total = g.cur.fetchone()[0]
	page, per_page, offset = get_page_items()

	sql = sql_queries.get_loans_tickets.format(offset, per_page)
	g.cur.execute(sql)

	tickets = g.cur.fetchall()

	pagination = get_pagination(page=page,
								per_page=per_page,
								total=total,
								record_name='tickets',
								format_total=True,
								format_number=True,
								)
	return render_template('tickets_list.html', tickets=tickets,
							page=page,
							per_page=per_page,
							pagination=pagination,
							page_title='Loans',
							)

@app.route('/misc')
def misc():
	g.cur.execute(sql_queries.all_misc_count)
	total = g.cur.fetchone()[0]
	page, per_page, offset = get_page_items()

	sql = sql_queries.get_misc_tickets.format(offset, per_page)
	g.cur.execute(sql)

	tickets = g.cur.fetchall()

	pagination = get_pagination(page=page,
								per_page=per_page,
								total=total,
								record_name='tickets',
								format_total=True,
								format_number=True,
								)
	return render_template('tickets_list.html', tickets=tickets,
							page=page,
							per_page=per_page,
							pagination=pagination,
							page_title='Misc',
							)

@app.route('/ticket/<int:ticket_id>')
def show_ticket(ticket_id):

	sql = sql_queries.get_ticket.format(ticket_id)
	g.cur.execute(sql)

	ticket = g.cur.fetchone()
	return render_template('ticket_detail.html', ticket=ticket)

if __name__ == '__main__':
	app.run()