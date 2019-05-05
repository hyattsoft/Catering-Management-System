
美多商场项目：前后端分离
 
一、 项目准备：
1 商业模式
	B2B -- 企业对企业（Business to Business）
		阿里巴巴、慧聪网
	C2C -- 个人对个人（Customer to Customer）
		淘宝、瓜子二手车
	B2C -- 企业对个人（Business to Customer)
		唯品会、美多商场
	C2B -- 个人对企业（Customer to Business)
		海尔商城
	O2O -- 线上到线下（Online to Offline）
		美团、饿了吗
	F2C -- 工厂到个人（Factory to Customer）
		戴尔
	B2B2C -- 企业-企业-个人
		京东商城、天猫商城
2 开发流程
	项目立项（招投标、可行性分析）
	需求分析（很重要）
		需求分析说明书：给客户看的
		需求规格说明书：给开发人员看的
	产品原型（产品部）
		分析：
			分析网站的功能架构
			开发服务器的选择
			开发环境
		研发人员
			架构设计、数据库设计、单元测试：代码模块实现和测试（防止后门和bug）
		前端
			UI页面设计、前端代码编写
	网站代码整合（循坏上面步骤）
	集成测试（系统测试）
	网站发布（不断迭代升级，进行优化）
3 需求分析
	用户部分
		注册
			图片验证码
			短信验证码
		登录
			第三方登录（QQ登录）
		个人信息
			邮箱填写与验证
			浏览历史记录
		地址管理
			省市区地址信息加载
			新增修改删除地址
			设置默认地址
		修改密码
	商品部分
		首页
			商品分类
			广告控制
		商品列表
		商品详情
		商品搜索
	购物车部分
		购物车管理
	订单部分
		提交订单
		我的订单
		订单评价
	支付部分
		支付宝支付
4 项目架构
	项目采用前后端分离的应用模式
	前端使用Vue.js
		jQuery：选择某个网页元素，然后对它进行某种操作
		ajax：向后端请求数据
	后端使用Django REST framework
	MySQL：主从同步、双机热备
	Redis：session缓存
	celery：异步服务
	FastDFS：分布式服务
5 创建工程
	在git平台创建工程（注意：公司中通常使用gitlab私有服务器）操作流程一样
		项目名称：meiduo
		.gitignore：python
	ssh方式：加密传送通道
		rsa秘钥对（公钥 私钥）
			RSA：非对称加密算法
				私钥：用来加密数据
				公钥：用来解密数据
		生成秘钥对
			ssh-keygen -t rsa（Ubuntu、win10命令）
		文件保存地址（有默认值）回车
		cd .ssh
		cat 打开私钥（id_rsa）、公钥（id_rsa.pub）文件
		将公钥添加到git中（设置）
		clone项目
	在命令窗口中进入项目，查看分支
		git branch
	创建分支
		git checkout -b dev（名称）
	创建前端目录
		mkdir front_end_pc
	将前端代码放入目录中
	本地提交
		git commit -m"增加了静态文件"
	push
		git push origin dev:dev
			第一次push的时候，会提示是否使用公私钥，输入yes即可
	合并
		在git平台，点击 Pull Request --> 选择源分支（dev）目标分支（master）--> 添加合并请求说明 --> 创建
		管理员点击合并 --> 合并分支 --> 接受Pull Request
	安装live_server（跟python没有关系）
		windows下安装node.js下载安装包即可
		Ubuntu下安装node.js
			方法一：（需要翻墙）
				https://github.com/nodesource/distributions/blob/master/README.md（参考）
				curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash  - 
				sudo apt-get install -y nodejs
			方法二：（ubuntu下编译程序）
				0、下载安装文件wget https://nodejs.org/dist/v10.13.0/node-v10.13.0.tar.gz
				1、解压 tar zxvf node-v10.13.0.tar.gz
				2、进入目录，执行sudo ./configure
				3、执行编译命令 sudo make  (要求目录中必须有一个MakeFile文件)
				4、执行安装 sudo make install
			方法三：
				sudo apt install nodejs
			方法四：(推荐)
			1、安装nvm  （node version manager）
				curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
			2、执行source ~/.bashrc
			3、nvm install node
		安装live_server
			npm install -g live-server
	在静态文件目录下运行live-server
		live-server运行在8080端口下，可以通过127.0.0.1:8080来访问静态页面。			
	创建Django REST framework工程
		创建虚拟环境
			mkvirtualenv meiduo -p python3
			pip install django==1.11.11
			pip install djangorestframework
			pip install pymysql
		在meduo目录下创建项目meiduo_mall
			django-admin startproject meiduo_mall
		用pycharm打开meiduo文件夹，配置一下解释器，为刚刚虚拟环境中的python
	调整工程目录
		在根目录meiduo_mall下创建包docs，logs，scripts
		在子meiduo_mall目录下创建包apps，libs，settings，utils
			apps 存放Django的应用
			libs 存放第三方的库文件
			settings 存放配置文件的目录，分为开发dev和线上prod
			utils 存放项目自己定义的公共函数或类等
			docs 用于存放一些说明文档资料
			scripts 用于存放管理脚本文件
		并且在将settings.py拖到settings文件夹中改名字为dev.py
		创建应用
			在meiduo/meiduo_mall目录下输入：python manage.py startapp users
		注册应用：rest_framework和users
			users注册的路径需要注意，每次都要以meiduo_mall_.apps开头
				解决：sys.path是python解释器导包的路径，如果我们能够给users所在的包添加进去那就可以了
