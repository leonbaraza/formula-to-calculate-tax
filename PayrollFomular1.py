# Tax calculation
# 0 – 12,298	            10%
# On the next 11,587	15%
# On the next 11,587	20%
# On the next 11,587	25%
# Over 47,059	        30%


# Global Variables declarations
fullname = ""
totalAllowances = 0
basicSalary = 0
deductionNSSF = 0
newTaxableIncome = 0


class Payroll:
    def __init__(self, first, last, pay, allowances):
        self.first = first
        self.last = last
        self.email = first + "." +last +"@company.com"
        self.pay = pay
        self.allowances = allowances
        self.employeeType = type


    def fullname(self):
        return ('{} {}'.format(self.first.capitalize(), self.last.capitalize()))

    def totalAllowances(self):
        pass

# Basic salary plus the alowances

    def basicsalary(self):
        basicsalary = self.pay + self.allowances
        # return ("{:,}".format(basicsalary))
        return basicsalary

# New Taxable income
#     Here deduct the NSSF

    def deductionsNSSF(self):
        if self.basicsalary() >= 18000:
            deductionsNSSF = (18000 * 0.06)

        elif self.basicsalary() > 0 and self.basicsalary() < 18000:
            deductionsNSSF = (self.basicsalary() * 6)/100

        else:
            deductionsNSSF = 0

        # elif self.basicsalary() > 0 and self.basicsalary() < 18000:
        #     deductionsNSSF = (6000 * 0.06)

        return deductionsNSSF

# Calculate the new Taxable income
#     basicsalary() - deductionsNSSF()

    def newTaxableIncome(self):
        newTaxableIncome = self.basicsalary() - self.deductionsNSSF()

        return newTaxableIncome
# Tax Calculation

    def consultant(self):
        if self.employeeType == "consultant":
            totalPayee = self.newTaxableIncome() * 0.05

# Tax1
    def tax1(self):

        if self.newTaxableIncome() > 0:

            tax1 = 12298 * 0.1

        else:
            tax1 = 0

        return round(tax1, 2)
        # return tax1

    def tax2(self):
        newTaxIncome = self.newTaxableIncome()-12298

        if newTaxIncome >= 12299:
            tax2 = (23885 - 12298) * 0.15

        elif newTaxIncome > 0:
            tax2 = newTaxIncome * 0.15

        else:
            tax2 = 0

        return round(tax2, 2)
        # return tax2

    def tax3(self):

        newTaxIncome = self.newTaxableIncome()-23885

        if newTaxIncome >= 23886:
            tax3 = (35472 - 23885)*0.20

        elif newTaxIncome >0:
            tax3 = newTaxIncome*0.2

        else:
            tax3 = 0

        return round(tax3, 2)
        # return tax3

    def tax4(self):
        newTaxIncome = self.newTaxableIncome()-35472

        if newTaxIncome >= 35473:
            tax4 = (47059 - 35472)*0.25

        elif newTaxIncome > 0:
            tax4 = newTaxIncome* 0.25

        else:
            tax4 = 0

        return round(tax4, 2)
        # return tax4

    def tax5(self):
        newTaxIncome = self.newTaxableIncome() - 47059

        if newTaxIncome > 47059:
            tax5 = newTaxIncome * 0.30

        elif newTaxIncome>0:
            tax5 = newTaxIncome * 0.30

        else:
            tax5 = 0

        return round(tax5, 2)
        # return tax5

# Paye before relief
#   Add all tax

    def totalPaye(self):
        totalPaye = self.tax1()+self.tax2()+self.tax3()+self.tax4()+self.tax5()

        # return round(totalPaye, 2)
        return totalPaye

# Calculate Payable tax after relief
#     deduct Personal relief -> 1,408

    def payableTaxAfterRefief(self):
        if self.totalPaye() > 1408:

            pTax = self.totalPaye() - 1408

        else:
            pTax = 0

        return round(pTax, 2)
        # return pTax



# Calculate NHIF

    def deductionsNHIF(self):
        if self.basicsalary() > 0 and self.basicsalary() <= 5999:

            dNHIF = 150

        elif self.basicsalary() >= 6000 and self.basicsalary() <= 7999:

            dNHIF = 300

        elif self.basicsalary() >= 8000 and self.basicsalary() <= 11999:

            dNHIF = 400

        elif self.basicsalary() >= 12000 and self.basicsalary() <= 14999:

            dNHIF = 500

        elif self.basicsalary() >= 15000 and self.basicsalary() <= 19999:

            dNHIF = 600

        elif self.basicsalary() >= 20000 and self.basicsalary() <= 24999:

            dNHIF = 750

        elif self.basicsalary() >= 25000 and self.basicsalary() <= 29999:

            dNHIF = 850

        elif self.basicsalary() >= 30000 and self.basicsalary() <= 34999:

            dNHIF = 900

        elif self.basicsalary() >= 35000 and self.basicsalary() <= 39999:

            dNHIF = 950

        elif self.basicsalary() >= 40000 and self.basicsalary() <= 44999:

            dNHIF = 1000

        elif self.basicsalary() >= 45000 and self.basicsalary() <= 49999:

            dNHIF = 1100

        elif self.basicsalary() >= 50000 and self.basicsalary() <= 59999:

            dNHIF = 1200

        elif self.basicsalary() >= 60000 and self.basicsalary() <= 69999:

            dNHIF = 1300

        elif self.basicsalary() >= 70000 and self.basicsalary() <= 79999:

            dNHIF = 1400

        elif self.basicsalary() >= 80000 and self.basicsalary() <= 89999:

            dNHIF = 1500

        elif self.basicsalary() >= 90000 and self.basicsalary() <= 99999:

            dNHIF = 1600

        elif self.basicsalary() >= 100000:

            dNHIF = 1700

        else:
            dNHIF = 0

        return dNHIF

# Calculate the net salary
# Net salary = new taxable income - payable tax after relief - nhif

    def netSalary(self):
        netSalary = self.newTaxableIncome()-self.payableTaxAfterRefief()-self.deductionsNHIF()

        return round(netSalary,2)

    # return ("{:,}".format(number))








#
# FName = "LEON"
# LName = "WAKOLI"
# Salary = 90000
# Benefits = 0
#
#
# p1 = Payroll(FName, LName, Salary, Benefits)
#
#
#
#
# #
# # print( "Basic Salary : " "{:,}".format(p1.basicsalary()))
# #
# # print(f'\n {p1.last}')
#
# print("Full name : " +p1.fullname() +"\n"
#       "Email Address : " +p1.first.lower() +"." +p1.last.lower() +"@company.com" +"\n"
#       "Basic Salary : Kshs " "{:,}".format(p1.basicsalary()) +"\n"
#       "Deductable NSSF : Kshs " "{:,}".format(p1.deductionsNSSF()) +"\n"
#       "Taxable income : Kshs " "{:,}".format(p1.newTaxableIncome())+"\n"
#       "Paye: Tax on Taxable Income : Kshs " "{:,}".format(p1.totalPaye())+"\n"
#       "Personal Relief : Kshs " "{:,}".format(1408)+"\n"
#       "Tax net off Relief : Kshs" "{:,}".format(p1.payableTaxAfterRefief())+"\n"
#       "NHIF Contribution : Kshs " "{:,}".format(p1.deductionsNHIF())+"\n" +"\n"
#       "Net Pay : Kshs " "{:,}".format(p1.netSalary())
#       )

