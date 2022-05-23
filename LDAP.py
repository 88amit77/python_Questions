###code=1
# import ldap
# con = ldap.initialize('ldap://localhost:389', bytes_mode=False)
# con.simple_bind_s('login', 'secret_password')
# results = con.search_s('ou=people,dc=example,dc=org', ldap.SCOPE_SUBTREE, "(cn=Raphaël)")
# print(results)
# # output==[
# #     ("cn=Raphaël,ou=people,dc=example,dc=org", {
# #         'cn': [b'Rapha\xc3\xabl'],
# #         'sn': [b'Barrois'],
# #     }),
# # ]

##code=2
# from ldap3 import Server, Connection, SAFE_SYNC
#
# server = Server('my_server')
# conn = Connection(server, 'my_user', 'my_password', client_strategy=SAFE_SYNC, auto_bind=True)
#
# status, result, response, _ = conn.search('o=test', '(objectclass=*)')
# # usually you don't need the original request (4th element of the returned tuple)
#
# ##code--3
# import ldap
# conn = ldap.initialize('ldap://ad.server.domain.com')
# conn.protocol_version = 3
# conn.set_option(ldap.OPT_REFERRALS, 0)
# conn.simple_bind_s('user@domain.com', 'WrongPassword')
# ldap.INVALID_CREDENTIALS: {'info': '80090308: LdapErr: DSID-0C090334, comment: AcceptSecurityContext error, data 52e, vece', 'desc': 'Invalid credentials'}
# # conn.simple_bind_s('user@domain.com', 'CorrectPassword')
# # (97, [])
# try:
#   conn.simple_bind_s('user@domain.com', 'SubmittedPassword')
#   conn.search_st('DC=domain,DC=com', ldap.SCOPE_SUBTREE, '(objectClass=container)', 'name', 0, 30)
# except ldap.INVALID_CREDENTIALS:
#   user_error_msg('wrong password provided')
#
# ##code==4
# import ldap
# def authenticate():
#     conn = ldap.initialize('ldap://ldap.example.com')
#     conn.protocol_version = 3
#     conn.set_option(ldap.OPT_REFERRALS, 0)
#     try:
#         username = 'user_id'
#         password = 'motdepasse'
#         user = "%s@domain" %username
#         result = conn.simple_bind_s('user', 'password')
#     except ldap.INVALID_CREDENTIALS:
#         print("Invalid credentials")
#         return "Invalid credentials"
#     except ldap.SERVER_DOWN:
#         print("Server down")
#         return "Server down"
#     except ldap.LDAPError as e:
#         if type(e.message) == dict and e.message.has_key('desc'):
#             return "Other LDAP error: " + e.message['desc']
#         else:
#             print("Other LDAP error: ")
#             return "Other LDAP error: " + e
#     finally:
#         conn.unbind_s()
#         print("Succesfully")
#     return "Succesfully authenticated"
#
# authenticate()

import ldap3
#import ldap  # run 'pip install python-ldap' to install ldap module.
conn = ldap3.open("ldaphost.company.com")
conn.simple_bind_s("myuser@company.com", "mypassword")
