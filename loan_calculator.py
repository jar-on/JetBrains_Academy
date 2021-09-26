import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
test = [args.payment, args.principal, args.periods, args.interest]
if sum(1 for arg in test if not arg) > 1:
    print("Incorrect parameters.")
    exit()

if args.payment is not None:
    payment = float(args.payment)
if args.principal is not None:
    principal = int(args.principal)
if args.periods is not None:
    periods = int(args.periods)
if args.interest is not None:
    interest = float(args.interest) / 1200


def payment_amount():
    variable = (1 + interest) ** periods
    payment = math.ceil(principal * (interest * variable) / (variable - 1))
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {payment * periods - principal}")


def no_of_payments():
    variable = payment / (payment - (interest * principal))
    periods = math.ceil(math.log(variable, (1 + interest)))

    if periods < 12:
        print(f"It will take {periods} months to repay this loan!")
    elif periods == 12:
        print('It will take 1 year to repay this loan!')
    elif periods % 12 == 0:
        print(f'It will take {int(periods / 12)} years to repay this loan!')
    else:
        print(f'It will take {int(periods // 12)} years and {math.ceil(periods % 12)} months to repay this loan!')
    print(f"Overpayment = {int(payment * periods - principal)}")


def loan_principal():
    variable = (1 + interest) ** periods
    principal = payment / ((interest * variable) / (variable - 1))
    print(f"Your loan principal = {int(principal)}!")
    print(f"Overpayment = {math.ceil(payment * periods - principal)}")


def diff_payments():
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters.")
        exit()
    sum_of_payments = 0
    for month in range (periods):
        month += 1
        payment = math.ceil(principal / periods + interest * (principal - ((principal * (month - 1)) / periods)))
        sum_of_payments += payment
        print(f"Month {month}: payment is {payment}")
    print(f"Overpayment = {math.ceil(sum_of_payments - principal)}")


if args.type == "annuity":
    if not args.payment:
        payment_amount()
    if not args.periods:
        no_of_payments()
    if not args.principal:
        loan_principal()
else:
    diff_payments()
