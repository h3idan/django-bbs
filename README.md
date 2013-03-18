django-bbs
==========

简介：
	基于Django web框架开发的简单的论坛。富文本编辑器使用的Uedtior。
	Ueditor来自开源社区github。（此版本中的Ueditor本人已经修复csrf错误。可以直接部署）
	主要功能：
		注册，登陆，发帖（无刷新），回帖（无刷新），
		权限设置（自己只能删除自己发的帖子），分页功能
		
	
开发环境：
	python 2.7.3 + Django 1.4.3 MySQL 5.5.28 + vim 7.3
	
	
测试方法：
	在MySQL中简历数据库：bbs
	shell下执行：
		1）python manage.py syncdb
		2）python manage.py runserver
	浏览器输入：127.0.0.1:8000
	
	
	
