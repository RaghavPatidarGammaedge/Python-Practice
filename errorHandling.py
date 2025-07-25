n1=int(input("enter a number to be divided\n"))

try:
    ans = 100 / n1

except ZeroDivisionError:
    print("ZeroDivisionError")

except ValueError:
    print("ValueError")

else:          #executed when none error arises
    print("Result is", ans)

finally:       #Always executable block
    print("Execution complete.")


class InvalidNoException(Exception):
    def __init__(self,no ,msg="number must be an accurate integer"):
        self.no=no
        self.msg=msg
        super().__init__(self.msg)



if n1 > 10 :
    raise InvalidNoException(n1,msg="number must be greater than 10")


