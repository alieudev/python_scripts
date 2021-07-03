class Employee: 

	num_of_emps = 0
	raise_amt = 1.04 

	def __init__(self, first, last, pay): 
		self.first = first 
		self.last = last 
		self.pay = pay 

		Employee.num_of_emps += 1 

	@property
	def email(self): 
		return f'{self.first}.{self.last}@company.com'

	@property
	def fullname(self): 
		return f'{self.first} {self.last}'

	@fullname.setter
	def fullname(self, name): 
		first, last = name.split(' ')
		self.first = first
		self.last = last

emp_1 = Employee('Alieu', 'Baldeh', 100_000)
emp_1.fullname = 'Bouba Kaba'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)



	def apply_raise(self): 
		self.pay = int(self.pay * self.raise_amt)


	@classmethod 
	def set_raise_amt(cls, amount): 
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('_')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day): 
		if day.weekday() == 5 or day.weekday() == 6: 
			return False
		return True

	def __repr__(self): 
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self): 
		return '{} - {}'.format(self.fullname(), self.email.lower())


class Developer(Employee): 
	raise_amt = 1.10

	def __init__(self, first, last, pay, pro_lang):
		super().__init__(first, last, pay)

		#Another one you can use 
		#Employee.__init__(self, first, last, pay)

		self.pro_lang = pro_lang

class Manager(Employee): 
	raise_amt = 1.25

	def __init__(self, first, last, pay, title, fv_snack, employees=None):
		super().__init__(first, last, pay)
		self.title = title
		self.fv_snack = fv_snack
		if employees is None: 
			self.employees = []
		else: 
			self.employees = employees
	def add_emp(self, emp): 
		if emp not in self.employees: 
			self.employees.append(emp)

	def remove_emp(self, emp): 
		if emp in self.employees: 
			self.employees.remove(emp)

	def print_emps(self): 
		for emp in self.employees: 
			print('--->', emp.fullname())







dev_1 = Developer('Alieu', 'Baldeh', 80_000, 'Python')
dev_2 = Developer('Bouba', 'Mballo', 60_000, 'Java')

mgn_1 = Manager('Aboubacar', 'Kaba', 100_000, 'Ops Manager', 'Cookies', [dev_1])

print(repr(dev_1))
print(str(dev_1))

Prints only the __str__ 
print(dev_1)

print(isinstance(mgn_1, Employee))
print(issubclass(Developer, Employee))

mgn_1.add_emp(dev_2)
mgn_1.print_emps()
mgn_1.remove_emp(dev_2)
mgn_1.add_emp(dev_1)
mgn_1.print_emps()

print(help(Developer))
print(dev_1.email.lower(), dev_1.pro_lang)
print(dev_2.email.lower(), dev_2.pro_lang)
print(mgn_1.email.lower(), mgn_1.title, mgn_1.fv_snack)

import datetime 
my_date = datetime.date(2020, 11, 29)

print(Employee.is_workday(my_date))


emp_str_1 = 'John-Doe-70_000'
emp_str_2 = 'Steve-Smith-30_000'
emp_str_3 = 'Jane-Doe-90_000'


new_emp_1 = Employee(first, last, int(pay))

print(new_emp_1.email)
print(new_emp_1.pay)

 

