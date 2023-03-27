## Docker of Stable Diffusion Webui
基于[Stable Diffusion Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)的一些客制化并打包为docker镜像。

### docker运行：
[点击这里查看docker/README.md](docker/README.md)

### 其他备注：
    - webui.py中修复onlyapi模式下没有正常加载Lora模型的问题；
    - 增加.dockerignore文件；
    - 增加docker脚本文件夹；
    - 增加Stable Diffusion Webui使用api批量出图的脚本：
        - test/generate
        - test/utils
