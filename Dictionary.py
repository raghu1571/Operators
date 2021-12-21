key=['JAKKA','RAGHU','KIRAN']
values=['PYTHON','JAVA','JS']
data=dict(zip(key,values))
print (data)
data['KUMAR'] = 'C'
print(data)
del data ['KIRAN']
print(data)
print("*************************")
prog = {'JS': 'ATOM', 'CS': 'VS', 'PYTHON':['PYCHARM','SUBLIME'],'JAVA':{'JSE':'NETBEANS','JEE':'ECLIPSE'}}
print(prog)

print(prog['JS'])

print(prog['PYTHON'])

print(prog['PYTHON'] [1])

print(prog['JAVA'])

print(prog['JAVA'] ['JEE'])
