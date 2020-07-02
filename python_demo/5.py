


phone = None
email = None
idNumber = None

idpfind = {}
applyfind = {}

# 判断任一一个不为空
if not phone and not email and not idNumber:
    print("手机号, 邮箱, 身份证必须填一个")
else:
    if phone:
        idpfind.update({"phone_number":{"$regex":".+{}".format(phone)}})
        applyfind.update({"phone":phone})

    if email:
        idpfind.update({"email": email})
        applyfind.update({"email": email})

    if idNumber:
        applyfind.update({"idNumber":idNumber})
        if not idpfind:
            idpfind.update({"idNumber":idNumber})

print(idpfind)
print(applyfind)

if not idpfind or not applyfind:
    print("查询条件不能为空")
