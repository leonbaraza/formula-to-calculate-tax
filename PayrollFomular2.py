from LeonPayrollNew import netSalary


Name = "LEON"
LName = "WAKOLI"
Salary = 90000
Benefits = 0


p1 = Payroll(FName, LName, Salary, Benefits)
F

print(f'\n')
print(f'Full name : {p1.fullname()} \n'
      f'Email Address :  {p1.first.lower()}.{p1.last.lower()}@company.com \n'
      f'Basic Salary : Kshs {"{:,}".format(p1.basicsalary())} \n'
      f'Deductable NSSF : Kshs {"{:,}".format(p1.deductionsNSSF())} \n'
      f'Taxable income : Kshs  { "{:,}".format(p1.newTaxableIncome())} \n'
      f'Paye: Tax on Taxable Income : Kshs { "{:,}".format(p1.totalPaye())} \n'
      f'Personal Relief : Kshs {"{:,}".format(1408)} \n'
      f'Tax net off Relief : Kshs {"{:,}".format(p1.payableTaxAfterRefief())} \n'
      f'NHIF Contribution : Kshs { "{:,}".format(p1.deductionsNHIF())} \n \n'
      f'Net Pay : Kshs  {"{:,}".format(p1.netSalary())}'
      )