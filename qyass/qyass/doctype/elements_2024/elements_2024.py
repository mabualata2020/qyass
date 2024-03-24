# Copyright (c) 2024, IT Systematic and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Elements2024(Document):
	def before_save(self):
		self.calculate_proof_count()

	def calculate_proof_count(self):
			if self.proof_count:
				if self.completed_count:
					self.complete_percent = self.completed_count / self.proof_count
				if self.reviewed_count:
					self.reviewed_percent = self.reviewed_count / self.proof_count