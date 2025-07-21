hours_worked_month = int(input("hours worked in month: "))
value_hour_work = float(input("Value of hours in work: "))
salary_brute = hours_worked_month * value_hour_work
tax_inss = salary_brute * 0.10
tax_sindicate = salary_brute * 0.03
fgts = salary_brute * 0.11


if salary_brute <= 900:
    print("Salary is isent of IR")
    print("Tax of INSS %.2f " % tax_inss)
    print("Tax of sindicate %.2f " % tax_sindicate)
    print("FGTS = %.2f " % fgts)
    print("Total discounts %.2f" % (tax_inss + tax_sindicate))
    print("Salary liquid %.2f " % (salary_brute - (tax_inss + tax_sindicate)))

elif salary_brute <= 1500:
    print("Salary with discount 5%", (salary_brute * 0.05))
    print("Tax of INSS %.2f " % tax_inss)
    print("Tax of sindicate %.2f " % tax_sindicate)
    print("FGTS = %.2f " % fgts)
    print("Total discounts %.2f" % (tax_inss + tax_sindicate + (salary_brute * 0.05)))
    print("Salary liquid %.2f " % (salary_brute - (tax_inss + tax_sindicate)))

elif salary_brute <= 2500:
    print("Salary with discount 10%", (salary_brute * 0.10))
    print("Tax of INSS %.2f " % tax_inss)
    print("Tax of sindicate %.2f " % tax_sindicate)
    print("FGTS = %.2f " % fgts)
    print("Total discounts %.2f" % (tax_inss + tax_sindicate + (salary_brute * 0.10)))
    print("Salary liquid %.2f " % (salary_brute - (tax_inss + tax_sindicate)))

else:
    print("Salary with discount 20%", (salary_brute * 0.20))
    print("Tax of INSS %.2f " % tax_inss)
    print("Tax of sindicate %.2f " % tax_sindicate)
    print("FGTS = %.2f " % fgts)
    print("Total discounts %.2f" % (tax_inss + tax_sindicate + (salary_brute * 0.20)))
    print("Salary liquid %.2f " % (salary_brute - (tax_inss + tax_sindicate)))
