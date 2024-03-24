# Copyright (c) 2024, IT Systematic and contributors
# For license information, please see license.txt

import frappe
import random
from frappe import _


def execute(filters=None):
	columns, data , chart , report_summary= get_columns(), get_data() , get_chart() , get_report_summary()
	return columns, data , None , chart , report_summary


def get_data():
	sql = f'''select name,sum(proof_count) as proof_count_sum from `tabElements-2024`  group by name'''
	data = frappe.db.sql(sql , as_dict = 1)
	return data

def get_columns():
	return[	{
		"fieldname": "name",
		"fieldtype": "Link",
		"label": _("Elements-2024"),
		"options":"Elements-2024",
		"width": 170
		},
		{
			"fieldname": "proof_count_sum",
			"fieldtype": "Int",
			"label": _("Proof Count Sum"),
			"width": 110

		},]

def get_chart():
	data = get_data()
	labels =[]
	values = []
	for entry in data:
		labels.append(entry["name"])
		values.append(entry["proof_count_sum"])

	chart = {'data':{'labels':labels,'datasets':[{'values':values}]},'type':'bar'}
	return chart

def get_report_summary():
	possible_colors = [
		"Red", "Blue", "Green", "Yellow", "Orange", "Purple",
		"Cyan", "Magenta", "Lime", "Pink", "Teal", "Lavender"
	]

	data = get_data()
	report_summary = []
	count = 0
	for entry in data:
		if count > len(possible_colors) -1:
			count = 0
		dict = {}
		dict["label"] = entry["name"]
		dict["value"] = entry["proof_count_sum"]
		dict["indicator"] = possible_colors[count]
		report_summary.append(dict)
		count +=1



	report_summary = report_summary
	return report_summary


