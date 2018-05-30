1.ssh -keygen -t rsa -C "yourmailaddr@xxx.com"
2.注册账号
3.把pub发给组长
4.组长在Title写下组员的名字，再把组员的pub粘到key处
5.组长new一个repository
6.每个人
	git config --global user.name ''
	git config --global user.email mailaddr@xxx.com
7.组长组员克隆远程仓库:git clone git@github.com:账号名/项目名.git
	直接复制这条语句:Clone or download
8.进入虚拟环境，创建一个项目
	gjango-admin startproject xxx
9.本地操作
    9.1 将文件添加到暂存区
    git add file1 file2 ...
    git add dir
    
    9.2 提交到仓库
    git commit -m '备注信息'

    9.3 推送到github
    git push origin master

    9.4 历史查询、回溯
    git log     # 会显示每个人(name+mail)提交的信息
    git log --pretty=oneline    # 简短显示历史信息，但看不到是谁的提交
    git reflog                  # 历史命令

    # 历史回退，用版本号可以回退到任何一次提交
    git reset HEAD(版本号)      # 从仓库回滚(撤销修改)到暂存区
                                # HEAD是当前版本，HEAD^是上一次版本，依次类推
    git checkout filename       # 再把回滚文件还原到工作区

    9.6 把远程仓库的变化拉到本地
    git pull    # 修改公用代码事先要沟通一下






