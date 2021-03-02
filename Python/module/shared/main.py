import common


print("type please")
var = common.entry(returnType="bool", failureMsg="faillut msg", blackList=["yes"])
print("-->", var)

