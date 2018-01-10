# coding:utf-8
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from ihome import create_app


#实际上，程序的运行时需要去区分开发模式和发布模式的，这个模式的控制，也应该由manage来管理
app,db = create_app('develop')

manager = Manager(app)

#创建迁移对象
migrate = Migrate(app, db)
#给manager添加db命令
manager.add_command('db',MigrateCommand)




if __name__ == '__main__':
    manager.run()
