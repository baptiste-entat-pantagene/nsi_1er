import common


print("type your name")
varStr = common.entry(returnType="str")
print("name -->", varStr)

print("\ntype your age")
varInt = common.entry(returnType="int")
print("age -->", varInt)

print("\ntype one char")
varChar = common.entry(returnType="char")
print("char -->", varChar)

print("\ntype yes or no")
varBool = common.entry(returnType="bool")
print("bool -->", varBool)