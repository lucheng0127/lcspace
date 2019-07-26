# Django + Nuxt.js 实现的类似vultr的VPS管理站点

## 架构
* Nuxt.js 实现前端页面
* axios 实现前端api
* django rest framework 实现后端restful接口
* 后端api接口复制数据库表的读写
* task复制镜像管理以及虚拟机生命周期管理（使用rq实现异步任务）
* python实现进程守护，读取数据库表信息和任务完成标志，并更新task运行状态到数据库表中
虚拟机生命周期控制依赖libvirt，需要有本地或者可远程连接的资源池