6 项目配置
	增加启动参数runserver
	修改manage.py中的settings.py的文件路径
	创建数据库，并且创建用户
		create user meiduo identified by 'meiduo'; 
		grant all on meiduo_mall.* to 'meiduo'@'%'; 
		flush privileges;
	配置数据库
		安装 pymysql
			pip install pymysql
		记得在meiduo/meiduo_mall/__init__.py文件中添加
			import pymysql
			pymysql.install_as_MySQLdb()
		如果报错：
	安装django-redis，并配置
		pip install django-redis
	时区配置
	日志配置
	异常配置
	Pycharm提示设置
		将一级目录meiduo设置为根目录
		将二级目录meiduo下的apps文件夹设置为根目录
	js版本配置
		js语法是在js6版本才出现的，但是pycharm默认的是5.1，需要进行修改
二、用户部分
1 用户模型类
	创建自定义的用户模型类
		模型类继承 django.contrib.auth.models.AbstractUser
	在配置文件中进行配置
		AUTH_USER_MODEL = "users.User"
	配置完成之后，才能执行第一次数据库迁移
		python manage.py makemigrations
		python manage.py migrate
2 用户注册接口
	设计接口的思路
		分析接口业务逻辑
		分析接口的功能任务
			接口的请求方式：GET、POST、PUT
			接口的URL路径定义
			需要前端传递的数据及数据格式
			返回前端的数据及数据格式
	注册业务接口分析
		图片验证码
		短信验证码
		用户名判断是否存在
		手机号判断是否存在
		注册保存用户数据
	图片验证码
		访问方式：
			DET /image_codes/(?P<image_code_id>[\w-]+)/
		在apps中创建应用verifications，并注册
		创建视图ImageCodeView(APIView)
			接受参数
			# 校验参数（URL中（正则匹配）已经实现）
			生成验证码图片
				第三方的包captcha（放在子目录meiduo_mall/libs中）
				text, image = captcha.generate_captcha()
			保存真实值
				在配置文件中添加一个新的redis配置verify_codes，用于存放验证码数据
				redis_conn = get_redis_connection("verify_codes")
				创建常量 IMAGE_CODE_REDIS_EXPIRES
					在当前目录中创建文件constants.py，定义常量IMAGE_CODE_REDIS_EXPIRES，设置为5 * 60 （即5分钟）
				redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
			返回图片
				# 固定返回验证码图片数据，不需要REST framework框架的Response帮助我们决定返回响应数据的格式
				# 所以此处直接使用Django原生的HttpResponse即可
				# 指明返回值类型
				return HttpResponse(image, content_type="images/jpg")
		创建路由url
			前后端分离基本不需要重定向，所以不需要设置name属性
		注册路由
	设置域名
		前端
			www.meiduo.site
		后端
			api.meiduo.site
		ubuntu编辑/etc/host文件，可以设置本地域名
			sudo vim /etc/hosts
		在文件中增加两条信息
			127.0.0.1   api.meiduo.site
			127.0.0.1   www.meiduo.site
		windows系统中若设置本地域名，hosts文件在如下目录：
			C:\Windows\System32\drivers\etc
		修改settings配置中的ALLOWED_HOSTS
		前端js请求不能写死，以防日后修改域名
		在在前端front_end_pc/js目录中新建host.js文件
			var host = 'http://api.meiduo.site:8000';
		图片验证码后端测试
			运行报错，安装pillow安装包
				缺少PIL，这是因为我们用到了captcha，这个captcha是生成图片验证码的，要用到图片相关的包PIL。
				我们安装Pillow即可（PIL安装比较麻烦，会有各种问题，所以就安装了可以完全替代PIL的Pillow包）
	短信验证码
		访问方式：
			GET /sms_codes/(?P<mobile>1[3-9]\d{9})/?image_code_id=xxx&text=xxx
		在应用verifications中创建视图SMSCodeView(GenericAPIView)
			校验参数（由序列化器完成）
				实现序列化器类，创建serializers.py文件夹 
			生成短信验证码
				sms_code = "%06d" % random.randint(0, 999999)
			保存短信验证码 保存发送记录
			发送短信
				使用云通讯第三方平台
			返回
		补充redis管道
		补充删除图片验证码的逻辑
			避免用户拿着同一个图片验证码，获取多次短信验证码
			在比较图片验证码之前删除redis中的图片验证码（拿出验证码，就删除，可以避免很多问题）
	跨域请求CORS
		OPTION
		浏览器会发送给option请求询问，后端是否支持
		后端提供option请求的支持，告诉浏览器，支持哪些域名访问
		Django中间件提供option请求
			安装第三方包
				pip install django-cors-headers
			添加应用
			设置中间层，在最上边添加中间件
			添加白名单
	使用Celery发送短信
		定义任务
		celery_app = Celery()
		
		@celery_app.task
		def send_sms_code(a, b, c):
			pass
		
		发布任务
		send_sms_code.delay(a, b, c)
		
		在一级目录meiduo_mall中创建celery_tasks包
			Celery目录搭建
				创建main.py、config.py文件，sms包（sms包中创建tasks.py文件）
			安装扩展
				pip install -U Celery
			创建celery应用（main.py）
				celery_app = Celery("meiduo")
			对celery进行配置（config.py）
				broker_url = "redis://127.0.0.1/15"
			导入celery配置（main.py）
				celery_app.config_from_object('celery_tasks.config')
			导入任务（main.py）
				celery_app.autodiscover_tasks(['celery_tasks.sms'])
			将之前的发送短信验证码的代码copy到task.py文件中，并加以修改
				不需要返回值（这个任务执行，已经不需要给前端返回响应了）
			celery要执行的任务中有要获取日志looger，就需要知道django项目的配置文件才行
				logger = logging.getLogger("django")
			为celery使用django配置文件进行设置（main.py）
				if not os.getenv('DJANGO_SETTINGS_MODULE'):
					os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'
			将这个方法变为异步任务
				在send_sms_code函数上添加装饰器@celery_app.task(name="send_sms_code")
		使用Celery发送短信验证码
			expires = constants.SMS_CODE_REDIS_EXPIRES // 60
			temp_id = constants.SMS_CODE_TEMP_ID
			send_sms_code.delay(mobile, sms_code, expires, temp_id)
		celery的main是需要单独启动的   /meiduo/meiduo_mall$
			celery -A celery_tasks.main worker -l info
	判断帐号是否存在
		判断用户名是否存在
		判断手机号是否存在
	用户注册
		在users包中创建视图UserView(CreateAPIView) 相当于(CreateModelMixin, GenericAPIView)
			需要传入参数
				username、password、password2、sms_code、mobile、allow
			用序列化完成以下功能
				接收参数
				校验参数
				保存用户数据，密码加密
				序列化，返回数据
			创建序列化器
				CreateUserSerializer(serializers.ModelSerializer )
			对字段进行校验
			实现对密码的加密
				移除数据库模型类中不存在的属性
				重写create方法：增加密码加密
	Django REST framework JWT
		JWT（Json web token）
			JWT由头部、载荷、签证组成，中间由“.”隔开
		安装JWT
			pip install djangorestframework-jwt
		认证配置
			指明token的有效期
	登录
		使用JWT手动签发token
			from rest_framework_jwt.settings import api_settings
			jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
			jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
		在注册视图中创建token
			修改CreateUserSerializer序列化器，在create方法中增加手动创建token的方法
		直接添加url
			Django REST framework JWT提供了登录签发JWT的视图，可以直接使用
		在返回值中增加username和user_id
			在users/utils.py 中创建
			修改配置文件
	多账号登录
		重写authenticate方法
			自定义用户名或手机号认证
				获取用户对象 
				如果用户对象存在，校验密码
				如果不存在，返回
		在配置文件中告知Django使用我们自定义的认证后端