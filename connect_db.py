def connec_sqlserver():
    import pymssql

    server = "187.32.43.13"
    # 连接服务器地址
    user = "root"
    # 连接帐号
    password = "1234"
    # 连接密码
    test_db = "*****"
    conn = pymssql.connect(server, user, password, test_db)  #获取连接
    return conn


def connec_mysql():
    import pymysql

    server = "187.32.43.13"    # 连接服务器地址
    user = "root"
    # 连接帐号
    password = "1234"
    # 连接密码
    test_db = "***"
    conn = pymysql.connect(server, user, password,test_db)  #获取连接
    return conn
