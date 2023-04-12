aclNum = int(input ("ingrese un valor de acl:"))
if aclNum >= 1 and aclNum <= 99: 
    print("Esta es una acl Estandar")
elif aclNum >= 100 and aclNum <= 199:
    print("esta es una acl extendida")
elif aclNum >= 1300 and aclNum <= 1999:
    print("Esta es una acl Estandar")
elif aclNum >= 2000 and aclNum <= 2699:
    print("esta es una acl extendida")
else:
    print("Esta no pertenece a una acl")
